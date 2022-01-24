void main()
{
    int n;
    printf("Enter a number between 1 to 5");
    scanf("%d",&n);
    switch (n)
    {
    case 1:
        printf("you entered one");
        break;
    case 2:
        printf("you entered two");
        break;
    case 3:
        printf("you entered three");
        break;
    case 4:
        printf("you entered four");
        break;
    case 5:
        printf("you entered five");
        break;
    default:
        printf("Wrong choice");
        break;
    }
}
