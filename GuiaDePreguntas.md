# Guia de preguntas
## U1. Conceptos Basicos

**Sistemas reactivos**
- Un sistema reactivo es aquel que responde a estímulos externos en un tiempo determinado.

**El testing es suficiente?**
- NO, el testing no es suficiente, ya que no se puede probar todas las posibles combinaciones de estados y eventos.
- Como el testing no es suficiente tenemos que modelar el sistema para poder probarlo. Por ejemplo con redes de petri.

**Que es la Traza o interleaving y que relacion tiene con los t-invariantes?**
- La traza o interleaving de un sistema concurrente es la secuencia de eventos o transiciones que ocurren en el sistema.
- Los t-invariantes son invariantes de transicion, que son invariantes que se cumplen (siempre) en cada uno de los pasos de la traza.

**Que es la vivacidad y el deadlock?**
- La **Vivacidad** en los sistemas concurrentes se refiere a que el sistema va a avanzar, es decir, que no se quedara trabado en un estado.

- El **DeadLock** o interbloqueo es un estado en el que se encuentran dos o mas procesos o hilos. Se encuentran bloqueandose mutuamente, es decir, que ninguno puede avanzar debido a que esta esperando que el otro termine o envie un mensaje.

**Un problema concurrente se ejecuta siempre igual?**
- NO, un problema concurrente puede ejecutarse de diferentes formas, debido al indeterminismo que existe a la hora de ejecutarse los hilos.

**Diferencias entre Paralelismo y concurrencia**
- El **Paralelismo** es la ejecucion de dos o mas tareas al mismo tiempo, es decir, que se ejecutan en simultaneo.
- La **Concurrencia** es la ejecucion de dos o mas tareas en un mismo intervalo de tiempo, es decir, que se ejecutan en forma alternada.

**Nota:** Esas son algunas de las preguntas/disparadores mas comunes respecto a los Conceptos Basicos. Se recomienda leer la bibliografia para poder responder mas preguntas.


## U2. Manejo basico de threads

**Diferencia entre el metodo start() y run() de un hilo**
- En el lenguaje de programacion Java metodo **start()** es el encargado de crear un nuevo hilo y ejecutar el metodo **run()** en el nuevo hilo. 
Mientras que el metodo **run()** es el encargado de ejecutar el codigo del hilo.

**Procesos vs Hilos**
- Un **Proceso** es un programa en ejecucion, es decir, que es una instancia de un programa en ejecucion. Un proceso tiene su propio espacio de memoria, es decir, que no comparte memoria con otros procesos.
- Un **Hilo** es una unidad de ejecucion dentro de un proceso. Un proceso puede tener uno o mas hilos. Los hilos comparten el espacio de memoria del proceso.

- **Estados de los hilos**
    - **New:** El hilo fue creado pero no se ha iniciado.
    - **Ready:** El hilo esta creado y listo para ser ejecutado.
    - **Running:** El hilo esta siendo ejecutado.
    - **Blocked:** El hilo esta bloqueado, es decir, que esta esperando que se libere un recurso.
    - **Sleeping:** El hilo esta durmiendo, es decir, que esta esperando que pase un tiempo determinado.
    - **Waiting:** El hilo esta esperando que otro hilo termine de ejecutarse y notifique.
    - **Dead:** El hilo termino de ejecutarse.

.
- **Estados de los Procesos**:
    - **New:** El proceso fue creado pero no se ha iniciado.
    - **Ready:** El proceso esta listo para ser ejecutado.
    - **Running:** El proceso esta siendo ejecutado.
    - **Blocked:** El proceso esta bloqueado, es decir, que esta esperando que se libere un recurso.
    - **Dead:** El proceso termino de ejecutarse.

**Si el procesador no le da tiempo de ejecucion al hilo, en que estado se encuentra?**
- El hilo se encuentra en el estado **Ready**.

## U3. Sincronizacion basada en memoria compartida
En esta seccion si bien hay preguntas estan muy relacionadas al concepto de cada tipo ed sincronizacion, entonces solo vamos a definir cada una a modo resumen.

Los metodos de sincronizacion basada en memoria compartida (ordenados por complejidad) son:

- **Establecer secciones criticas:** Mecanismos que permitiendo la ejecucion de un bloque de codigo en forma segura.
    - **Synchronized:** Es el mas simple de implementar, ya que solo se necesita agregar la palabra reservada **synchronized** en la firma del metodo. Este metodo es el mas costoso en cuanto a tiempo de ejecucion, ya que se necesita obtener el lock del objeto.

    - **Lock:** Es un mecanismo mas complejo de implementar, ya que se necesita crear un objeto de tipo **Lock** y luego utilizar los metodos **lock()** y **unlock()** para obtener y liberar el lock del objeto. Este metodo es mas rapido que el metodo **synchronized**.
    
- **Mediante semaforos:** Tienen una variable entera que indica la cantidad de recursos disponibles y se comparte entre los hilos.
    - **Semaphore:** Es un mecanismo mas complejo de implementar, ya que se necesita crear un objeto de tipo **Semaphore** y luego utilizar los metodos **acquire()** y **release()** para obtener y liberar el lock del objeto. Este metodo es mas rapido que el metodo **Lock**.

    - **CycleBarrier:** Es un mecanismo mas complejo de implementar, ya que se necesita crear un objeto de tipo **CycleBarrier** y luego utilizar el metodo **await()** para obtener el lock del objeto. Este metodo es mas rapido que el metodo **Lock**.

- **Mediante Monitores:** Son modulos de alto nivel que encapsulan los metodos de sincronizacion.
    - **Monitor:** Es un mecanismo mas complejo de implementar, ya que se necesita crear un objeto de   tipo **Monitor** y luego utilizar los metodos **wait()** y **notify()** para obtener y liberar el lock del objeto. Este metodo es mas rapido que el metodo **Lock**.

Productor consumidor con semaforos
    - Cuantos semaforos se necesitan para el modelo productor-consumidor con buffer de huecos y de items?
    - A ese semaforo con cuanto lo puedo inicializar?
- Politicas de los semaforos/monitores no se bien.    

- **Semaforos**
    - como funciona, 
    - es un objeto?, 
    - tiene dueño? No, no tiene dueño ya que no es como un lock
    - Puedo elegir que hilo quiero que despierte en un semaforo?
    - Tiene sentido inicializar un semaforo en 0?
    - Productor consumidor, dibujar, semaforos por buffer, importa orden de acceso a los semaforos? Si, primero buffer, y despues mutex
    - Ventajas de la cola de cortesia, para que sirve? Cola de cortesia sirve para cederle tiempo a uno que venga urgido
    - si hay mas de un hilo, tengo forma de saber a cual despertare? No recuerda si hay alguna forma de configurar el semaforo para configurar esas polticas. Que datos les tengo que dar a uno cuando inicializo en java? Puedo pasar un valor 0?
    - Los semaforos se pueden configurar para que sean una FIFO?
    - semáforos, qué son y para qué se usan, qué operaciones puedo realizar con ellos, ownership
    - Productor consumidor, dibujar, semáforos por buffer, importa orden de acceso a los semáforos? Si, primero buffer, y después mutex

- Monitor
    - como funcionan, 
    - para qué se usan, 
    - que tipos de colas existen
    - cual es el beneficio de una cola de cortesía. 
    - qué acciones puedo realizar sobre una cola de espera de condición (irme a dormir, despertar, preguntar por quienes están durmiendo)
    - en el momento en que un hilo despierta a otro adentro del monitor, y uno nuevo toma el mutex, quien toma el control de la ejecución? la jvm, el dispatcher, estados de los procesos
    - cuales son los beneficios de utilizar un monitor frente a semáforos?



## U4. Gramatica, lenguajes y automatas
**Definicion de automata y gramatica**
- Un **automata** es una construccion logica que permite representar un sistema que recibe una entrada y genera una salida. Un automata esta compuesto por un conjunto de estados, un alfabeto de entrada, un alfabeto de salida y una funcion de transicion. Los automatas se pueden clasificar en deterministas y no deterministas.
- Una **gramatica** es un conjunto de reglas que permiten generar un lenguaje. Las gramaticas se pueden clasificar en regulares, libres de contexto, sensibles al contexto y recursivamente enumerables.

**Maquians de estado**
- Una maquina de estado es un modelo matematico que permite representar un sistema que se encuentra en un estado determinado y que puede cambiar de estado en funcion de una entrada. Las maquinas de estado se pueden clasificar en maquinas de moore y maquinas de mealy.

**Maquinas de Moore vs Maquinas de Mealy**
- Las maquinas de Moore son maquinas de estado finito que se caracterizan por tener una salida que depende unicamente del estado actual. Las maquinas de Moore se pueden representar mediante un diagrama de estados o mediante una tabla de estados.
- Las maquinas de Mealy son maquinas de estado finito que se caracterizan por tener una salida que depende del estado actual y de la entrada. Las maquinas de Mealy se pueden representar mediante un diagrama de estados o mediante una tabla de estados.

**Cual es mas segura de usar?**
- La maquina de Moore es mas segura de usar porque la salida depende unicamente del estado actual, mientras que en la maquina de Mealy la salida depende del estado actual y de la entrada.

**Maquina de Turing**
- Una maquina de Turing o automata de tipo 0 es un automata con cabezal movil que se mueve libremente sobre una cinta infinita. La funcion de transicion que depende del estado actual y del simbolo que se encuentra en la cinta.

**Automata lineal acotado**
- Un automata acotado es un automata con cabezal movil que se mueve sobre una cinta acotada. La funcion de transicion que depende del estado actual y del simbolo que se encuentra en la cinta.

**Automata de pila**
- Un automata de pila es un automata con cabezal movil que se mueve sobre una cinta acotada y que tiene una pila. Esto lo limita a ser un automata de tipo 1. La funcion de transicion que depende del estado actual, del simbolo que se encuentra en la cinta y del simbolo que se encuentra en el tope de la pila.

**Automata finito**
- Un automata finito es un automata con cabezal movil que se mueve sobre una cinta acotada en una sola direccion y que no tiene memoria. 

**Jerarquia de Chomsky**
- La jerarquia de Chomsky es una clasificacion de los lenguajes formales en funcion de la complejidad de las gramaticas que los generan. La jerarquia de Chomsky se compone de 4 niveles: lenguajes regulares, lenguajes libres de contexto, lenguajes sensibles al contexto y lenguajes recursivamente enumerables.


**Relacionar simbolo, palabra, vocaculario, universo del discurso, gramatica y lenguaje**
- **Simbolo**: Un simbolo es la unidad mas pequeña de un lenguaje.
- **Palabra**: Una palabra es una secuencia de simbolos.
- **Vocabulario**: Un vocabulario es un conjunto de simbolos.
- **Universo del discurso**: El universo del discurso es el conjunto de todas las palabras que pueden ser generadas por una gramatica.
- **Gramatica**: Una gramatica es un conjunto de reglas que permiten generar un lenguaje.
- **Lenguaje**: Un lenguaje es un conjunto de palabras que respetan una gramatica en particular.

**La gramatica para que sirve? quien la usa?**
- La gramatica sirve para generar un lenguaje. La gramatica es utilizada por un automata para reconocer un lenguaje.

- Relacion entre automatas y el caso practico del estacionamiento.

## U5. Redes de Petri
**Que son las Redes de petri temporales?**
- Las redes de petri temporales son aquellas en donde las transiciones pueden tener un tiempo de demora. Las redes de petri temporales se pueden clasificar en redes de petri temporales deterministas y redes de petri temporales no deterministas.

**Clasificacion: Delay y Tiempo**
- En una PN con delay, el tiempo asociado al firing de una transición indica el tiempo que
tarda en concretarse el firing de esta transición
- En una PN con tiempo (PNT) se especifica la duración del firing de una transición mediante
la asociación de un intervalo que abarque todas las posibilidades de duración de la actividad. Esto
presenta la ventaja de analizar un sistema en los peores escenarios.

**Semantica de tiempo debil y fuerte**
- La semantica de tiempo fuerte indica en que momento y con que condiciones se debe realizar el firing de la transicion. Esta semantica es apropiada para el modelado de sistemas en tiempo real.
- En la semantica de tiempo debil la transicion no esta obligada a dispararse, pero, si lo hace, debe ser en el intervalo especificado.

**Red de Petri Autonoma y No Autonoma**
- Una Red de Petri es autonoma cuando sus instantes de firing sond esconocidos o noe stan indicados
- Una Red de Petri No es autonoma cuando se disparan sus transiciones cumpliendo condiciones de sensibilizado y estan asociadas a un evento externo.

**Conflictos**
- Un conflicto estructural se da cuando una plaza tiene mas de una transicion de salida.

**La red de petri es deterministica?**
- Una red de petri es deterministica cuando no tiene conflictos, todas sus transiciones puede ser definidas logicamente.

**Una rdp es determinista, puede no ser deterministica?**
- Una red de petri deterministica puede no ser deterministica si tiene conflictos.

*Qque parte de la red puede tener el indeterminismo?**
- Si tiene conflictos es el indeterminista, entonces donde tenga conflictos

**Que es el grado de sensibilizado de una transicion**
- El grado de sensibilizado de una transicion es la cantidad de tokens que debe tener cada plaza de entrada para que la transicion este sensibilizada.

**Fairness (permisos y parametros)**
- El fairness es un mecanismo que permite que una transicion se dispare cuando se cumple una condicion. El fairness se puede implementar mediante un parametro o un permiso.

## Redes en PIPE
### Listas de Youtube para practicar
- [Juan Rivera Tecnologia](https://www.youtube.com/watch?v=oLOYJmmcgmo&list=PLmg7O-zMXJjuTuJFhtRspMTr2RfjX_Naa)
- [SocialLearningService](https://www.youtube.com/watch?v=pgFfMc6J3YU&list=PLj1yRsEYVjuVUqFTwAz8a6qoSv9F4gDAU)
- [SLS Open](https://www.youtube.com/watch?v=2cb_Eit0j58&list=PL55DwcAO0cqw0db8MVIPdnigin8_0mAgU)
- [Conferencia Redes de Petri Bs.As](https://www.youtube.com/watch?v=WnfS5qEB8Wc)
- [Red de petri temporal](https://www.youtube.com/watch?v=WnfS5qEB8Wc)
- [Ejemplos Luis Salinas](https://www.youtube.com/watch?v=O_p56f0O6O0)

- Productor consumidor con 3 lugares en el buffer.
    - Ver invariantes y propiedades
    - Convertir la red en segura
    - Meter un deadlock.
- Red de la barberia
- Cena de los Filosofos
    - Se puede representar con una red de petri coloreada? Si, se puede.
    - En la red de filosofos, invariantes de transicion, para que sirven y si tienen. Invariantes de plaza, que es lo que son? Relacionar con filosofos. explicacion fisica de que significa.
    - preguntó si estaba acotada, si tenía deadlock, si era segura, si era de libre elección, liveness
    - ya que se repetían las estructuras, cómo podia hacer para que con una sola represente a los 3 filósofos? haciendola coloreada
    - mostrar los invariantes de plaza y de transición, decir qué eran y que representaban fisicamente
