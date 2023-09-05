<!-- Proyecto SearchingForFiles -->

# SearchingForFiles

![Logo del proyecto](url_del_logo.png)

Este proyecto es una herramienta de búsqueda de patrones en archivos que le permite encontrar y recopilar información útil de manera eficiente. Busque patrones en archivos dentro de una carpeta y guarde los resultados en un archivo CSV con facilidad.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Contribuidores](#contribuidores)
- [Licencia](#licencia)
- [Notas Adicionales](#notas-adicionales)
- [Autor](#autor)

## Instalación

Para utilizar esta herramienta, siga estos pasos:

1. Cree un entorno virtual (venv) para aislar las dependencias del proyecto:

   ```bash
   python -m venv venv
Active el entorno virtual:

Windows:

bash
Copy code
venv\Scripts\activate
Linux/macOS:

bash
Copy code
source venv/bin/activate
Instale las bibliotecas requeridas:

bash
Copy code
pip install pyttsx3 pandas kivy
Configuración
Antes de comenzar, asegúrese de haber configurado correctamente el entorno virtual y las bibliotecas necesarias. Si ha seguido los pasos de instalación, su entorno estará listo para usar.

## Uso
Para utilizar esta herramienta:

Ejecute el programa proporcionando la ruta completa de la carpeta que desea buscar.

Ingrese el patrón de búsqueda en el cuadro de texto correspondiente (por ejemplo, $CFG->).

Opcionalmente, puede especificar si desea eliminar duplicados en los resultados. Ingrese "Sí" o "No" en el cuadro de texto correspondiente.

Haga clic en el botón "Buscar".

Los resultados se guardarán en un archivo CSV llamado variables.csv en el directorio actual.

Se le preguntará si desea abrir el archivo CSV. Puede abrirlo haciendo clic en "Sí" o cerrar la ventana emergente haciendo clic en "No".

## Contribuidores
Este proyecto ha sido posible gracias a las contribuciones de:

Nombre del Contribuidor 1
Nombre del Contribuidor 2
¡Gracias por su valiosa contribución!

## Licencia
Este proyecto está bajo la licencia Nombre de la Licencia. Consulte el archivo LICENSE.md para obtener más detalles.

## Notas Adicionales
Asegúrese de que las bibliotecas requeridas estén instaladas antes de ejecutar el programa.

Este programa utiliza la biblioteca Kivy para su interfaz gráfica, por lo que la apariencia puede variar según la plataforma.

Los resultados se guardan en un archivo CSV llamado variables.csv.

## Autor
Este proyecto fue creado y es mantenido por:

##Juan Pablo
Perfil de GitHub