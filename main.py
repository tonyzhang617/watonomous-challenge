boundaries = [([200, 200, 200], [255, 255, 255]), ([190, 160, 80], [250, 220, 125])]
new_images = []

for (lw, up) in boundaries:
    lower = np.array(lw)
    upper = np.array(up)
    print(lower, upper)

    mask = cv2.inRange(image, lower, upper)
    new_images.append(cv2.bitwise_and(image, image, mask = mask))

range_img = cv2.addWeighted(new_images[0], 1.0, new_images[1], 1.0, 0)

plt.imshow(range_img, cmap='gray')

# TODO: Build your pipeline that will draw lane lines on the test_images
# then save them to the test_images_output directory.

gray_img = grayscale(range_img)
# poly_a = np.array([[0, height-10], [width, height-10], [(width) / 2, (height) / 2]], np.int32)
# region_img_a = region_of_interest(hough_img, [poly])
height, width = gray_img.shape
poly_bottom = np.array([[0, height/2], [0, height], [width, height], [width, height/2]], np.int32)
# poly_bottom = np.array([[0, height], [width, height], [width/2, height/2]], np.int32)
bottom_img = region_of_interest(gray_img, [poly_bottom])

gaussian_img = gaussian_blur(bottom_img, 5)
canny_img = canny(gaussian_img, 64, 128)
hough_img = hough_lines(canny_img, 1, np.pi/180, 50, 8, 16)

poly_tg = np.array([[0, height], [width, height], [width/2, height/2]], np.int32)
final_img = region_of_interest(hough_img, [poly_tg])

# plt.imshow(gaussian_img, cmap='gray')
plt.imshow(final_img, cmap='gray')
