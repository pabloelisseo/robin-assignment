# robin-assignment
Repositorio con el codigo referente al ejercicio planteado por Robin Rover en el fichero 'Prueba Técnica - Robin rover Data Science.pdf'

## Entorno
El codigo ha sido desarrollado en un container de Docker con la funcionalidad `Dev Containers` de `VSCode`. De todas formas es independiente de esta plataforma y el Dockerfile del container se encuentra en la carpeta .devcontainer.

Algunas partes del Dockerfile pueden dar a confusion debido a un known issue de mongoDB en debian y su integracion como servicio.

## Ejecucion

La primera tarea se encuentra en el script `db_insert.py`.
Antes de ejecutar este script, es necesario lanzar el servicio de mongoDB con el siguiente comando:

``` shell
    sudo service mongodb start
```

La segunda tarea, por comodidad y posibilidad de explicar paso a paso, ha sido desarrollada en el fichero `models.ipynb`. El cual es un Jupyter Notebook en el que se ha realizado una comparacion de 4 modelos en el intento de prediccion de marca para una descripcion de articulo dado.

