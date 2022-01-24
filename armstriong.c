void main()
{
    int a,t,temp;
    printf("Enter a number");
    scanf("%d",&a);
    temp=a;
    for(;a!=0;a=a/10)
    {
       t=t+(a%10)*(a%10)*(a%10);
    }

    if (temp==t)
    {
        printf("%d is a armstrong number",t);
    }
    else
    {
        printf("%d is not a armstrong number",temp);
    }
}
