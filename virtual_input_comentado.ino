/** Inicialização das variáveis **/
byte power_pin = 2;            //configura pino 2 como pino de alimentação da fpga
byte control_pin = 3;           //configura pino 3 como pino de controle
int power_state = LOW;      // variável que indica se a FPGA está ligada/desligada.      
int received;                        // variável para receber dados vindo da comunicação serial com a GUI                            
byte bitread;                      //variável auxiliar para ler bit a bit  
//bool is_sent = false;
bool is_connected = false;  //variável para verificar a conexão da FPGA com a GUI        
bool is_power_blocked = false; // variável para bloquear o botão de ligar/desligar a FPGA.

unsigned long beam_millis = millis(); // timestamp for last beam sent
//unsigned long sent_millis;            // ts for output clock state change
unsigned long input_millis;           // ts for last input received
unsigned long power_on_millis;        // ts for how long the board is on
unsigned long power_off_millis;       // ts for last power toggle

/** Inicializa a comunicação serial com o computador através
 * do monitor serial e os configurar os pinos digitais de 2 a 9 como output.
**/
void setup()
{
  // Configura a taxa de transmissão da porta serial para 9600 bits/segundo
  Serial.begin(9600); 
  // Configura os pinos de 2 a 9 como saída
  pinMode(2, OUTPUT); 
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  
  // Desativa os pinos de 4 a 9 (zera a tensão)  
  for (int j = 4; j<10; j++) 
    digitalWrite(j, LOW);
}
/** Loop principal para comunicação e controle da placa DE2-115**/
void loop()
{
  
// Verifica se há dados para leitura na porta serial, se não houver entra no while e a cada 1 segundo verifica a conexão com a GUI.
while(!Serial.available()) {  
    // Send beacon every 1 second
    if ((millis() - beam_millis) > 1000) {
      beam_millis = millis();
      if (is_connected)       
Serial.write(50);       // informa à aplicação que o dispositivo está devidamente conectado à ela.
      else
        Serial.write(40);     // informa a falta de conexão para a aplicação.
    }

    // Change output control signal state
    //if (is_sent && (millis() - sent_millis) > 100) {
    //  digitalWrite(control_pin, LOW);
    //  is_sent = false;
    //}

    /** Desbloqueia o botão de power/off da FPGA 10s após a última alternância de estado.**/
    if (is_power_blocked && (millis() - power_off_millis) > 10000)
      is_power_blocked = false;

    /** Disconnect and turn off fpga if user is idle for 10 min **/
    if (is_connected && (millis() - input_millis) > 595000) {
      is_connected = false;
      if (power_state) {
        is_power_blocked = true;
        power_state = LOW;
        digitalWrite(power_pin, power_state);
        power_off_millis = millis();
      }
    }

    // Turn fpga off after 10 min of use
    if (power_state && (millis() - power_on_millis) > 600000) {
      is_power_blocked = true;
      power_state = LOW;
      digitalWrite(power_pin, power_state);
      power_off_millis = millis();
    }
  }
  input_millis = millis();        // atualiza o tempo de entrada com o valor de tempo atual
  received = Serial.read();    //lê o dado enviado pelo computador

  // Confirm connection
  if (!is_connected) {
     // GUI confirma conexão com o arduíno
    if (received == 41) {
      // Arduino responde à mensagem da GUI
Serial.write(42);
      is_connected = true;
    }
  }

 /** Disconnect and power off fpga **/

// Mensagem da GUI para o arduino para desligar a fpga
  else if (received == 88) { 
    is_connected = false;
    if (power_state) {
      is_power_blocked = true;
      power_off_millis = millis();
      power_state = LOW;
      digitalWrite(power_pin, power_state);
    }
  }

/** Bloco para ler os bits da variável received e configurar os pinos de saída (4-9) com o código referentes ao sw ou button acionado e envia para a fpga decodificar com o módulo virtual_input.v **/

  // Verifica se a mensagem enviada pela GUI corresponde à alteração dos SWs ou Bottons
  else if (received >= 0 && received < 22) {
    // Configura os pinos de 4 a 9 com o valor de saída correspondente à received
    for (int j = 0; j<6; j++) {        
      bitread = bitRead(received, j);     // retorna o bit na posição j de received
      digitalWrite(j+4, bitread);
    }
    delay(1);
    // define o control_pin (pino 2) como HIGH para que a fpga faça a leitura da mensagem enviada
    digitalWrite(control_pin, HIGH);
    delay(1);
// define o control_pin (pino 2) como LOW para que a fpga faça a leitura da mensagem enviada
    digitalWrite(control_pin, LOW);
    //is_sent = true;
    //sent_millis = millis();
  }

/** Aplica um reset na fpga, definindo seus sw e botton ao estado inicial da placa. Ao colocar os pino de 4 a 9 no estado HIGH, no interface virtual_imput.v na fpga vai levar ao caso default **/
  else if (received == 127) {
    for (int j = 0; j<6; j++) {      //loop para definir os pinos 4 a 9 como HIGH
      digitalWrite(j+4, HIGH);
    }
    delay(1);
    digitalWrite(control_pin, HIGH);
    delay(1);
    digitalWrite(control_pin, LOW);
    //is_sent = true;
    //sent_millis = millis();
  }
 /** Bloco para ligar ou desligar a placa a partir do teclado virtual, quando o usuário altera o estado do botão power on/off no teclado a GUI envia a mensagem 90 para o arduino, e ele altera o estado da placa a partir do estado anterior da mesma.**/
  else if(received == 90) {
       if (is_power_blocked)
      Serial.write(92);
       else if (power_state) {
      is_power_blocked = true;
      power_off_millis = millis();
      power_state = LOW;
      digitalWrite(power_pin, power_state); //desativa pino de energia
      Serial.write(91);
         } else {
      is_power_blocked = true;
      power_off_millis = millis();
      power_state = HIGH;
      digitalWrite(power_pin, power_state); //ativa pino de energia
      Serial.write(91);
    }
  }
}
