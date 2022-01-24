void main()
{
    int d;
    float f;
    printf("Enter number of days");
    scanf("%d",&d);
    if (d<=5)
    {
        f=d*0.5;
        printf("Fine is: %f",f);
    }
    else if (d>5 && d<=10)
    {
        f=d*1;
        printf("Your fine is: %f",f);
    }
    else if (d>10 && d<=30)
    {
        f=d*5;
        printf("Your fine is: %f",f);
    }
    else if (d<30)
    {

        printf("Your membership has been suspended);
    }

}
