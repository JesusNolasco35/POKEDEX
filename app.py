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
    pokemon_name = request.form.get('pokemon_name', '').lower().strip()

    if not pokemon_name:
        flash('Ingresa un nombre de Pokémon', 'warning') 
        return redirect(url_for('index'))


    resp = requests.get(f"{API}{pokemon_name}")

    if resp.status_code == 200:
        pokemon_data = resp.json()

        pokemon_info = {
            'name': pokemon_name.title(),
            'id': pokemon_data['id'],
            'image': pokemon_data['sprites']['front_default'],  
            'height': pokemon_data['height'] / 10, 
            'weight': pokemon_data['weight'] / 10, 
            'abilities': [ability['ability']['name'].title() for ability in pokemon_data['abilities']]
        }

        return render_template('pokemon.html', pokemon=pokemon_info)
    else:
        flash(f'Pokémon "{pokemon_name}" no encontrado', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
