# Guia de preguntas
## U1. Conceptos Basicos
- Sistemas reactivos
- testing insuficiente
- Traza (interleaving) y t-invariantes.
- vivacidad y deadlock
- Un problema concurrente se ejecuta siempre igual?
- Paralelismo y concurrencia

## U2. Manejo basico de threads
- Diferencia entre el start y run de un thread.
- Procesos vs Hilos
- Estados de los hilos y los procesos
- Si el procesador no le da tiempo de ejecucion, en que estado esta?

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
