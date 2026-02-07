# Print numbers from 1–100 but replace multiples of 3 with 'Fizz' and 5 with 'Buzz'.

for i in range(1,101):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)