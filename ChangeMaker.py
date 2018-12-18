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

Denoms1 = [1, 5, 10, 25]  # <-- US denominations
Denoms2 = [1, 4, 5]        # <-- 'Weird' denominations
values = [8, 11, 17, 41, 105]

for each in values:
   change = make_change(Denoms1, each)
   print("Total Value: "+str(each))
   print_change(change)
