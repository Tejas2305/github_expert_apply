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
    int i,j,min=0,max=0;
    min=max=a[0][0];
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            if(min>a[i][j])
            {
                min=a[i][j];
            }
            else if(max<a[i][j])
            {
                max=a[i][j];
            }
        }
    }
    printf("Max is: %d\nMin is: %d",max,min);
}
