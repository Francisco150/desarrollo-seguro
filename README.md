# Analizador de Cadenas - Proyecto Unidad 1

## Información General

Este software es una utilidad técnica desarrollada en Python diseñada para procesar listas de texto y extraer la cadena con mayor número de caracteres de forma eficiente.

### Descripción
El programa recibe una lista de palabras, valida mediante lógica interna que los datos sean correctos y devuelve la cadena más larga.

En caso de existir varias palabras con la misma longitud máxima, el algoritmo aplica una ordenación alfabética para determinar el resultado final.

### Tecnologías utilizadas
- Lenguaje: Python 3.10 o superior
- Framework de testing: unittest (librería estándar de Python)
- Librerías de soporte: random, string

---

## Guía de despliegue

A continuación se describen los pasos necesarios para ejecutar el programa en un entorno local.

### 1. Requisitos previos
- Tener instalado Python 3.10 o superior.
- Verificar la instalación con:

    python --version

### 2. Preparación del entorno
Asegúrese de que los siguientes archivos se encuentran en el mismo directorio:

- `mychar.py`
- `test_mychar.py`
- `.gitignore`

### 3. Ejecución del programa
Ejecutar el programa principal:

    python mychar.py

El sistema solicitará la introducción de 5 palabras y devolverá la cadena más larga según la lógica implementada.

### 4. Ejecución de pruebas
Para validar el funcionamiento del programa:

    python test_mychar.py

Se ejecutarán las pruebas unitarias utilizando el framework unittest.

---

## Tabla de Trazabilidad

| Versión | Fecha       | Descripción de Cambios |
|--------|------------|----------------------|
| v1.0.0 | 20/04/2026 | Implementación de la función cadena_mas_larga y lógica de desempate en mychar.py |
| v1.1.0 | 20/04/2026 | Creación de la rama desarrollo-seguro y desarrollo de pruebas unitarias en test_mychar.py |
| v1.2.0 | 20/04/2026 | Fusión de cambios (Merge Fast-forward) a la rama main y redacción de la documentación técnica |

---

## Checklist de Seguridad

Se ha implementado una estrategia de seguridad para proteger el código y el entorno mediante el uso de un archivo `.gitignore`. Los elementos protegidos e ignorados son:

**Carpeta `__pycache__/`:**  
Contiene archivos de bytecode compilados. Se ignora para evitar la distribución de archivos específicos de la arquitectura local y proteger rutas internas del sistema del desarrollador.

**Entornos virtuales (`venv/`, `.env`):**  
Se excluyen para asegurar que las dependencias se gestionen de forma aislada en cada equipo y para evitar la exposición accidental de variables de entorno o credenciales.

**Metadatos del sistema operativo (`.DS_Store`, `Thumbs.db`):**  
Se protegen para evitar que información residual de la estructura de archivos local se filtre al repositorio público de GitHub.

**Archivos de registro (`*.log`):**  
Se descartan para prevenir la exposición de trazas de ejecución que pudieran contener información sensible sobre errores del sistema o del entorno.