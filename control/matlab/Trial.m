% function Run_Assay(dev_1, dev_2, Run_Odor_State, Run_Air_State, FileID)

fid = fopen('Trial.txt', 'w');

for i = 1:5     
   
    for j = 1:10        
        
        time_1 = fix(clock);
        
        time_1 = num2str(time_1(4:6));
        
        pause(2);
        
        time_2 = fix(clock);
        
        time_2 = num2str(time_2(4:6));
        
        Cell_Trial = [i, j, i^2, j^2, time_1, time_2];
        
        fwrite(fid, Cell_Trial);
        
    end
end

fclose(fid);