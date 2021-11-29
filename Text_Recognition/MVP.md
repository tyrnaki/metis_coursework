## Towards Text Recognition in Illicit Advertisements: Character Recognition in Images

The goal of this project is to begin to create a process through which text can be scraped from online advertisements tied to illicit supply chains. Oftentimes, organizations that supply raw chemicals towards for drug production (fentanyl, for example) use text embedded in images to avoid basic online censorship (see example below). This effort will help analysts and investigators collect information related to these suppliers (phone numbers, products offered, etc). 

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/Text_Recognition/images/huanhao.jpg" alt="drawing" width="400" position='absolute' float='right'/>


In order to begin to extract text from these images, I plan to use a neural network (NN) to recognize individual characters (letters and numbers). The initial NN uses character examples from the [Chars74k dataset](http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/#download), which includes examples of numbers (0-9) and letters (a-z, upper & lowercase) as handwritten, computer font, and photos from real life. Each character has at least 1,000 images associated with it for a total of 74,185 images in the dataset; the model predicts on 62 different classes.

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/Text_Recognition/images/example_letters.png" alt="drawing" width="300" position='absolute' float='right'/>

On training data, the initial NN yeilded an accuracy of 0.7154 and a loss of 0.9133; while on test data it yeilded similar results with an accuracy of 0.7125 and loss of 0.9403.

In order to tie this model back to the project's business case, I took screenshots of characters as seen in some illicit advertisements. The model was able to predict well on more distict characters (A & M) but had difficulty distinguishing between characters with some similarities in shape (0 versus U, for example). 

<img src="https://github.com/tyrnaki/metis_coursework/blob/main/Text_Recognition/images/A_results.png" alt="drawing" width="400" position='absolute' float='left'/>
<img src="https://github.com/tyrnaki/metis_coursework/blob/main/Text_Recognition/images/O_results.png" alt="drawing" width="400" position='absolute' float='right'/>


I plan to improve the model by applying transfer learning as appropriate. 
