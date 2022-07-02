#include <Wire.h>

void setup()
{
  Wire.begin(0x0A);                
  Wire.onReceive(receiveEvent);
  digitalWrite(SCL, LOW);
  digitalWrite(SDA, LOW);
  Serial.begin(115200);          
}

void loop() {
  if(Serial.available() > 0){
    check_btn_send = Serial.read(); //arduino recebe mensagem 
    if(check_btn_send==10){ //confere se a mensagem = 10
      Serial.write(20); //caso igual, envia mensagem = 20
      mov_string = Serial.read(); //arduino armazena string de movimento
    }
  }
}

void receiveEvent(int numBytes)
{
  while (1 < Wire.available())
  { 
    char td = Wire.read();
    Serial.print(td);        
  }
  int valor = Wire.read();    
  Serial.println("");
  Serial.println(valor, HEX);   
  Serial.println(valor, BIN);
  Serial.println(valor, OCT);
  Serial.println(valor);       
}
