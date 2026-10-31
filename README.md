Análisis de Mortalidad en Colombia (2019)

Introducción del proyecto

Aplicación web interactiva desarrollada con Dash y Plotly para explorar y analizar los datos de mortalidad en Colombia durante el año 2019.

Objetivo

Identificar patrones demográficos, causas principales de muerte y variaciones regionales/temporales mediante visualizaciones dinámicas.

Estructura del proyecto

├── app.py                   # Código principal del dashboard y servidor
├── requirements.txt         # Dependencias del proyecto
├── Anexo1.NoFetal2019...xlsx # Datos de mortalidad DANE 2019
├── Divipola_CE_.xlsx        # Codificación geográfica de Colombia
├── Anexo2.CodigosDeMuerte...# Catálogo CIE-10 de causas de muerte
└── README.md                # Documentación del proyecto


Requisitos

python == 3.10+

dash == 2.14.0+

pandas == 2.0.0+

plotly == 5.15.0+

openpyxl == 3.1.0+

gunicorn == 21.2.0+

Software

Lenguaje: Python

Dashboard / Interfaz: Dash, HTML/Core Components

Visualización: Plotly Express

Procesamiento de datos: Pandas

Servidor de producción: Gunicorn

Plataforma PaaS: Render

Instalación

Clonar repositorio: git clone https://github.com/tu-usuario/mortalidad-colombia.git

Ir al directorio: cd mortalidad-colombia

Instalar dependencias: pip install -r requirements.txt

Ejecutar localmente: python app.py (acceder en http://127.0.0.1:8050/)

Despliegue en Render

Subir proyecto a repositorio público en GitHub.

Crear un Web Service en Render conectado al repositorio.

Configurar Build Command: pip install -r requirements.txt

Configurar Start Command: gunicorn app:server

Desplegar en instancia gratuita.

Visualizaciones y Resultados

1. Distribución por Departamento (Mapa/Barras)

Descripción: Total de defunciones por departamento en 2019.

Hallazgo: Concentración de la mortalidad en departamentos con mayor densidad poblacional (Bogotá D.C., Antioquia y Valle del Cauca).

2. Tendencia Temporal (Líneas)

Descripción: Evolución mensual de muertes durante el año.

Hallazgo: Comportamiento uniforme a lo largo de los meses, sin picos atípicos pronunciados en 2019.

3. Top 5 Ciudades Violentas (Barras)

Descripción: Ciudades con mayor número de homicidios.

Hallazgo: Cali y Medellín encabezan las cifras absolutas de agresiones fatales con arma de fuego.

4. Top 10 Ciudades con Menor Mortalidad (Circular)

Descripción: Municipios con menor registro de defunciones.

Hallazgo: Corresponde a municipios de menor densidad poblacional de regiones periféricas.

5. Top 10 Causas de Muerte (Tabla)

Descripción: Listado detallado de causas según código y nombre CIE-10.

Hallazgo: Las enfermedades isquémicas del corazón y enfermedades crónicas de las vías respiratorias representan las primeras causas de muerte.

6. Mortalidad por Sexo y Departamento (Barras Apiladas)

Descripción: Comparación del total de defunciones entre hombres y mujeres por región.

Hallazgo: El número de muertes masculinas supera a la femenina en la mayoría de departamentos, influenciado por causas externas y violencia.

7. Distribución por Grupos de Edad (Histograma)

Descripción: Muertes agrupadas según la escala de edad (GRUPO_EDAD1).

Hallazgo: El volumen de mortalidad se concentra significativamente en las etapas de vejez y longevidad.
