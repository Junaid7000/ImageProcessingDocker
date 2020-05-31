import numpy as np
import cv2
import matplotlib.pyplot as plt

def open_image(image_path):
    '''open image for the test.
    '''
    image = cv2.imread(image_path)
    print(f"shape: {image.shape}")

    # cv2.imshow('test_image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



if __name__ == "__main__":
    test_img = "./img_rainbow.jpeg"
    open_image(test_img)
