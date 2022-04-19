#include <stdbool.h> // Header-file for boolean data-type.
#include <time.h>
#include <avr/io.h> // Header-file that includes the apropriate IO definitions for the device      
#include <util/delay.h> // Header-file for busy-wait delay loops

#define power_pin PD2
#define control_pin PD3
#define F_CPU 16000000UL // CPU frequency?
#define set_bit(Y,bit_x) (Y|=(1<<bit_x))    //ativa o bit x da variável Y (coloca em 1)
#define clr_bit(Y,bit_x) (Y&=~(1<<bit_x))   //limpa o bit x da variável Y (coloca em 0)

/** Inicialização das variáveis **/

// variável que indica se a FPGA está ligada/desligada.
int power_state = 0;
// variável para receber dados vindo da comunicação serial com a GUI
int received;
// variável auxiliar para ler bit a bit
unsigned char bitread;
// bool is_sent = false;
// variável para verificar a conexão da FPGA com a GUI
bool is_connected = false;
// variável para bloquear o botão de ligar/desligar a FPGA.
bool is_power_blocked = false;

unsigned long beam_millis = clock(); // timestamp for last beam sent (testar função clock())
// unsigned long sent_millis;            // ts for output clock state change
unsigned long input_millis;     // ts for last input received
unsigned long power_on_millis;  // ts for how long the board is on
unsigned long power_off_millis; // ts for last power toggle

void setup(void){
  DDRD = 0b11111100; //configura os pinos 2 a 7 como saída
  DDRB = 0b00000011; //configura os pinos 8 a 9 como saída
  PORTD = 0b00001111; //desativa os pinos 4 a 7 (zera a tensao)
  PORTB = 0b11111100; //desativa os pinos 8 a 9 (zera a tensao)
}

int main() {
  setup();
  // Loop principal para comunicação e controle da placa DE2-115
  while(1){
    // Loop cuja condição verifica se há dados para leitura na porta serial

      // Send beacon every 1 second

      // Unblock fpga power in 10 sec after last toggle

      // Disconnect and turn off fpga if user is idle for 10 min

      // Turn fpga off after 10 min of use

    input_millis = clock();
    //received = Serial.read(); (buscar equivalente)

    // Confirm connection
    
    // Disconnect and power off fpga
    else if (received == 88) {
      is_connected = false;
      if (power_state) {
        is_power_blocked = true;
        power_off_millis = clock();
        power_state = 0;
        clr_bit(PORTD,PD2);
      }
    }
    // Read received byte as bits and set output pins

    // Reset fpga to initial state 
    else if (received == 127){
      set_bit(PORTD,PD4);
      set_bit(PORTD,PD5);
      set_bit(PORTD,PD6);
      set_bit(PORTD,PD7);
      set_bit(PORTB,PB0);
      set_bit(PORTB,PB1);
      _delay_ms(1000);       //Delay de 1 segundo
      set_bit(PORTD,PD3);
      _delay_ms(1000);       //Delay de 1 segundo
      clr_bit(PORTD,PD3);
      }
    // Toggle fpga power
    
  }
  return 0;
}
