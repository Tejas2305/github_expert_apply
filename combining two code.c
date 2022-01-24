void main()
{
    int n;
    int t=0;
    int i, space,k = 0;
    printf("Enter a number between 1 to 5");
    scanf("%d",&n);
    switch (n)
    {
    case 1:

        for (int i=1;i!=5;i++)
        {
            t=(t*10)+i;
            printf("\n%d",t);
        }
        break;
    case 2:
        for(int i=1234;i!=0;i=i/10)
        {
            printf("\n%d",i);
        }
        break;
    case 3:
        for (int i=0;i!=5;i++)
        {
            printf("\n");
            for(int c=1;c!=(i+1);c++)
            {
                printf("%d",i);
            }
        }
        break;
    case 4:
        for (int i=1;i!=5;i++)
        {
            printf("\n");
            for(int c=5;c!=(i);c--)
            {
                printf("*");
            }
        }
        break;
    case 5:

        for (i = 1; i <= 5; ++i, k = 0)
        {
            for (space = 1; space <= 5 - i; ++space) {
            printf("  ");
        }
            while (k != 2 * i - 1)
            {
                printf("* ");
                ++k;
            }
            printf("\n");
        }
        break;
    default:
        printf("Wrong choice");
        break;
    }
}
