import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Dict, Optional, List


def get_ignore_list(gitignore_path: str) -> List[str]:
    """讀取 .gitignore 並解析忽略的檔案/目錄"""
    if not os.path.exists(gitignore_path):
        return []

    with open(gitignore_path, "r", encoding="utf-8") as f:
        return [line.rstrip("/ \n") for line in f if line.strip()] + [".git"]


def get_file_structure(root: str, ignore_list: List[str]) -> Dict[str, Optional[dict]]:
    """遞迴取得目錄結構，並忽略指定的路徑"""
    structure = {}

    for item in os.listdir(root):
        full_path = os.path.join(root, item)
        relative_path = os.path.relpath(full_path, start=root)

        # 忽略列表檢查
        if any(segment in ignore_list for segment in relative_path.split(os.sep)):
            continue

        if os.path.isdir(full_path):
            structure[item] = get_file_structure(full_path, ignore_list)
        else:
            structure[item] = os.path.getsize(full_path)

    return structure


def select_directory(title: str) -> str:
    """彈出對話框讓使用者選擇目錄"""
    return filedialog.askdirectory(title=title)


def generate_file_structure():
    """UI 觸發函式，執行目錄掃描並儲存 JSON"""
    root_path = select_directory("選擇要掃描的根目錄")
    if not root_path:
        return

    save_folder = select_directory("選擇儲存 JSON 的目錄")
    if not save_folder:
        return

    gitignore_path = os.path.join(root_path, ".gitignore")
    ignore_list = get_ignore_list(gitignore_path)
    structure = get_file_structure(root_path, ignore_list)

    output_filename = os.path.basename(os.path.normpath(root_path)) + "_structure.json"
    output_file = os.path.join(save_folder, output_filename)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(structure, f, ensure_ascii=False, indent=4)

    messagebox.showinfo("完成", f"檔案結構已儲存到：\n{output_file}")


def create_ui():
    """建立簡單的 UI 介面"""
    root = tk.Tk()
    root.title("目錄結構導出工具")
    root.geometry("300x200")

    label = tk.Label(root, text="選擇根目錄並導出 JSON 檔案", font=("Arial", 12))
    label.pack(pady=20)

    button = tk.Button(
        root, text="開始", font=("Arial", 12), command=generate_file_structure
    )
    button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_ui()
