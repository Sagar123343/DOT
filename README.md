# Directory Organizer (System Engineering)

1. Project Title & Goal: A Python script that scans a folder, moves `.txt` files into `Text_Files/`, moves `.png/.jpg` files into `Images/`, and renames moved files with a `DDMMYYYY` timestamp (example: `image_28012026.png`).

2. Setup Instructions: Exact commands to run your code

```powershell
cd "C:\Users\hp\OneDrive\Desktop\DOT"
py -3 .\directory_org.py
```

When prompted, type/paste the folder path and press Enter, for example:

`Enter Folder Path: C:\Users\hp\OneDrive\Desktop\Folder`

Or run it in one command (no prompt):

```powershell
py -3 .\directory_org.py "C:\path\to\your\folder"
```

3. The Logic (How you thought):

• Why did you choose this approach?
I used `pathlib` to scan the directory and simple extension checks (`.suffix.lower()`) to route files into the right subfolder. `shutil.move` handles both moving and renaming in one operation, keeping the script small and reliable.

• What was the hardest bug you faced, and how did you fix it?
Avoiding accidental overwrites when two files end up with the same timestamped name. I fixed it by adding `ensure_unique_path()`, which appends `_1`, `_2`, etc. if the destination filename already exists.

4. Future Improvements: If you had 2 more days, what would you add?
I’d add recursive organization (`--recursive`), a `--dry-run` mode to preview changes, and a configurable rules file (JSON/YAML) so new categories (PDFs, zips, videos) can be added without changing code.