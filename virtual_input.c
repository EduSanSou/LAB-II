#include <stdbool.h> // Header-file for boolean data-type.
#define F_CPU 16000000UL // CPU frequency?
#include <avr/io.h> // Header-file that includes the apropriate IO definitions for the device      
#include <util/delay.h> // Header-file for busy-wait delay loops

/** Inicialização das variáveis **/

unsigned char power_pin = 2;
unsigned char control_pin = 3;
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

unsigned long beam_millis = millis(); // timestamp for last beam sent (buscar forma para C)
// unsigned long sent_millis;            // ts for output clock state change
unsigned long input_millis;     // ts for last input received
unsigned long power_on_millis;  // ts for how long the board is on
unsigned long power_off_millis; // ts for last power toggle

int main() {
  DDRD = 0b11111100; //configura os pinos 2 a 7 como saída
  DDRB = 0b00000011; //configura os pinos 8 a 9 como saída
  while(1){
    PORTD = 0b11110000; //desativa os pinos 4 a 7 (zera a tensao)
    PORTB = 0b00000011; //desativa os pinos 8 a 9 (zera a tensao)
    //
    // Loop principal para comunicação e controle da placa DE2-115
    //
  }
  return 0;
}
