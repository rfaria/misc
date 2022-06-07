#include <stdio.h>

int main() {
    int n, i;
    float avg, point;
    int again=1;
    
    while(again){
        avg=0, point=0;
        
        printf("Enter the sample size: ");  
        scanf("%d", &n);
        
        for(i=1; i<=n; i++){
            printf("Sample point %d: ", i);  
            scanf("%f", &point);
            avg = avg + point;
        }
       
        avg = avg/(float)n;
        printf("The average is %f", avg);
    
        printf("\nDo you want to go again? (1/0)");  
        scanf(" %d", &again);
    }
    printf("Thanks for using the program!");
    return 0;
}
