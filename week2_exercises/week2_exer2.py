import sys
import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 5
user = 'pyclass'
passwd = '88newclass'


def telnet_login(conn, user, passwd):

    conn.read_until('sername:', TELNET_TIMEOUT)
    conn.write(user + '\n')
    conn.read_until('ssword:', TELNET_TIMEOUT)
    conn.write(passwd + '\n')

def telnet_connection():

    ip_addr = '50.76.53.27'
    try:
        conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        return conn
    except Exception:
        sys.exit('Could not connect')

def send_command(conn, command):

    conn.write(command + '\n')
    time.sleep(1)
    output = conn.read_very_eager()
    return output


def main():

    conn = telnet_connection()
    telnet_login(conn, user, passwd)
    time.sleep(1)
    output = send_command(conn, 'show ip int brief')
    print output


if __name__ == "__main__":
    main()
