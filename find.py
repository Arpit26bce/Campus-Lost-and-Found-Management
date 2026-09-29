def search_item():

    print('---->  SEARCH  <----')
    print('1. Search Lost Items --->')
    print('2. Search Found Items --->')

    choice = input('Enter Your Choice --> ')

    search = input('Enter The Item You Want To Search --> ')

    if choice == '1':

        with open("lost.txt", "r") as f:
            x = f.read()

        if search.lower() in x.lower():
            print('Item Found In Lost Items !!')
            print(x)
        else:
            print('Item Not Found')

    elif choice == '2':

        with open("found.txt", "r") as f:
            x = f.read()

        if search.lower() in x.lower():
            print('Item Found In Found Items !!')
            print(x)
        else:
            print('Item Not Found !!')

    else:
        print('Invalid Choice !!')