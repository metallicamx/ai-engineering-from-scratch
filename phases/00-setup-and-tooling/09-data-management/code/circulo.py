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
# Área de un círculo

La fórmula es: **A = π × r²**

En este notebook calculamos el área para un radio de 5 unidades.
"""

# %%
import math

radio = 5
area = math.pi * radio ** 2
print(f"Radio: {radio}")
print(f"Área:  {area:.4f}")

# %% [markdown]
"""
## Verificación

Sabemos que π ≈ 3.1416, así que:
3.1416 × 25 = **78.54** (aproximadamente)
"""

# %%
assert abs(area - 78.5398) < 0.01, f"El área {area} no coincide con lo esperado"
print("✔ Verificación correcta")   
