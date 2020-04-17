# cuilCalculator

Un pequeño script para obtener el cuil de un lote de datos. Para ejecutar el mismo, debe clonar el repositorio y ejecutar el siguiente comando:

```
python3 readWriteCsv.py --file path_file

```

La estructura del archivo, que debe ser nombrado como test.csv, deberá ser la siguiente:

```
dni | sexo
35124455 | F
55112223 | M
11223344 | M
77889944 | F
```

El resultado, es un nuevo archivo .csv, denominado result.csv, en la raiz del repositorio.

Para obtener ayuda, utilice el comando:

```
python3 readWriteCsv.py --help

```

Opciones:

```
usage: readWriteCsv.py [-h] [-d DNI] [-s {F,M}] [-f FILE] [-F {con,sin}]

optional arguments:
  -h, --help            show this help message and exit
  -d DNI, --dni DNI     número de documento (debe tener mínimo 7 dígitos)
  -s {F,M}, --sex {F,M}
                        F: femenino; M: masculino
  -f FILE, --file FILE  ruta absoluta del archivo .csv con los datos
  -F {con,sin}, --format {con,sin}
                        formato que debera tener el cuil/cuit, ['con','sin']
                        guiones
```
