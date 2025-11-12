from flask import Flask, render_template, request, redirect, url_for, flash
import requests
API = "https://pokeapi.co/api/v2/pokemon/"

app = Flask(__name__)
app.secret_key = '123456'

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/search', methods=['POST'])
def search_pokemon():
    pokemon_name = request.form['pokemon_name'].lower().strip()

    resp = requests.get(f"{API}{pokemon_name}")
    
    if not pokemon_name:
        flash('ingresa un nombre de pokemon')
        return redirect(url for('index'))
    
    if resp.status_code == 200:
        pokemon_data = resp.json()
        return render_template('pokemon.html', pokemon=pokemon_data)




    pokemon_info = {
    'name': pokemon_name,
    'id': pokemon_data['id'],
    'habilities':[a['hability']['name'].title() for a in pokemon_data['abilities']],
    'sprite': pokemon_data['sprites']['front_default']
}
    return render_template('pokemon.html', pokemon=pokemon_info)




if __name__ == '__main__':
    app.run(debug=True)
