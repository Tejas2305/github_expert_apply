//if 1000 10%
// if not 0%
void main()
{
    int p,q;
    float t;
    printf("Enter price of product");
    scanf("%d",&p);
    printf("Enter quantity:");
    scanf("%d",&q);
    t=q*p;
    if (p==1000)
    {
        printf("discount applied");
        printf("\npls pay %f",t-(t*0.1));
    }
    else if (p<1000)
    {
        printf("no discount applied");
        printf("\npls pay %f",t);
    }
}
