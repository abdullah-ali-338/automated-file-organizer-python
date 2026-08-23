# Automated File Organizer & Audit Logger (Python)

A deterministic, lightweight Python automation script designed to clean cluttered file systems. It automatically scans directories, classifies files across 7 distinct categories by extension, and maintains an execution audit log.

---

## Features

* **Rule-Based Classification:** Categorizes files into Documents, Images, Code, Videos, Audio, Archives, and Executables using extension-based classification.
* **Audit Logging:** Uses Python's `logging` module to track moved files, timestamps, and caught exceptions in `organizer_audit.log`.
* **Fault-Tolerant Execution:** Handles invalid directory paths, duplicate file name collisions, and permission exceptions without crashing.
* **Cross-Platform:** Built exclusively with Python standard libraries (`os`, `shutil`, `logging`), requiring zero external dependencies.

---

## Tech Stack & Concepts

* **Language:** `Python`
* **Programming Style:** `Procedural / Modular`
* **Standard Libraries:** `os`, `shutil`, `logging`
* **Core Concepts:**

  * File System Automation
  * Directory Traversal
  * File Classification
  * File Operations
  * Exception Handling
  * Logging
  * Path Validation
  * Duplicate File Handling

---

## Project Structure

```text
├── file_organizer.py       # Main automation and classification logic
├── organizer_audit.log     # Execution and error audit log
└── README.md               # Documentation
```

---

## Getting Started

### Prerequisites

Python 3.8 or above installed on your system.

### Usage

#### 1. Clone the Repository

```bash
git clone https://github.com/abdullah-ali-338/automated-file-organizer-python.git
cd automated-file-organizer-python
```

#### 2. Run the Script

```bash
python file_organizer.py
```

#### 3. Select the Target Directory

Provide the path of the directory you want to organize.

Press `Enter` to organize the current directory.

```text
Enter directory path:
```

---

## File Classification

The organizer sorts files into 7 predefined categories.

```text
Documents
Images
Code
Videos
Audio
Archives
Executables
```

Files are classified according to their extensions.

Example:

```text
report.pdf       -> Documents
photo.jpg        -> Images
main.cpp         -> Code
movie.mp4        -> Videos
song.mp3         -> Audio
backup.zip       -> Archives
program.exe      -> Executables
```

Files with unsupported extensions are handled separately without interrupting the execution process.

---

## Automation Workflow

The program follows a deterministic workflow:

```text
Target Directory
       |
       v
Scan Files
       |
       v
Read File Extension
       |
       v
Classify File
       |
       v
Create Category Folder
       |
       v
Move File
       |
       v
Write Audit Log
```

Each file is processed individually, allowing errors to be logged while the remaining files continue processing.

---

## Audit Logging

Every execution generates activity records inside:

```text
organizer_audit.log
```

The logging system records:

* File operations
* Destination categories
* Execution timestamps
* Exceptions
* Permission errors
* File conflicts

Example:

```text
2026-08-23 14:02:11 | INFO | Moved report.pdf -> Documents
2026-08-23 14:02:11 | INFO | Moved main.cpp -> Code
2026-08-23 14:02:12 | ERROR | Permission denied: protected.txt
```

This provides a persistent record of the organizer's actions.

---

## Error Handling

The program handles common file-system problems without terminating the complete operation.

Supported cases include:

```text
Invalid directory path
Permission denied
Duplicate file names
Unsupported file extensions
File operation errors
```

When an exception occurs, the error is recorded in the audit log and processing continues with the remaining files.

---

## Duplicate File Handling

If a destination already contains a file with the same name, the organizer prevents accidental overwriting.

Example:

```text
report.pdf
report_1.pdf
report_2.pdf
```

This preserves existing files while allowing the organizer to complete the operation.

---

## Example

Before execution:

```text
Downloads/
├── report.pdf
├── photo.jpg
├── main.py
├── movie.mp4
├── song.mp3
├── backup.zip
└── setup.exe
```

After execution:

```text
Downloads/
├── Documents/
│   └── report.pdf
├── Images/
│   └── photo.jpg
├── Code/
│   └── main.py
├── Videos/
│   └── movie.mp4
├── Audio/
│   └── song.mp3
├── Archives/
│   └── backup.zip
└── Executables/
    └── setup.exe
```

---

## Performance

The organizer processes files through a single directory scan and performs classification using extension lookups.

The approach keeps the implementation lightweight and avoids external dependencies.

---

## Key Learning Outcomes

This project demonstrates practical Python programming through:

* File system automation
* Directory traversal
* Extension-based classification
* File movement with `shutil`
* Path operations with `os`
* Exception handling
* Structured logging
* Cross-platform scripting
* Persistent execution auditing

---

## Controls

| Input          | Action                     |
| -------------- | -------------------------- |
| Directory path | Select target directory    |
| `Enter`        | Organize current directory |
| `Ctrl+C`       | Stop execution             |

---

## License

This project is intended for educational and academic purposes.
