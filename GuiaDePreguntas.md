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
- Productor consumidor con semaforos
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
- Definicion de automata y gramatica.
- Relacion entre automatas y el caso practico del estacionamiento.
- Maquinas de estado.
- Maquina de moore vs mealy, cual es mas segura de usar?
    - Maquinas de Moore
    - Maquinas de Mealy
    - Maquina de Turing, acotado, pila, finito.
- Automatas de tipo 0 y 1 (explicacion de las jerarquias)
- qué es el universo del discurso, autómatas, jerarquías de gramáticas.
- cómo funciona un autómata de pila
- Relacionar simbolo, palabra, vocaculario, universo de .... , gramatica y lenguaje
- La gramatica para que sirve? quien la usa?

## U5. Redes de Petri
- Redes de petri temporales, clasificacion delay vs tiempo.
- Semantica de tiempo debil y fuerte.
- red de petri no autonoma
- Conflictos
- La red de petri es deterministica?
- Una rdp es determinista,puede no ser deterministica?
- que parte de la red puede tener el indeterminismo?  rta: si tiene conflictos es el indeterminista
- Que es el grado de sensibilizado de una transicion
- Fairness (permisos y parametros) Pregunta si tiene una herramienta para haer una red de petri, hacer un consumidor productor con buffer acotado

## Redes en PIPE
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
