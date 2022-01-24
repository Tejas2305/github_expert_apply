void main()
{
    int ch,n1,n2;
    printf("Enter a number");
    scanf("%d",&n1);
    printf("Enter a number");
    scanf("%d",&n2);
    printf("What should i do?\n1 for +\n2 for -\n3 for *\n4 for /\n5 for remeber");
    scanf("%d",&ch);
    switch (ch)
    {
    case 1:
        printf("%d",n1+n2);
        break;
    case 2:
        printf("%d",n1-n2);
        break;
    case 3:
        printf("%d",n1*n2);
        break;
    case 4:
        printf("%d",n1/n2);
        break;
    case 5:
        printf("%d",n1%n2);
        break;
    default:
        printf("Wrong choice");
        break;
    }
}
