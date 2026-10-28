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
# Área y perímetro de un cuadrado

Fórmulas:
- **Área** = lado²
- **Perímetro** = 4 × lado

Calculamos para un lado de 7 unidades.
"""

# %%
lado = 7
area = lado ** 2
perimetro = 4 * lado
print(f"Lado:      {lado}")
print(f"Área:      {area}")
print(f"Perímetro: {perimetro}")

# %% [markdown]
"""
## Verificación

- Área: 7² = **49**
- Perímetro: 4 × 7 = **28**
"""

# %%
assert area == 49, f"Área incorrecta: {area}"
assert perimetro == 28, f"Perímetro incorrecto: {perimetro}"
print("✔ Verificación correcta")   
