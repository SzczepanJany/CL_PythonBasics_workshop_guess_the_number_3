from flask import Flask, request

app = Flask(__name__)

def guessing(min_num, max_num):
    """
    Function is computing next guess
    """
    result = int(((max_num - min_num)/2)+min_num)
    return result


@app.route('/', methods=['GET','POST'])
def guess():
    if request.method == "GET":
        Computer_guess_min = 0
        Computer_guess_max = 1000
        result = guessing(Computer_guess_min,Computer_guess_max)
        page = f'''
            <form action="/" method="POST">
            
            <H1>"Think of a number from {Computer_guess_min} to {Computer_guess_max} and I will guess it in max ten moves."</H1> 
            <br><br>
            <label for="Computer_guess">Im guessing: {result}</label>
            <input type=hidden id="Computer_guess_min" name="Computer_guess_min" value={Computer_guess_min}><br><br>        
            <input type=hidden id="Computer_guess_max" name="Computer_guess_max" value={Computer_guess_max}><br><br>        
            <button name="button_answer" value = 1 type="submit">Too much</button>
            <button name="button_answer" value = 2 type="submit">Too little</button>
            <button name="button_answer" value = 3 type="submit">You won!</button>
            </form>
        '''
    
    if request.method == "POST":
        Computer_guess_min = int(request.form["Computer_guess_min"])
        Computer_guess_max = int(request.form["Computer_guess_max"])
        answer_value = request.form["button_answer"]
        result = guessing(Computer_guess_min,Computer_guess_max)
        Computer_guess_min, Computer_guess_max, result, status = main(result,Computer_guess_min,Computer_guess_max,answer_value)
        result = guessing(Computer_guess_min,Computer_guess_max)
        if status == 1:
            page = f'''
            {answer_value}
            {Computer_guess_min}, {Computer_guess_max}, {status}
            <br>
            <H1>I won!!</H1>
            <H2> {result} </H2>
            '''
        else:    
            page = f'''
             <form action="/" method="POST">
            <label for="Computer_guess">Im guessing: {result}</label>
            <input type=hidden id="Computer_guess_min" name="Computer_guess_min" value={Computer_guess_min}><br><br>        
            <input type=hidden id="Computer_guess_max" name="Computer_guess_max" value={Computer_guess_max}><br><br>        
            <input type=hidden id="result" name="result" value={result}><br><br> 
            <button name="button_answer" value = 1 type="submit">Too much</button>
            <button name="button_answer" value = 2 type="submit">Too little</button>
            <button name="button_answer" value = 3 type="submit">You won!</button>

            </form>
        '''
    return page


def main(result, min_number, max_number, answer):
    
    is_win = int(answer)
    if is_win == 1:
        max_number = result
    elif is_win == 2:
        min_number = result
    else:
        return (min_number, max_number, result, 1)

    return (min_number, max_number, result, 0)


if __name__ == '__main__':
    app.run(debug=False)