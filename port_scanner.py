import socket
import threading

# Function to scan a range of ports on a target IP
def port_scan(target_ip, start_port, end_port, open_ports, lock):
    # Loop through each port in the given range
    for port in range(start_port, end_port + 1):
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set timeout so scan doesn't hang on closed/filtered ports
            s.settimeout(0.5)
            
            # Attempt to connect to the target IP and port
            result = s.connect_ex((target_ip, port))
            # If result is 0, the port is open
            if result == 0:
                # Use lock to safely update shared list across threads
                with lock:
                    open_ports.append(port)
            # Close the socket after each attempt
            s.close()
        except socket.error:
            # Ignore socket errors and continue scanning
            pass

# Function to divide the port range among multiple threads
def divide_port_range(start_port, end_port, num_of_threads):
    # Total number of ports to scan
    total_ports = end_port - start_port + 1
    # Number of ports each thread should handle
    ports_per_thread = total_ports // num_of_threads
    # Remaining ports after equal division
    remainder = total_ports % num_of_threads 
    
    ranges = []
    current_start = start_port
    # Create port ranges for each thread
    for i in range(num_of_threads):
        # Calculate end port for this thread
        current_end = current_start + ports_per_thread - 1
        # Distribute leftover ports one by one
        if remainder > 0:
            current_end += 1
            remainder -= 1
        # Append the range as a tuple
        ranges.append((current_start, current_end))
        # Move to the next starting port
        current_start = current_end + 1
        
    return ranges
    

def main():
    # Take user input for target IP and port range
    target_ip = input("Enter the target IP address: ").strip()
    start_port = int(input("Enter the start port: ").strip())
    end_port = int(input("Enter the end port: ").strip())
    
    # Number of threads to use for scanning
    num_of_threads = 10
    # Lock to synchronize access to shared resources
    lock = threading.Lock()
    # List to store open ports
    open_ports = []
    # List to keep track of thread objects
    threads = []
    
    # Divide port range among threads
    port_ranges = divide_port_range(start_port, end_port, num_of_threads)
    # threading.Thread(target=FUNCTION_NAME, args=(arg1, arg2, ...))
    for start_port,end_port in port_ranges:
        # Create a thread for each port range
        thread = threading.Thread(target = port_scan, args = (target_ip, start_port, end_port, open_ports, lock) )
        threads.append(thread)
        # Start the thread
        thread.start()
    
    # Wait for all threads to finish execution
    for thread in threads:
        thread.join()
    
    # Sort the list of open ports
    open_ports.sort()
    print("\nOpen Ports are: ")
    # Display the open ports
    print(open_ports)      
    

# Entry point of the program
if __name__ == "__main__":
    main()