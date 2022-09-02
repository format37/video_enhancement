import cv2
import os
import json
import sys


def main():

    # Parameters
    with open('service/images2video.json', 'r') as f:
        config = json.load(f)
    
    images_path = config['images_path']
    # if path is not exist, warn and exit
    if not os.path.exists(images_path):
        print('Images path is not exist!')
        exit()

    ascending_sorting_order = int(config['ascending_sorting_order'])
    # scaling_size = int(config['scaling_size'])

    # read all files in path    
    filenames = []
    for fname in os.listdir(images_path):
        filenames.append(os.path.join(images_path, fname))
    if ascending_sorting_order:
        # sort filenames by name ascending
        filenames = sorted(filenames)
    else:
        # sort filenames by name descending
        filenames = sorted(filenames, key=lambda x: x.split('/')[-1], reverse=True)

    # read images
    images = []
    for fname in filenames:
        # read image
        try:
            img = cv2.imread(fname)
            # compare sizes
            """if scaling_size != img.shape[0]:
                # resize image
                img = cv2.resize(img, (scaling_size, scaling_size))
                # resize image
                img = cv2.resize(img, (scaling_size, scaling_size))"""
            # add image to list
            images.append(img)
        except Exception as e:
            print('Error while reading: ', fname, str(e))

    fps = int(config['fps'])

    # create a video
    height, width, layers = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(config['output_file_name'], fourcc, fps, (width, height))
    for image in images:
        video.write(image)
    cv2.destroyAllWindows()
    video.release()


if __name__ == '__main__':
    main()
