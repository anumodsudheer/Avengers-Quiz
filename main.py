from flask import Flask, render_template, redirect, request

app = Flask(__name__)
Questions = [
    {
        'id': 1,
        'question': 'Who is the Captain of the Avengers?',
        'options': ['Iron-Man', 'Hulk', 'Thunder-Thor', 'Captain America'],
        'answer': 'Captain America'
    },
    {
        'id': 2,
        'question': 'Who is skilled avenger in real world also?',
        'options': ['Tony', 'Wanda', 'steve', 'Natasha'],
        'answer': 'Natasha'
    },
    {
        'id': 3,
        'question': 'Very Powerfull stone in avenger?',
        'options': ['Power Stone', 'Mind Stone', 'Soul Stone', 'Time stone'],
        'answer': 'Power Stone'
    },
    {
        'id': 5,
        'question': 'Which avenger is not a god?',
        'options': ['Thor', 'Loki', 'Wanda', 'Odin'],
        'answer': 'Wanda'
    },
    {
        'id': 6,
        'question': 'Who is god of thunder?',
        'options': ['IronMan', 'Hulk', 'Thor', 'wanda'],
        'answer': 'Thor'
    },
    {
        'id': 7,
        'question': 'Who is the strongest Avenger in the below list?',
        'options': ['Hulk', 'Thor', 'Captain America', 'wanda'],
        'answer': 'Thor'
    },
    {
        'id': 8,
        'question': 'What is the Real name of Wanda?',
        'options': ['Natasha', 'Steve', 'tony', 'Elizabeth olsen'],
        'answer': 'Elizabeth olsen'
    },
    {
        'id': 9,
        'question': 'who is the creator of Avenger?',
        'options': ['Wanda', 'Steve', 'Tony', 'Nick fury'],
        'answer': 'Nick fury'
    },
    {
        'id': 10,
        'question': 'What is the suit of Iron man in avenger end-game?',
        'options': ['Nano-suite', 'Adamantium', 'Uru', 'Steel'],
        'answer': 'Nano-suite'
    },

]
score=0
present_question=0
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_quiz():
    global present_question, score
    present_question = 0
    score = 0
    return redirect('/quiz')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global present_question, score

    if request.method == 'POST':
        answer = request.form.get('answer')

        if answer == Questions[present_question]['answer']:
            score += 1

        present_question += 1

        if present_question >= len(Questions):
            return redirect('/result')

    if present_question < len(Questions):
        question = Questions[present_question]
        return render_template('quiz.html', question=question)
    else:
        return redirect('/result')

@app.route('/result')
def result():
    global score
    return render_template('result.html', score=score, total_questions=len(Questions))

@app.route('/fan', methods=['POST'])
def fan():
    score = int(request.form.get('score'))
    percentage = (score / len(Questions)) * 100
    return render_template('fan.html', percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)

