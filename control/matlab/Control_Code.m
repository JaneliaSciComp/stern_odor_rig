clear;

clc;

SerialPort_1 = '/dev/tty.usbmodem1411'; % Find the ports that the modular devices are plugged into

SerialPort_2 = '/dev/tty.usbmodem1421'; %On a Mac and Linux, this is a ls dev command in the terminal. Find the
                                        %port number listed for /dev/tty.usbmodem or /dev/ttyUSB or /dev/ttyACM
                                        %respectively

[dev_1, dev_2] = Port_Assign(SerialPort_1, SerialPort_2);

Odors = Odorants();
 
FileID = Create_File(Odors);
 
[Pres, Side, Odor_Write] = Odor_Presentation(Odors);

Write_Odor_File(FileID, Odor_Write);
                          
[Run_Odor_State, Run_Air_State] = State_Assign(Pres, Side);
 
Run_Assay(dev_1, dev_2, Run_Odor_State, Run_Air_State, FileID);
 
fclose(FileID);

        
        
 








    
