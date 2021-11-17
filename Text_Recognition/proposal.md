### Scraping Information from Illicit Chemical Advertisements using Deep Learning

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build? Who benefits from exploring this question or building this model/system?

Background: Many of the chemicals used to create synthetic drugs such as fentanyl and methamphetamine are [openly advertised online by chemical distributors](https://www.scmp.com/magazines/post-magazine/long-reads/article/3123109/chinas-fentanyl-connection-suppliers-fuelling) (largely in China). These distributors often try to evade chemical regulations and subsequent online marketplace regulations in China and the United States through advertisements using terms and spellings that are not easily machine readable, as well as through embedding contact and product information in images. 

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/Text_Recognition/images/Combined.png" alt="drawing" width="500" position='absolute' float='right'/>


Purpose: This project aims to use deep learning to recognize and extract text from images. This will help analysts looking at open source commerical data more quickly collect and connect data associated with illicit chemical distributors, in turn supporting investigations. 

Customers: Government analysts.

#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data? What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? If modeling, what will you predict as your target?

The algorithm will be trained and tested using images from the [COCO-Text dataset](https://bgshih.github.io/cocotext/#h2-download). Each image in the dataset (63,686 images) contains text annotation & whether or not the text is: machine-printed vs. handwritten, legible vs. illgible, or English vs. non-English. 

Ultimately, I will test the model on images scraped from business to business wholesale websites (such as the ones above) used by chemical distributors. As these advertisements are limited, I will use them as a final check for the utility of my model. 

The goal of the model is to 1) detect if there is text in a given image and 2) to extract the image with reasonable accuracy. 


#### Tools:
* How do you intend to meet the tools requirement of the project? 

I plan to use neural network tools such as TensorFlow/Keras as well as OpenCV and YOLO for computer vision. 

* Are you planning in advance to need or use additional tools beyond those required?

BeautifulSoup and other tools for web scraping.
Visualization tools where appropriate (tbd).

#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

An MVP for this project would be an algorithm that can detect whether or not a given image has text. In a more advanced version of the project, it would be able to detect and extract text from new images. 
