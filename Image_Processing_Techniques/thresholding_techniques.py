import cv2
import matplotlib.pyplot as plt

def binary_thresholding(image, threshold_value, max_value):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(
        gray_image, 
        threshold_value, 
        max_value, 
        cv2.THRESH_BINARY
    )
    
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.title("Grayscale Image")
    plt.imshow(gray_image, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.title("Binary Image (Thresholding)")
    plt.imshow(thresholded_image, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()


def adaptive_thresholding(image, threshold_value, max_value):
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(
        gray_image, 
        threshold_value, 
        max_value, 
        cv2.THRESH_BINARY
    )

    adaptive_image = cv2.adaptiveThreshold(
        gray_image,
        max_value,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=11,
        C=2
    )

    plt.figure(figsize=(16, 4))
    plt.subplot(1, 4, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.title("Grayscale Image")
    plt.imshow(gray_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.title("Binary Thresholding")
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.title("Adaptive Thresholding")
    plt.imshow(adaptive_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


def otsu_thresholding(image, threshold_value, max_value):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, otsu_image = cv2.threshold(
        gray_image, 
        threshold_value, 
        max_value, 
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title("Grayscale Image")
    plt.imshow(gray_image, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Otsu's Thresholding")
    plt.imshow(otsu_image, cmap="gray")
    plt.axis("off")

    plt.tight_layout()
    plt.show()