
with open('1input.txt', 'r') as infile:
    line = infile.read()  

numbers = list(map(int, line.split()))

if len(numbers) != 10:
    print("В файле должно быть ровно 10 чисел.")
else:
    
    product = 1
    for num in numbers:
        product *= num

    
    with open('1output.txt', 'w') as outfile:
        outfile.write(str(product))
