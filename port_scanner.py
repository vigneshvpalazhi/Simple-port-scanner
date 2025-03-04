from socket import *
import time

startTime = time.time()

if __name__ == '__main__':
    while True:  # Loop to keep asking for valid input
        target = input('Enter the host to be scanned: ')
        try:
            t_IP = gethostbyname(target)
            print('Starting scan on host: ', t_IP)
            break  # Exit loop if hostname resolves successfully
        except gaierror as e:
            if target.lower() == 'full':
                print("Error: 'full' is not a valid hostname. Please enter a valid host (e.g., 'example.com' or an IP address).")
            else:
                print(f"Error: Could not resolve host '{target}'. {str(e)}")
                print("Please check the hostname or your network connection and try again.")
            continue  # Ask for input again

    port_upto = input(
        "Enter the port you wanna scan upto:('full' for full port scan): ")

    if port_upto.lower() == "full":
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
        try:
            max_port = int(port_upto) + 1
            for i in range(0, max_port):
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
        except ValueError:
            print("Error: Please enter a valid number for the port range or 'full' for a full scan.")

    print('Time taken:', time.time() - startTime)
