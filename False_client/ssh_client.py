import paramiko
from paramiko.transport import Transport

class CustomSSHClient(paramiko.SSHClient):
    def connect_with_custom_banner(
        self, hostname, port=22, username=None, password=None, banner_version="SSH-2.0-OpenSSH_7.3p1"
    ):
        """
        Conecta al servidor SSH con un banner modificado.
        """
        try:
            # Crear el objeto de transporte
            transport = Transport((hostname, port))

            # Modificar el banner que enviará el cliente
            transport.local_version = banner_version

            # Iniciar conexión
            transport.start_client()

            # Autenticar con usuario y contraseña
            transport.auth_password(username=username, password=password)
            print("[INFO] Autenticación completada exitosamente.")

            # Retornar el transporte para operaciones adicionales si es necesario
            return transport
        except Exception as e:
            print(f"[ERROR] Error durante la conexión: {e}")
        finally:
            transport.close()
            print("[INFO] Conexión cerrada.")

# Configuración
hostname = "172.17.0.6"  # Dirección IP del servidor
port = 22  # Puerto SSH
username = "prueba"  # Usuario real
password = "prueba"  # Contraseña real
custom_banner = "SSH-2.0-OpenSSH_?"  # Banner personalizado

# Crear cliente SSH y conectarse con parámetros personalizados
ssh_client = CustomSSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect_with_custom_banner(
    hostname=hostname,
    port=port,
    username=username,
    password=password,
    banner_version=custom_banner,
)
