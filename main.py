from flask import Flask, request

app = Flask(__name__)

def guessing(min_num, max_num):
    """
    Function is computing next guess
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



@app.route('/', methods=['GET','POST'])
def guess():
    if request.method == "GET":
        Computer_guess_min = 0
        Computer_guess_max = 1000
        page = f'''
            <form action="/" method="POST">
            
            <input type=hidden id="Computer_guess_min" name="Computer_guess_min" value={Computer_guess_min}>
            <input type=hidden id="Computer_guess_max" name="Computer_guess_max" value={Computer_guess_max}>        
            <H1>"Think of a number from {Computer_guess_min} to {Computer_guess_max} and I will guess it in max ten moves." 
            <br><br>
            <button type="submit">Let's begin!!</button>
            </form>
        '''
    
    if request.method == "POST":
        Computer_guess_min = request.form["Computer_guess_min"]
        Computer_guess_max = int(request.form["Computer_guess_max"]) - 3 
        page = f'''
            {Computer_guess_min}
            {Computer_guess_max}
            <form action="/" method="POST">
            <label for="Computer_guess">Im guessing: </label>
            <input type=hidden id="Computer_guess_min" name="Computer_guess_min" value={Computer_guess_min}><br><br>        
            <input type=hidden id="Computer_guess_max" name="Computer_guess_max" value={Computer_guess_max}><br><br>        
            <button type="submit">Too much</button>
            <button type="submit">Too little</button>
            <button type="submit">You won!</button>

            </form>
        '''
    return page


def main():
    min_number = 0
    max_number = 1000
#    print(f"Think of a number from {min_number} to {max_number} and I will guess it in max ten moves.")

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


if __name__ == '__main__':
    app.run(debug=False)