#include <stdbool.h>
#include <time.h>
#include <avr/io.h>
#include <util/delay.h>
#include <util/atomic.h>

//#define F_CPU 16000000UL  //Frequência para delay.h
#define FOSC 16000000UL   //Frequência para a UART
#define BAUD 9600
#define MYUBRR FOSC/16/BAUD-1
#define POWER_PIN PD2
#define CONTROL_PIN PD3
#define set_bit(Y,bit_x) (Y|=(1<<bit_x))    //ativa o bit x da variável Y (coloca em 1)
#define clr_bit(Y,bit_x) (Y&=~(1<<bit_x))   //limpa o bit x da variável Y (coloca em 0)

volatile unsigned long count_millis;

/************** Cabeçalho das funções ***************/

void UART_Init(unsigned int ubrr);
void UART_Transmit(unsigned char data);
unsigned char UART_Receive(void );
void setup(void);
int main(void );

/************** UART ***************/

void UART_Init( unsigned int ubrr)
{
  /*Set baud rate */
  UBRR0H = (unsigned char)(ubrr>>8);
  UBRR0L = (unsigned char)ubrr;
  /*Disable double speed*/
  UCSR0A = 0;
  /*Enable receiver and transmitter */
  UCSR0B = (1<<RXEN0)|(1<<TXEN0);
  /* Set frame format: 8data, 1 stop bit, none parity */
  UCSR0C = (0<<USBS0)|(1<<UCSZ01)|(1<<UCSZ00);
}

void UART_Transmit(unsigned char data)
{
  /* Wait for empty transmit buffer */
  while (!(UCSR0A & (1<<UDRE0)))
  ;
  /* Put data into buffer, sends the data */
  UDR0 = data;
}

unsigned char UART_Receive(void)
{
  /* Wait for data to be received */
  while (!(UCSR0A & (1<<RXC0)))
  ;
  /* Get and return received data from buffer */
  return UDR0;
}


/************** Contador tempo ms ***************/

void TIMER_init(void){
  
  TCCR2A = 0x00;
  TCCR2B |= (1<<CS21);
  TCNT2 = 56;
  TIMSK2 |= (1<<TOIE2);
  
  count_millis = 0;
  
}

ISR (TIMER2_OVF_vect)
{
  TCNT2   =    56;
  count_millis ++;
  
}

unsigned long TIMER_return(void){
  unsigned long aux_millis;

  ATOMIC_BLOCK(ATOMIC_FORCEON) {
    aux_millis = count_millis;
  }
  return aux_millis;
}

/************** Configurações iniciais ***************/

void SETUP_init(void){
  DDRD = 0b11111100;  //configura os pinos 2 a 7 como saída
  DDRB = 0b00000011;  //configura os pinos 8 a 9 como saída
  PORTD = 0b00001111; //desativa os pinos 4 a 7
  PORTB = 0b11111100; //desativa os pinos 8 a 9
  
  UART_Init(MYUBRR);
  TIMER_init();
  
}

int main() {
  
  cli();
  SETUP_init();
  
  unsigned char power_state = 0;            // variável que indica se a FPGA está ligada/desligada.
  unsigned char received;               // variável para receber dados vindo da comunicação serial com a GUI
  unsigned char bitread;            // variável auxiliar para ler bit a bit
  bool is_connected = false;          // variável para verificar a conexão da FPGA com a GUI
  bool is_power_blocked = false;        // variável para bloquear o botão de ligar/desligar a FPGA.
  unsigned long beam_millis = TIMER_return(); // timestamp for last beam sent
  unsigned long input_millis;         // ts for last input received
  unsigned long power_on_millis;        // ts for how long the board is on
  unsigned long power_off_millis;       // ts for last power toggle
  
  /* Loop principal para comunicação e controle da placa DE2-115 */
  
  while(1){
    /*verifica se há dados para leitura na porta serial*/
    cli();
    while ((UCSR0A & (1<<RXC0)) == 0) {
      if ((TIMER_return() - beam_millis) > 1000) {
        beam_millis = TIMER_return();
        if (is_connected)
        UART_Transmit(50);
        else
        UART_Transmit(40);
      }
    }
    
    /* Desbloqueia o botão power/off da API 10sec após o ultimo toggle*/
    if (is_power_blocked && (TIMER_return() - power_off_millis) > 10000)
    is_power_blocked = false;

    /** Desconecta e desliga a FPGA depois de 10 min ociosa **/
    if (is_connected && (TIMER_return() - input_millis) > 595000) {
      is_connected = false;
      if (power_state) {
        is_power_blocked = true;
        power_state = 0;
        PORTD |= (power_state << POWER_PIN);
        power_off_millis = TIMER_return();
      }
    }

    /** Desliga a FPGA depois de 10 min de uso **/
    if (power_state && (TIMER_return() - power_on_millis) > 600000) {
      is_power_blocked = true;
      power_state = 0;
      //PORTD |= (power_state << POWER_PIN);
      clr_bit(PORTD, POWER_PIN);
      power_off_millis = TIMER_return();
    }
  }

  input_millis = TIMER_return();
  received = UART_Receive();

  /* Confirma conexão */ 
  if (!is_connected) {
    if (received == 41) {
      UART_Transmit(42);
      is_connected = true;
    }
  }
  
  /* Desconecta e deslisga a FPGA */
  else if (received == 88) {
    is_connected = false;
    if (power_state) {
      is_power_blocked = true;
      power_off_millis = TIMER_return();
      power_state = 0;
      clr_bit(PORTD, POWER_PIN);
    }
  }

  /* Lê o byte recebido como bits e set nos pinos de saída */ 
  else if (received >= 0 && received < 22) {
    for (int j = 0; j<6; j++) {
      bitread = bitRead(received, j);
      digitalWrite(j+4, bitread);
    }
    _delay_ms(1000);
    set_bit(PORTD,CONTROL_PIN);
    _delay_ms(1000);
    clr_bit(PORTD,CONTROL_PIN);
  }

  /* Reinicia a FPGA */ 
  else if (received == 127){
    set_bit(PORTD,PD4);
    set_bit(PORTD,PD5);
    set_bit(PORTD,PD6);
    set_bit(PORTD,PD7);
    set_bit(PORTB,PB0);
    set_bit(PORTB,PB1);
    _delay_ms(1000);       //Delay de 1 segundo
    set_bit(PORTD,CONTROL_PIN);
    _delay_ms(1000);       //Delay de 1 segundo
    clr_bit(PORTD,CONTROL_PIN);
  }
  
  /* Desliga a FPGA */ 
  else if(received == 90) {
    if (is_power_blocked)
      UART_Transmit(92);
    else if (power_state) {
      is_power_blocked = true;
      power_off_millis = TIMER_return();
      power_state = 0;
      clr_bit(PORTD, POWER_PIN); //desativa pino de energia
      UART_Transmit(91);
    } 
    else {
      is_power_blocked = true;
      power_off_millis = TIMER_return();
      power_state = 1;
      set_bit(PORTD, POWER_PIN);; //ativa pino de energia
      UART_Transmit(91);
    }
  }

  sei();
  return 0;
}
