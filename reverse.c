void main()
{
    int a,t;
    printf("Enter a number");
    scanf("%d",&a);
    for(;a!=0;a=a/10)
    {  t=t*10;
       t=t+(a%10);

    }
    printf("%d",t);
}
