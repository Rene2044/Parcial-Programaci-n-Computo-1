def registrar_viajes():
    """
    Permite al usuario registrar múltiples viajes de transporte público.
    """
    viajes = []
    while True:
        print("\n--- Nuevo Viaje ---")
        ruta = input("Nombre de la ruta: ")

        while True:
            try:
                tiempo = int(input("Tiempo del viaje (en minutos): "))
                if tiempo > 0:
                    break
                else:
                    print("Por favor, ingresa un tiempo positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero para el tiempo.")

        while True:
            try:
                costo = float(input("Costo del viaje (en USD): "))
                if costo >= 0:
                    break
                else:
                    print("Por favor, ingresa un costo positivo o cero.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número para el costo.")

        viajes.append({"ruta": ruta, "tiempo": tiempo, "costo": costo})

        continuar = input("\n¿Deseas registrar otro viaje? (s/n): ").lower()
        if continuar != 's':
            break
    return viajes

def generar_reporte(viajes):
    """
    Genera y muestra un reporte de los viajes, ordenados por costo.
    """
    # Ordenar los viajes por costo de mayor a menor
    viajes_ordenados = sorted(viajes, key=lambda x: x['costo'], reverse=True)

    total_tiempo = sum(viaje['tiempo'] for viaje in viajes)
    total_costo = sum(viaje['costo'] for viaje in viajes)

    print("\n" + "="*30)
    print("    REPORTE DE VIAJES")
    print("="*30)
    print("(Ordenados del más caro al más barato)")

    print("\n--- Detalle de Viajes ---")
    for viaje in viajes_ordenados:
        print(f"- Ruta: {viaje['ruta']:<15} | Tiempo: {viaje['tiempo']} min | Costo: ${viaje['costo']:.2f}")

    print("\n--- Resumen Semanal ---")
    print(f"Tiempo total invertido: {total_tiempo} minutos")
    print(f"Gasto total en transporte: ${total_costo:.2f}")
    print("\n" + "="*30)


def main():
    """
    Función principal del programa.
    """
    print("Bienvenido al Sistema de Registro de Transporte Público")
    lista_viajes = registrar_viajes()
    if lista_viajes:
        generar_reporte(lista_viajes)
    else:
        print("\nNo se registraron viajes. Finalizando programa.")

if __name__ == "__main__":
    main()
