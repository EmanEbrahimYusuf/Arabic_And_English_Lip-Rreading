import tensorflow as tf
from typing import List
import cv2
import os 

vocab = [x for x in "abcdefghijklmnopqrstuvwxyz'?!123456789 "]
char_to_num = tf.keras.layers.StringLookup(vocabulary=vocab, oov_token="")

num_to_char = tf.keras.layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), oov_token="", invert=True
)

def load_video(path:str) -> List[float]: 
    #print(path)
    cap = cv2.VideoCapture(path)
    frames = []
    for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))): 
        ret, frame = cap.read()
        frame = tf.image.rgb_to_grayscale(frame)
        frames.append(frame[190:236,80:220,:])
    cap.release()
    
    mean = tf.math.reduce_mean(frames)
    std = tf.math.reduce_std(tf.cast(frames, tf.float32))
    return tf.cast((frames - mean), tf.float32) / std
    
def load_alignments(path:str) -> List[str]: 
    #print(path)
    with open(path, 'r') as f: 
        lines = f.readlines() 
    tokens = []
    print(lines)
    for line in lines:
        line = line.split()
        if line[2] != 'sil': 
            tokens = [*tokens,' ',line[2]]
    print(tokens)
    char_nums = char_to_num(tf.strings.unicode_split(tokens, input_encoding='UTF-8')).to_tensor()
    result = char_nums[1:]
    return result

def load_data(path: str): 
    path = bytes.decode(path.numpy())
    file_name = path.split('\\')[-1].split('.')[0]
  
    file_name = path.split('\\')[-1].split('.')[0]
    video_path = os.path.join(r'C:\Users\Eman\Desktop\GP_LipReading\data\Test_Eng\1','videos',f'{file_name}.mpg')
    print(video_path)
    alignment_path = os.path.join(r'C:\Users\Eman\Desktop\GP_LipReading\data\Test_Eng\1','alignments',f'{file_name}.align')
    print(alignment_path)
    frames = load_video(video_path) 
    alignments = load_alignments(alignment_path)
    print(alignments)
    
    return frames, alignments


def load_data2(path: str): 

    path = bytes.decode(path.numpy())

    frames = load_video(path) 
    
    
    return frames