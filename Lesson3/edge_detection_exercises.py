# This is one way to write the gradient in the y-direction

def image_gradient_in_y(image):
    """
    This function will return the gradient of a gray-scale image in the Y-direction
    The differences of pixel values will be amplified by amplify_diff().
    """
    (n_row, n_col) = image.shape

    # Save the changes into a list
    diff_list = []

    for col_j in range(n_col):

        if IMAGE_DEBUG == True:
            print("col_j: %i"%(col_j))

        for row_i in range(n_row):
            if row_i == 0:
                diff_list.append(0)

                if IMAGE_DEBUG == True:
                    print("          row_i: %i ,  value = %i"%(row_i, small_blur[row_i, col_j]))
            else:
                value = int(image[row_i,   col_j])
                prev  = int(image[row_i-1, col_j])

                diff  = amplify_diff(value - prev)
                diff_list.append(diff)

                if IMAGE_DEBUG == True:
                    print("          row_i: %i ,  value = %i,  prev = %i,  diff = %i "%(row_i, value, prev, diff))

    # Convert the list back into an array of the same shape as the input image
    # Note: that we operated on the columns first and then rows so
    #       the resulting list is n_col x n_row long which must be transposed
    #       back to the n_row x n_col as in the original picture dimension
    diff_array = np.reshape(diff_list, (n_col, n_row)).T

    return diff_array

#######################################
# Test it on small gray road

road_gradient_y_img = image_gradient_in_y(small_gray_road_img)

plt.figure(figsize=(14,10))
plt.subplot(1, 3, 1)
plt.imshow(small_gray_road_img, cmap='gray')

plt.subplot(1, 3, 2)
plt.imshow(small_blur, cmap='gray')

plt.subplot(1, 3, 3)
plt.imshow(road_gradient_y_img, cmap='gray')

plt.show()

#######################################
# Test it on gray zebra

zebra_gradient_y_img = image_gradient_in_y(zebra_gray_blur_img)

plt.title("Zebra Gradient Y")
plt.imshow(zebra_gradient_y_img, cmap='gray')
plt.show()

#######################################
# Add the X and Y gradient zebra images
zebra_gradient_xy_img = cv2.bitwise_or(zebra_gradient_x_img, zebra_gradient_y_img, mask = None)

plt.figure(figsize=(20, 20))
plt.subplot(1, 3, 1)
plt.title("Zebra Gradient X")
plt.imshow(zebra_gradient_x_img, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("Zebra Gradient Y")
plt.imshow(zebra_gradient_y_img, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Zebra Gradient XY")
plt.imshow(zebra_gradient_xy_img, cmap='gray')
plt.show()

#######################################
# This is a smarter way to write the gradient in the y-direction from Joshua S.
# which does not require transposing the final list array

def image_gradient_in_y(image):
    (n_row, n_col) = image.shape
    # Save the changes into a list
    diff_list = []
    for row_i in range(n_row):
        if IMAGE_DEBUG == True:
            print("row_i: %i"%(row_i))
        for col_j in range(n_col):
            if col_j == 0:
                diff_list.append(0)
                if IMAGE_DEBUG == True:
                    print("          col_j: %i ,  value = %i"%(col_j, small_blur[row_i, col_j]))
            else:
                value = int(image[row_i, col_j])
                prev  = int(image[row_i-1, col_j])
                diff  = amplify_diff(value - prev)
                diff_list.append(diff)
                if IMAGE_DEBUG == True:
                    print("          col_j: %i ,  value = %i,  prev = %i,  diff = %i "%(col_j, value, prev, diff))
    # Convert the list back into an array of the same shape as the input image
    diff_array = np.reshape(diff_list, (n_row, n_col))
    return diff_array

#######################################
# This combines the gradients from X and Y directions in one function
# by looping through the rows and columns only once which reduces processing time
def image_gradient_in_xy2(image):
    """
    This function will return the gradient of a gray-scale image.
    The differences of pixel values will be amplified by amplify_diff().
    """
    (n_row, n_col) = image.shape

    # Save the changes into a list
    diff_list = []

    for row_i in range(n_row):
        if IMAGE_DEBUG == True:
            print("row_i: %i"%(row_i))

        for col_j in range(n_col):
            if col_j == 0:
                diff_list.append(0)
                if IMAGE_DEBUG == True:
                    print("          col_j: %i ,  value = %i"%(col_j, small_blur[row_i, col_j]))
            else:
                value = int(image[row_i, col_j])

                # Calculate gradients in both X and Y directions
                prev_x  = int(image[row_i, col_j-1])
                prev_y  = int(image[row_i-1, col_j])

                diff_x  = amplify_diff(value - prev_x)
                diff_y  = amplify_diff(value - prev_y)

                # Combined the gradients for both X and Y directions
                diff_max = max(diff_x, diff_y)

                diff_list.append(diff_max)
                if IMAGE_DEBUG == True:
                    print("          col_j: %i ,  value = %i,  prev = %i,  diff = %i "%(col_j, value, prev, diff))

    # Convert the list back into an array of the same shape as the input image
    diff_array = np.reshape(diff_list, (n_row, n_col))

    return diff_array

# Test this function with the gray zebra
zebra_gradient_xy2_img = image_gradient_in_xy2(zebra_gray_blur_img)

plt.title("Zebra Gradient XY")
plt.imshow(zebra_gradient_xy2_img, cmap='gray')
plt.show()
