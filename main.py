#############################################################
#                                                           #
#                   Krushna Vyas                            #
#        This project is under MIT License                  #
#                 Copyright © 2025                          #
#                                                           #
#############################################################

from Image_Processing_Techniques.edge_detection import canny_edge, laplacian_edge, sobel_edge
from Image_Processing_Techniques.thresholding_techniques import binary_thresholding, adaptive_thresholding, otsu_thresholding
import cv2

image = cv2.imread('.datasets/dog.jpg')

thresholding_methods = {
    '1': lambda: binary_thresholding(image, 127, 255),
    '2': lambda: adaptive_thresholding(image, 127, 255),
    '3': lambda: otsu_thresholding(image, 0, 255),
}

edge_methods = {
    '1': lambda: sobel_edge(image),
    '2': lambda: canny_edge(image),
    '3': lambda: laplacian_edge(image),
}

while True:
    print("\nWhat would you like to run?")
    print("(1) Thresholding Techniques\n(2) Edge Detection\n(3) Quit")
    main_choice = input("Enter your choice: ").strip().lower()
    if main_choice == '3' or main_choice == 'quit':
        break
    elif main_choice == '1':
        print("(1) Binary\n(2) Adaptive\n(3) OTSU\n(4) Back")
        while True:
            what_to_run = input("Enter the Image Processing Techniques you wish to use (or 'back' to return): ").strip().lower()
            if what_to_run == 'back' or what_to_run == '4':
                break
            func = thresholding_methods.get(what_to_run)
            if func:
                func()
            else:
                print("Invalid option. Please select a valid technique or type 'back' to return.")
    elif main_choice == '2':
        print("(1) Sobel Edge\n(2) Canny Edge\n(3) Laplacian Edge\n(4) Back")
        while True:
            what_to_run = input("Enter the corresponding number to run the detection method (or 'back' to return): ").strip().lower()
            if what_to_run == 'back' or what_to_run == '4':
                break
            func = edge_methods.get(what_to_run)
            if func:
                func()
            else:
                print("Invalid option. Please select a valid technique or type 'back' to return.")
    else:
        print("Invalid option. Please select 1, 2, or 3.")
