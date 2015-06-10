% Read images from the directory and get fly centroid coordinates
function Read_Im()

Directory = datestr(now, 'yyyymmdd/HH:MM:SS');

File_Path = ['~/odor_rig_data', Directory];

Images = cell(1, 1800);


for i = 1:1800
    
    Img_Name = [Directory, i];
    
    Images{i} = Img_Name;
    
end


cd(File_Path);

Output_File_Name = [Directory, '.txt'];

FileID = fopen(Output_File_Name, 'w');

Background = imread('Background', 'png');

Background = im2bw(Background, 0.3);

for i = 1:1800
    
    Img = Imread(Images{i});
    
    Img = im2bw(Img, 0.3);
    
    Img = Img - Background;
    
    % Img = 1 - Img
    
    CC = bwconncomp(Img);
    
    Stats_Area = regionprops(CC, 'Area');
    
    IDX = find([Stats_Area.Area] > 25 & [Stats_Area.Area] < 75);
    
    Img_Mod_CC = ismember(labelmatrix(CC), IDX);
    
    Stats_Centroid = regionprops(Img_Mod_CC, 'Centroid');
    
    Centroid = [Stats_Centroid.Centroid];
    
    formatSpec = '20%i\n';
    
    fprintf(FileID, formatSpec, Centroid);
    
    %Write Centroid to Input File as Appropriate
    
end
    
    
    
    
    


