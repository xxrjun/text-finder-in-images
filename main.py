import cv2
import pytesseract
import os
import json
import glob

# 設定tesseract的路徑
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'


# OCR的函數
def ocr_image(input_path):
    img = cv2.imread(input_path)
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    words = list(zip(data['text'], data['left'], data['top'], data['width'], data['height']))
    return words


# 對每張圖片進行OCR並儲存結果
ocr_results = {}
if os.path.exists('ocr_results.json'):
    with open('ocr_results.json', 'r') as f:
        ocr_results = json.load(f)
else:
    image_files = glob.glob('./images/*')
    for image_file in image_files:
        print(f'Processing image {image_file}')
        ocr_results[image_file] = ocr_image(image_file)

    # 將結果寫入JSON檔案
    with open('ocr_results.json', 'w') as f:
        json.dump(ocr_results, f)

# 使用者輸入搜尋文字
while True:
    keyword = input('Enter a keyword (or "exit" to quit): ')
    if keyword.lower() == 'exit':
        break

    # 對每張圖片進行搜尋
    for image_file in image_files:
        words = ocr_results[image_file]
        img = cv2.imread(image_file)
        found = False
        for word, left, top, width, height in words:
            if keyword in word:
                print(f'Keyword found in {image_file} at position {left}, {top}')
                img = cv2.rectangle(img, (left, top), (left + width, top + height), (0, 255, 0), 2)
                found = True
        if found:
            cv2.imshow('img', img)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            print(f'Keyword not found in {image_file}')
