# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ai-engineering)
#     language: python
#     name: ai-engineering
# ---

# %% [markdown]
"""
# Ejercicio 1
- Cargar el conjunto de datos GLUE con la configuración MRPC e inspeccionar los primeros 5 ejemplos
"""

# %%

from datasets import load_dataset

# 1. Cargar la tarea de paráfrasis (equivalente moderno a glue/mrpc)
dataset = load_dataset("google-research-datasets/paws", "labeled_final")

# 2. Inspeccionar los primeros 5 ejemplos del split 'train'
label_names = dataset["train"].features["label"].names

for i in range(5):
    ejemplo = dataset["train"][i]          # <- acceso por índice: devuelve dict
    print(f"\n--- Ejemplo {i+1} ---")
    print(f"id        : {ejemplo['id']}")
    print(f"sentence1 : {ejemplo['sentence1']}")
    print(f"sentence2 : {ejemplo['sentence2']}")
    print(f"label     : {ejemplo['label']} ({label_names[ejemplo['label']]})")

# %% [markdown]
"""
# Ejercicio 2
- Transmitir (stream) el conjunto de datos C4 y contar cuántos ejemplos puedes procesar en 10 segundos
"""

# %%

import time
from datasets import load_dataset

ds = load_dataset("allenai/c4", "en", streaming=True, split="train")
iterador = iter(ds)

start = time.time()
count = 0

for ejemplo in iterador:
    # "procesar" = leer el texto (aquí solo accedemos a la clave 'text')
    _ = ejemplo["text"]
    count += 1
    if time.time() - start >= 10:
        break

print(f"Procesé {count} ejemplos en 10 segundos")

# %% [markdown]
"""
# Ejercicio 3
- Convertir un conjunto de datos a Parquet y comparar el tamaño del archivo con CSV
"""

# %%

from datasets import load_dataset
import os

# 1. Cargar dataset
ds = load_dataset("google-research-datasets/paws", "labeled_final", split="train")

# 2. Guardar en ambos formatos
ds.to_csv("paws.csv")
ds.to_parquet("paws.parquet")

# 3. Comparar tamaños
csv_size = os.path.getsize("paws.csv")
parquet_size = os.path.getsize("paws.parquet")

print(f"CSV:      {csv_size:,} bytes ({csv_size / 1024 / 1024:.1f} MB)")
print(f"Parquet:  {parquet_size:,} bytes ({parquet_size / 1024 / 1024:.1f} MB)")
print(f"Ratio:    CSV/Parquet = {csv_size / parquet_size:.1f}x")

# %% [markdown]
"""
# Ejercicio 4
- Crear una división de entrenamiento/validación/prueba 70/15/15 con una semilla fija y verificar los tamaños
"""

# %%

from datasets import load_dataset

SEED = 42  # semilla global

# 1. Cargar dataset completo
ds = load_dataset("google-research-datasets/paws", "labeled_final", split="train")
total = len(ds)
print(f"Total: {total}")

# 2. Crear splits 70/15/15 reutilizando la misma seed
splits = ds.train_test_split(test_size=0.30, seed=SEED)
final = splits["test"].train_test_split(test_size=0.50, seed=SEED)

train_ds = splits["train"]
val_ds = final["train"]
test_ds = final["test"]

# 3. Verificar tamaños
print(f"Train: {len(train_ds)} ({len(train_ds)/total*100:.1f}%)")
print(f"Val:   {len(val_ds)} ({len(val_ds)/total*100:.1f}%)")
print(f"Test:  {len(test_ds)} ({len(test_ds)/total*100:.1f}%)")
