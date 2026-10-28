import networkx as nx
import matplotlib.pyplot as plt

# lineas 1, 2 y 3 del metro cdmx
lineas = {
    "Linea 1": [
        "Observatorio", "Tacubaya", "Juanacatlán", "Chapultepec", "Sevilla",
        "Insurgentes", "Cuauhtémoc", "Balderas", "Salto del Agua",
        "Isabel la Católica", "Pino Suárez", "Merced", "Candelaria",
        "San Lázaro", "Moctezuma", "Balbuena", "Boulevard Puerto Aéreo",
        "Gómez Farías", "Zaragoza", "Pantitlán",
    ],
    "Linea 2": [
        "Cuatro Caminos", "Panteones", "Tacuba", "Cuitláhuac", "Popotla",
        "Colegio Militar", "Normal", "San Cosme", "Revolución", "Hidalgo",
        "Bellas Artes", "Allende", "Zócalo", "Pino Suárez", "San Antonio Abad",
        "Chabacano", "Viaducto", "Xola", "Villa de Cortés", "Nativitas",
        "Portales", "Ermita", "General Anaya", "Tasqueña",
    ],
    "Linea 3": [
        "Indios Verdes", "Deportivo 18 de Marzo", "Potrero", "La Raza",
        "Tlatelolco", "Guerrero", "Hidalgo", "Juárez", "Balderas",
        "Niños Héroes", "Hospital General", "Centro Médico", "Etiopía",
        "Eugenia", "División del Norte", "Zapata", "Coyoacán", "Viveros",
        "Miguel Ángel de Quevedo", "Copilco", "Universidad",
    ],
}
colores = {"Linea 1": "hotpink", "Linea 2": "blue", "Linea 3": "olive"}

G = nx.Graph()
for linea, estaciones in lineas.items():
    for i in range(len(estaciones) - 1):
        G.add_edge(estaciones[i], estaciones[i + 1], linea=linea)

print("Estaciones:", G.number_of_nodes())
print("Conexiones:", G.number_of_edges())
print("Ruta Observatorio - Universidad:", nx.shortest_path(G, "Observatorio", "Universidad"))

pos = nx.kamada_kawai_layout(G)
plt.figure(figsize=(14, 10))
for linea, color in colores.items():
    aristas = [(u, v) for u, v, d in G.edges(data=True) if d["linea"] == linea]
    nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color=color, width=4, label=linea)
nx.draw_networkx_nodes(G, pos, node_size=60, node_color="white", edgecolors="black")
nx.draw_networkx_labels(G, pos, font_size=7)
plt.title("Metro CDMX")
plt.legend()
plt.axis("off")
plt.savefig("metro_grafo.png")
plt.show()
