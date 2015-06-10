function Run_Assay(dev_1, dev_2, Run_Odor_State, Run_Air_State, FileID)
for i = 1:5     %Subtrial Index
    
    for j = 1:10        %Presentation Index         %Cell_Trial = {Run_Odor_State(i,j), Run_Air_State(i,j), time, 
        
        dev_1.recallState(Run_Odor_State(i,j));
        
        dev_1.recallState(Run_Air_State(i,j));
        
        dev_2.setMfcFlows('[40 4 4]');
        
        time_1 = datestr(now);
        
        time_1 = time_1(13:20);
        
        pause(2);
        
        time_2 = datestr(now);
        
        time_2 = time_2(13:20);
        
        Cell_Trial = [int2str(i), '   ', int2str(j), '   ', int2str(Run_Odor_State(i,j)), '   ', int2str(Run_Air_State(i,j)), '   ', time_1, '   ', time_2];
        
%       formatSpec = '%i %i %i %i \n\n';
        
        fwrite(FileID, Cell_Trial);
    end
end
end