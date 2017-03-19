# phash
Perceptual Hashing Alogrithim that compares two images

## About
This perceptual hashing algorithm will determine if two images are similar (same) or different. The result will show the hash value differences. From a high level the two images are reduced,greyscaled,averaged,compared to the average, and hashed. The hash results are then compared for similiarties.

# Set Up
This app is built on python3. You will need [numpy](https://scipy.org/install.html) and [PIL](http://stackoverflow.com/questions/20060096/installing-pil-with-pip)

```
pip3 install PIL
```
You should change the shabang (#!) at the begining of the file if your python3 executable path is not under **/usr/bin/env**

# Running
To run the program simply run the following command on your terminal emulator of choice.
```
python3 main.py IMG1_PATH.jpg IMG2_PATH.jpg
```
The results will then be printed as stdout. If the file is unopenable by PIL it will raise an exception.

## Inspiration and Sources
- http://www.phash.org/
- http://www.hackerfactor.com/blog/?/archives/432-Looks-Like-It.html

### footnote
I may plan on expanding this project into making the algorithm more versatile and robust in handling different types of images and potentially videos (Frame by Frame).
