#include <stdio.h>

int main()
{
    int i, j;

    char *table1[3][2] = {
        { "A1", "A2" },
        { "B1", "B2" },
        { "C1", "C2" },
    };

   char *table2[3][4] = {
        {"a1", "a2", "a3", "a4"},
        {"a2", "b2", "b3", "b4"},
        {"a3", "c2", "c3", "c4"},
    };

   char *table3[3][6];


   int t1rows = sizeof(table1)/sizeof(table1[0]);
   int t1col = sizeof(table1[0])/sizeof(table1[0][0]);
   int t2rows = sizeof(table2)/sizeof(table2[0]);
   int t2col = sizeof(table2[0])/sizeof(table2[0][0]);

   for(int r = 0; r<t1rows; r++) {
       for(int c = 0; c<t1col; c++) {
           table3[r][c] = table1[r][c];
       } 
   } 


   for(int r = 0; r<t2rows; r++) {
       for(int c = 0; c<t2col; c++) {
           table3[r][c+t1col] = table2[r][c];
       } 
   }



   printf("table3:\n\n");

   // detta skriver ut table3:
   for(i = 0; i < 3; i++){
     for(j = 0; j < 6; j++)
       printf("%s ", table3[i][j]);

     printf("\n");
   }

   printf("\ntable3 transposed:\n\n");
   
   char *table4[6][3];

   for(j = 0; j < 6; j++){
       for(i = 0; i < 3; i++){
           table4[j][i] = table3[i][j]; 
           printf("%s ", table4[j][i]);
       }
       printf("\n");
   }
  
   return 0;
}
