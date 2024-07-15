# WE BALL
# We take two nums(numin,numax), one is the smallest, other is the biggest, after each operation we increase from the first number by one, 
# Once the first number reaches numax, set it back to numin, and increase the second number by 1 
# Once both numbers reach numax, break
# We add all the results to the list, any repeating results will not get added
# After all the calculations, sort the list

numlist = []

def fermi():
  
  # Asking for nums politely :3
  numin, numax, step = int(input("input the smallest number ")), int(input("input the biggest number ")) + 1, int(input('input the power of numbers '))

  # Setting up the calculation
  num1, num2 = numin, numin

  # This while loop will keep doing calculations until both numbers(num1, num2) are equal to numax
  while num1 and num2 != numax and numax:

    # We do num1**step + num2**step = result**step, and print the result(res)
    restepd = num1 ** step  +  num2 ** step
    res = restepd ** (1/step)

    # Check if the number has anything after the dot, print only the numbers that don't have anything after the dot
    # Dotcheck looks for where the dot is, so we could compare everything behind it with the ".0"
    dotcheck = str(float(res)).find('.')
    
    #zerornot checks all the numbers after the dot
    zerornot = str(float(res))[dotcheck+1:]

    #use zerornot to find all the numbers w/o anything after the dot
    if zerornot == '0' and int(res) not in numlist:
      numlist.append(int(res))

    # We check if there's need to increase the numbers
    # If num1 != numax then += 1
    if num1 != numax - 1:
      num1 += 1

    # If num1 == numax then set it to 1 and num2 += 1
    elif num1 == numax -1  and num2 != numax:
      num1 = numin
      num2 += 1
    # If numbers are numax, operation breaks
  
  # Sort the list
  numlist.sort()

  # Print the list
  print(numlist)

fermi()