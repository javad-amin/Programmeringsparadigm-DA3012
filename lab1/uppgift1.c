#include <stdio.h>

int main()
{
  int secret = 63;
  int guess;
  while(1) {
      printf("Guess a number between 1 and 99: ");
      if (scanf("%d", &guess) != 1) {
          printf("What have you been smoking?!\n");
          break;
      }
      if (guess < 1 || guess >99) {
         printf("You must guess a number between 1 and 99!\n");
      }
      else if (guess < secret) {
          printf("Too low!\n");
      }
      else if (guess > secret) {
          printf("Too High!\n");
      }
      else if (guess == secret) {
          printf("Correct!\n");
          break;
      }
  }


  return 0;
}
