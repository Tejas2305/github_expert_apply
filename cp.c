void main()
{
    float sp,p,c;
    printf("Enter selling price:");
    scanf("%f",&sp);
    printf("Enter Profit:");
    scanf("%f",&p);
    sp=sp/15;
    p=p/15;
    c=sp-p;
    printf("Cost price is: %f",c);
}
