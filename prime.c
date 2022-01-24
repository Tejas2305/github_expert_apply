void main()
{
    int c;
    for(int n=1;n!=101;n++)
    {
        c=0;
        for (int i = 1; i <= n; i++)
        {
            if (n % i == 0)
            {
                c++;
            }
        }
        if (c == 2)
        {
            printf("\n%d is a Prime number",n);
        }
}
}
