void main()
{
    int x1,y1,x2,y2,x3,y3;
    printf("Enter the cordinates");
    scanf("%d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3);
    if (x1==x2==x3 || y1==y2==y3)
    {
        printf("They are on same plane");
    }
    else {
        printf("They don't lie on same line");
    }
}
