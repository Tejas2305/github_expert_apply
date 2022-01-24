void main()
{
    int c,d,temp;
    printf("Enter value of c");
    scanf("%d",&c);
    printf("Enter value of d");
    scanf("%d",&d);
    printf("Value of c is %d",c);
    printf("\nValue of d is %d",d);
    temp=d;
    d=c;
    c=temp;
    printf("\nValue of c after interchanging is %d",c);
    printf("\nValue of d after interchanging is %d",d);
}
