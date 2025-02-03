# Image Renaming Script

This Python script renames image files in the specified folder in two steps:

1. **Assign a unique temporary name** using UUID to avoid filename conflicts.
2. **Rename files in order of creation time** following the format: `WF-YYYY-MM-DD_(PXX).ext`.

## Features
- Supports common image formats: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`, `.mov`.
- Sorts images by their creation time.
- Allows the user to specify a starting number for indexing.
- Ensures filenames remain unique during processing.

## Prerequisites
- Python 3.x

## Usage
1. Place the script inside the target folder where the images are stored.
2. Run the script:
   ```bash
   python script.py
   ```
3. Enter the starting number when prompted (or use the default value `1` if input is invalid).
4. The script will rename images following the pattern `WF-YYYY-MM-DD_(PXX).ext`.

## Example
**Before execution:**
```
photo1.jpg
photo2.png
photo3.gif
```

**After execution (assuming today's date is 2025-02-03 and starting number is 1):**
```
WF-2025-02-03_(P01).jpg
WF-2025-02-03_(P02).png
WF-2025-02-03_(P03).gif
```

## Notes
- The script operates on files in the current directory (`./`).
- It first assigns temporary names before renaming them to avoid conflicts.
- Sorting is based on the file creation time.

## License
This script is free to use and modify for any personal or commercial projects.

