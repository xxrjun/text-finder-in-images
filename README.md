# OCR Image Keyword Search

OCR Image Keyword Search is an efficient and user-friendly Python application that utilizes **Optical Character Recognition (OCR)** to search for user-specified keywords in a set of images. The application uses the Tesseract OCR engine and OpenCV for image processing, and stores OCR results for faster subsequent searches.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later.
- Put the images you want to search in the `./images` directory.

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/xxrjun/text-finder-in-images.git
   ```

2. Set up a virtual environment (optional, but recommended):

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place the images you want to search in the `./images` directory.
2. Run the main script:

   ```bash
   python main.py
   ```

3. When prompted, enter the keyword you want to search for. The program will search for the keyword in the images and display any images where the keyword is found. Press 'q' to close the image window and continue with the next image.

4. To exit the program, enter 'exit' when prompted for a keyword.
