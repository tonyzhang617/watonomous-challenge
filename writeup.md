<!--
  This is a Markdown file. To view it properly, go to https://github.com/tonyzhang617/watonomous-challenge/blob/master/writeup.md
-->

# Lane Line Finding Challenge Write-up By Tianyi (Tony) Zhang

### How to Get Up and Running
See `README.md`.

### Thought Process
I carefully examined the example images, and arrived at the following conclusions:
1. The lane lines are white or yellow (almost) straight lines on brownish black roads
2. The lane lines can be continuous or dotted
3. The lane lines are on the lower half of the image
4. The two lane lines are each at around +40 and -40 degrees to the vertical
5. Only the first lane lines to the left and right of the vertical center need to be identified

### Exploration
By reading the Jupyter Notebook in the provided GitHub repository, I was able to discover the helper functions I need to get started. The second cell in the notebook tells me that *The tools you have are color selection, region of interest selection, grayscaling, Gaussian smoothing, Canny Edge Detection and Hough Tranform line detection.* I Googled these terms one by one, and read through the result pages to get an idea of what these techniques do. Then I summarized the following points:
1. Canny Edge Detector can significantly reduce the amount of data to be processed in an image by detecting edges. Its output image will be a black image with white highlights for edges.
2. The accuracy of edge detection is negatively impacted by image noise. Thus the image need to be first processed with a Gaussian Blur to be rid of noise.
3. The image has to be in grayscale before it is processed with Gaussian Blur.
4. The Hough Line Transform is able to detect straight lines in an image. However, edge detection needs to be applied beforehand.
5. Region of interest can be applied to focus on the mostly likely area for lane lines.

From these findings, I came up with the following pipeline:

Region of Interest (Focus on the lower half of the image) &rarr; Grayscale &rarr; Gaussian Filter &rarr; Canny Edge Detection &rarr; Hough Line Transform

### Making Improvements
The procedure above works relatively well. However, it has a few flaws.
1. Canny Edge Detection not only picks up the edges formed by lane lines, but also picks up edges of the horizon and vehicles. Thus unwanted straight lines are recognized by Hough Line Transform.
2. Using the lower half of the image doesn't remove the straight lines formed by other lane lines and the edge of asphalt.

To tackle these issues, I came up with the following solutions:
1. Use color selection to isolate lane lines by their white and yellow colors.
2. Apply a more specific region of interest selection (a triangle formed by the center, lower left corner, and lower right corner of the image).

### Final Pipeline
Region of Interest (lower half of the image) &rarr; Color Selection &rarr; Grayscale &rarr; Gaussian Filter &rarr; Canny Edge Detection &rarr; Region of Interest (lower triangle) &rarr; Hough Line Transform

### Difficulties
I encountered several difficulties during the process. Being new to the field of computer vision, I accomplished things by trial and error. For example, I tried out different parameter values for the functions that apply Gaussian Blur and Hough Line Transform to get them working.

I spent quite some time playing with the values for color range selection. Initially, I tried the range between the brighest yellow and a darker yellow, but the lane lines weren't picked up. Then I came up with the idea of using GIMP to sample the colors on the image. By putting in the actual colors, I was able to isolate the color of the lane lines.

### Room for Improvement
My solution has the following flaws:
1. The program only recognizes straight lane lines in the center of the image. If the vehicle is changing lines and turning in the picture, the program would mostly likely fail.
2. Only yellow and white lane lines are recognized
3. The program focuses entirely on the lower half of the image. Thus if the road is going uphill in front of the vehicle, the lines get cut off.
4. Only lane line segments are recognized by the program. I would like to add the feature for extending the lines.

**********

### Viewing the Code
To view the notebook without running it, simply go to [this page]( https://github.com/tonyzhang617/watonomous-challenge/blob/master/lane_line_finding.ipynb).

### Screenshots
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/notebook.png" width="600px" />
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/result0.png" width="240px" />
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/result1.png" width="240px" />
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/result2.png" width="240px" />
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/result3.png" width="240px" />
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/result4.png" width="240px" />
<img src="https://raw.githubusercontent.com/tonyzhang617/watonomous-challenge/master/screenshots/result5.png" width="240px" />
