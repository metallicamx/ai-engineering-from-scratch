import torch

def check_gpu_and_models():
    if torch.cuda.is_available():
        # 1. Obtener memoria total de la GPU (en GB)
        total_memory_bytes = torch.cuda.get_device_properties(0).total_memory
        total_memory_gb = total_memory_bytes / (1024**3)

        # Obtener memoria libre actual
        free_memory_bytes = torch.cuda.mem_get_info()[0]
        free_memory_gb = free_memory_bytes / (1024**3)

        print(f"🔍 Hardware detectado:")
        print(f"  - Memoria total: {total_memory_gb:.2f} GB")
        print(f"  - Memoria libre: {free_memory_gb:.2f} GB")
        print("-" * 40)

        # 2. Calcular límites dinámicos según la memoria total
        # Regla: 2 bytes por parámetro (fp16)

        # Límite teórico (100% de VRAM)
        max_params_theoretical_b = (total_memory_bytes / 2) / (10**9)

        # Límite realista para entrenamiento (usamos 60% de la memoria total para parámetros)
        # Esto deja 40% libre para gradientes, optimizador y activaciones
        memory_for_params_bytes = total_memory_bytes * 0.60
        max_params_realistic_b = (memory_for_params_bytes / 2) / (10**9)

        print("📊 Estimación de capacidad de modelo (fp16):")
        print(f"  - Límite teórico (100% VRAM): ~{max_params_theoretical_b:.2f}B parámetros")
        print(f"  - Límite realista (60% VRAM): ~{max_params_realistic_b:.2f}B parámetros")
        print("-" * 40)

        # 3. Definir una lista de modelos comunes para verificar
        # params_b: número de billones (billions) de parámetros
        models_to_check = [
            {"name": "Llama-3-8B", "params_b": 8.0},
            {"name": "Phi-3-mini", "params_b": 3.8},
            {"name": "Gemma-2B", "params_b": 2.0},
            {"name": "Llama-3-1B", "params_b": 1.0},
            {"name": "BERT-Base", "params_b": 0.11},
            {"name": "Mistral-7B", "params_b": 7.0},
            {"name": "Llama-3-70B", "params_b": 70.0} # Para ver el caso extremo
        ]

        print("🔍 Verificación de modelos específicos (fp16):")
        print(f"  (Basado en {total_memory_gb:.2f} GB de VRAM)\n")

        for model in models_to_check:
            # Calcular tamaño en GB: (Parámetros * 2 bytes) / 1024^3
            model_size_gb = (model["params_b"] * 10**9 * 2) / (1024**3)

            # Calcular porcentaje de uso de la memoria total
            usage_pct = (model_size_gb / total_memory_gb) * 100

            # Lógica de decisión dinámica
            if model_size_gb > total_memory_gb:
                status = "❌ NO CABE (OOM)"
                note = "Requiere más VRAM o cuantización (4-bit)."
            elif usage_pct > 95:
                status = "⚠️ Crítico (Inferencia solo)"
                note = "Apenas cabe, sin espacio para entrenamiento."
            elif usage_pct > 60:
                status = "⚠️ Ajustado (Entrenamiento difícil)"
                note = "Necesita Batch Size muy pequeño o cuantización."
            elif usage_pct > 30:
                status = "✅ SÍ CABE (Bueno)"
                note = "Espacio suficiente para entrenar."
            else:
                status = "✅ Ideal (Máximo rendimiento)"
                note = "Mucho espacio libre para batch size grande."

            print(f"  {model['name']} ({model['params_b']}B):")
            print(f"     Tamaño: ~{model_size_gb:.2f} GB ({usage_pct:.1f}% de tu GPU)")
            print(f"     Estado: {status}")
            if note:
                print(f"     Nota: {note}")
            print()

    else:
        print("❌ No se detectó una GPU NVIDIA.")
        print("   Para usar esta herramienta, necesitas:")
        print("   1. Una tarjeta NVIDIA con drivers instalados.")
        print("   2. O ejecutar este script en Google Colab (Runtime -> Change runtime type -> GPU).")

if __name__ == "__main__":
    check_gpu_and_models()
