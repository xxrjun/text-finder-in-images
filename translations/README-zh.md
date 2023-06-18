![GitHub license](https://img.shields.io/github/license/xxrjun/text-finder-in-images) ![GitHub repo size](https://img.shields.io/github/repo-size/xxrjun/text-finder-in-images)

Languages: [English](README.md) | [中文](translations/README-zh.md)

# OCR 圖像關鍵字搜尋

OCR 圖像關鍵字搜尋是一個高效且易於使用的 Python 應用程式，利用 **光學字符識別（OCR)** 技術在一組圖像中搜尋用戶指定的關鍵字。該應用程式使用 Tesseract OCR 引擎和 OpenCV 進行圖像處理，並儲存 OCR 結果以加快後續搜尋的速度。

## 先決條件

在開始之前，請確保您已經滿足以下需求：

- Python 3.6 或更高版本。
- 你的機器已安裝 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)。

  ### 對於 **Windows** 使用者

  可以從 [UB Mannheim Github 頁面](https://github.com/UB-Mannheim/tesseract/wiki) 下載安裝程式並按照安裝說明進行操作。

  ### 對於 **Mac** 使用者，可以使用 Homebrew 安裝 Tesseract：

  ```bash
  brew install tesseract
  ```

  ### 對於 **Linux** 使用者，可以使用 apt 安裝 Tesseract：

  ```bash
  sudo apt install tesseract-ocr
  ```

- 將您想要搜尋的圖片放置在 `./images` 目錄下。

## 安裝

1. 將此存儲庫克隆到您的本地機器。

   ```bash
   git clone https://github.com/xxrjun/text-finder-in-images.git
   ```

2. 設置虛擬環境（可選，但推薦）：

   ```bash
   python3 -m venv venv
   ```

3. 啟動虛擬環境：

   ```bash
   source venv/bin/activate
   ```

4. 安裝所需的 Python 套件：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方式

1. 將您想要搜尋的圖片放置在 `./images` 目錄下。
2. 運行主腳本：

   ```bash
   python main.py
   ```

3. 當被提示時，輸入您想要搜尋的關鍵字。該程式將在圖像中搜尋關鍵字，並顯示找到關鍵字的任何圖像。按 'q' 關閉圖像視窗並繼續下一個圖像。

4. 若要退出程式，當被提示輸入關鍵字時，輸入 'exit'。(OCR)\*\* 技術在一組圖像中搜尋用戶指定的關鍵字。該應用程式使用 Tesseract OCR 引擎和 OpenCV 進行圖像處理，並儲存 OCR 結果以加快後續搜尋的速度。

## 先決條件

在開始之前，請確保您已經滿足以下需求：

- Python 3.6 或更高版本。
- 您的機器已安裝 Tesseract OCR。

  對於 **Windows** 使用者，您可以從 [UB Mannheim Github 頁面](https://github.com/UB-Mannheim/tesseract/wiki) 下載安裝程式並按照安裝說明進行操作。

  對於 **Mac** 使用者，您可以使用 Homebrew 安裝 Tesseract：

  ```bash
  brew install tesseract
  ```

  對於 **Linux** 使用者，您可以使用 apt 安裝 Tesseract：

  ```bash
  sudo apt install tesseract-ocr
  ```

- 將您想要搜尋的圖片放置在 `./images` 目錄下。

## 安裝

1. 將此存儲庫克隆到您的本地機器。

   ```bash
   git clone https://github.com/xxrjun/text-finder-in-images.git
   ```

2. 設置虛擬環境（可選，但推薦）：

   ```bash
   python3 -m venv venv
   ```

3. 啟動虛擬環境：

   ```bash
   source venv/bin/activate
   ```

4. 安裝所需的 Python 套件：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方式

1. 將您想要搜尋的圖片放置在 `./images` 目錄下。
2. 運行主腳本：

   ```bash
   python main.py
   ```

3. 當被提示時，輸入您想要搜尋的關鍵字。該程式將在圖像中搜尋關鍵字，並顯示找到關鍵字的任何圖像。按 'q' 關閉圖像視窗並繼續下一個圖像。

4. 若要退出程式，當被提示輸入關鍵字時，輸入 'exit'。
