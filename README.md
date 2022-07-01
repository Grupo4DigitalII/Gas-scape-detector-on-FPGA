# GAS SCAPE DETECTOR FOR INDUSTRIES - ON FPGA

<img width="400" alt="detector" src="https://user-images.githubusercontent.com/108437348/176722706-d3264a1f-eaaa-4324-b12c-c3f64b6f57f4.jpeg">


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

### Efecto Esperado
El proyecto busca diseñar una alternativa de monitoreo de posibles fugas de gas, mediante el uso de un robot capaz de patrullar una trayectoria alrededor de la cual mide constantemente la concentración de gases, permitiendo así la detección temprana de dichas fugas, además de evitar la exposición directa de personas a las mismas.

Aunque el robot en sí mismo no soluciona la fuga de gas, permite obtener datos con los cuales un operario o trabajador de la planta puede prepararse para la reparación adecuadamente, minimizando al máximo posibles riesgos para su integridad.

## 3. Perifericos
* Arduino - UART

<img width="250" alt="arduino" src="https://user-images.githubusercontent.com/108437348/176717523-a2db9fff-16c8-4a65-92bf-6b24baf1bb12.png">

Actúa como conversor de la señal recibida en el sensor MQ2. Se encarga de recibir la señal analoga y convertirla a señal digital.


* Seguidor de linea:

<img width="250" alt="KY033" src="https://user-images.githubusercontent.com/108437348/176566935-141974bb-db18-4c46-94e1-7e05ff3942ac.png">

Los sensores escogidos para la función de seguimiento de línea fueron los módulos KY-033, los cuales mediante un haz concentrado de luz infrarroja, pueden detectar si la superficie que tienen justo enfrente es o no reflectante, entregando una salida digital de 1 bit, como se muestra en la siguiente tabla:
 
<img width="250" alt="Tabla1" src="https://user-images.githubusercontent.com/108437348/176576640-2e1b4338-9aad-438f-b7ee-3a22be6fdad9.png">

Adicionalmente, la sensibilidad del dispositivo puede ajustarse fácilmente mediante un potenciómetro, usado en la mayoría de los casos para modificar la distancia a la cual el dispositivo puede diferenciar satisfactoriamente entre una superficie reflectante o no reflectante. Los pines que posee el dispositivo se muestran en la siguiente tabla:

<img width="250" alt="tabla2" src="https://user-images.githubusercontent.com/108437348/176577990-61a70f6f-069f-467c-9215-344f16a65a31.png">

* Sensor de Gas

<img width="250" alt="MQ2" src="https://user-images.githubusercontent.com/108437348/176566919-61dd6d5c-8801-4e8b-8543-65a1290e3ba5.png">

Para la detección de gas se seleccionó un módulo con un sensor de la familia MQ, específicamente el MQ-2, el cual es sensible al hidrógeno molecular ($H_2$), Gas Licuado de Petróleo (GLP), Metano ($CH_4$), Monóxido de Carbono (CO), Alcohol, Humo y Propano. Se escogió este sensor, ya que permite simular su funcionamiento con gases de una zona industrial con el uso de metano, el cual puede ser conseguido y manipulado, por ejemplo, con un encendedor desechable, sin embargo, no se debe olvidar tomar medidas de seguridad.

<img width="400" alt="curvaSensibilidadMQ2" src="https://user-images.githubusercontent.com/108437348/176578309-39952e01-d9c0-462d-b6b8-8a377d173791.png">

La mínima cantidad que puede detectar el dispositivo es 200ppm, mientras que la máxima es alrededor de 10000ppm. La siguiente tabla contiene el orden de los pines del sensor:

<img width="250" alt="tabla3" src="https://user-images.githubusercontent.com/108437348/176579104-e4f6b8fb-c8e5-4287-b9c0-bc0a85ff45a0.png">

Aunque el dispositivo tiene salida digital, esta solo envía un estado alto cuando se supera un nivel de concentración determinado por el potenciómetro, por ello, para el desarrollo del proyecto y una medición adecuada de la concentración de gas en el aire, se debe usar la salida analógica, por lo que se hace necesario implementar un conversor análogo a digital, el cual es que se va a comunicar con la FPGA.


* Comunicación Wi-Fi:

<img width="250" alt="ESP-32" src="https://user-images.githubusercontent.com/108437348/176566952-9a6c523a-0d3c-4fb4-98b4-35f7710d13c4.jpg">
 
Para realizar la comunicación Wi-Fi, se escogió el SoC ESP32, el cual tiene integrado un microprocesador con tecnología integrada para trabajar con Wi-Fi y Bluetooth. Este módulo facilita el envío de los datos al poderse programar para este propósito con librerías disponibles en la web, comunicándose con el procesador de la FPGA mediante UART.
 
* L298N Dual H-Bridge motor driver:

<img width="250" alt="modulo L298N" src="https://user-images.githubusercontent.com/108437348/176566847-1c70fb78-549e-4451-aff2-d4e7073fe5cc.png">

<img width="250" alt="motores" src="https://user-images.githubusercontent.com/108437348/176568182-6849816f-1fc4-43ea-8e1d-ca6cbcfa9f55.png">

Este modulo bidireccional para motores, esta basado en el circuito integrado de puente H dual L298, el cual permite el control independiente, en ambos sentidos de giro, de hasta dos motores bien sea motores DC o motores paso a paso.


## 4. Mapa de memoria 
El mapa de memoria del proyecto puede ser accedido y revisado completamente en el documento "Soc_MemoryMap.csv", que puede ser visualizado con mayor facilidad en algún programa como Excel o LibreOffice Calc, sin embargo, a continuación se presentan algunos datos importantes depositados en dicho archivo.

En primer lugar, se muestra el mapa de memoria de la sección de perifericos, con cada uno de los que fueron usados en el desarrollo e implementación del proyecto, adjuntando una breve descripción del uso de cada uno de ellos.

| Periferico | Nombre | Dirección Base | Descripción |
|-------------|---------|---------|----------------|
| Driver Motores | `driverM` |  0x82001000 | Módulo controlador para los motores, creado en verilog. |
| Uart ESP-32 | `uart1` | 0x82004000 | Módulo uart usado para la comunicación con la ESP-32. |
| Uart Arduino | `uart2` | 0x82005000 | Módulo uart usado para la comunicación con el arduino. |
| Uart PC | `uart` | 0x82006800 | Módulo uart que permite la comunicación con el computador, usado principalmente para pruebas. | 

Se destaca de forma adicional, los registros mapeados en memoria del módulo driver del motor, con el fin de explicar su finción.

| Registro | Dirección | r/w |  Descripción |
| --- | --- | --- | --- |
| `driverM_statusM` | 0x82001000 | ro | Permite la lectura del estado actual de los sensores de línea, y por consecuencia, de los motores. |
| `driverM_ena` | 0x82001004 | rw | Permite habilitar o deshabilitar el movimiento de los motores al escribir en el un 0 (deshabilitar) o un 1 (habilitar). |

**NOTA: El archivo verilog de este módulo se encuentra en la carpeta /module/verilog.** 


## 5. Explicación codigo - modulos

Previo a la explicación del sistema, se muestra un corto vídeo del dispositivo en funcionamiento, con el fin de facilitar la comprensión de esta sección.

https://user-images.githubusercontent.com/108437348/176825390-9b62fde0-2165-4866-a7dd-da3f8394d124.mp4

En un primer momento, se propuso el siguiente diagrama de cajas para el Sistema en Chip ("SoC").

<img width="350" atl="diagrama cajas general" src="https://user-images.githubusercontent.com/108437348/176575029-c837ae64-28e0-492c-b1ef-f1fea796c78f.png">

No obstante, el prototipo final se representa mejor con el siguiente diagrama:



El funcionamiento del dispositivo se puede explicar brevemente de la siguiente forma:

1. El procesador solicita mediante el módulo `uart2` al arduino, el valor medido por el sensor de gases MQ-2.
2. Se compara si el valor supera un umbral definido en el código, de ser así, deshabilita el funcionamiento de los motores, de lo contrario se habilitan.
3. Cada segundo se envía el dato a través del `uart1` a la ESP-32, la cual lo carga al servidor de la aplicación "Blynk" para la visualización en App móvil o web del valor en tiempo real y una gráfica donde se registra la variación de la concentración del gas en ppm.  

Al superar la concentración definida como umbral, el dispositivo se detiene con el objetivo de dar tiempo al usuario final de percatarse de una posible fuga y tomar las medidas necesarias. La siguiente tabla muestra lo que vería el usuario del dispositivo al usar la web o la App.

| Web | App |
| --- | --- |
|<img width="350" atl="Medición baja concentración web" src="https://user-images.githubusercontent.com/108437348/176831790-f8a33cb0-6853-43b9-a85b-7613d7351fc4.png"> <br> <img width="350" atl="Medición alta concentración web" src="https://user-images.githubusercontent.com/108437348/176833023-f918b1d2-c8e6-4f6d-b709-86ce2d9975e6.png"> | <img width="300" atl="Medición con App móvil" src="https://user-images.githubusercontent.com/108437348/176832727-0688e4dd-1a55-45f1-a456-d4145f965a47.jpg">|


## 6. Partes - Presupuesto

<img width="250" alt="nexys-a7-obl-600" src="https://user-images.githubusercontent.com/108437348/176568131-23067dcc-98f9-4cbb-b73f-726cad7f492e.png">

| Partes | Precio aprox. |
| ------------- | ------------- |
| KY-033  | 14.000  |
| MQ2 | 10.000 |
| ESP32 | 32.000  |
| L298N | 18.000  |
| Ruedas| 30.000  |
| Cables| 10.000 |
| Base carro |8.000  |
| Arduino | 52.000  |
| Power bank  | 17.000 |


## 7. Desafíos
### Durante el desarrollo:
* Alimentacion externa - Tipo de alimentación y ajuste
* Duración de la bateria - 2000mAh dura aproximadamente 40 minutos con carga 
* Desarrollo de protocolos de comunicación y conversión 
### A futuro:

* Ajustar el diseño del carro para que se pueda prensar a la tubería de la compañía con la que se vaya a trabajar.
* Reducir la vecidad del carro para que haga un escaneo completo.
* Agregar otros sensores, lo cual haga más sensible la lectura de gases presentes.
 
