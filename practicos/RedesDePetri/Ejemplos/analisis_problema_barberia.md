# Red de Petri Problema de la Barberia


## Enunciado
La red de petri "Problema de la barberia" modela una barberia donde hay n=2 barberos, cada uno con su sillon de barbero. Ademas, tenemos una sala de espera con m=5 bancos en la que se sientan los clientes para esperar su turno. El funcionamiento se rige por las siguientes normas:
- Si no hay clientes que atender, el barbero espera (en su sillon).
- Los clientes entran de a uno a la barberia.
- Si hay clientes esperando y el barbero esta libre, el barbero llama al siguiente cliente y lo atiende.
- Si llega un cliente mientras los barberos estan ocupados, se sienta en la sala de espera.
- Los clientes se atienden sobre demanda, no rige un orden de llegada.
- Para cobrar hay una sola caja y debe ser atendida por un barbero, este barbero no podra atender mientras cobra en la caja.

## Analisis



1. ¿La red tiene deadlock?

2. ¿Cuántos invariantes de plaza tiene la red?
**P-invariantes**
//Completar

3. ¿La red es viva?

4. ¿La red es limitada?

5. ¿Existen conflictos en la red?

6. ¿La red es segura?

7. ¿Cuántos lugares tienen arcos inhibidores en sus plazas de entrada?

8. ¿Existen transiciones conflictivas?

9. ¿La red tiene invariante de marcado?

10. Clasificacion:
    - Maquina de estado: NO
    - Grafo de marcado: NO
    - Libre eleccion: NO
    - Libre eleccion extendida: NO
    - Red de Petri Simple : SI
    - Red de Petri Simple Extendida: SI