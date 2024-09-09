# bdb-dns/bbog-gid-onpods-scripts-db

# Descripción General
Llene aquí la descripción ampliada sobre el contenido del repositorio 
arquitect@ o desarrollador@!

## Estructura de Esquemas 
El proyecto cuenta con la siguiente estructura de carpetas:  

**ODS_STAG:** Configuración lógica asociada a los objetos pertenecientes al usuario "ODS_STAG" dentro de la base de datos PDODS, con el propósito de Almacenar la información que llega de los diferentes aplicativos para brindar la disponibilidad 
en cuanto a consultas históricas y de generación de reportes y archivos.  `By:@RZAMBR3`

**ICV:** Configuración lógica asociada a los objetos pertenecientes al usuario "ICV" dentro de la base de datos PDODS, con el propósito de almacenar y generar información asociada al árbol de NODOS consultada desde CRM.  `By:@RZAMBR3`

## :rocket: Workflow GitHub Actions :rocket: 
Este repositorio proporciona un flujo de trabajo diseñado para el despliegue de bases de datos utilizando el motor Oracle, permitiendo la gestión de uno o varios esquemas. El flujo se ejecuta tras validar que las carpetas que representan los esquemas han tenido modificaciones. Posteriormente, se ejecuta el archivo `INSTALL.sql` en el orden especificado en el archivo `OrdenInstalación.txt`.

![image](https://github.com/user-attachments/assets/d92115a3-14b5-4a9b-8f30-ffd59f0f8c5a)

> [!IMPORTANT]
> 1. El archivo `OrdenInstalacion.txt` debe ir organizado en el orden de ejecución de cada uno de los esquemas.
> 2. Para los archivos: `OrdenInstalacion.txt`, `INSTALL.sql` se deben tener configurada la codificación “UTF-8” y la secuencia de fin de línea. “LF” o bien, se sugiere editar directamente en GitHub conservando la codificación de los archivos.

## Estructura del repositorio
El proyecto cuenta con la siguiente estructura de carpetas
~~~
/bdb-dns/bbog-gid-onpods-scripts-db
├── *.github*
│
├── /ICV
│   ├── Function/
│   ├── Package/
│   ├── Scripts/
│   ├── INSTALL.sql
│
├── /ODS_STAG
│   ├── Function/
│   ├── Package/
│   ├── Scripts/
│   ├── INSTALL.sql
│
├── OrdenInstalacion.txt
└── README.md

~~~
**ICV**, **ODS_STAG**, Carpetas que contienen los artefactos específicos para cada esquema.
**OrdenInstalación.txt** Archivo que define el orden de ejecución de los esquemas
**INSTALL.sql**ste Script ejecuta:
- Instalacion cambiando SCHEMA actual a **ICV**
- Compilación Scripts
- Compilación procedimientos almacenados
- Compilación de paquetes modificados

Esto según ubicación dada en la línea:
~~~
@./&1/ICV/
~~~
 
 Ejemplo: 
 ~~~
 @./&1/ICV/Procedure/P_ICV_PS_CUOTA_TBL.sql
~~~
 
 Compila el procedimiento almacenado *P_ICV_PS_CUOTA_TBL.sqpl* ejecutando el Script .sql ubicado en la ruta **@./&1/ICV/Procedure/**

 


  *README* creado septiembre 09 de 2024
