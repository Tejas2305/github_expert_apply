void display(int *);
void main()
{
    int array[10];
    for (int i=0;i<10;i++)
        scanf("%d",&array[i]);
    display(&array);
}
void display(int *a)
{
    for (int i=0;i<10;i++,a++)
        printf("%d",*a);
}
