import sys, os
from PIL import Image
from optparse import OptionParser



def walk_dir(dir):
    image_list = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if (ext.lower() == 'jpg' or ext.lower() == 'png' or ext.lower() == 'JPG'):
                path = root + os.sep + name
                image_list.append(path)
    return image_list



def resize_save(im, width, path):
    image_name = im.filename.split(os.sep)[-1]
    save_name = path + os.sep + image_name
    size = [224, 224] 
    new_im = im.resize(size)
    print ('save_name: ', save_name)
    new_im.save(save_name)



def auto_resize(im, width):
    size = im.size
    height = int(float(width) / size[0] * size[1])
    return (int(width), height)

# look for subfolder
def dir_fold(image_path):
    dirs_list = []
    for root, dirs, files in os.walk(image_path):
        for  dirname in dirs:
            dirs_list = dirs
    return dirs_list

if __name__ == '__main__':
    prep_path = 'training_data'
    image_width = 224
    input_path = 'input_data'
    dirs = dir_fold(prep_path)
    print("dirs: \n", dirs)
    i = 0
    while i < 103:
     image_path = prep_path + os.sep + dirs[i]
     print(dirs[i])
     try:
        width = image_width
        save_path = input_path + os.sep + dirs[i]
        i += 1
        if (not os.path.exists(save_path)):
            os.mkdir(save_path)
        image_list = walk_dir(image_path)
        for path in image_list:
            im = Image.open(path)
            resize_save(im, width, save_path)
     except Exception as e:
        print('error', e)
