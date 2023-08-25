import requests
import sys

def obtener_pokemon(nombre):
    BASE_URL = f"https://pokeapi.co/api/v2/pokemon/{nombre}/"
    response = requests.get(BASE_URL)
    return response.json()

def generar_html(pokemon, tipo):
    with open(f"{pokemon['name']}.html", 'w') as file:
        file.write(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
        <link href="https://fonts.cdnfonts.com/css/pokemon-solid" rel="stylesheet">
        <link rel="stylesheet" href="./style.css">        
    </head>
                   
    <body class="tipo-{tipo}">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    
        <div class="">
            <div class="card_completa mb-3 monos" style="max-width: 540px;">
                <div class="row g-0 align-items-center">
                    <div class="col-md-4">
                    <img class="img_pokemon" src="{pokemon['sprites']['front_default']}" alt="{pokemon['name']}">
                    </div>
                        <div class="col-md-8">
                            <div class="card-tipo-{tipo}">
                                <h1>{pokemon['name'].capitalize()}</h1>
                                <p><span class="fw-bold">ID:</span> {pokemon['id']}</p>
                                <p><span class="fw-bold">Altura:</span> {pokemon['height']}</p>
                                <p><span class="fw-bold">Peso:</span> {pokemon['weight']}</p>
                                <p><span class="fw-bold">Tipo:</span> {', '.join([t['type']['name'] for t in pokemon['types']])}</p>
                                <p><span class="fw-bold">Habilidades:</span> {', '.join([t['ability']['name'] for t in pokemon['abilities']])}</p>
                                <p>
                                 <button onclick="window.modal.showModal();" class="btn btn-outline-dark display-center">
                                    Descubre los movimientos de {pokemon['name']}
                                </button>
                                </p>                               
                                <dialog id="modal"  class="outline-dark ">
                                    <p><span class="fw-bold">Movimientos de {pokemon['name']} !! </span> {', '.join([t['move']['name'] for t in pokemon['moves']])}</p>
                                    <button onclick="window.modal.close();">Cerrar</button>
                                </dialog>
                            </div>
                        </div>
                    </div>
                </div> 
            </div>
        </div>                              
    </body>
                        
    </html>""")

if __name__ == "__main__":
    nombre = sys.argv[1]
    pokemon = obtener_pokemon(nombre)
    tipo_principal = pokemon['types'][0]['type']['name']
    generar_html(pokemon, tipo_principal)
