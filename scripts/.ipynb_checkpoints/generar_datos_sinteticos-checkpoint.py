from pathlib import Path

import pandas as pd
from faker import Faker


def generar_datos_aprendices(num_registros=100):
    if num_registros < 0:
        raise ValueError("num_registros debe ser mayor o igual a cero")

    fake = Faker("es_CO")
    programas = [
        "Análisis y Desarrollo de Software",
        "Gestión Administrativa",
        "Diseño Multimedia",
        "Contabilidad y Finanzas",
        "Gestión del Talento Humano",
    ]
    estados = ["En formación", "En etapa productiva", "Certificado", "Retirado"]

    registros = []
    for indice in range(1, num_registros + 1):
        nombre = fake.first_name()
        apellido = fake.last_name()
        registros.append(
            {
                "id_aprendiz": indice,
                "nombre": nombre,
                "apellido": apellido,
                "correo": fake.email(),
                "telefono": fake.phone_number(),
                "programa_formacion": fake.random_element(programas),
                "numero_ficha": fake.bothify(text="######"),
                "fecha_inicio": fake.date_between(start_date="-3y", end_date="today"),
                "estado": fake.random_element(estados),
                "ciudad": fake.city(),
            }
        )

    return pd.DataFrame(registros)


def main():
    proyecto = Path(__file__).resolve().parents[1]
    carpeta_salida = proyecto / "data" / "raw"
    carpeta_salida.mkdir(parents=True, exist_ok=True)

    archivo_salida = carpeta_salida / "seguimiento_aprendices_sintetico.xlsx"
    datos = generar_datos_aprendices()
    datos.to_excel(archivo_salida, index=False)
    print(f"Se generaron {len(datos)} registros en: {archivo_salida}")


if __name__ == "__main__":
    main()