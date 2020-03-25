#include <stdio.h>
#include <string.h>

int main()
{
  char str[] = "!looc os si 2103AD";
  int n = strlen(str);

  for (int i = 0; i<=n-1; i++) {
      printf("%c", str[n-i] );
  }

  printf("\n");
  return 0;
}
