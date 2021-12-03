# Deep learning for Text Recognition in Illicit Advertisements
Walter Tyrna

## Abstract
The goal of this project is to a deep learning model to identify characters (letters & numbers) in real life images found online - particularly advertisements for [chemicals used in synthetic drug production](https://whmonad.en.made-in-china.com/product/EFBTbnGPggky/China-Safety-Delivery-CAS-288573-56-8-79099-07-3-443998-65-0-in-Stock.html). Illicit actors that sell these chemicals use text embedded in images to avoid some online regulations and web scrapes. This model will help analysts following illicit supply chains save time in data collection and analysis.  

## Design
This project uses image data from the [Chars74K dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/) because it includes handwritten and machine generated characters - both of which are commonly used by illicit actors. There are 62 distinct classes of character. 

I run two models for this project: a simple Convolutional Neural Network (CNN) and transfer learning model that uses MobileNet as a base frozen layer with the simple CNN layered on top. I selected MobileNet because it is a lightweight model (as compared to VGG16, for example), which allowed for faster training time without exessive computational strain. Early stopping was applied to both models during training to minimize overfit.
 
## Data
There are 62 classes of character with at least 1000 images per character (0-9, a-z, A-Z). Each character has handwritten, computer generated (font), and real life examples. In total the dataset consists of 74,185, 128x128 images. 

## Algorithms
*Data Upload & EDA* ([clean](https://github.com/tyrnaki/metis_coursework/blob/6ea14b87b72de6ab2f4b27789e1fddb7b635cd39/NPS/Reddit%20Scraper.ipynb))
1. Download datset from Chars74k
2. Create train, validate, test folders
3. Explore data

*Model Creation* ([clean]())
1. Set train, validate, test datsets
2. Establish parameters for early stopping (patience=2 for val_loss)
3. Create simple CNN
4. Train and test simple CNN
5. Save model
6. Plot CNN train and testing results
7. Upload MobileNet and freeze layers for transfer learning
8. Create transfer learning model (MobileNet + simple CNN)
9. Train and test transfer learning model
10. Save model
11. Plot transfer learning model train and testing results
12. Plot combined transfer learning and CNN model results
13. Create visualizations for model architecture 

*Model Evaluation* ([clean]())
1. Upload saved models
2. Create function to upload and test real life image screenshots
3. Evaluate model performance on real life images
4. Create confusion matrix on test data
5. Create dataframe on test data (true versus predicted values) to determine which characters had the most mislabeling

## Tools
- Pandas for data manipulation
- Matplotlib & Plotly for graphics
- Numpy for array/matrix creation and manipulation
- Splitfolders for data seperation
- Tensorflow/Keras for Neural Network creation 


## Communication
Slides and visuals presented.
