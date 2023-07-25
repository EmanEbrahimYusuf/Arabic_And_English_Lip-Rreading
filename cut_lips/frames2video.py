import cv2
import numpy as np
import glob
from vedio2frames import video2frames_func
import os


# classes=os.listdir('data')
# print(classes)
# for cls in classes:
#     list_vid=os.listdir(os.path.join('data', cls))
#     try:
#         os.mkdir(f'data2/{cls}')
#     except:
#         continue
#     for i , name in enumerate(list_vid):
#         try:
#             print(name)
#             print(f'data/{cls}\\'+name)
#             img_array=video2frames_func(f'data/{cls}\\'+name)

            
#             out = cv2.VideoWriter(f'data2/{cls}/'+name,cv2.VideoWriter_fourcc(*'DIVX'), 30, (300,200))
#             for i in range(len(img_array)):
#                 out.write(img_array[i])
#             out.release()
#             print('------------------------------------------------')
#         except:
#             continue


# list_vid=os.listdir('Mema Toaany')
# for i , name in enumerate(list_vid):

#     print(name)
#     img_array=video2frames_func('Mema Toaany\\'+name)
#     out = cv2.VideoWriter('Mema Toaany2/'+name,cv2.VideoWriter_fourcc(*'DIVX'), 30, (300,200))
#     for i in range(len(img_array)):
#         out.write(img_array[i])
#     out.release()
# print(f'data/{cls}\\'+name)
# img_array=video2frames_func(r'cut_lips\اريد الحساب.avi')
# out = cv2.VideoWriter(r'cut_lips\test preocess\الحساب.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, (300,200))
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
import os
import cv2

def process_videos(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all video files in the input directory
    for filename in os.listdir(input_dir):
        if not filename.endswith('.avi'):
            continue
        
        # Extract frames from input video
        input_path = os.path.join(input_dir, filename)
        img_array = video2frames_func(input_path)
        print(input_path)
        # Create output video file
        output_path = os.path.join(output_dir, filename)
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), 30, (300,200))

        # Write frames to output video file
        for i in range(len(img_array)):
            out.write(img_array[i])

        # Release output video file
        out.release()
input_dir = 'unseen'
output_dir = 'unseen_data'
process_videos(input_dir, output_dir)