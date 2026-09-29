def claim_item():

    a = {}

    print('---->  CLAIM ITEM  <----')

    b = input('Enter The Item You Want To Claim --> ')
    c = input('Enter Your Name --> ')
    d = input('Describe The Item To Prove It Is Yours --> ')

    a['Item'] = b
    a['Name'] = c
    a['Proof'] = d
    a['Status'] = 'Pending'

    with open("claims.txt", "a") as f:
        f.write(str(a))

    print('Claim Submitted Successfully !!')
    print('Status: Pending')


def view_claims():

    with open("claims.txt","r") as f:
        x = f.read()

    print('----> CLAIMS <----')
    print(x)
