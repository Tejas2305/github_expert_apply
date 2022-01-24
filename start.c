void swap(int *, int *);
void main()
{
    int a,b;
    printf("Enter a number");
    scanf("%d",&a);
    printf("Enter b number");
    scanf("%d",&b);
    printf("value of a: %d\n value of b: %d",a,b);
    swap(&a,&b);

}
void swap(int *x, int *y)
{
    int z,a;
    z=*x;
    *x=*y;
    *y=z;
    printf("\nvalue of a: %d\n value of b: %d",*x,z);
}
