from utils.generador import generar_casos
import datetime
import os
import csv

# Crear carpeta de salida si no existe
os.makedirs("outputs", exist_ok=True)

def guardar_markdown(historia, resultado, timestamp):
    nombre_md = f"outputs/testcases_{timestamp}.md"
    contenido_md = f"""# Historia de Usuario:
{historia}

---

## Casos de Prueba Generados

{resultado}
"""
    with open(nombre_md, "w", encoding="utf-8") as f:
        f.write(contenido_md)
    print(f"[✓] Archivo Markdown guardado en: {nombre_md}")

def guardar_csv(resultado, timestamp):
    nombre_csv = f"outputs/testcases_{timestamp}.csv"
    rows = []

    # Parseo básico: separa por títulos
    bloques = resultado.split("Título:")
    for bloque in bloques[1:]:  # el primero no contiene un caso
        titulo = bloque.strip().split("\n")[0]
        pasos = "\n".join([line for line in bloque.strip().split("\n") if line.startswith("1.") or line.startswith("2.") or line.startswith("3.")])
        resultado_esperado = [line for line in bloque.split("\n") if "Resultado esperado" in line]
        resultado_final = resultado_esperado[0].replace("Resultado esperado: ", "") if resultado_esperado else ""
        rows.append([titulo, pasos, resultado_final])

    # Escribir archivo CSV
    with open(nombre_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Título", "Pasos", "Resultado Esperado"])
        writer.writerows(rows)

    print(f"[✓] Archivo CSV guardado en: {nombre_csv}")

def guardar_feature(resultado, timestamp):
    nombre_feature = f"features/testcases_{timestamp}.feature"
    os.makedirs("features", exist_ok=True)

    # Extraer la sección de Gherkin desde el texto generado por IA
    if "Escenarios Gherkin:" in resultado:
        seccion_gherkin = resultado.split("Escenarios Gherkin:")[-1].strip()
    else:
        seccion_gherkin = resultado.strip()  # fallback

    with open(nombre_feature, "w", encoding="utf-8") as f:
        f.write(seccion_gherkin)

    print(f"[✓] Archivo .feature guardado en: {nombre_feature}")

if __name__ == "__main__":
    historia = input("Escribe la historia de usuario: ")
    resultado = generar_casos(historia)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")

    guardar_markdown(historia, resultado, timestamp)
    guardar_csv(resultado, timestamp)
    guardar_feature(resultado, timestamp)
