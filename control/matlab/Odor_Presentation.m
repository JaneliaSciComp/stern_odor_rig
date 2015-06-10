
%Randomise and generate the order of odor presentation for this assay

%Refer to Rig Schematic for experiment design

function [Pres, Side, Odor_Write] = Odor_Presentation(Odors)
Pres = zeros(5,5);

Pres(1,:) = randperm(5);

for i = 2:5
    
    j = 1;
    
    Flag = randperm(5);
    
    while(j <= i-1)
        
        if Flag(1) == Pres(j,1)
            
            Flag = randperm(5);
            
            j = 1;
        
        else
            
            j = j+1;
            
        end
       
    end
    
    Pres(i,:) = Flag;
end
            
Side = round(rand(5,5));
Odor_Write = Odors(Pres);
end
