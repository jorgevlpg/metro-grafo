# Metro CDMX como grafo (networkx)

Modelo de las líneas 1, 2 y 3 del Metro de la Ciudad de México como un **grafo no dirigido**:

- **Nodos** = estaciones (62)
- **Aristas** = tramos entre estaciones seguidas (62)
- **Transbordos** = estaciones que pertenecen a más de una línea (Balderas, Pino Suárez, Hidalgo)

El script también calcula la ruta más corta entre dos estaciones con `nx.shortest_path`.

Al correr el script se genera la imagen `metro_grafo.png` con el dibujo del grafo.

## Cómo correrlo

```bash
pip install -r requirements.txt
python metro_grafo.py
```
