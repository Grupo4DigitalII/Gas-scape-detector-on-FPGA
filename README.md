# Gas-scape-detector-on-FPGA
This project seeks to design an alternative method for the constant monitoring of sensitive areas of different plants, through the use of a robot that can constantly census the concentrations of gases in the environment of these areas and send this data for analysis at any time.


## 1. Objetivos 
### General: 
Construir un prototipo de robot detector de fugas de gases para uso en refinerías o plantas industriales.
### Especificos:
* Desarrollar un módulo de adquisición y digitalización de concentración de gas en el ambiente
* Desarrollar módulo de movimiento del dispositivo que permita el seguimiento de línea
* Desarrollar módulo de comunicaciones inalámbricas para la transición de datos al usuario

## Problema
### Necesidad
Un procedimiento usual para la identificación de fugas de gas en refinerías es el uso de diferentes tipos de sensores, por ejemplo, sensores infrarrojos que permiten detectar columnas de gas o Analizadores de Vapor Tóxico, con los cuales se miden las concentraciones de diversos gases en puntos donde se deban verificar fugas, sin embargo, estos sensores requieren de operarios para su uso, por lo que realmente no dan una retroalimentación constante de este factor de riesgo, a la vez que exponen a la persona que los opera a posibles concentraciones peligrosas de diversos gases o vapores.

### Impacto buscado 
El proyecto busca diseñar una alternativa de monitoreo de posibles fugas de gas, mediante el uso de un robot capaz de patrullar una trayectoria alrededor de la cual mide constantemente la concentración de gases, permitiendo así la detección temprana de dichas fugas, además de evitar la exposición directa de personas a las mismas.

Aunque el robot en sí mismo no soluciona la fuga de gas, permite obtener datos con los cuales un operario o trabajador de la planta puede prepararse para la reparación adecuadamente, minimizando al máximo posibles riesgos para su integridad.

## 3. Perifericos
* Motores - Paralelo
* Arduino - UART
* Esp32 - UART
* Seguidor de linea:

Los sensores escogidos para la función de seguimiento de línea fueron los módulos KY-033, los cuales mediante un haz concentrado de luz infrarroja, pueden detectar si la superficie que tienen justo enfrente es o no reflectante, entregando una salida digital de 1 bit, como se muestra en la siguiente tabla:
 
<img width="250" alt="Tabla1" src="https://user-images.githubusercontent.com/108437348/176576640-2e1b4338-9aad-438f-b7ee-3a22be6fdad9.png">

Adicionalmente, la sensibilidad del dispositivo puede ajustarse fácilmente mediante un potenciómetro, usado en la mayoría de los casos para modificar la distancia a la cual el dispositivo puede diferenciar satisfactoriamente entre una superficie reflectante o no reflectante.

<img width="250" alt="KY033" src="https://user-images.githubusercontent.com/108437348/176566935-141974bb-db18-4c46-94e1-7e05ff3942ac.png">
 

<img width="250" alt="modulo L298N" src="https://user-images.githubusercontent.com/108437348/176566847-1c70fb78-549e-4451-aff2-d4e7073fe5cc.png">

<img width="250" alt="MQ2" src="https://user-images.githubusercontent.com/108437348/176566919-61dd6d5c-8801-4e8b-8543-65a1290e3ba5.png">



<img width="250" alt="ESP-32" src="https://user-images.githubusercontent.com/108437348/176566952-9a6c523a-0d3c-4fb4-98b4-35f7710d13c4.jpg">

<img width="250" alt="nexys-a7-obl-600" src="https://user-images.githubusercontent.com/108437348/176568131-23067dcc-98f9-4cbb-b73f-726cad7f492e.png">

<img width="250" alt="motores" src="https://user-images.githubusercontent.com/108437348/176568182-6849816f-1fc4-43ea-8e1d-ca6cbcfa9f55.png">

<img width="350" atl="diagrama cajas general" src="https://user-images.githubusercontent.com/108437348/176575029-c837ae64-28e0-492c-b1ef-f1fea796c78f.png">

## 4. Mapa de memoria 
## 5. Explicación codigo - modulos 
## 6. Partes - Presupuesto

## 7. Funcionamiento
* Control de seguidor de linea
* Sensor de gases
* Comunicación inalmbrica
 
