# Image Processing Techniques

A Python-based toolkit for exploring and applying advanced image processing techniques, enabling users to analyze, enhance, and transform images with ease and flexibility.

## Features
- Thresholding techniques: Binary, Adaptive, and OTSU thresholding
- Edge detection methods: Sobel, Canny, and Laplacian
- Modular codebase for easy extension and experimentation

## Project Structure
```
Image-Processing-Techniques/
├── .datasets/                  # Sample images for processing
├── Image_Processing_Techniques/
│   ├── edge_detection.py       # Edge detection functions
│   └── thresholding_techniques.py # Thresholding functions
├── main.py                     # Main CLI application
├── LICENSE
└── README.md
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Image-Processing-Techniques.git
   cd Image-Processing-Techniques
   ```
2. Install the required dependencies:
   ```bash
   pip install opencv-python
   pip install matplotlib
   ```

## Usage
1. Place your input images in the `.datasets/` directory (e.g., `dog.jpg`).
2. Run the main application:
   ```bash
   python main.py
   ```
3. Follow the interactive menu to select thresholding or edge detection techniques.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.