######################################################
# Zachary Norman and Erjie Zhang
# Input  - Customer names and purchase amounts
#        - Number of top customers
# Output - The names of the top customers
# Processing - This program finds the top customers
#              and returns a list of them for display
######################################################

##########
# DRIVER #
##########
def main():
    customerData = []

    # Input
    purchaseAmount = int(input("Enter the customer's purchase amount: "))
    customerName = input("Enter the customer's name: ")
    customerData.append((customerName, purchaseAmount))

    while purchaseAmount != 0:
        purchaseAmount = int(input("Enter the customer's purchase amount, or 0 to exit: "))

        if purchaseAmount != 0:
            customerName = input("Enter the customer's name: ")
            customerData.append((customerName, purchaseAmount))

    print()
    topN = int(input("Enter the number of top customers to display: "))

    print("\n")
    # Output
    print("Names of best customers: " + ", ".join(nameOfBestCustomers(customerData, topN)))


#############
# FUNCTIONS #
#############
def nameOfBestCustomers(customerData, topN):
    """
    Finds the topN number of top customers and returns a list of them in order
    :param customerData: A list of tuples that includes the customer's name and purchase amount
    :param topN: The number of top customers to return
    :return: A list of strings of the names of the top customers in order
    """

    # Check if the number of top customers to return is greater than the number of customers
    if len(customerData) <= topN:
        return [data[0] for data in customerData]

    # Copy the customer data list
    customerDataCopy = customerData[:]
    output = []

    for i in range(topN):
        # Obtain the index of the top purchase amount
        index = [data[1] for data in customerDataCopy].index(max([data[1] for data in customerDataCopy]))

        # Add the name of the person to the output
        output.append(customerDataCopy[index][0])

        # Remove the customer from the copied list
        del customerDataCopy[index]

    return output


main()
