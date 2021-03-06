# ChangeMaker
Generate change to customers and plot counts per coin type

## Imports
```Python3
from collections import Counter
import matplotlib.pyplot as plt
```

## Calculate Change Due
```Python3
def make_change(denoms, value):
    """
    :param denoms: list of denomination types
    :param value: total change due 
    :return: Counter dict of denominations to achieve total value
    """
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
```
## Plotting    
(Under Construction)
```Python3
def plot_change(coinery):
    """
    :param coinery: Counter dict of denominations and counts
    Generate Plot of denominations by count w/ title and axis labels
    """
    labels, values = coinery.items()
    plt.bar(labels, values)
    plt.title("Change Due To Customer")
    plt.xlabel("Coin Types")
    plt.ylabel("Counts").set_rotation(0)
    plt.show()
```

## Generate Output
```Python3
def print_change(coinery):
    """
    :param coinery: Counter dict of denominations and counts
    Prints k,v pairs of denomination type, counts, and total value
    """
    x=[{"Coin Value": k, "Amount": v} for k, v in coinery.items()]
    for each in x:
        print(each)
    print("\n")
```
## Example Output:    
Parameters: 
    `total_due = [10, 15, 21, 34]`
    `coin_types = [1, 3, 5, 7, 10]`
    
<img src="https://github.com/ajh1143/ChangeMaker/blob/master/Images/coins.png" class="inline"/><br>

## Example Main
```Python3
if __name__ == "__main__":
    total_due=[10,15,21,34]
    coin_types=[1,3,5,7,10]
    
    for each in total_due:
       change = make_change(coin_types, each)
       print("Total Value: "+str(each))
       print_change(change)
```
