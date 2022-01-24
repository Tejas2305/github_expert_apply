void main()
{

    printf("Enter a number");
    int n,o=0,e=0;
    scanf("%d",&n);
    while(n>0)
    {
        if (n%2==0)
        {
            printf("\n%d even",n);
            e++;
        }
        else
        {
            printf("\n%d odd",n);
            o++;
        }
        n--;
    }

    printf("\n%d even numbers",e);
    printf("\n%d odd numbers",o);
}
