
#include <stdio.h>
#include <stdlib.h>

void insert_in_sorted(int x, int * xs, int n)
{
  // här ska ni skriva kod
  int *ptr = xs + n - 1;
  while (ptr >= xs && *ptr > x) {
    *(ptr + 1) = *ptr;
    ptr--;
  }
  *(ptr + 1) = x;
}

int *insertion_sort(int *xs, int n)
{
  // initialisera en lista av rätt storlek
  int *out = malloc(n * sizeof(int));

  // här ska ni också skriva kod
  int i = 0;
  int *ptr = xs;
  while (i < n) {
    insert_in_sorted(*(ptr++), out, i);
    i++;
  }

  return out;
}

int main () {
  int list[] = { 12, -3, 27, 2, 3, 1, 9 };

  // beräkna längden på list
  int n = sizeof(list) / sizeof(int);

  int * xs = insertion_sort(list,n);

  for (int i=0;i<n;i++)
    printf("%d ",*(xs + i));

  printf("\n");
  return 0;
}
