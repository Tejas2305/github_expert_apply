//bs=1500
//ha=10%
//da=90%
//bs=1500>=
//ha=5000
//da=98%
void main()
{
    int bs;
    float ha,da,gs;
    printf("Enter your basic salary");
    scanf("%d",&bs);
    if (bs<1500)
    {
        ha=bs*0.1;
        da=bs*0.9;
        gs=bs+ha+da;
        printf("Your gross salary is %f",gs);
    }
    else if (bs>=1500)
    {
        ha=500;
        da=bs*0.98;
        gs=ha+bs+da;
        printf("Your gross salary is %f",gs);
    }
}
