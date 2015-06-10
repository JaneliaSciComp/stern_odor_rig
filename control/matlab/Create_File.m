
%Write all the relevant data from this assay into a file, starting with the
%odors used

function FileID = Create_File(Odors)

Name_Of_File = datestr(now, 'dd-mmm-yy HH:MM:SS');

File_Path = '/Users/shruthi/Documents/Olfactory Rig/'; % ~/odor_rig_data

File_Path_New = [File_Path, Name_Of_File];

FileID = fopen(File_Path_New, 'w');

for i = 1:6
    
    fprintf(FileID, '%s\t', 'Chemical Compound');
    
    fprintf(FileID, '%i\t\t', i);
    
    fprintf(FileID, '%s\n', Odors{i});
end
end