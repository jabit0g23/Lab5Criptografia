# Utiliza la imagen base de Ubuntu
FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Actualiza los paquetes e instala OpenSSH Server
RUN apt-get update && apt-get install -y openssh-server && mkdir /var/run/sshd

# Configura una contraseña para el usuario root
RUN echo 'root:password' | chpasswd

# Permite el inicio de sesión root por SSH
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Evita que el contenedor termine cerrándose
CMD ["/usr/sbin/sshd", "-D"]

# Expone el puerto 22 para SSH
EXPOSE 22
