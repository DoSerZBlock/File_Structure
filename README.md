# File_Structure

一個將檔案目錄結構轉換為 JSON 格式的工具。

A utility to convert file directory structures into JSON format.

## 功能 / Features

- 遞迴掃描目錄結構 / Recursively scans directory structures
- 轉換為 JSON 格式 / Converts to JSON format
- 支援根據 .gitignore 忽略檔案和資料夾 / Supports ignoring files and folders based on .gitignore rules
- 圖形界面操作 / Graphical user interface
- 自訂 JSON 檔案儲存位置 / Custom JSON file save location
- 紀錄檔案大小 / Records file sizes

## 使用方式 / Usage

### 執行程式 / Run the program

```
python main.py
```

### 操作步驟 / Operation steps

1. 點擊「開始」按鈕 / Click the "Start" button
2. 在彈出的對話框中選擇要掃描的根目錄 / Select the root directory to scan in the dialog
3. 再選擇要儲存 JSON 檔案的位置 / Then select where to save the JSON file
4. 完成後會顯示通知訊息 / A notification will appear when complete

## JSON 輸出格式 / JSON Output Format

輸出的 JSON 格式如下 / The output JSON follows this structure:

```json
{
  "資料夾名": {
    "子資料夾名": {
      "檔案名.txt": 1024
    },
    "另一個檔案.md": 512
  }
}
```

檔案名對應的值為檔案大小（以位元組為單位）/ The value associated with each file name is the file size in bytes.

## 技術細節 / Technical Details

- 使用 tkinter 實現圖形界面 / Using tkinter for GUI
- 若目標資料夾含有 .gitignore 檔案，會自動排除被忽略的項目 / Automatically excludes items listed in .gitignore file if present
- 輸出的 JSON 檔案使用 UTF-8 編碼並縮排 / Output JSON files are UTF-8 encoded and indented
- 輸出檔案名稱格式為：[選擇的根目錄]_file_structure.json / Output filename format: [selected_root_directory]_file_structure.json

## 系統需求 / Requirements

- Python 3.6 或更高版本 / Python 3.6 or higher
- tkinter (通常包含在標準 Python 安裝中) / tkinter (usually included in standard Python installation)

## 注意事項 / Notes

- 自動忽略 .git 資料夾 / .git folder is automatically ignored
- 檔案名稱可能包含非 ASCII 字符 / File names may contain non-ASCII characters
- 檔案結構以 tree-like 結構呈現，其中資料夾是中間節點，檔案是葉子節點 / File structure is presented in a tree-like structure where directories are nodes and files are leaf nodes