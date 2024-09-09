# bdb-dns/bbog-gid-onpods-scripts-db

# Descripción General
Llene aquí la descripción ampliada sobre el contenido del repositorio 
arquitect@ o desarrollador@!

## Estructura de Esquemas 
El proyecto cuenta con la siguiente estructura de carpetas:  

**ODS_STAG:** Configuración lógica asociada a los objetos pertenecientes al usuario "ODS_STAG" dentro de la base de datos PDODS, con el propósito de Almacenar la información que llega de los diferentes aplicativos para brindar la disponibilidad 
en cuanto a consultas históricas y de generación de reportes y archivos. 
>**By:@RZAMBR3**

**ICV:** Configuración lógica asociada a los objetos pertenecientes al usuario "ICV" dentro de la base de datos PDODS, con el propósito de almacenar y generar información asociada al árbol de NODOS consultada desde CRM. >**By:@RZAMBR3**

## :rocket: Workflow GitHub Actions :rocket: 
Flujo de trabajo diseñado para el despliegue de base de datos con motor Oracle para uno o varios esquemas.
Para ejecutarse el flujo se valida que las carpetas que representan el esquema tengan alguna modificación y ejecuta el archivo 'INSTALL.sql' en el orden especificado en el archivo 'OrdenInstalación.txt'.

![image](https://github.com/user-attachments/assets/d92115a3-14b5-4a9b-8f30-ffd59f0f8c5a)

> [!IMPORTANT]
> 1. El archivo `OrdenInstalacion.txt` debe ir organizado en el orden de ejecución de cada uno de los esquemas.
> 2. Para los archivos: `OrdenInstalacion.txt`, `INSTALL.sql` se deben tener configurada la codificación “UTF-8” y la secuencia de fin de línea. “LF” o bien, se sugiere editar directamente en GitHub conservando la codificación de los archivos.

  
  *README* creado septiembre 09 de 2024
