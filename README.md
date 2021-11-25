# Generate-IL-program-TM221-Schneider
Program that generates code in IL format for Schneider TM221 programmable controllers.  It implements autonomous calendars in the PLC, programmable by modbus through user-defined functions.


Se describe el trabajo realizado para la programación implícita de calendarios de los autómatas PLC TM221 de marca Schneider.

Un calendario para una variable concreta precisa utilizar 100MW (palabras) del autómata para su programación.

La codificación de las palabras se observa en la siguiente tabla:

| bit | Descripción |
| ------ | ------ |
| 0 | Habilitación, días Entero[1-7]|
| [1-12] | LUNES, 6 intervalos horarios, BCD |
| [13-24] | MARTES, 6 intervalos horarios, BCD |
| [25-36] | MIÉRCOLES, 6 intervalos horarios, BCD |
| [37-48] | JUEVES, 6 intervalos horarios, BCD|
| [49-60] | VIERNES, 6 intervalos horarios, BCD|
| [61-72] | SÁBADO, 6 intervalos horarios, BCD|
| [73-84] | DOMINGO, 6 intervalos horarios, BCD|
| 85 | Bit de activación |

![image](uploads/54837e96ee7c351095a9c922efd9d072/image.png)

Cada variable de vigia precisa de 7 bloques de funciones definidas por el usuario que se colocan en una Tarea/Rung correspondiente:

![image](uploads/2797ccd26b2b33f92f6dabfb6767a5ff/image.png)

El bit de enable ataca a la entrada dle bloque y el bit de activación a la salida del módulo.

Cada bloque de función definido sigue la siguiente estructura:

**1.** Bit enable

**2.** Correspondencia día semana

**3.** Intervalos horarios 

**4.** Señal de activación 

![image](uploads/f90079640f591e7c87fa4720f1a7284f/image.png)


**1. Bit enable**

El bit de "enable" una señal de habilitación del calendario que viene dada por Vigia para habilitar un calendario.

**2. Correspondencia día semana**

Si se habilita un calendario correspondiente para un día de la semana, los intervalos que se configuren solo deben de actuar para el día en concreto, por ello se define una comprobación del día correspondiente.

**3. Intervalos horarios**

Cada día de la semana tiene reservados 6 intervalos para definir el rango horario en el cual la salida va a estar activa.

**4. Señal de activación**

La señal de activación recoge la señal enviada por los calendarios que va a atacar a cada uno de los cirucitos.

Dependiendo de la lógica seguida en el autómata para la activación y desactivación de los circuitos, se utiliza la señal de activación para dicho cometido, en nuestro caso un flanco de subida enviará una señal de activación, y un flanco de bajada una señal de desactivación.


**Horarios en vigia**

Cada horario tiene un tipo definido en vigía y cada dispositivo va a tener su variable horario asociada **HORARIO_X**

Cada variable ataca a una MW concreta que corresponde a la palabra programada explícitamente en el código del autómata:

AQUÏ VA LA IMAGEN!! del dispositivo


**Automatización programación código PLC**

El programa de las imágenes se ha codificado en Ladder (LD) pero para automatizar su escritura se puede utilizar el formato (IL).

![image](uploads/73f75e944611d8475eb4014fbcc67739/image.png)

Para ello cada línea del programa ahora tiene asociada una fila concreta y el usuario puede modificar más rápidamente el código.

Para hacer la programación más eficiente se ha creado un script en python que mediante una MW de referencia segenera un fichero de texto, con las líneas correspondientes que hay que pegar en el programa, acelerando la creacción y actualización de los diferentes bloques de funciones.

| Archivo | Descripción |
| ------ | ------ |
| gen_program.py | Script |
| plantilla.txt | plantilla de referencia |
| programa_dia_x_reg_x.txt | Programa generado |

Para ejecutar el archivo se utiliza la consola de windows o un entorno de anaconda dónde esté instalado python.

![image](uploads/5c4031ef59fce2e24877cc224b1bac70/image.png)

Una vez ejecutado el programa te pide que le indiques el día de la semana

![image](uploads/342faaa4652498444959eada4a16376a/image.png)

En segundo lugar te pide que le indiques la palabra de referencia base.
![image](uploads/ebe4d28597f14c5a8e17f4340b46c9cc/image.png)

El programa muestra por pantalla el código generado, también disponible en el fichero "programa_dia_x_reg_x".

![image](uploads/72ce2b661ce53983fad5ad02b6d5a04e/image.png)

Una vez abierto el fichero de texto con bloc de notas, el usuario debe de copiar y pegar las líneas correspondientes en formato (IL) en el programa del autómata.
