# 📂 Directory Organizer (System Engineering)

---

## **1. Project Title & Goal**
**Directory Organizer** is a Python script that scans a user-specified folder, automatically organizes files by type (text and images), and renames moved files using a `DDMMYYYY` timestamp to keep the directory clean and structured.

---

## **2. Setup Instructions**
Follow the steps below to run the project using **PowerShell / VS Code Terminal**:

```powershell
cd "C:\Users\hp\OneDrive\Desktop\DOT"
py -3 .\directory_org.py
```
 When prompted, enter the folder path to organize:
```Enter Folder Path: C:\Users\hp\OneDrive\Desktop\Folder```
Alternatively, run the script in one command (no prompt):
```py -3 .\directory_org.py "C:\path\to\your\folder"```

## **3. The Logic (How you thought)**
• Why did you choose this approach?
I used Python’s pathlib module to scan directories in a clean, readable, and platform-independent way.
File extensions are checked using .suffix.lower(), ensuring accurate classification of files.
The shutil.move() function handles both moving and renaming files in a single step, making the script efficient and easy to maintain.

• What was the hardest bug you faced, and how did you fix it?
The most challenging issue was preventing file overwrites when multiple files received the same timestamp-based name.
To solve this, I implemented an ensure_unique_path() function that automatically appends suffixes like _1, _2, etc., if a filename already exists in the destination folder.

## **4. Output Screenshots**
📌 Before Organization
<img width="1915" height="1010" alt="Screenshot 2026-01-28 123332" src="https://github.com/user-attachments/assets/468a94c2-795d-4741-b47b-212317090683" />
📌 After Organization
<img width="1175" height="653" alt="Screenshot 2026-01-28 123446" src="https://github.com/user-attachments/assets/510c042f-f9d8-4064-8bfa-33d14ac48d59" />
## **5.Future Improvements**

If I had two more days to extend this project, I would implement the following enhancements:
🔹 Recursive directory organization using a --recursive flag
🔹 Dry-run mode (--dry-run) to preview changes before executing them
🔹 Configurable rules file (JSON/YAML) to allow easy addition of new categories such as PDFs, ZIP files, and videos without modifying the core code
