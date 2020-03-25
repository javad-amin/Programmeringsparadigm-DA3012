#include <stdio.h>

int sort(int xs[], int n) {
    int i = 1;
    int j;
    int tmp;
    loopi:
        tmp = xs[i];
        j = i;

    loopj:
        xs[j] = xs[j-1];

        if (j > 0 && tmp < xs[j-1]) {
            j=j-1;
            goto loopj;
        } 

        if (i<n) {
            i++;
            xs[j]=tmp;
            goto loopi;
        }

    return 0;
}

int main()
{
    int xs[] = { 12, -3, 27, 2, 3, 1, 9 };
    
    sort(xs,7);
    
    int i=0;
    print:
        printf("%d ",xs[i]);
        if (i<6){
            i++;
            goto print;
        }
    
    printf("\n");
    return 0;
}
