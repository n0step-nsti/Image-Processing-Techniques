import cv2
import matplotlib.pyplot as plt

def sobel_edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel (gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel (gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(sobel_combined, cmap='gray'), plt.title('Sobel Edges')
    plt.show()

def canny_edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny (blurred, threshold1=50, threshold2=150)
    plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Canny Edges')
    plt.show()


def laplacian_edge(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    laplacian_abs = cv2.convertScaleAbs(laplacian)
    plt.subplot(1, 2, 1), plt.imshow(gray, cmap='gray'), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(laplacian_abs, cmap='gray'), plt.title('Laplacian Edges')
    plt.show()