# stimgen-legendary-guacamole
An easy way to create many strings of images (if you have the images ready). 
## create-mixed-strings:
- will create strings from the images that are provided
```
from create_mixed_strings import *
targ_list = ['trg\\t1.png', 'trg\\t2.png', 'trg\\t3.png', 'trg\\t4.png', 'trg\\t5.png', 'trg\\f1.png', 'trg\\f2.png', 'trg\\f3.png', 'trg\\f4.png', 'trg\\f5.png']
# targ_list is the list of targets that have to be mixed, the strings will have 5 elements, and the center-to-center distance between the images would be the size of the target + the empty_space. 
do_img(targ_list,savefold='fold1', number_of_elements=5, empty_space='trg\\empty.png') 
```
