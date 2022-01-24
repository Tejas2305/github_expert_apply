void main()
{
    int n,t=1;
    printf("Enter a number");
    scanf("%d",&n);
    do
    {
        t=n*t;
        n--;
    }
    while(n>=1);
    printf("%d",t);
}
