import paramiko
from config import REMOTE_HOST, REMOTE_USER, REMOTE_PASSWORD


def ssh_connect(hostname, username, password, command):
    ssh_client = paramiko.sshCliente()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.cliente.exec_command(command)

        # Read the output of the command
        output = stdout.read().decode()

        # Close te SSH connection
        ssh_client.close()

        return output
    
    except paramiko.AuthenticationException as e:
        return f"Authentication failed: {str(e)}"
    except paramiko.SSHException as e:
        return f"SSH Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"