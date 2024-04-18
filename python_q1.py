# create a function with a name avg
# which takes a variable numbers
# and returns the float of average of the numbers with 2 decimals
# if in put is only 1 number return that number with 2 decimals

def avg(*args):
    
    length = len(args)
    total = sum(args)
    if length == 1:
        return "{:.2f}".format(float(args[0]))
    average = total / length
    return "{:.2f}".format(float(average))
result = avg('D')

print(result)

