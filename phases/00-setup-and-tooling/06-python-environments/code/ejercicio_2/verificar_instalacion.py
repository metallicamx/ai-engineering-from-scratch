import sys

def verificar_version(nombre_paquete, version_esperada):
    try:
        modulo = __import__(nombre_paquete)
        version_actual = modulo.__version__
        
        if version_actual == version_esperada:
            print(f"✅ {nombre_paquete}: Correcto ({version_actual})")
            return True
        else:
            print(f"❌ {nombre_paquete}: Incorrecto. Esperado {version_esperada}, instalado {version_actual}")
            return False
    except ImportError:
        print(f"❌ {nombre_paquete}: No encontrado en el entorno.")
        return False
    except Exception as e:
        print(f"❌ {nombre_paquete}: Error al verificar ({e})")
        return False

def main():
    print(f"--- Verificación de Entorno (Python {sys.version.split()[0]}) ---\n")
    
    # Configuración de versiones deseadas
    paquetes = {
        "numpy": "2.3.5",
        "anthropic": "0.37.1"
    }
    
    todos_correctos = True
    
    for paquete, version in paquetes.items():
        if not verificar_version(paquete, version):
            todos_correctos = False
            
    print("\n---------------------------------------------")
    if todos_correctos:
        print("🎉 ¡Todas las versiones son correctas!")
    else:
        print("⚠️  Hay discrepancias en las versiones.")
        print("Ejecuta: pip install numpy==2.3.5 anthropic==0.125.0")
    
    # Prueba funcional rápida (opcional)
    try:
        import numpy as np
        # Operación básica de numpy
        arr = np.array([1, 2, 3])
        assert np.mean(arr) == 2.0
        print("✅ Prueba funcional de NumPy: OK")
    except Exception as e:
        print(f"❌ Prueba funcional de NumPy fallida: {e}")

if __name__ == "__main__":
    main()   
