
%Input odor of presentation of odors

function Write_Odor_File(FileID, Odor_Write)
fprintf(FileID, '\n\n%s\n\n', 'Order of Odors Presented');

formatSpec = '%s\t';

for row = 1:5
    
    fprintf(FileID, formatSpec, Odor_Write{row, :});
    fprintf(FileID, '%s\n', ' ');
    
end
end