def guessing(min_num, max_num):
    """
    Function is computing next guest
    """
    result = int(((max_num - min_num)/2)+min_num)
    return result

def answer():
    """
    Function is waiting for an answer from user
    """
    while True:
        while True:
            result = input("Choose an answer: 1 - 'Too much', 2 - 'Too little', 3 - 'You guessed!'")
            try:
                result = int(result)
                break
            except ValueError:
                print("Don't cheat!")
        if result in [1, 2, 3]:
            break
    return result



min_number = 0
max_number = 1000
print(f"Think of a number from {min_number} to {max_number} and I will guess it in max ten moves.")

i = 1
while True and i < 11:
    result = guessing(min_number,max_number)
    print(f"I'm guessing ({i}) {result}")
    is_win = answer()
    i += 1
    if is_win == 1:
        max_number = result
    elif is_win == 2:
        min_number = result    
    else:
        print("I won!")
        break
if i > 10:
    print("I lost")