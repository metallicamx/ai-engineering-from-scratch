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
# Área y perímetro de un triángulo

Triángulo rectángulo con catetos de **3** y **4** unidades.

Fórmulas:
- **Área** = ½ × base × altura
- **Perímetro** = a + b + c
"""

# %%
a, b, c = 3, 4, 5
area = 0.5 * a * b
perimetro = a + b + c
print(f"Lados:     {a}, {b}, {c}")
print(f"Área:      {area}")
print(f"Perímetro: {perimetro}")

# %% [markdown]
"""
## Verificación

- Área: ½ × 3 × 4 = **6**
- Perímetro: 3 + 4 + 5 = **12**
"""

# %%
assert area == 6, f"Área incorrecta: {area}"
assert perimetro == 12, f"Perímetro incorrecto: {perimetro}"
print("✔ Verificación correcta")   
