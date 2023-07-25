import os


# # list_vid=os.listdir('Mema Toaany')
# # for i , name in enumerate(list_vid):
# #     os.rename('Mema Toaany/'+name, 'Mema Toaany/'+'Mema Toaany'+str(i)+'.avi')

classes=os.listdir(r"Datasets\Lip_reading_dataset_for_arabic\Masa_Alkhayr\vids")
print(classes)

for i , name in enumerate(classes):
    print(name)
    # list_vid=os.listdir(os.path.join(r"Datasets\Lip_reading_dataset_for_arabic\Masa_Alkhayr\vids", cls))
    # print(list_vid)
    # for i , name in enumerate(list_vid):

    os.rename(f"Datasets\Lip_reading_dataset_for_arabic\Masa_Alkhayr\\vids/"+name, f"Datasets\Lip_reading_dataset_for_arabic\Masa_Alkhayr\\vids/Masa_Alkhayr"+str(i)+'.avi')

# import random
# print(random.randint(0,60))