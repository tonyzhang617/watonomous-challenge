# Write-up By Tianyi (Tony) Zhang

### Programming Language
After carefully reading through the materials, I decided to use Python to tackle this challenge. Although C++ is recommended, it is more difficult and time-consuming to implement features in than Python. Considering the time constraint of this challenge, I will go with Python. If sufficient time is left by the end, I will migrate the code into C++.

### Thought Process
I examined the example images and arrived at the following conclusions:
1. The lane lines are white or yellow lines/curves on brownish black roads
2. The lane lines can be continuous or dotted
3. The lane lines are on the lower half of the image
4. The lane lines are at around 40 degrees
5. Only the first lane lines to the left and right of the vertical center need to be identified

### Exploration
By reading the Jupyter Notebook in the repository, I was able to discover the helper functions I need to get started. The second cell tells me that *The tools you have are color selection, region of interest selection, grayscaling, Gaussian smoothing, Canny Edge Detection and Hough Tranform line detection.* I first Googled these terms one by one, and skimmed through the result pages to get an idea of what these techniques do. Then I summarized the following points:
1. Color selection can isolate lane lines by their white and yellow colors
2. Canny Edge Detector can significantly reduce the amount of data to be processed in an image by detecting edges. Its output image will be a black image with white highlights for edges.
3. The accuracy of edge detection is negatively impacted by image noise. Thus the image need to be first processed with a Gaussian filter to be rid of noise.
4. The Hough Line Transform is able to detect straight lines in an image. However, edge detection needs to be applied beforehand.
5. Region of interest can be applied first to isolate the mostly likely area for lane lines.

### Pipeline
Region of Interest &rarr; Color Selection &rarr; Grayscale &rarr; Gaussian Filter &rarr; Canny Edge Detection &rarr; Region of Interest &rarr; Hough Line Transform
Grayscale &rarr; Region of Interest &rarr; Gaussian Filter &rarr; Canny Edge Detection &rarr; Hough Line Transform

### Setbacks
I have had a lot of success since the beginning. Lines of horizon, where road meets land. Solution: color selection

finding the range is quite hard
Use the color picker in GIMP
