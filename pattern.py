increment = True;
i=1;

while i!=0:
    if(i==5):
        increment=False;

    for j in range(i):
        print('*', end=' ');
    print();
        
    if(increment):
        i=i+1;
    else:
        i=i-1;

   
