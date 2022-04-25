"""
You are visiting a farm to collect fruits. The farm has a single 
row of fruit trees. You will be given two baskets, and your goal 
is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character 
represents a fruit tree. The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit 
to how many fruit a basket can hold. You can start with any tree, 
but you can’t skip a tree once you have started.

You will pick exactly one fruit from every tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
"""
# implementation
def fruits_into_baskets(fruits):
    start, end = 0,0
    l = {}
    while end < len(fruits):
        if fruits[end] not in l:
            l[fruits[end]] = 0
        l[fruits[end]] += 1
        while len(l) > 2:
            l[fruits[start]] -= 1
            if l[fruits[start]] == 0:
                del l[fruits[start]]
            start += 1
        end += 1
    return end - start

# examples
def main():
  print("Maximum number of fruits: " 
           + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " 
           + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()
