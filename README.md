# OpenSSH Docker Lab

## Comandos utilizados

### Crear imágenes de Docker

Ejecuta los siguientes comandos para construir las imágenes Docker necesarias:

```bash
docker build -t c1_image ./C1
docker build -t c2_image ./C2
docker build -t c3_image ./C3
docker build -t c4_image ./C4
docker build -t ssh-client-false ./False_client
```

### Crear contenedores
Crea los contenedores a partir de las imágenes generadas:

```bash
docker run -it --name c1 c1_image
docker run -it --name c2 c2_image
docker run -it --name c3 c3_image
docker run -it --name c4 c4_image
docker run -it --name s1 -p 2224:22 c4_image
docker run --rm --network bridge ssh-client-false
```

### Verificar la versión de Ubuntu
Para confirmar la versión del sistema operativo dentro de un contenedor, usa el siguiente comando:

```bash
cat /etc/os-release
```

### Configurar credenciales en el servidor SSH
Dentro del contenedor del servidor (s1), configura las credenciales de usuario y reinicia el servicio SSH:

```bash
useradd -m prueba && echo "prueba:prueba" | chpasswd
mkdir -p /var/run/sshd
service ssh restart
```

### Capturar tráfico de red
Para realizar capturas del tráfico generado entre los clientes y el servidor, utiliza los siguientes comandos:

```bash
sudo tcpdump -i docker0 -w c1_s1.pcap
sudo tcpdump -i docker0 -w c2_s1.pcap
sudo tcpdump -i docker0 -w c3_s1.pcap
sudo tcpdump -i docker0 -w c4_s1.pcap
```
### Conectar por SSH
Conéctate al servidor desde los clientes utilizando SSH:

```bash
ssh prueba@172.17.0.6
```

### Análisis
Las capturas de tráfico (.pcap) pueden analizarse utilizando herramientas como Wireshark para examinar los detalles del handshake TCP, el intercambio de claves, y el tráfico cifrado.