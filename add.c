void main()
{
    int a[5],i,t;
    t=0;
    printf("enter 4 element of array");
    for(i=0;i<5;i++)
    {
        scanf("%d",&a[i]);
        t=t+a[i];
    }
    printf("The addition is %d",t);
}
