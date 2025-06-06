# Bitcoin v0.1 – Código Original de Satoshi Nakamoto

Este repositorio contiene el código fuente de la primera versión pública de Bitcoin (v0.1), creada por Satoshi Nakamoto y lanzada en enero de 2009. También incluye una versión de prueba más antigua, de noviembre de 2008, que nunca fue publicada oficialmente hasta ahora.

El proyecto implementa una moneda digital descentralizada, que permite transferencias de valor entre personas sin necesidad de un intermediario (como un banco). Esta es la base del sistema que hoy se conoce como blockchain.

## Contenido del repositorio

- `nov08/`: versión prototipo anterior al lanzamiento público.
- `bitcoin0.1/`: versión pública original lanzada en 2009.
- `study/`: código fuente organizado para análisis.
- `bitcoin.pdf`: documento original (whitepaper) que describe el concepto de Bitcoin.

## ¿Cómo funciona Bitcoin v0.1?

Bitcoin funciona a través de una red distribuida de computadoras (nodos) que comparten información entre sí. Estos son los componentes principales del sistema:

### 1. Red Peer-to-Peer (P2P)

Bitcoin se basa en una red P2P. Cada nodo del sistema se conecta con otros y se comunica para compartir información sobre nuevas transacciones y bloques.

### 2. Transacciones

Las transacciones son mensajes que indican que cierta cantidad de bitcoins ha sido enviada de una dirección a otra. Cada transacción está firmada digitalmente, lo que garantiza que solo el dueño de las monedas puede usarlas.

### 3. Bloques y Cadena de Bloques

Las transacciones se agrupan en bloques. Cada bloque también contiene una referencia al bloque anterior, formando así una "cadena de bloques" (blockchain).

### 4. Prueba de Trabajo (Proof of Work)

Para agregar un nuevo bloque a la cadena, los nodos deben resolver un problema matemático difícil. Esto se conoce como minería. Resolver este problema prueba que se ha hecho un trabajo computacional (de ahí el nombre "prueba de trabajo").

### 5. Recompensas y Minería

El primer nodo que resuelve el problema del bloque recibe una recompensa en bitcoins recién creados. Esto incentiva a los participantes a mantener la red funcionando.

### 6. Scripting

Bitcoin incluye un lenguaje de scripts muy básico, usado para definir las reglas sobre cómo se pueden gastar las monedas (por ejemplo, asegurarse de que una firma sea válida).

## Tecnologías y lenguajes

El código está principalmente escrito en:

- C++ (la lógica del sistema)
- C (algunas funciones de red y sistema)
- Recursos del sistema Windows (al tratarse de la primera versión, es dependiente de Windows)

## ¿Por qué es importante?

Este código representa el primer paso en la creación de Bitcoin y el nacimiento de la tecnología blockchain. Aunque es muy básico en comparación con las versiones actuales, incluye todos los elementos esenciales: red descentralizada, blockchain, minería, validación de transacciones, y firma digital.

Estudiarlo ayuda a entender cómo funciona Bitcoin desde su base, sin la complejidad añadida de años de desarrollo posterior.


---
