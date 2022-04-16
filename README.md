# IDS705FinalProject

This is the repo for the Final Project of IDS 705 from Team 7.

In order to run and replicate our project, run IDS705FinalNotebook.ipynb. We recommend using an environment with GPU, either using a local GPU or GoogleColab/AmazonCloud9.

To install all dependencies, run pip install -r requirements.txt. 

Prior to running the code please add your own Kaggle.json file to the same folder as the ipynb file. The kaggle.json file can be obtained from the kaggle website.
Refer to https://www.kaggle.com/docs/api under the Authentication section for more info on how to get the kaggle.json file.

## Road Signs Classification for Extreme Driving Conditions

- In this project, we aim to develop a model that can be deployed in a camera to identify and warn drivers of upcoming relevant signage in normal conditions as well as adverse weather conditions.
- We propose a Convolutional Neural Network(CNN) model which was built off the LeNet architecture to accurately classify signs and compare the performances across multiple datasets which include simulated adverse weather conditions (we also tried pre-trained models including Resnet18, Resnet50,and Resnet101). 
- The model utilizing a training dataset that contains only dark images yields the highest accuracy for normal and adverse conditions. Therefore using this model we can accurately identify and warn visually impaired drivers of road signs up ahead and prevent potential accidents.

### Data

**GTSRB - German Traffic Sign Recognition Benchmark Dataset**
(Link to the dataset: https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)

The German Traffic Sign Benchmark is a multi-class, single-image classification challenge held at the International Joint Conference on Neural Networks (IJCNN) 2011. The dataset consists of more than 50,000 pictures of traffic signs in 43 classes. It is considered a large, lifelike database.

**Road Sign Detection Dataset**
(Link to the dataset: https://www.kaggle.com/datasets/andrewmvd/road-sign-detection)

This dataset contains 877 images of 4 distinct classes for the objective of road sign detection.
Bounding box annotations are provided in the PASCAL VOC format
The classes are:
Trafic Light;
Stop;
Speedlimit;
Crosswalk.

The preprocessing code can be found in 10_code/Low Visibility Road Conditions Simulations.ipynb

### Experiment

we generated datasets that are simulations of rainy weather, foggy weather, dark environment, and bright environment for our experiments as they are common challenging driving conditions for individuals with impaired vision. The image distortions are simulated by blurring the pixels, altering brightness and situations, and adding randomized noises to the images.

<img width="604" alt="Screen Shot 2022-04-15 at 7 52 54 PM" src="https://user-images.githubusercontent.com/89416055/163653371-29d519d7-e25f-4a9a-8443-793659c32a9a.png">

We designed a 6-components experimental process that allows us to compare how a model trained by different images would respond to adverse driving conditions. For each component of the experiment, one or multiple types of distortion effect(s) are applied to the original training dataset. Component 1 contains the original training images and serves as the baseline for the experiment. Models trained in other components are compared to the baseline model. Component 2 comprises images with mixed distortion effects -- 20% original images, 20% rainy images, 20% foggy images, 20% dark images, and 20% bright images. Components 3 to 6 comprise images with only one distortion effect, where rainy, foggy, dark, and bright effects were applied separately to the original training images. Then, all training images are normalized prior to training. We then trained a LeNet model for each component and tested them on six testing datasets -- original, rain, fog, dark, bright, and mixed (same effects breakdown as the mixed training dataset). Each experiment component would output six AUC scores corresponding to each testing dataset, and the model performance is evaluated by comparing average AUC scores across different components.

<img width="778" alt="Screen Shot 2022-04-15 at 7 54 39 PM" src="https://user-images.githubusercontent.com/89416055/163653449-3fb17074-fd76-419c-8e54-b37418661e84.png">

### Conclusion

After extensive model testing in different low visibility scenarios, we found that LeNet (batch size 200, epochs 20, learning rate 0.001) is the best performing model and is trained on the dark dataset which consistently classifies road signs with an average AUC score of 0.758. Therefore, the takeaway of our project is that to maximize the performance of street sign classification across all conditions it is most beneficial to train on a nighttime dataset.

#### limitations and suggestions for references

The dataset we used is imbalanced as 55% of the dataset consists of speed limit signs and only 0.5% of the dataset consist of traffic light images. As a result, our model performed poorly in classifying under-representative classes. Moreover, our simulated images may not accurately reflect the real-world circumstances perceived through the camera and only cover some of the adverse driving conditions that drivers can possibly encounter. How close the simulated images can imitate the real world will significantly affect the performance of our neural network if applied to real settings.

For future work, we recommend collecting more images of stop signs, crosswalk signs, and traffic lights. We suggest training the model with a more balanced dataset, so that the classifier could recognize underrepresented classes more accurately. If possible, repeat our experimental procedure on real-life images instead of simulated images to investigate what kinds of training data would be most helpful in terms of boosting classifier accuracy on low visibility road sign images. 

Link to demo video: https://www.youtube.com/watch?v=aE_gAPqHsCs
