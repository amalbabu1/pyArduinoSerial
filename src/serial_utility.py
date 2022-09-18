
import serial.tools.list_ports



def get_data():
    with serial.Serial() as ser:
        try:
            selected_port = get_current_serial_port()
            ser.baudrate = 9600
            ser.port = selected_port[1]
            ser.open()
            ser.flushInput
            while ser.is_open:
                data = ser.readline()
                yield data
        except:
            raise Exception("Port ejected")
           

def get_current_serial_port():    
    ports_identified = serial.tools.list_ports.comports()
    port_list = [(index, port.device) for index, port in enumerate(ports_identified)]
    # print(port_list)
    
    if port_list:
        if len(port_list) == 1:
            selected_port = port_list[0]
        else:
            print("select the port")
            for port in port_list:
                print(f"{port[0]} -> {port[1]}")
            selected = int(input())
            selected_port = port_list[selected]
        print(f"port {selected_port[1]} is selected\n") 
        return selected_port
    else:
        raise Exception("No ports opened")