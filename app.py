from flask import Flask, render_template, redirect, url_for, request, jsonify, session, flash
import requests

API = "https://pokeapi.co/api/v2/pokemon/"
app = Flask(__name__)
app.secret_key = 'claveultramegasecreta'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscarpokemon', methods=['POST'])
def buscar_pokemon():
    pokemon_name = request.form.get('pokemon_name', '').strip().lower()

    if not pokemon_name:
        flash('Por favor, ingrese el nombre de un Pokémon.', 'error')
        return redirect(url_for('inicio'))

    try:
        resp = requests.get(f"{API}{pokemon_name}")
        
        if resp.status_code == 200:
            pokemon_data = resp.json()

            pokemon_info = {
                'name': pokemon_data['name'].title(),
                'id': pokemon_data['id'],
                'height': pokemon_data['height'] / 10,  
                'weight': pokemon_data['weight'] / 10,  
                'sprites': pokemon_data['sprites']['front_default'],
                'abilities': [ability['ability']['name'] for ability in pokemon_data['abilities']],
            }

            return render_template('pokemon.html', pokemon=pokemon_info)
        else:
            flash('Pokémon no encontrado. Intente nuevamente.', 'error')
            return redirect(url_for('inicio'))
    except requests.exceptions.RequestException:
        flash('Error al buscar el pokemon.', 'error')
        return redirect(url_for('inicio'))  

if __name__ == '__main__':
    app.run(debug=True)