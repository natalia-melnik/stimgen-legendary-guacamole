import numpy as np
import matplotlib.pyplot as plt
import itertools
import scipy.misc
import os


def concat_images(imga, imgb):
    """
    Combines two color image ndarrays side-by-side.
    """
    ha,wa = imga.shape[:2]
    hb,wb = imgb.shape[:2]
    max_height = np.max([ha, hb])
    total_width = wa+wb
    new_img = np.zeros(shape=(max_height, total_width, 3))
    new_img[:ha,:wa]=imga
    new_img[:hb,wa:wa+wb]=imgb
    return new_img

def concat_n_images(image_path_list):
    """
    Combines N color images from a list of image paths.
    """
    output = None
    for i, img_path in enumerate(image_path_list):
        img = plt.imread(img_path)[:,:,:3]
        if i==0:
            output = img
        else:
            output = concat_images(output, img)
    return output

def create_dir(dir):
    try:
        os.mkdir(dir)
    except OSError:
        print ("Creation of the directory %s failed" % dir)
    else:
        print ("Successfully created the directory %s " % dir)


def do_img(targ_list,savefold='fold1', number_of_elements=5, empty_space='trg\\empty.png'):
    create_dir(savefold)
    list1 = list(set(list(itertools.permutations(targ_list,
                                                 number_of_elements))))  
    print len(list1)

    for img1 in list1:
        #print img1
        nlst = []
        for emp in img1:
            nlst.append(emp)
            nlst.append(empty_space)  # add the empty (this will be the center-to-center distance)

        nlst = nlst[:-1]  # removes the last empty...
        #print nlst
        output = concat_n_images(nlst)
        name = '_'.join([i.split('\\')[1].split('.')[0] for i in img1])

        scipy.misc.toimage(output).save(savefold+'/' + name + '.png')
        
