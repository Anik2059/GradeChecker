# Note : 
"""1️⃣ “If the mark is NOT between 0 and 100 (inclusive), then it is invalid.”

So it catches:

Negative numbers (−1, −10, etc.)

Numbers above 100 (110, 999, etc.)

Anything outside the valid range

2️⃣ Why this works

if not (0 <= mark <= 100) → checks invalid marks first.

elif after it → only executes if the first condition is False (i.e., mark is valid).

Then the normal if-elif-else chain handles all valid marks.

🧠 Why this is perfect

while True: → keeps asking until a valid number is entered.

try-except → handles non-numeric inputs gracefully.

if not (0 <= mark <= 100) → checks invalid range first.

elif chain → efficiently determines the grade.

break → stops the loop after a valid grade is given. """


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])   # MUST include methods=['GET', 'POST']
def gradechecker():
    grade = ""
    error = ""

    if request.method == 'POST':
        mark_input = request.form.get('mark', '')
        try:
            mark = int(mark_input)
            if not (0 <= mark <= 100):
                error = "Invalid mark! Enter a number from 0 to 100."
            else:
                if 80 <= mark <= 100:
                    grade = "A+"
                elif 75 <= mark <= 79:
                    grade = "A"
                elif 70 <= mark <= 74:
                    grade = "A-"
                elif 67 <= mark <= 69:
                    grade = "B+"
                elif 62 <= mark <= 65:
                    grade = "B-"
                elif 60 <= mark <= 61:
                    grade = "B"
                elif 57 <= mark <= 59:
                    grade = "C+"
                elif 52 <= mark <= 55:
                    grade = "C-"
                elif 50 <= mark <= 51:
                    grade = "C"
                elif 40 <= mark <= 49:
                    grade = "D"
                else:
                    grade = "Fail !"
        except ValueError:
            error = "Invalid input! Please enter a number."

    return render_template('index.html', grade=grade, error=error)

if __name__ == '__main__':
    app.run(debug=True)
