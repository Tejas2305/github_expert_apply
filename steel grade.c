void main()
{
    int st,h;
    float c;
    printf("Enter hardness of steel");
    scanf("%d",&h);
    printf("Enter carbon content in steel");
    scanf("%f",&c);
    printf("Enter tensil streangth of steel");
    scanf("%d",&st);

    if (c>=0.6 && h>=50 &&st>=5600)
    {
        printf("Grade 10 steel");
    }
    else if (c>=0.6 && h>=50)
    {
        printf("Grade 9 steel");
    }
}
