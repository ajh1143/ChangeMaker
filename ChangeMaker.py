from collections import Counter
import matplotlib.pyplot as plt

def make_change(denoms, value):
    """
    :param denoms: list of denomination types
    :param value: total change due 
    :return: Counter dict of denominations to achieve total value
    """
    #Create copy of input denomination/coin list
    denoms = denoms.copy()
    #Create empty list of used coins
    denom_list = []
    #While value above 0 and denom length above 0
    while value >= 0 and len(denoms) > 0:
        #Set max coin value
        max_denom = max(denoms)
        #Check if coin too large to use
        if value - max_denom >= 0:
            #Add used coin to list of used coins
            denom_list.append(max_denom)
            #print("Adding" + str(max_denom))
            #Set new value after subtracting used coin
            value = (value - max_denom)
        #If coin too large to be used, remove from list
        else:
            #print("Removing" + str(max_denom))
            denoms.remove(max_denom)
    # Generate Counter() of coins used
    coins = Counter(denom_list)
    # Return Counter() of coins used
    return coins

def plot_change(coinery):
    """
    :param coinery: Counter dict of denominations and counts
    Generate Plot of denominations by count w/ title and axis labels
    """
    # Generate coin type and value
    labels, values = coinery.items()
    # Generate bar plot using labels and values
    plt.bar(labels, values)
    # Add title to plot
    plt.title("Change Due To Customer")
    # Add x-axis label
    plt.xlabel("Coin Types")
    # Add y-axis label and rotate horizontally 
    plt.ylabel("Counts").set_rotation(0)
    # Show plot
    plt.show()

def print_change(coinery):
    """
    :param coinery: Counter dict of denominations and counts
    Prints k,v pairs of denomination type, counts, and total value
    """
    # Create k,v pairs of coin value and amount
    coins_used =[{"Coin Value": k, "Amount": v} for k, v in coinery.items()]
    # For each coin used, print coin and amount
    for each in coins_used:
        print(each)
    # Break to new line
    print("\n")

if __name__ == "__main__":
    total_due=[10,15,21,34]
    coin_types=[1,3,5,7,10]
    
    for each in total_due:
       change = make_change(coin_types, each)
       print("Total Value: "+str(each))
       print_change(change)
