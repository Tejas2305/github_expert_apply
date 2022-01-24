void main()
{

int n;
printf("Enter a number to be check for positive or negative");
scanf("%d",&n);
if (n>0)
{
    printf("%d is a positive number",n);
}
else if(n<0)
{
    printf("%d is a negative number",n);
}
else if (n==0)
{
    printf("The number is 0");
}

}
