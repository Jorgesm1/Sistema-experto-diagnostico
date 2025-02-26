## Sistema Experto para Diagnóstico Simple

Este sistema experto realiza diagnósticos básicos basados en los síntomas ingresados por el usuario. Utiliza reglas predefinidas para proporcionar un diagnóstico.

### Funcionamiento

1. **Entrada de Síntomas**:
   - El usuario ingresa síntomas respondiendo "sí" o "no" a preguntas específicas.

2. **Reglas de Diagnóstico**:
   - **Resfriado común**: Fiebre, tos y dolor de garganta.
   - **Neumonía**: Fiebre, tos y dificultad para respirar.
   - **Mononucleosis**: Fiebre, fatiga y dolor de garganta.
   - **COVID-19**: Fiebre y dificultad para respirar.
   - **Otros casos**: Si los síntomas no coinciden con ninguna condición conocida, se recomienda consultar a un médico.

3. **Salida**:
   - El sistema imprime un diagnóstico basado en los síntomas ingresados.

### Ejecución

Para ejecutar el programa, usa el siguiente comando:

```bash
python sistema_experto.py