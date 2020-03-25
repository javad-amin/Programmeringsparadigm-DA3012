#include <stdio.h>

void swap(int *x, int *y) {
  int t = *x;
  *x = *y;
  *y = t;
}

int main()
{
  int x = 10;
  int y = 20;

  printf("(x , y) = (%d , %d)\n", x, y);

  swap(&x,&y);

  printf("(x , y) = (%d , %d)\n", x, y);

  return 0;
}

