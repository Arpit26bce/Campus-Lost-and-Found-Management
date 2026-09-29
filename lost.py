
def lost_item():
    l=[]
    a={}

    print('---->  Adding Lost Item  <----')
    b=input('Enter The Item Lost ---> ')
    c=input('Enter The Colour Of Item ---> ')
    d=input('Enter Location Where It Was Last Seen ---> ')
    e=input('Enter Date Item Was Lost ---> ')
    a['Item']=b
    a['Colour']=c
    a['Location']=d
    a['Date']=e
    l.append(a)
    with open("lost.txt","w") as f:
        f.write(str(l))
    print('--->  Item Added In Lost Items  <---')
def view_items():
    with open("lost.txt","r") as f:
        x=f.read()
    print(x)




        

    

    

