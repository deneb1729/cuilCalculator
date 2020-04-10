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