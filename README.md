# Overview

* This project contains a Machine Learning Model trained to recognize images of cats and dogs and a command line interface application that allows you to send images to the model and receive predictions.

# Getting Started

* Installing Python
    * Visit this URL to download Python 3.11.8: https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe
    * Go to your downloads file and open "python-3.11.8-amd64" (see figure 1).
    * Once the window is open, at the very bottom, check the box that says "Add python.exe to PATH", then click "Install Now" (see figure 2).
    * Once you see the window say "Setup was successful", close the window.
    * To check that Python was installed correctly, click the windows icon and search for and open "terminal" (see figure 3). 
    * Once the terminal window is open, type "python --version". The response should say "Python 3.11.8" (see figure 4).
    * Leave your terminal window open. We'll come back to it later. 

* Setting up the application
    * Go to the location where you downloaded the .zip file containing the code.  
    * Right click and select "Extract All..." (see figure 5). 
    * A window will open with a location for where the files will be extracted. Click "Extract". 
    * Once the extraction is complete, double click on the file "capstone-main". This should show another file called "capstone-main". 
    * Right click on the "capstone-main" folder and select "Copy as path" (see figure 6). 
    * Navigate back to your terminal window and type "cd", then the spacebar, then type ctrl + v, then press enter (see figure 7).  
    * Next, copy and paste the below command into<> your terminal. This is going to install all the different kinds of code that this application needs to run It will finish after a few minutes (see figure 8).
        * ```    
          pip install --no-cache-dir -r requirements.txt
          ```
    * Once it has finished, scroll all the way to the bottom and type "clear" into the terminal and press enter. This should clear your terminal window (see figure 9 and 10). 
    * Leave your terminal window open. We'll come back to it later. 

* Running the application
    * Find an image of a dog or a cat and save it on your computer.
    * Navigate to the image, right click, then select "Copy as path" (see figure 11).
    * Navigate back to your terminal and copy the code below into the terminal. 
        * ```
          python main.py
          ```
    * The terminal will ask you to input the path to the image. Type ctrl + v (see figure 12). 
    * Once you push enter, the application will tell you whether it thinks it's a cat or a dog and the % confidence it has for the prediction.
    * Repeat these steps as many times as you would like!
 
# Figures

* ## Figure 1

![](/md%20_images/python_download.png)

* ## Figure 2

![](/md%20_images/python_path.png)

* ## Figure 3

![](/md%20_images/terminal.png)

* ## Figure 4

![](/md%20_images/python_version.png)

* ## Figure 5

![](/md%20_images/extract_zip.png)

* ## Figure 6

![](/md%20_images/extract_path.png)

* ## Figure 7

![](/md%20_images/cd_path.png)

* ## Figure 8

![](/md%20_images/add_dependancies.png)

* ## Figure 9

![](/md%20_images/clear.png)

* ## Figure 10

![](/md%20_images/cleared_terminal.png)

* ## Figure 11

![](/md%20_images/image_path.png)

* ## Figure 12

![](/md%20_images/use_app.png)
