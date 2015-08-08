import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6


class TelnetConn(object):

    def __init__(self, ip_addr):
        self.ip = ip_addr

    def login(self, remote_conn, username, password):
        '''
        Login to network device
        '''
        output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
        remote_conn.write(username + '\n')
        output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
        remote_conn.write(password + '\n')
        return output

    def send_command(self, remote_conn, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        remote_conn.write(cmd + '\n')
        time.sleep(1)
        return remote_conn.read_very_eager()

    def disable_paging(self, remote_conn, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(remote_conn, paging_cmd)

    def telnet_connect(self, ip_addr):
        '''
        Establish telnet connection
        '''
        try:
            return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except socket.timeout:
            sys.exit("Connection timed-out")


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    username = 'pyclass'
    password = getpass.getpass()

    telnet = TelnetConn('50.76.53.27') 
    telnet_conn = telnet.telnet_connect(telnet.ip)
    telnet.login(telnet_conn, username, password)
    telnet.disable_paging(telnet_conn)
    output = telnet.send_command(telnet_conn, 'show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    telnet_conn.close()

if __name__ == "__main__":
    main()
