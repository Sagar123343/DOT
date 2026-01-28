from __future__ import annotations

import sys
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class Rules:
    # Configuration for which extensions go into which subfolders.
    text_extensions: tuple[str, ...] = (".txt",)
    image_extensions: tuple[str, ...] = (".png", ".jpg")
    text_folder_name: str = "Text_Files"
    images_folder_name: str = "Images"


# Return a filename-safe date stamp in DDMMYYYY format.
def timestamp_ddmmyyyy() -> str:
    return datetime.now().strftime("%d%m%Y")


# If a path already exists, add _1, _2, ... to avoid overwriting.
def ensure_unique_path(path: Path) -> Path:
    if not path.exists():
        return path

    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


# Build the final destination path (folder + timestamped filename).
def build_destination_path(file_path: Path, destination_dir: Path) -> Path:
    new_name = f"{file_path.stem}_{timestamp_ddmmyyyy()}{file_path.suffix.lower()}"
    return ensure_unique_path(destination_dir / new_name)


# Move a file into a destination folder and rename it with a timestamp.
def move_and_rename(file_path: Path, destination_dir: Path) -> Path:
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination_path = build_destination_path(file_path, destination_dir)
    return Path(shutil.move(str(file_path), str(destination_path)))


# Scan a folder and organize files into Text_Files/ and Images/.
def organize_folder(folder: Path, rules: Rules = Rules()) -> dict[str, int]:
    if not folder.is_dir():
        raise FileNotFoundError(f"Folder not found: {folder}")

    text_dir = folder / rules.text_folder_name
    images_dir = folder / rules.images_folder_name

    moved_text = 0
    moved_images = 0

    for item in folder.iterdir():
        if not item.is_file():
            continue

        suffix = item.suffix.lower()
        if suffix in rules.text_extensions:
            move_and_rename(item, text_dir)
            moved_text += 1
        elif suffix in rules.image_extensions:
            move_and_rename(item, images_dir)
            moved_images += 1

    return {"text": moved_text, "images": moved_images}


def main() -> int:
    folder_input = " ".join(sys.argv[1:]).strip().strip('"') if len(sys.argv) > 1 else ""
    if not folder_input:
        folder_input = input("Enter Folder Path: ").strip().strip('"')

    if not folder_input:
        print("No folder path provided. Exiting.")
        return 1

    folder = Path(folder_input).resolve()

    counts = organize_folder(folder)
    print(f"Organized: {folder}")
    print(f"  Moved text files:  {counts['text']}")
    print(f"  Moved image files: {counts['images']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())