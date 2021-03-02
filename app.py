from flask import Flask

app = Flask(__name__)



#very special message from our Make School mascot:
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'




#make a route where the user can type in their favorite animal and get a response.
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

#'Completed all challenges'



#Write a route favorite_dessert for the URL /dessert/<users_dessert>. 
#If I visit the URL /dessert/donuts, I should see the text: How did you know I liked donuts?
@app.route('/dessert/<users_dessert>')
def favorite_desert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'Wow, How did you know I liked {users_dessert} That is my favorite dessert, too!'




#Write a route for the URL /madlibs/<adjective>/<noun> which takes in 2 strings 
#and displays a funny (but work-appropriate) story using them!
@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    return f'{adjective} {noun}'




#Write a route multiply that takes in 2 numbers, multiplies them, and displays the results. 
#Use the URL /multiply/<number1>/<number2>, then take in number1 and number2 as parameters.
@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    return f"{num1} times {num2} is {int(num1) * int(num2)}."



#Write a route, sayntimes, that will repeat a string a given number of times. 
# Use the URL /sayntimes/<word>/<n>.#
@app.route('/sayntimes/<word>/<n>')
def words(word, n):
    x=''
    for _ in range(0, int(n)):
        x+= f'word '
    return x


@app.route('/reverse/<word>')
def reverse(word):
    reversedString=""
    index = len(str(word))
    while index > 0:
        reversedString += word [index-1]
        index = index -1
    return f'{reversedString}'

@app.route('/strangecaps/<word>')
def strangecaps(word):
    strangeWord=""
    for char in range(len(word)):
        if not char % 2 :
            strangeWord = strangeWord + word[char].upper()
        else:
            strangeWord = strangeWord + word[char].lower()
    return f'{strangeWord}'


#Write a route dicegame that chooses a random number from 1 to 6. 
#If the user rolls a 6, they win the game; otherwise, they lose.

@app.route('/dicegame')
def dicegame():
    return f"You rolled a {random.randint(1,6)}"

if __name__ == '__main__':
    app.run(debug=True) 
