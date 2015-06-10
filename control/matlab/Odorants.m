
%Input the chemicals to be used in the assay based on which (th) beaker
%they have been placed in

function Odors = Odorants()

display('Place Water Containing Beaker in Position 6');

Odor_1 = input('Enter Chemical in Beaker 1: ', 's');

Odor_2 = input('Enter Chemical in Beaker 2: ', 's');

Odor_3 = input('Enter Chemical in Beaker 3: ', 's');

Odor_4 = input('Enter Chemical in Beaker 4: ', 's');

Odor_5 = input('Enter Chemical in Beaker 5: ', 's');

%Odor_6 = input('Enter Chemical in Beaker 6', 's');  %This is water

Odor_6 = 'Water';

Odors = {Odor_1; Odor_2; Odor_3; Odor_4; Odor_5; Odor_6};

end
