#!/usr/bin/env python3

# Created by: Nika Zamani
# Created on: April 2021
# This program calculates total from subtotal and tax


import constants


def main():
    # this function calculates total from subtotal and tax
    
    # input
    sub_total = float(input("Enter the subtotal: $"))
    
    # process
    tax = sub_total * constants.HST
    total = sub_total + tax
    
    # output
    print("")
    print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}"
        .format(tax, total))
        
        
if __name__ == "__main__":
    main()
