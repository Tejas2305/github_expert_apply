void main()
{
    int a[3][3],b[3][3],j,t,i;
    t=0;
    printf("Enter number of array 1");
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            scanf("%d",&a[i][j]);
            t=t+a[i][j];
        }
    }
    printf("Enter number of array 2");
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            scanf("%d",&b[i][j]);
            t=t+a[i][j];
        }
    }
    printf("The addition is %d",t);
}
