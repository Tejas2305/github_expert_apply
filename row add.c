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
    int i,j,t=0;
    for(j=0;j<3;j++)
    {
       t=a[j][0];
    }
    printf("addition is %d",t);
}
