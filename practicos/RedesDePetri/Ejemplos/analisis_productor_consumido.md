# Red de Petri Productor-Consumidor

## Enunciado
La red de petri productor consumidor es una red de petri que modela un sistema de productor consumidor. En este sistema, un productor produce un producto y lo coloca en un buffer compartido. Un consumidor toma el producto del buffer y lo consume. El buffer tiene una capacidad limitada, por lo que el productor debe esperar si el buffer está lleno y el consumidor debe esperar si el buffer está vacío.

## Analisis

1. ¿La red tiene deadlock?
No, porque ninguna transicion es conflictiva.

2. ¿Cuántos invariantes de plaza tiene la red?
**P-invariantes**

3. ¿La red es viva?

4. ¿La red es limitada?

5. ¿Existen conflictos en la red?

6. ¿La red es segura?

7. ¿Cuántos lugares tienen arcos inhibidores en sus plazas de entrada?

8. ¿Existen transiciones conflictivas?

9. ¿La red tiene invariante de marcado?

10. Clasificacion:
    - Maquina de estado: NO
    - Grafo de marcado: SI
    - Libre eleccion: SI
    - Libre eleccion extendida: SI
    - Red de Petri Simple : SI
    - Red de Petri Simple Extendida: SI