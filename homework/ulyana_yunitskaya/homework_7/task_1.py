my_number = int(10)

while True:
    user_input = int(input('Write the number'))
    if user_input != my_number:
        print('Try again')
        continue
    else:
        break
print('Congratulations! You guessed it!')
