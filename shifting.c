void display(int [][3]);
void main()
{
    int i,j,a[3][3];
    for (i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
            scanf("%d",&a[i][j]);
    }
    display(a);
}
void display (int a[][3])
{
    int i,j,t[3][3];
    for(j=0;j<3;j++)
        t[j][0]=a[j][0];
    for(j=0;j<3;j++)
        a[j][0]=a[0][j];
    for(j=0;j<3;j++)
        a[0][j]=t[j][0];
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            printf("\n%d",a[i][j]);
        }
    }
}
