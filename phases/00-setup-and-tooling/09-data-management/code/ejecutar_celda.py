#!/usr/bin/env python3
"""Ejecuta una celda específica de un notebook.

Uso:
    python ejecutar_celda.py notebook.ipynb [índice]

Ejemplo:
    python ejecutar_celda.py practica.ipynb 3
"""

import sys

import nbformat
from nbclient import NotebookClient

# Obtiene la ruta del notebook desde el primer argumento.
nb_file = sys.argv[1]

# Usa el índice indicado como segundo argumento.
# Si no se proporciona, ejecuta la primera celda (índice 0).
idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0

# Lee el notebook en formato nbformat v4.
nb = nbformat.read(nb_file, as_version=4)

# Crea un cliente que ejecutará las celdas con el kernel especificado.
client = NotebookClient(nb, kernel_name="ai-engineering")

# Inicia el kernel y ejecuta únicamente la celda indicada.
with client.setup_kernel():
    client.execute_cell(nb.cells[idx], idx)

# Guarda el notebook, incluidos los outputs de la celda ejecutada.
nbformat.write(nb, nb_file)

# Confirma que terminó la ejecución.
print(f"Celda {idx} ejecutada.")

