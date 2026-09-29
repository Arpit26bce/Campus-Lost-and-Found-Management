def found_item():
    l=[]
    a={}

    b=input('Enter The Item Found --> ')
    c=input('Enter The Colour Of The Item --> ')
    d=input('Enter Location Item Found --> ')
    e=input('Enter Date Item Was Found --> ')
    a['Item']=b
    a['Colour']=c
    a['Location']=d
    a['Date']=e
    l.append(a)
    with open("found.txt","a") as f:
        f.write(str(a))
def view_items_found():
    with open("found.txt","r") as f:
        x=f.read()
    print(x)
