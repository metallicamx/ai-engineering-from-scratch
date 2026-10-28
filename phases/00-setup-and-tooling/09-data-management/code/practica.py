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
# Paso 2: Cargar un conjunto de datos

Esto descarga el conjunto de datos de reseñas de películas IMDB. Después de la primera descarga, se carga desde la caché en `~/.cache/huggingface/datasets/`. ✅
"""

# %%
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb")
print(dataset)
print(dataset["train"][0])


# %% [markdown]
"""
# Paso 3: Transmitir conjuntos de datos grandes  

Algunos conjuntos de datos son demasiado grandes para caber en el disco. La transmisión los carga fila por fila sin descargar todo el conjunto.
"""

# %%

from datasets import load_dataset

dataset = load_dataset( "wikimedia/wikipedia", "20231101.en", split="train", streaming=True)

for example in dataset.take(5):
    print(example["title"])

# %% [markdown]
"""
# Paso 4: Formatos de conjuntos de datos

La biblioteca `datasets` utiliza Apache Arrow por debajo. Puedes convertir a otros formatos dependiendo de lo que necesite tu pipeline.

Para trabajos de IA, Parquet es el mejor formato de almacenamiento. Arrow es con lo que trabajas en memoria. CSV y JSON son para intercambio.
"""

# %%

from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

dataset.to_csv("imdb_train.csv")
dataset.to_json("imdb_train.json")
dataset.to_parquet("imdb_train.parquet")

# %% [markdown]
"""
# Paso 5: Divisiones de datos

Todo proyecto de ML necesita tres divisiones:

- Entrenamiento: El modelo aprende de esto (típicamente 80%)

- Validación: Verificas el progreso durante el entrenamiento (típicamente 10%)

- Prueba: Evaluación final después de completar el entrenamiento (típicamente 10%)

Algunos conjuntos de datos vienen pre-divididos. Cuando no es así, divídelos tú mismo.

Establece siempre una semilla para garantizar la reproducibilidad. La misma semilla produce la misma división cada vez
"""

# %%
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

split = dataset.train_test_split(test_size=0.2, seed=42)
train_val = split["train"].train_test_split(test_size=0.125, seed=42)

train_ds = train_val["train"]
val_ds = train_val["test"]
test_ds = split["test"]

print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")

# %% [markdown]
"""
# Paso 6: Descargar y almacenar en caché modelos

Los modelos son archivos grandes. La biblioteca `huggingface_hub` se encarga de la descarga y el almacenamiento en caché. 

Los modelos se almacenan en caché en `~/.cache/huggingface/hub/`. Una vez descargados, se cargan instantáneamente en ejecuciones posteriores.
"""

# %%

from huggingface_hub import hf_hub_download, snapshot_download

model_path = hf_hub_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    filename="config.json"
)
print(f"Cached at: {model_path}")

model_dir = snapshot_download("sentence-transformers/all-MiniLM-L6-v2")
print(f"Full model at: {model_dir}")

# %% [markdown]
"""
# Paso 7: Gestionar archivos grandes

Los pesos del modelo y los conjuntos de datos grandes no deben guardarse en git.
"""

# %% [markdown]
"""
# Paso 8: Patrones de almacenamiento 

**El almacenamiento local** funciona para conjuntos de datos de menos de ~10 GB. La caché de HF se encarga de esto automáticamente.

**El almacenamiento en la nube** es para todo lo que sea más grande o compartido entre máquinas
"""

# %%

import os

local_path = os.path.expanduser("~/.cache/huggingface/datasets/")

# s3_path = "s3://my-bucket/datasets/"
# gcs_path = "gs://my-bucket/datasets/"
