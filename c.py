# -------------------------------------------------------------------------------
# Name:       Exemple d'utilisation du module Folium pour créer une carte avec 2 couches
# Author:     Philippe Vismara & Hazaël Jones
#




 -------------------------------------------------------------------------------
import folium
import webbrowser


#---- creation d'une carte sans couche (tuile) centrée sur le campus de la Gaillarde avec un zoom 13
carte = folium.Map(location=[43.6170253, 3.8548513], tiles=None, zoom_start=13)
#-- si vous utilisez la fonction fit_bounds() à la fin du script, vous pouvez créer une carte sans préciser la position et le zoom
#carte = folium.Map()

# ajout de deux couches (tuiles) à la carte
#  - la couche Open Street Map
folium.TileLayer('openstreetmap', name='Open Street Map').add_to(carte)
#  - la couche esri issue du SIG ArcGIS qui sera nommée 'Esri Imagery'
folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                 name='Esri Imagery',
                 attr="EsriImagery").add_to(carte)

#---- création d'un marqueur orange centré sur le site de La Valette
marqueur = folium.Marker(location=[43.647397, 3.878509], popup='<i>La Valette</i>',
                         icon=folium.Icon(color='orange'), tooltip='Click me!')
# ajout du marqueur à la carte
marqueur.add_to(carte)


#---- création et ajout d'un cercle bleu de 200 points
folium.Circle(radius=100, location=[43.61702, 3.85485],
              popup='Cercle bleu de La Gaillarde', color='blue', fill=False,
              tooltip='Click me!').add_to(carte)

#---- creation d'un chemin composé de 3 points
# chaque point sera décrit par un couple (tuple) de coordonnées : ( latitude, longitude )
# - on crée le chemin (liste) vide
path = []
# - ajout des points (coordonnées) à la liste
path.append((43.6170253, 3.8548513))
path.append((43.647756, 3.867185))
path.append((43.647397, 3.878509))
# - création d'un chemin rouge et épais (2.5) à partir de la liste (variable path) de coordonnées
chemin = folium.PolyLine(path, color="red", weight=2.5, opacity=1)
# - ajout du chemin a la carte
chemin.add_to(carte)

### facultatif
## centrer la carte sur le rectangle englobant tous les éléments ajoutés
carte.fit_bounds( carte.get_bounds() )

# TOUJOURS EN DERNIER (pour éviter un bug dans la librairie), ajout d'un selecteur de couche (en haut à droite de la carte)
folium.LayerControl().add_to(carte)

#---- enregistrement de la carte dans une page web (fichier)
# - nom du fichier utilisé pour stocker la page web
fichierweb = "mymap.html"
# - enregistrement d'une page web affichant la carte
carte.save(outfile=fichierweb)

#---- affichage dans le navigateur web
# - chargement de la page dans le navigateur web par defaut
webbrowser.open_new_tab(fichierweb)
# - sous MacOS utiliser plutôt le code suivant
#import os
#webbrowser.open_new_tab("file://" + os.getcwd() + "/" + fichierweb)
