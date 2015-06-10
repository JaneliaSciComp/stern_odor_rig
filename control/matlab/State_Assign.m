

%Run_Air_State and Run_Odor_State contain, respectively, the states that
%need to be activated to present air and odor to the chamber in the order
%and side specified in Pres and Side


% Run_Odor_State(i,j) and Run_Air_State(i,j) have to be activated at the
% same time; 'i' is the subtrial number and 'j' indexes the 10 different
% presentations within a subtrial

function [Run_Odor_State, Run_Air_State] = State_Assign(Pres, Side)

Run_Odor_State = zeros(5,10); %States are single numbers that map onto channels

Run_Air_State = zeros(5,10); 

% 'i'th odor - 0,i,i+7 (left) 0,i,i+15 (right) or state 2*i - 1 (left) and
% 2*i (right)


 for row = 1:5
     
     for column = 1:2:10
         
         if Side(row, (column+1)/2) == 0    %Left
             
             Run_Odor_State(row, column) = 2*Pres(row, (column+1)/2) - 1; %Odour on the left means air on the right
             
             Run_Air_State(row, column) = 2 * 6;
        
         else                               %Right
             
              Run_Odor_State(row, column) = 2*Pres(row, (column+1)/2); %Odour on the right means air on the left
              
              Run_Air_State(row, column) = 2 * 6 - 1;
              
         end
         
     end
     
     for column = 2:2:10
         
         Run_Odor_State(row, column) = 2 * 6;
         
         Run_Air_State(row, column) = 2 * 6 - 1;
         
     end
     
 end
end