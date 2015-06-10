%Create instances of class ModularDevice for the power switch controller
%and the mass flow controller using the port serial numbers that these
%modular devices are connected to

% We want dev_1 to be an instance of the power switch controller and
% dev_2 to be an instance of the mass flow controller

function [dev_1, dev_2] = Port_Assign(SerialPort_1, SerialPort_2)

dev_1 = ModularDevice(SerialPort_1);

dev_2 = ModularDevice(SerialPort_2);

dev_1.open();

dev_2.open();

Info_1 = dev_1.getDeviceInfo();

Info_2 = dev_2.getDeviceInfo();


if strcmp(Info_1.name(),'power_switch_controller') == 0
    
    Dummy = SerialPort_1;
    
    SerialPort_1 = SerialPort_2;
    
    SerialPort_2 = Dummy;
    
    dev_1 = ModularDevice(SerialPort_1);
    
    dev_2 = ModularDevice(SerialPort_2);
    
    dev_1.open();
    
    dev_2.open();
end

dev_1.setAllChannelsOff();

dev_2.setMfcFlows('[0,0,0]');

end