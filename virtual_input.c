#include <stdbool.h> // Header-file for boolean data-type.
#include <time.h>
#include <avr/io.h> // Header-file that includes the apropriate IO definitions for the device      
#include <util/delay.h> // Header-file for busy-wait delay loops

#define power_pin PD2
#define control_pin PD3
#define F_CPU 16000000UL // CPU frequency?
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
  
  while(1){
    //
    // Loop principal para comunicação e controle da placa DE2-115
    //
  }
  return 0;
}

/**teste**/
