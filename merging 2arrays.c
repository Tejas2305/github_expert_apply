void main()
{
    int a[5],b[5],c[10],i,j;
    for(i=0;i<5;i++)
    {
        scanf("%d",&a[i]);
        c[i]=a[i];
    }
    i=5;
    for(j=0;j<5;i++,j++)
    {
       scanf("%d",&b[j]);
       c[i]=b[j];
    }
    for(int z=0;z<10;z++)
        printf("%d",c[z]);


}
