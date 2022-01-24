void main()
{
    int n,temp,i;
    printf("Enter a number");
    scanf("%d",&temp);
while(i<=8)
{
    printf("Enter a number");
        scanf("%d",&n);
        if(temp>n)
        {
        }
        else if (n>temp)
        {
            temp=n;
        }
        i++;
}
printf("%d is max",temp);
}
