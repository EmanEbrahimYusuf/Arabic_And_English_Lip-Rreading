import tensorflow as tf
from typing import List
import cv2
import os 
vocab = ['{}'.format(x) for x in " اأبتثجحخدذرزسشصضطظعغفقكلمنهـويةءىئ"]
char_to_num = tf.keras.layers.StringLookup(vocabulary=vocab, oov_token="")
num_to_char = tf.keras.layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(), oov_token="", invert=True
)

def load_video(path:str) -> List[float]:

    cap = cv2.VideoCapture(path)
    frames = []
    for _ in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))): 
        ret, frame = cap.read()
        frame = tf.image.rgb_to_grayscale(frame)
        frame=frame/255
        frames.append(frame[:150,70:230,:])
    cap.release()
    return  tf.cast((frames), tf.float32) 


def load_alignments(path:str) -> List[str]:
    with open(path, 'r',encoding='utf-8') as f: 
        line = f.readline()
    tokens = []
    line = line.split()
    for l in line:
        tokens = [*tokens,' ',l]
    res = ''.join(tokens)
    #z = reverse_string(res)
    char_nums = char_to_num(tf.strings.unicode_split(tokens, input_encoding='UTF-8')).to_tensor()
    result = char_nums[1:]
    return result

def load_data(path: str): 

    path = bytes.decode(path.numpy())
    folder_name=path.split('\\')[-3]
    print(folder_name)
    file_name = path.split('\\')[-1].split('.')[0]
    print(file_name)
    video_path = os.path.join(r'C:\Users\Eman\Desktop\GP_LipReading\data\Arabic_Train_Test\test',folder_name,'vids',f'{file_name}.avi')
    alignment_path = os.path.join(r'C:\Users\Eman\Desktop\GP_LipReading\data\Arabic_Train_Test\test',folder_name,'align',f'{file_name}.txt')
    frames = load_video(video_path) 
    
    alignments = load_alignments(alignment_path)
    return frames, alignments

def load_data2(path: str): 

    path = bytes.decode(path.numpy())

    frames = load_video(path) 
    
    
    return frames

