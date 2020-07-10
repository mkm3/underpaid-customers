def find_underpaid_customers(path):
    """ Identify which customers underpaid """

    print()
    print("UNDERPAID CUSTOMER LIST:")
    print()

    the_file = open(path)
    # assigning variable to our open function, passing through produce report (path)
    melon_cost = 1.00

    for line in the_file:
    # iterating through each line of the produce report

        line = line.rstrip()
        #removes the whitespace to the right of the string

        words = line.split('|')
        #item is created by split string when "|" is located in line

        list_number = words[0]
        customer_name = words[1]
        customer_melons = float(words[2])
        customer_paid = float(words[3])
        #variables for our print statement below

        customer_expected = customer_melons * melon_cost
        #calculating the expected price for the total bill
        if customer_expected > customer_paid:
        #use if statement to get evaluate whether cust_expected is greater that cust_paid
        #if greater, print customer info
          print("Customer: {}".format(customer_name))
          print("List #: {}".format(list_number))
          print("Expected Pay: ${}".format(customer_melons))
          print("Paid: ${}".format(customer_paid))
          print()


    the_file.close()


find_underpaid_customers("customer-orders.txt")

