#include<stdio.h>

int factorial(int);

int main(){
int num, fact;
printf("Enter number: ");
scanf("%d", &num);
fact = factorial(num);
printf("\nFactorial of %d is: %d\n", num, fact);
return 0;
}

int factorial(int n){
if(n==0)
	return 1;
return(n*factorial(n-1));
}
