import pytesseract
from PIL import Image

# Set the path for tesseract executable
# If you're on Windows, it might look like this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_with_location(image_path):
    # Open the image
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text_data = pytesseract.image_to_data(img, lang="chi_sim+eng")

    # Process and print the text and its location
    for count, data in enumerate(text_data.splitlines()):
        if count > 0:
            data = data.split()
            if len(data) == 12:
                text, x, y, width, height = data[11], data[6], data[7], data[8], data[9]
                print(f"Text: {text}, Position: ({x}, {y}), Size: ({width}x{height})")

import pytesseract
from PIL import Image

# Set the path for tesseract executable if needed
# pytesseract.pytesseract.tesseract_cmd = r'<path_to_your_tesseract_executable>'

def extract_text_by_blocks(image_path):
    # Open the image
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    # The configuration '6' stands for Assume a single uniform block of text.
    text_data = pytesseract.image_to_data(img, config='--psm 6')

    # Initialize a list to hold all the blocks
    text_blocks = []

    # Process the text data
    for count, data in enumerate(text_data.splitlines()):
        if count > 0:  # Skip the first line as it contains headers
            data = data.split()
            if len(data) == 12:  # This ensures that the data line is valid
                block_num, text, x, y, width, height = data[2], data[11], int(data[6]), int(data[7]), int(data[8]), int(data[9])
                # Grouping the text by block number
                if block_num not in text_blocks:
                    text_blocks.append({'block_num': block_num, 'text': [text], 'x': x, 'y': y, 'width': width, 'height': height})
                else:
                    text_blocks[-1]['text'].append(text)

    # Print the blocks and their locations
    for block in text_blocks:
        print(f"Block Number: {block['block_num']}, Text: {' '.join(block['text'])}, Position: ({block['x']}, {block['y']}), Size: ({block['width']}x{block['height']})")

# Example usage
# extract_text_by_blocks("test.png")

# Example usage
# extract_text_with_location("test.png")
def extract_text(image_path, psm_mode):
    # Preprocess the image
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image with the chosen psm mode
    custom_config = f'--psm {psm_mode}'
    text_data = pytesseract.image_to_data(img, config=custom_config)

    # Output the recognized text
    print("Recognized Text:")
    print(pytesseract.image_to_string(img, config=custom_config))

    # Output the text with location
    print("\nText with Location:")
    for count, data in enumerate(text_data.splitlines()):
        if count > 0:  # Skip the first line with column names
            data = data.split()
            if len(data) == 12:  # Valid data line
                text, x, y, width, height = data[11], data[6], data[7], data[8], data[9]
                print(f"Text: {text}, Position: ({x}, {y}), Size: ({width}x{height})")

# Example usage with PSM 6
extract_text("test.png", 6)
