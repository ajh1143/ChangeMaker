from collections import Counter
import matplotlib.pyplot as plt

def make_change(denoms, value):
    denoms = denoms.copy()
    denom_list = []
    while value >= 0 and len(denoms) > 0:
        max_denom = max(denoms)
        if value - max_denom >= 0:
            denom_list.append(max_denom)
            #print("Adding" + str(max_denom))
            value = (value - max_denom)
        else:
            #print("Removing" + str(max_denom))
            denoms.remove(max_denom)
    coins = Counter(denom_list)
    return coins

def plot_change(coinery):
    labels, values = coinery.items()
    plt.bar(labels, values)
    plt.title("Change Due To Customer")
    plt.xlabel("Coin Types")
    plt.ylabel("Counts").set_rotation(0)
    plt.show()

def print_change(coinery):
    x=[{"Coin Value": k, "Amount": v} for k, v in coinery.items()]
    for each in x:
        print(each)
    print("\n")

if __name__ == "__main__":
    total_due=[10,15,21,34]
    coin_types=[1,3,5,7,10]
    
    for each in total_due:
       change = make_change(coin_types, each)
       print("Total Value: "+str(each))
       print_change(change)
