# Programa de Marcas de Agua para PDFs

Este programa (`watermark_batch.py`) permite añadir marcas de agua de texto a múltiples archivos PDF de forma automática.

## Características

- Añade marcas de agua de texto personalizadas a archivos PDF
- Procesa múltiples archivos PDF en lote
- La marca de agua se coloca en diagonal (rotada 45 grados)
- Usa un color gris claro semi-transparente para no obstaculizar la lectura del contenido
- Preserva el tamaño original de cada página del PDF
- Mantiene la calidad del PDF original

## Requisitos

El programa requiere las siguientes bibliotecas Python:

- PyPDF2
- reportlab

## Instalación y Configuración

1. Crear un entorno virtual:

```bash
python -m venv env
```

2. Activar el entorno virtual:

En Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

En Windows CMD:

```cmd
.\env\Scripts\activate
```

En Linux/Mac:

```bash
source env/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Crear los directorios necesarios:

```bash
mkdir -p pdfs_originales
mkdir -p pdfs_con_marca
```

## Ejecución del Programa

1. Coloca los archivos PDF que deseas procesar en el directorio `pdfs_originales/`

2. Ejecuta el script:

```bash
python watermark_batch.py
```

3. Los archivos PDF con marca de agua se guardarán en el directorio `pdfs_con_marca/`

## Instalación y Configuración

1. Crear un entorno virtual:

```bash
python -m venv env
```

2. Activar el entorno virtual:

En Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

En Windows CMD:

```cmd
.\env\Scripts\activate
```

En Linux/Mac:

```bash
source env/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Crear los directorios necesarios:

```bash
mkdir pdfs_originales
mkdir pdfs_con_marca
```

## Estructura del Proyecto

```
watermark/
├── pdfs_originales/     # Directorio para los PDFs originales
├── pdfs_con_marca/      # Directorio donde se guardarán los PDFs con marca de agua
└── watermark_batch.py   # Script principal
```

## Funcionamiento

El programa está compuesto por tres funciones principales:

### 1. `create_watermark(text, pagesize)`

- Crea un PDF con la marca de agua
- El texto se renderiza en fuente Helvetica, tamaño 180
- La marca de agua se crea con color gris claro (60%) y 20% de opacidad
- El texto se centra y rota 45 grados

### 2. `add_text_watermark(pdf_path, watermark_text, output_path)`

- Procesa un único archivo PDF
- Añade la marca de agua a todas las páginas del PDF
- Guarda el resultado en un nuevo archivo

### 3. `batch_add_text_watermark(input_dir, watermark_text, output_dir)`

- Procesa todos los archivos PDF en un directorio
- Crea el directorio de salida si no existe
- Mantiene los nombres originales de los archivos

## Uso

Por defecto, el programa:

1. Busca archivos PDF en el directorio `pdfs_originales`
2. Añade la marca de agua "Copia" a cada archivo
3. Guarda los nuevos PDFs en el directorio `pdfs_con_marca`

## Personalización

Para modificar el comportamiento predeterminado, puedes ajustar las siguientes variables al final del script:

```python
input_directory = 'pdfs_originales'     # Directorio de entrada
watermark_text = 'Copia'                # Texto de la marca de agua
output_directory = 'pdfs_con_marca'     # Directorio de salida
```
