void p1(int);
void main()
{
    int i=123456;
    p1(i);

}
void p1(int i)
{
    for(;i!=0;i=i/10)
        {
            printf("\n%d",i);
        }
}
