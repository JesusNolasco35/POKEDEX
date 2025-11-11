from flask import Flask, render_template, request, redirect, url_for, flash

API = "https://pokeapi.co/api/v2/pokemon/"

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form['pokemon_name'].lower().strip()

    resp = requests.get(f"{API}{pokemon_name}")
    
    if resp.status_code == 200:
        pokemon_data = resp.json()
        return render_template('pokemon.html', pokemon=pokemon_data)

if __name__ == '__main__':
    app.run(debug=True)
