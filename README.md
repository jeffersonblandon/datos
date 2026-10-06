
3.1 Para entender la jerarquía del valor del dato, utilizamos la pirámide DIKW (Data, Information, Knowledge, Wisdom/Decision):
Dato: Es un valor, símbolo o medida aislada sin interpretar (ej. 68% o 3).
Información: Es el dato puesto en contexto (ej. El aprendiz tiene una asistencia del 68%).
Conocimiento / Análisis: Interpretación de patrones (ej. La inasistencia compromete el cumplimiento de los resultados de aprendizaje).
Decisión: La acción o intervención que se ejecuta a partir de la evidencia obtenida.

Situación / Contexto
Dato
Información
Decisión Posible
Monitoreo de Infraestructura TIC
Uso de CPU = 96%; Memoria RAM = 92% durante 4 horas continuas.
El servidor principal de base de datos está sufriendo sobrecarga de recursos en horario laboral.
Escalar los recursos del servidor (Cloud) o redistribuir la carga mediante un balanceador de procesos.
Despliegue de Código / CI-CD
Fails = 14; Build time = 45 min en la rama main.
El tiempo de compilación y los fallos de pruebas automatizadas están retrasando las entregas del sprint.
Refactorizar la suite de pruebas unitarias y reestructurar el pipeline de integración continua.
Control de Consumo de Servicios Web
Peticiones HTTP 500 = 150 en el endpoint /api/v1/auth.
El microservicio de autenticación presentó fallos masivos tras el último despliegue.
Hacer un rollback a la versión estable anterior e investigar los logs de excepciones.

3.2 Diagnóstico de aprendizajes previos
Respuestas al Cuestionario Diagnóstico


¿Qué es un dato y qué diferencia tiene frente a la información? 

un dato es una representacion primaria o registro crudo (un numero, una  cadena de texto, una fecha) que carece de significado por si solo. la informacion surge al procesar, estructura y contextualizar ese dato dentro de un marco de referencia.

       2 . Ejemplos de datos en un ambiente de formación:  
85% (Porcentaje de entrega de evidencias de una ficha).
08:15 AM (Hora de registro de ingreso al ambiente de aprendizaje).


       3. ¿que es archivo csv y para que se utiliza?
      CSV (Comma-Separated Values) es un formato estándar de texto plano que almacena datos tabulares. Cada línea corresponde a un registro (fila) y los campos se separan por comas o punto y coma. Se utiliza por su ligereza y alta compatibilidad entre bases de datos, herramientas de análisis e hiperlenguajes. 

Diferencia entre fila y columna en una tabla:
Fila (Registro/Tupla): Representa una observación o entidad individual (ej. todos los datos del aprendiz Juan Pérez).
Columna (Campo/Variable): Representa una característica o atributo medible compartido por todos los registros (ej. edad, promedio, asistencia).
Tipo de dato para almacenar una nota:
Se debe utilizar un número decimal (float), ya que permite registrar fracciones precisas de calificación (ej. 4.5 o 3.8).
Riesgo de trabajar datos personales sin autorización:
Incurrir en violaciones legales sobre la Ley de Habeas Data (como la Ley 1581 de 2012 en Colombia), exponiendo a las personas a suplantaciones de identidad, sesgos discriminatorios y pérdidas de privacidad, además de acarrear sanciones legales e institucionales.
Propuesta de pregunta sobre una tabla:
Dada una tabla de registro de entrega de proyectos:
¿Cuál es el porcentaje promedio de entregas a tiempo agrupado por jornada de formación?
Herramientas utilizadas previamente:
Experiencia práctica en el desarrollo de scripts en Python, consultas a bases de datos con SQL/PostgreSQL/MySQL, control de versiones con Git, y gestión de datos estructurados en Excel/CSV.
¿Qué significa que un dato esté incompleto o duplicado?
Incompleto (Valor Nulo/Missing Value): La ausencia de registro en una variable relevante, lo que puede distorsionar los cálculos estadísticos.
Duplicado: La presencia de dos o más filas que registran exactamente la misma entidad o transacción, sobreestimando los conteos.
Expectativa de aprendizaje en la ruta:
Aprender a estructurar un flujo de datos limpio, reproducible y automatizado usando Python para extraer patrones útiles y apoyar decisiones fundamentadas.


Dimensión
Nivel (1 a 4)
Justificación Breve
Python
3 (Intermedio)
Conocimiento de sintaxis básica, estructuras de control y desarrollo de APIs/scripts.
Excel / CSV
3 (Intermedio)
Manejo de tablas, delimitadores y exportación de estructuras.
Lectura de tablas
4 (Avanzado)
Interpretación clara de relaciones entidad-relación y datos tabulares.
Interpretación de gráficos
3 (Intermedio)
Capacidad de leer tendencias e indicadores clave.
Ética de datos
3 (Intermedio)
Comprensión de buenas prácticas de anonimización y gestión de datos sensibles.
Organización de archivos
4 (Avanzado)
Gestión estructurada de directorios y control de versiones con Git.


3.3 Contexto actual de la Ciencia de Datos
Explicación clave
La ciencia de datos moderna combina tecnología con responsabilidad social. Herramientas como la Inteligencia Artificial Generativa aumentan la velocidad de análisis, pero la interpretación del contexto y la ética siguen siendo responsabilidad del profesional.

[ CONTEXTO PRODUCTIVO Y SOCIAL ]
                                 │
                     (Plantea necesidades y problemas)
                                 │
                                 ▼
                         [ CIENCIA DE DATOS ]
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        ▼                        ▼                        ▼
     [ DATO ]             [ IA GENERATIVA ]           [ ÉTICA ]
        │                        │                        │
(Registro bruto /        (Acelera análisis,      (Garantiza privacidad,
 Calidad y Fuentes)      requiere validación)      evita sesgos)
        │                        │                        │
        └────────────────────────┼────────────────────────┘
                                 │
                                 ▼
                            [ DECISIÓN ]
                    (Acción basada en evidencia)


3.4 Ciclo de vida del dato aplicado
Aplicación a un caso práctico de desarrollo de software

[1. Pregunta] ──► ¿Qué endpoints de nuestra API presentan mayor latencia o tasa de errores?
       │
[2. Fuente] ──► Logs del servidor (Uvicorn/FastAPI) y métricas de consumo en formato JSON/CSV.
       │
[3. Exploración] ──► Revisión de columnas: timestamp, endpoint, status_code, response_time_ms.
       │
[4. Calidad] ──► Identificación de registros nulos en tiempo de respuesta o peticiones canceladas.
       │
[5. Análisis] ──► Cálculo del percentil 95 de tiempos de respuesta por ruta HTTP.
       │
[6. Comunicación] ──► Dashboard con alertas visuales de endpoints críticos.
       │
[7. Acción] ──► Refactorización de consultas SQL lentas e implementación de almacenamiento en caché.

3.5 Caso integrador inicial: Seguimiento académico
Preguntas Analíticas Iniciales (Entregable 3.5)
¿Qué porcentaje de aprendices de una ficha determinada registra una asistencia inferior al 80% y un promedio de actividades por debajo de 3.5?
¿Existe una correlación directa entre la cantidad de evidencias no entregadas y el porcentaje de inasistencia registrado?
¿Cuál es el promedio de actividades entregadas agrupado por ficha de formación en el último trimestre?
¿Cuántos aprendices requieren un plan de acompañamiento preventivo categorizados por nivel de riesgo (Bajo, Medio, Alto)?
¿En qué evidencias específicas se concentra el mayor volumen de bajas calificaciones o comentarios de oportunidad de mejora?
Próximo Paso: Configuración del Ambiente (Momentos 3.6 y 3.7)
En el siguiente paso vamos a estructurar el proyecto en tu sistema de archivos e implementar el script de verificación en Python.
ciencia-datos-python/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── outputs/
├── docs/
├── scripts/
├── README.md
└── requirements.txt
<img width="1920" height="1038" alt="image" src="https://github.com/user-attachments/assets/e2f3db12-b2a7-473c-927d-8d7eec2ed9e6" />
