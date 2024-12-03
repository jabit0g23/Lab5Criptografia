# Dockerfile para C4/S1
FROM ubuntu:22.10

# Actualización de paquetes e instalación de OpenSSH
RUN apt-get update && apt-get install -y openssh-client openssh-server && \
    apt-get clean

# Crear usuario de prueba
RUN useradd -m prueba && echo "prueba:prueba" | chpasswd

# Crear directorio para configuraciones de SSH
RUN mkdir /var/run/sshd

# Permitir login root con contraseña
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Exponer el puerto SSH
EXPOSE 22

# Comando por defecto
CMD ["/usr/sbin/sshd", "-D"]
