"""
Modelo de la red del Metro de la Ciudad de México como grafo.
Se modelan las líneas 1, 2 y 3.

- Cada ESTACIÓN es un nodo (vértice).
- Cada TRAMO entre dos estaciones seguidas es una arista.
- Las estaciones de TRANSBORDO aparecen en más de una línea,
  así que quedan conectadas a varias líneas automáticamente.
"""

import networkx as nx
import matplotlib.pyplot as plt

# 1) Datos: estaciones de cada línea, en orden
lineas = {
    "Línea 1": [
        "Observatorio", "Tacubaya", "Juanacatlán", "Chapultepec", "Sevilla",
        "Insurgentes", "Cuauhtémoc", "Balderas", "Salto del Agua",
        "Isabel la Católica", "Pino Suárez", "Merced", "Candelaria",
        "San Lázaro", "Moctezuma", "Balbuena", "Boulevard Puerto Aéreo",
        "Gómez Farías", "Zaragoza", "Pantitlán",
    ],
    "Línea 2": [
        "Cuatro Caminos", "Panteones", "Tacuba", "Cuitláhuac", "Popotla",
        "Colegio Militar", "Normal", "San Cosme", "Revolución", "Hidalgo",
        "Bellas Artes", "Allende", "Zócalo", "Pino Suárez", "San Antonio Abad",
        "Chabacano", "Viaducto", "Xola", "Villa de Cortés", "Nativitas",
        "Portales", "Ermita", "General Anaya", "Tasqueña",
    ],
    "Línea 3": [
        "Indios Verdes", "Deportivo 18 de Marzo", "Potrero", "La Raza",
        "Tlatelolco", "Guerrero", "Hidalgo", "Juárez", "Balderas",
        "Niños Héroes", "Hospital General", "Centro Médico", "Etiopía",
        "Eugenia", "División del Norte", "Zapata", "Coyoacán", "Viveros",
        "Miguel Ángel de Quevedo", "Copilco", "Universidad",
    ],
}

colores = {"Línea 1": "#F04E98", "Línea 2": "#005EB8", "Línea 3": "#AF9800"}

# 2) Crear el grafo (no dirigido: el metro va en ambos sentidos)
G = nx.Graph()

for linea, estaciones in lineas.items():
    # unir cada estación con la siguiente
    for i in range(len(estaciones) - 1):
        G.add_edge(estaciones[i], estaciones[i + 1], linea=linea)

# 3) Información básica del grafo
print("Número de estaciones (nodos):", G.number_of_nodes())
print("Número de tramos (aristas):", G.number_of_edges())

# Transbordos = estaciones que pertenecen a más de una línea
transbordos = []
for estacion in G.nodes:
    lineas_de_estacion = {G.edges[estacion, vecino]["linea"] for vecino in G.neighbors(estacion)}
    if len(lineas_de_estacion) > 1:
        transbordos.append(estacion)
print("Estaciones de transbordo:", transbordos)

# 4) Ejemplo de uso: ruta más corta entre dos estaciones
origen, destino = "Observatorio", "Universidad"
ruta = nx.shortest_path(G, origen, destino)
print(f"\nRuta más corta de {origen} a {destino} ({len(ruta) - 1} tramos):")
print(" -> ".join(ruta))

# 5) Dibujar el grafo y guardarlo como imagen
pos = nx.kamada_kawai_layout(G)
plt.figure(figsize=(14, 10))

for linea, color in colores.items():
    aristas = [(u, v) for u, v, d in G.edges(data=True) if d["linea"] == linea]
    nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color=color, width=4, label=linea)

nx.draw_networkx_nodes(G, pos, node_size=60, node_color="white", edgecolors="black")
nx.draw_networkx_nodes(G, pos, nodelist=transbordos, node_size=200, node_color="black")
nx.draw_networkx_labels(G, pos, font_size=7)

plt.title("Metro CDMX (Líneas 1, 2 y 3) como grafo")
plt.legend()
plt.axis("off")
plt.tight_layout()
plt.savefig("metro_grafo.png", dpi=150)
plt.show()
