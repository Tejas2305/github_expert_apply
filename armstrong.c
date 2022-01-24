void main()
{
    int a,t,temp;

    for (int i=1;i<501;i++)
    {a=i;

        t=0;
        for(;a!=0;a=a/10)
        {
        t=t+(a%10)*(a%10)*(a%10);
        }

        if (i==t)
        {
            printf("\n%d is a armstrong number",i;
        }

    }
}
