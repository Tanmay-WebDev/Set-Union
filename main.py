# Set Union

setc1 = {"apple", "banana", "cherry" , "grapes", "mango", "orange"}
setc2 = {"apple", "cherry" , "grapes", "mango", "orange", "kiwi", "papaya", "watermelon"}

print("Original Set 1: ")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\n Union Of Above Sets: " )
print(setc)