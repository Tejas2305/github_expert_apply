void main()
{

    char ch;
    printf("Enter a character");
    scanf("%s",ch);
    if (ch>=65 && ch<=90)
    {
        printf("Capital letter");
    }

    else if (ch>=97 && ch<=122)
    {
        printf("Small letter");
    }
    else if (ch>=48 && ch<=57)
    {
        printf("Number");
    }
    else
    {
        printf("special symbol")
    }
}
