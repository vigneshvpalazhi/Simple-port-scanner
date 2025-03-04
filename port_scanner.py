from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    port_upto = input(
        "Enter the port you wanna scan upto:('full' for full port scan): ")

    if port_upto == "full":
        for i in range(0, 65536):
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)

            conn = s.connect_ex((t_IP, i))
            if conn == 0:
                try:
                    service = getservbyport(i, 'tcp')
                    print(f'Port {i}: OPEN ({service})')
                except OSError:
                    print(f'Port {i}: OPEN (unknown service)')
        s.close()
    else:
        max_port = int(port_upto) + 1

        for i in range(0, int(max_port)):
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(1)

            conn = s.connect_ex((t_IP, i))
            if conn == 0:
                try:
                    service = getservbyport(i, 'tcp')
                    print(f'Port {i}: OPEN ({service})')
                except OSError:
                    print(f'Port {i}: OPEN (unknown service)')
        s.close()


print('Time taken:', time.time() - startTime)
