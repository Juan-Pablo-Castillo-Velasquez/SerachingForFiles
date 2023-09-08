# SearchingForFiles 🔍

<p align="center">
  <strong>¡Bienvenido a SearchingForFiles!</strong><br>
  <img src="https://th.bing.com/th/id/R.341a37d8a8b0d0ec888abb0a022bfd33?rik=Xu2qQ6vHw4I7AQ&pid=ImgRaw&r=0" height="200" alt="Imagen del proyecto">
</p>

## Tabla de Contenidos
<table align="center">
  <tr>
    <th><a href="#instalación">Instalación </a></th>
    <th><a href="#bibliotecas">Bibliotecas</a></th>
    <th><a href="#configuración">Configuración</a></th>
    <th><a href="#uso">Uso</a></th>
    <th><a href="#contribuidores">Contribuidores</a></th>
    <th><a href="#licencia">Licencia</a></th>
    <th><a href="#autor">Autor</a></th>
  </tr>
</table>

# Introducción

SearchingForFiles es una herramienta de búsqueda de patrones en archivos que le permite encontrar y recopilar información útil de manera eficiente. Busque patrones en archivos dentro de una carpeta y guarde los resultados en un archivo CSV con facilidad.

## Características

* **🔍 Búsqueda de patrones en archivos**
* **📁 Guardado de resultados en un archivo CSV**
* **✅ Opción para eliminar duplicados**
* **🖥️ Interfaz gráfica sencilla e intuitiva**

# Instrucciones para Instalar Python y Configurar las Variables de Entorno en Windows

Antes de comenzar con el desarrollo en Python, asegúrate de seguir estos pasos para instalar Python y configurar las variables de entorno en tu sistema Windows.

# Instalación :snake:


1. Accede al sitio web oficial de Python en [python.org/downloads](https://www.python.org/downloads/).
2. Descarga la última versión estable de Python para Windows haciendo clic en el botón de descarga. 📥
3. Ejecuta el instalador descargado. 🏁
4. Asegúrate de marcar la casilla "Add Python X.X to PATH" (donde X.X es la versión de Python que estás instalando). Esto es crucial para configurar las variables de entorno correctamente. ✔️
5. Continúa con la instalación siguiendo las instrucciones en pantalla. 🚀
6. Una vez finalizada la instalación, abre una ventana de comandos (CMD) o PowerShell para verificar que Python se ha instalado correctamente. Ejecuta el siguiente comando:

   ```
   python --version
   ```

## Bibliotecas


Para utilizar esta herramienta, siga estos pasos:

1. Cree un entorno virtual (venv) para aislar las dependencias del proyecto:

   ```bash
   python -m venv venv
   ```

**Active el entorno virtual:**

## Windows:

```bash
venv\Scripts\activate

```
## linux o Linux/macOS
```bash
source venv/bin/activate
```

# Bibliotecas 📚

```bash
pip install pyttsx3 pandas kivy
```

## Configuración ⚙️

Antes de comenzar, asegúrese de haber configurado correctamente el entorno virtual y las bibliotecas necesarias. Si ha seguido los pasos de instalación, su entorno estará listo para usar.

# uso 🚀

Una vez que hayas instalado Python, puedes ejecutar el programa proporcionando la ruta completa de la carpeta que deseas buscar.

1. **Supongamos que deseas buscar en la carpeta**
```
C:\Users\JuanPablo\Documents.
```

2. **Ingrese el patrón de búsqueda en el cuadro de texto correspondiente, por ejemplo:** 

```php
$CFG->.
```

3. **(Opcional) Seleccione si desea eliminar duplicados.**
<p align="center">
  <img src="./img/example2.png" alt="Descripción de la imagen" />
</p>

Haga clic en el botón "Buscar". ✅

Los resultados se guardarán en un archivo CSV llamado variables.csv en el directorio actual.
<p align="center">
  <img src="./img/example3.png" alt="Descripción de la imagen" />
</p>

## Contribuidores 👥
Este proyecto ha sido posible gracias a las contribuciones de:

<p align="center">
  <img src="https://avatars.githubusercontent.com/u/143448141?v=4" alt="Juan Pablo's GitHub Profile" width="100" height="100" style="border-radius: 50%;">
  <br>
  <strong>Juan Pablo</strong>
  <br>
  <a href="mailto:JUANPABLO2007k@gmail.com">JUANPABLO2007k@gmail.com</a>
</p>
<p align="center">
  <img src="https://avatars.githubusercontent.com/u/126941356?v=4" alt="Contribuidor 2's GitHub Profile" width="100" height="100" style="border-radius: 50%;">
  <br>
  <strong>Contribuidor 2</strong>
  <br>
  <a href="mailto:juan.velasquez@openlms.net">juan.velasquez@openlms.net</a>
</p>
## Licencia  📄
SearchingForFiles está bajo la Licencia MIT. Consulta el archivo LICENSE.md para obtener más detalles. 

## Autor:technologist::
Juan Pablo Castillo Velasquez

<img src="https://avatars.githubusercontent.com/u/143448141?v=4" alt="Imagen de perfil de GitHub" width="100" height="100" style="border-radius:50%">
GitHub [GitHub 🌐 Mi perfil en github](https://github.com/JuanPablo-Openlms)



## Notas Adicionales  📝
Asegúrese de que las bibliotecas requeridas estén instaladas antes de ejecutar el programa.

Este programa utiliza la biblioteca Kivy para su interfaz gráfica, por lo que la apariencia puede variar según la plataforma.

Los resultados se guardan en un archivo CSV llamado variables.csv.
