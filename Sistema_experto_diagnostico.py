def sistema_experto():
    print("Bienvenido al Sistema Experto de Diagnóstico Simple")
    print("Por favor, responde las siguientes preguntas con 'sí' o 'no'.")

    # Solicitar síntomas al usuario
    fiebre = input("¿Tienes fiebre? (sí/no): ").strip().lower()
    tos = input("¿Tienes tos? (sí/no): ").strip().lower()
    dolor_garganta = input("¿Tienes dolor de garganta? (sí/no): ").strip().lower()
    dificultad_respirar = input("¿Tienes dificultad para respirar? (sí/no): ").strip().lower()
    fatiga = input("¿Te sientes fatigado/a? (sí/no): ").strip().lower()

    # Reglas de diagnóstico
    if fiebre == "sí" and tos == "sí" and dolor_garganta == "sí":
        print("\nDiagnóstico: Podrías tener un resfriado común.")
    elif fiebre == "sí" and tos == "sí" and dificultad_respirar == "sí":
        print("\nDiagnóstico: Podrías tener neumonía. Deberías consultar a un médico.")
    elif fiebre == "sí" and fatiga == "sí" and dolor_garganta == "sí":
        print("\nDiagnóstico: Podrías tener mononucleosis. Deberías consultar a un médico.")
    elif fiebre == "sí" and dificultad_respirar == "sí":
        print("\nDiagnóstico: Podrías tener COVID-19. Deberías hacerte una prueba y aislarte.")
    else:
        print("\nDiagnóstico: Tus síntomas no coinciden con ninguna condición conocida. Si persisten, consulta a un médico.")

if __name__ == "__main__":
    sistema_experto()