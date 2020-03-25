#include <stdio.h>
#include <string.h>

void forward(char message[], int start, int end, int key){
    for (int i = 0; i<strlen(message); i++){
        if (message[i]>=start && message[i]<=end){
            if (message[i]+key > end){
                message[i] = message[i]+key-26;
            } else {
                message[i] = message[i]+key;
            }
        }
    }
}

void backward(char message[], int start, int end, int key){
    for (int i = 0; i<strlen(message); i++){
        if (message[i]>=start && message[i]<=end){
            if (message[i]-key < start){
                message[i] = message[i]-key+26;
            } else {
                message[i] = message[i]-key;
            }
        }
    }
}

void encrypt(char message[], int key)
{
    forward(message, 65, 90, key);
    forward(message, 97, 122, key);
}


void decrypt(char message[], int key)
{
    backward(message, 65, 90, key);
    backward(message, 97, 122, key);
}


int main()
{
  char message[] = "This message is super secret!";
  int key = 3;

  encrypt(message,key);

  printf("Encrypted message: %s\n", message);

  decrypt(message,key);

  printf("Decrypted message: %s\n", message);

  return 0;
}
