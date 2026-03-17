import random
import matplotlib.pyplot as plt

# Fijar la semilla para que el resultado sea reproducible.
random.seed(42) 

# --- FUNCIONES ---

def cumples(k):
    
    # Genera una lista de 'k' cumpleaños aleatorios (números del 1 al 365).
    lista_cumples = []
    for i in range(k):
        lista_cumples.append(random.randint(1, 365))
    return lista_cumples


def hay_coincidencia(cumples_lista):
   
    # Recibe una lista de cumpleaños. Devuelve True si hay al menos uno repetido, False si no.
    return len(set(cumples_lista)) != len(cumples_lista)


def proporcion_coincidencia(k, N):

    # Simula 'N' veces el experimento para 'k' personas y devuelve la proporción de coincidencias.
    coincidencias_totales = 0

    for i in range(N):
        grupo_cumples = cumples(k)  # Generamos un grupo de cumpleaños para 'k' personas
        if hay_coincidencia(grupo_cumples):  # Verificamos si hay coincidencia en ese grupo
            coincidencias_totales += 1  # Si hay coincidencia, incrementamos el contador

    return coincidencias_totales / N  # Devolvemos la proporción de coincidencias       
    

# --- EJECUCIÓN PRINCIPAL ---

if __name__ == "__main__":
    N = 1000 # La rúbrica pide N=1000
    probabilidades_estimadas = []

    rango_k = range(1, 51)  # Rango de k de 1 a 50
    
    # Calculamos para k de 1 a 50
    for k in range(1, 51):
        probabilidad = proporcion_coincidencia(k, N)
        probabilidades_estimadas.append(probabilidad)
        
        # Opcional: imprimir el resultado para ir viendo cómo avanza
        print(f"Para k={k} personas, la probabilidad estimada es {probabilidad}")

    print("Calculado!. Dibujando grafico...")
    
    plt.figure(figsize=(10, 6))
    plt.plot(rango_k, probabilidades_estimadas, marker='o', color='purple', linestyle='-', linewidth=2, label='Simulación (N=1000)')

    plt.axhline(y=0.5, color='red', linestyle='--', alpha=0.7, label='Límite 50%')
    plt.axvline(x=23, color='green', linestyle='--', alpha=0.7, label='23 personas')

    # Ponemos Título y etiquetas a los ejes
    plt.title('Simulación: El Problema del Cumpleaños', fontsize=14, fontweight='bold')
    plt.xlabel('Cantidad de personas en el grupo (k)', fontsize=12)
    plt.ylabel('Probabilidad Estimada', fontsize=12)

    # Detalles de facha: cuadricula de fondo y cartelito de referencias
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.show()
