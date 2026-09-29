from admin import admin_login
from claim import claim_item, view_claims
from find import search_item
from lost import *
from found import *
import time

def main():
    choice=0
    while choice!=9 :
        print()
        print("---> Lost And Found <---")
        print()
        print('---> MENU <---')
        print()
        print('--->  1.Add Lost Item  <---')
        print('--->  2.View Lost Items  <---')
        print('--->  3.Add Item Found  <---')
        print('--->  4.View Items Found  <---')
        print('--->  5.Find Lost Item  <---')
        print('--->  6.Claim Item  <---')
        print('--->  7.View Item Claims  <---')
        print('--->  8.Admin Login  <---')
        print('--->  9.End Program  <---')
        print()
        choice=int(input('---->  Enter Choice  ---->'))
        if choice == 1:
            print()
            lost_item()
        elif choice == 2:
            print()
            view_items()
        elif choice == 3:
            print()
            found_item()
        elif choice == 4:
            print()
            view_items_found()
        elif choice == 5:
            print()
            search_item()
        elif choice == 6:
            print()
            claim_item()
        elif choice == 7:
            print()
            view_claims()
        elif choice == 8:
            print()
            admin_login()
        elif choice == 9:
            print()
            print('Thank You For Using This Program')
        else :
            print()
            print('Invalid Choice !!')
        time.sleep(2)
main()



    



