#include <stdio.h>

int main() {
    for(int i=32;i<127;i++) {
        printf("%c ", i);
        if ((i-32) % 12 == 0) {
            printf("\n");
        }
    }

    printf("\n");
    return 0;
}
