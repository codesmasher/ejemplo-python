## ¿Cómo usar esta sección del repositorio?

Es necesario instalar la extensión _*Dev Containers*_ en _*Visual Studio Code*_ 

## Estructura del directorio

```
tutorial_dalto/
|-.devcontainer/
|  |- devcontainer.json
|  |- Dockerfile
|  |- requirements.txt
|- ejemplos/
|  |- debug.py
|  |- (...Ejemplos numerados) 
|- README.md (Este archivo)
```
## Cómo usarlo en VS Code

1. Instala la extensión "Dev Containers" en VS Code.
2. Abre la carpeta raíz del proyecto (my-python-app) en VS Code.
3. VS Code detectará el archivo .devcontainer y te ofrecerá "Reopen in Container".
4. Acepta y se construirá el contenedor automáticamente.
5. Abre main.py, coloca un breakpoint.

