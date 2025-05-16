# File Organizer

A simple Python script to automatically organize files in your Downloads folder by file type.

## Features

- Moves files into categorized folders (Images, Documents, Videos, Music, Archives, Code, Others)
- Easy to configure and use
- Supports common file extensions

## How It Works

The script scans your `Downloads` folder and moves files into subfolders based on their extension. Unmatched files are moved to an `Others` folder.

## Usage

1. **Requirements:**

   - Python 3.x installed

2. **Configuration:**  
   By default, the script organizes files in `C:\Users\faeln\Downloads`.  
   To change the folder, edit the `source_folder` variable in [`file_organizer.py`](file_organizer.py).

3. **Run the Script:**
   - Double-click `organizer_launcher.bat`  
     **OR**
   - Run from command line:
     ```sh
     python file_organizer.py
     ```

## File Type Categories

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`
- **Documents:** `.pdf`, `.docx`, `.txt`
- **Videos:** `.mp4`, `.mov`, `.avi`
- **Music:** `.mp3`, `.wav`
- **Archives:** `.zip`, `.rar`, `.7z`
- **Code:** `.py`, `.js`, `.html`, `.css`
- **Others:** Any file not matching above types

## Customization

To add or remove file types, edit the `file_types` dictionary in [`file_organizer.py`](file_organizer.py).

## License

This project is for personal use and demonstration purposes.
