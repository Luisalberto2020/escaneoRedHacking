

<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 9.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**Escaneo de Red**



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")




<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")



## Índice


[TOC]



# 


# Objetivo

Nuestro objetivo es crear una herramienta que sea capaz de escanear la red y todos los puertos para conocer mejor nuestra red.


# Solución

Hemos optado  por usar scapy ya que es una librería que trabaja con socket (bajo nivel de python) con lo cual no dependemos nada más que python para hacer el escaneo de red.


# Puesta en marcha


## Normal

pip install -r requirements.txt

python app.py -h


## Con env

python -m venv environment

pip install -r requirements.txt


## Con dev containers

Si te fijas en el proyecto se encuentra una carpeta llamada .dev containers  con lo cual si abres el proyecto con el vscode con la extensión dev containers le notificará que abra la carpeta en el contenedor y cuando se le habrá tendra un contenedor python con las dependencias instaladas


## Repositorio

[https://github.com/Luisalberto2020/escaneoRedHacking](https://github.com/Luisalberto2020/escaneoRedHacking)


# Ejemplos de uso

python app.py -r 192.168.95.176/30 -p 22,80 -t 2 -j salida.json

python app.py -r 192.168.95.176/30 -p all  -j salida.json

python app.py -r 192.168.95.176/30 -p 22,80 -t 2 -v -j salida.json

python app.py -i 192.168.95.178 -p 22,80 -pn


# Estructura del proyecto



* Archivo principal es app.py
* Archivo de pruebas testFuncionamiento.py
* **Utils**
    * **menu.py**: Se encarga de los argumentos y de imprimir por pantalla el resultado.
    * **network.py** Se encarga de comprobar los argumentos en tema de red aparte hace operaciones básicas de red como sacar los host de la red etc.
    * **ping.py**: Es la clase que cuando se construye hace un ping a una máquina y luego para obtener la información si está activa la máquina da un resumen de la información del ping en un diccionario etc.
    * **portScanner.py:**Es la clase que cuando se construye hace un escaneo de un puerto y luego tiene diversos métodos para obtener la información resultante en formato diccionario.
* **Servicios**
    * **AppService.py**: Es el servicio principal de la app llevando la lógica de la aplicación en especial con los métodos main_ping y main_scan con la gestión de los hilos y los bucles de generación de los objetos ping y port scanner.
    *  **almacenamientoService**:Es el que se encarga de almacenar los datos en formato json.

# 
        Algoritmo



## Tratado de errores con ValueError:

	

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





Como se ve en la foto si hay error de parseo mandara un value error que en el main lo capturara y mandará el mensaje



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>






## Manejo de los hilos:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


Aquí trabajamos con una cola de hilos donde le especificamos el número máximo de hilos y python gestiona que no pase nunca ese número máximo de hilos.


## Manejo de expresiones regulares

los argumentos se chequean con expresiones regulares como la siguiente con re.mach comprobamos que la ip sea correcta



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>






## Funciones estáticas

Son los objetos que no hace falta construirlos por ejemplo network y usamos funciones estáticas co @staticmetod



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")



## Programación orientada a objetos

Como se puede observar  las clases ping y scanPort son dos clases orientadas a objetos donde cuando se construye realizamos las operaciones y después consultamos y modificamos sus atributos



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>





# Pruebas 

Para las pruebas hemos comprobados los errores al introducir los datos como por ejemplo



<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>




y en el funcionamiento hemos hecho un programa de pruebas que se llama de testdefuncionamiento para probar el funcionamiento del programa


## Código a fondo por clases


## App:Services

La clase AppService define métodos estáticos que pueden ser invocados desde el exterior de la clase para realizar cada una de estas funcionalidades.

El método **main_ping **es el encargado de realizar el ping a una o varias direcciones IP. Recibe como parámetro un diccionario args que contiene información sobre qué direcciones IP deben ser escaneadas, el número de threads a utilizar, si se desea mostrar información verbose y si se desea realizar un ping null. Si se especifica una dirección IP, se realiza un ping a esa dirección. Si se especifica una red, se obtienen todas las direcciones IP de la red y se realiza un ping a cada una de ellas.

Si no se desea realizar un ping null, se comprueba si se debe utilizar un thread único o varios threads para realizar el ping. Si se utiliza un thread único, se itera sobre cada dirección IP y se realiza un ping a cada una de ellas. Si se utilizan varios threads, se utiliza un ThreadPoolExecutor para realizar el ping en paralelo a cada dirección IP.

Si se desea realizar un ping null, se itera sobre cada dirección IP y se añade una entrada al resultado con la dirección IP y un sistema y MAC desconocidos.

El método **main_scan **es el encargado de realizar el escaneo de puertos. Recibe como parámetros un diccionario args que contiene información sobre qué direcciones IP y puertos deben ser escaneados, el número de threads a utilizar, si se desea mostrar información verbose y si se desea mostrar el banner del servicio. Si se especifica una dirección IP y un puerto, se realiza un escaneo al puerto especificado en la dirección IP especificada. Si se especifica una dirección IP y varios puertos, se realiza un escaneo a todos los puertos especificados en la dirección IP especificada. Si se especifica una red, se obtienen todas las direcciones IP de la red y se realiza un escaneo a todos los puertos especificados en cada una de las direcciones IP.

Si se utilizan varios threads, se utiliza un ThreadPoolExecutor para realizar el escaneo en paralelo a cada puerto en cada dirección IP. Si no se utilizan threads, se itera sobre cada puerto y se realiza un escaneo a cada una ip y puerto e ip


## La clase Almacenamiento service 

La clase **AlmacenamientoService **define un método estático llamado save_json que se encarga de realizar esta operación.

El método **save_json **recibe como parámetros dos diccionarios con información sobre el ping y el escaneo de puertos, y una cadena de texto con el nombre del archivo donde se desea guardar la información.

La función itera sobre cada entrada del diccionario de ping y crea una nueva entrada en un diccionario resultado con la dirección IP como clave. La entrada incluye los datos de ping y los datos de escaneo de puertos correspondientes a la dirección IP.

Finalmente, se abre el archivo en modo escritura y se guarda el diccionario resultado en formato JSON con una indentación de 4 espacios.

**Clase Menu**

 La clase Menu define un constructor que se encarga de crear el menú y parsear los argumentos que se pasan al programa.

El constructor crea un objeto argparse.ArgumentParser y define los argumentos que se pueden pasar al programa. Se establecen grupos exclusivos entre el argumento red y el argumento ip, lo que significa que solo se puede especificar uno de los dos argumentos al invocar el programa.

El argumento red especifica la red que se desea escanear. El argumento ip especifica la dirección IP que se desea escanear. El argumento puerto especifica el puerto o puertos que se desean escanear en la dirección IP o red especificada. Si no se especifica ningún puerto, no se realiza ningún escaneo de puertos.

El argumento ping_null indica si se desea realizar un ping null. Si se especifica, no se realiza un ping previo para comprobar si la dirección IP está activa. El argumento verbose indica si se desea mostrar información adicional sobre el escaneo. El argumento threads indica el número de threads a utilizar para realizar el escaneo. El argumento banner indica si se desea mostrar el banner del servicio en el puerto escaneado. El argumento json indica si se desea guardar los resultados en un archivo JSON y especifica el nombre del


## Clase Network

La clase Network contiene métodos estáticos que permiten realizar diversas operaciones con una red.



* El método **check_ip **recibe una cadena que representa una dirección IP y comprueba si es una dirección IP válida utilizando una expresión regular.
* El método **get_ip **recibe una cadena que representa una red y devuelve la dirección IP de la red. Si la dirección IP no es válida, lanza una excepción de tipo ValueError.
* El método **check_subnet **recibe un número entero que representa una subred y comprueba si es una subred válida.
* El método **get_subnet **recibe una cadena que representa una red y devuelve la subred de la red. Si la subred no es válida, lanza una excepción de tipo ValueError.
* El método **check_network **recibe una cadena que representa una red y comprueba si la red es válida. Si la red es válida, devuelve True; de lo contrario, devuelve False.
* El método **get_total_hosts **recibe un número entero que representa una subred y calcula el número total de hosts que tiene la subred.
* El método **get_hosts **recibe una cadena que representa una red y devuelve una lista con todos los hosts de la red.
* El método **get_ports **recibe una cadena que representa un rango de puertos y devuelve una lista con los puertos especificados en la cadena. Si la cadena no es válida, lanza una excepción de tipo ValueError.
* El método **get_network **recibe una cadena que representa una red y devuelve una cadena que representa la red completa. Si la red no es válida, lanza una excepción de tipo ValueError.
* El método **__init__ **es el constructor de la clase. No tiene ninguna función específica en este caso.

**Clase Ping**

La clase Ping permite hacer un ping a una máquina y obtener información sobre la misma.



* El método **__init__ **es el constructor de la clase. Recibe una cadena que representa la dirección IP del objetivo y crea un paquete de ping utilizando la librería scapy.
* El método **is_alive **comprueba si la máquina está encendida enviando el paquete de ping y comprueba si se recibió una respuesta. Devuelve True si la máquina está encendida y False en caso contrario.
* El método **get_system **determina el sistema operativo de la máquina. Si la máquina está encendida, se utiliza el valor del campo ttl (time to live) de la respuesta para determinar el sistema operativo. Si la máquina está apagada, devuelve una cadena que indica que la máquina está apagada.
* El método **get_target **devuelve la dirección IP del objetivo.
* El método **get_summary **devuelve un diccionario con información resumida sobre la máquina. La información incluye la dirección IP, el sistema operativo y la dirección MAC de la máquina. Para obtener la dirección MAC, se utiliza el método getmacbyip de la librería scapy.layers.l2.

**Port Scanner**



*  La clase **PortScanner **permite escanear un puerto de una máquina y obtener información sobre el mismo.
* El método __init__ es el constructor de la clase. Recibe la dirección IP del host y el número del puerto que se desea escanear, y crea un paquete de escaneo de puerto utilizando la librería scapy.
* El método is_open comprueba si el puerto está abierto enviando el paquete de escaneo y comprueba si se recibió una respuesta. Si se recibió una respuesta y el flag 'SA' está presente en la respuesta, devuelve True; en caso contrario, devuelve False.
* El método **get_host **devuelve la dirección IP del host.
* El método **get_banner **devuelve una cadena con el nombre del servicio que utiliza el puerto. Si el puerto no está asociado con ningún servicio conocido, devuelve una cadena que indica esto.
* El método **get_summary **devuelve un diccionario con información resumida sobre el puerto. Si se especifica banner=True, la información incluirá el nombre del servicio que utiliza el puerto; de lo contrario, el diccionario indicará que la información del banner no está disponible.
