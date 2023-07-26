# Arabic_And_English_Lip-Rreading
## Deep learning project for predict text from lip movement
* This system captures videos of people speaking in Arabic or English, and utilizes lip movement to generate a prediction of the corresponding text.
### video preprocessing
* Obtain a fixed number of frames for all videos.
* Convert the video to individual frames.
* Detect the face in each frame.
* Detect the mouth region in each frame.
* Crop the region of interest containing the mouth.
* Convert the processed frames back into a video.
*  get fixed numper of frames for all videos
## models 
The models for Arabic and English lip-reading have been built using different architectures. The models are trained using the Connectionist Temporal Classification (CTC) decoder to generate predicted text from the lip movement data. The predicted text is then compared with the actual text to calculate the accuracy of the model.
##Accuracy
The accuracy achieved by the Arabic model is 80.1%, while the English model has an accuracy of 97%. 
##Data
It should be noted that the Arabic data used to train the model is private data owned by our team, while the English data is sourced from the Grid dataset.

 
