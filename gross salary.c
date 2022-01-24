void main()
{
    int bs,gs,da,ha;
    printf("Enter your basic salary:");
    scanf("%d",&bs);
    da=bs*0.4;
    ha=bs*0.2;
    gs=bs+da+ha;
    printf("Your da is: %d",da);
    printf("\nYour ha is: %d",ha);
    printf("\nSo your gross salary is: %d",gs);
}
