# Calculadora de Predicción y Distribución para Juegos de Azar (Crash/DICE)

Esta herramienta proporciona funciones para calcular interacciones, distribución de cantidades y el número máximo de interacciones posibles en escenarios de juegos de azar como Crash o DICE. También incluye una función para calcular la frecuencia de victorias.

## Funcionalidades

*   **Calcular interacciones y suma:** Calcula una secuencia de cantidades que se duplican en cada interacción y su suma total.
*   **Calcular distribución:** Distribuye una cantidad total entre un número dado de interacciones, dividiendo la cantidad restante a la mitad en cada paso.
*   **Calcular máximo de interacciones:** Calcula el número máximo de interacciones posibles dadas una cantidad inicial, un multiplicador, una probabilidad de perder y un límite de probabilidad.
*   **Calcular victorias:** Calcula la frecuencia promedio de victorias basándose en el número de victorias y derrotas.

## Instalación

No se requiere instalación especial, ya que es un script de Python puro. Asegúrate de tener Python 3 instalado en tu sistema.

## Uso

1.  **Descarga el script:** Clona este repositorio o descarga el archivo `app.py`.
2.  **Ejecuta el script:** Abre una terminal o línea de comandos, navega al directorio donde guardaste el script y ejecuta:

    ```bash
    python app.py
    ```

    Esto iniciará un menú interactivo.

## Menú Interactivo

El script presenta un menú con las siguientes opciones:

1.  **Calcular interacciones y suma:**

    *   Te pedirá el número de interacciones y la cantidad inicial.
    *   Imprimirá cada interacción y la cantidad resultante, así como la suma total.

2.  **Calcular distribución:**

    *   Te pedirá la cantidad total y el número de interacciones.
    *   Imprimirá la distribución de la cantidad entre las interacciones.

3.  **Calcular el número máximo de interacciones posibles:**

    *   Te pedirá los fondos disponibles, el multiplicador, la probabilidad de perder y un límite de probabilidad (con valor predeterminado).
    *   Mostrará una tabla con las interacciones, las apuestas, la probabilidad acumulada y los fondos restantes en cada paso.
    *   Finalmente, mostrará el número máximo de interacciones, la probabilidad acumulada total y los fondos restantes.

4.  **Calcular victorias:**

    *   Te pedirá el número de victorias y derrotas.
    *   Calculará y mostrará la frecuencia promedio de victorias.

5.  **Salir:** Termina la ejecución del script.

## Ejemplos de uso

**Calcular interacciones y suma:**

--- MENÚ ---

Calcular interacciones y suma ... Seleccione una opción: 1 Introduce el número de interacciones: 5 Introduce la cantidad inicial: 10 1 10.0000000000 2 20.0000000000 3 40.0000000000 4 80.0000000000 5 160.0000000000 Suma total: 310.0000000000

**Calcular el máximo de interacciones:**

--- MENÚ --- 3. Calcular el número máximo de interacciones posibles ... Seleccione una opción: 3 Introduce los fondos disponibles: 100 Introduce el multiplicador: 2 Introduce la probabilidad de perder (por ejemplo, 0.56): 0.5 Límite de probabilidad utilizado: 0.00001100 I Interacción AA Apuesta PT Probabilidad acumulada FT Fondos restantes
I1 |AA0.00001100 |PT0.5000000000 |FD99.99998900 I2 |AA0.00002200 |PT0.2500000000 |FD99.99996700 ...
El número máximo de interacciones posibles es: 16
La probabilidad acumulada después de estas interacciones es: 0.00001526
Fondos restantes: 99.99974500


## Consideraciones importantes

*   Se utiliza `Decimal` para cálculos de alta precisión y evitar errores de punto flotante, especialmente importantes en cálculos financieros o de probabilidad.
*   La función `calcular_max_interacciones` utiliza un límite de probabilidad para determinar cuándo detener los cálculos, evitando bucles infinitos en ciertos casos.
*   Este script proporciona herramientas de cálculo y simulación, pero no garantiza ganancias en juegos de azar. Los resultados reales pueden variar.

## Archivos

*   `app.py`: El script principal de Python.

## Autor

[Alexander Luna/Alexander-Luna]

## Licencia


Este proyecto se distribuye bajo la Licencia MIT con una cláusula de atribución para uso comercial.

Copyright (c) [2024] [Alexander Luna/Alexander-Luna]

Por la presente se concede permiso, libre de cargo, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para tratar el Software sin restricción, incluyendo sin limitación los derechos de usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y para permitir a las personas a las que se les proporcione el Software hacerlo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o porciones sustanciales del Software.

SI EL SOFTWARE (O UNA VERSIÓN MODIFICADA SUSTANCIALMENTE DEL MISMO) SE UTILIZA EN UN PRODUCTO COMERCIAL, SE DEBE INCLUIR UNA ATRIBUCIÓN CLARA Y VISIBLE AL AUTOR ORIGINAL ( [Alexander Luna/Alexander-Luna]) EN LA DOCUMENTACIÓN DEL PRODUCTO Y/O EN UNA SECCIÓN "ACERCA DE" O SIMILAR DENTRO DEL PRODUCTO.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO, PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO TIPO, QUE SURJA DE, O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.