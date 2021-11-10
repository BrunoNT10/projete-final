//Programa: Leitor RFID RDM6300
//Alteracoes e adaptacoes: Arduino e Cia

//Baseado no programa original de Stephane Driussi

#include <SoftwareSerial.h>
#include <RDM6300.h>

//Inicializa a serial nos pinos 2 (RX) e 3 (TX)
SoftwareSerial RFID(2, 3);

int Led = 13;
uint8_t Payload[6]; // used for read comparisons

RDM6300 RDM6300(Payload);
int LED = 4;

void setup()
{
  pinMode(Led, OUTPUT);
  //Inicializa a serial para o leitor RDM6300
  RFID.begin(9600);
  //Inicializa a serial para comunicacao com o PC
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(8, OUTPUT);
  //Informacoes iniciais
  //Serial.println("Leitor RFID RDM6300n");
}

void loop()
{
  //Aguarda a aproximacao da tag RFID
  while (RFID.available() > 0)
  {
    digitalWrite(Led, HIGH);
    uint8_t c = RFID.read();
    if (RDM6300.decode(c))
    {
      digitalWrite(LED, HIGH);
      delay(300);
      digitalWrite(LED, LOW);
      //Serial.print("ID TAG: ");
      //Mostra os dados no serial monitor
      for (int i = 0; i < 5; i++) {
        //Serial.print(Payload[i], HEX);
        
        Serial.print(Payload[i]);        
        Serial.print("");
      }
      Serial.println();
    }
   
  }
  int estadobotao = digitalRead(7);
  if (estadobotao == 1){
    Serial.println(estadobotao);
    delay(1000);
  }

  while (Serial.available() > 0){
    digitalWrite(LED, HIGH);
    char valor = Serial.read();
    Serial.println("recebi um valor");
    
    if (Serial.read() == 115){
      digitalWrite(LED, HIGH); 
    }
    
  }
  digitalWrite(8, HIGH);
  delay(1000);
  digitalWrite(8, LOW);
  delay(1000);
  
}
