# 📁 Automated File Organizer & Audit Logger

![Language](https://img.shields.io/badge/Language-Python_3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Personal_Use-blue?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-Python_%7C_OS_%7C_Shutil-orange?style=for-the-badge)

A deterministic, lightweight Python automation script designed to clean cluttered file systems. It automatically scans directories, classifies files across 7 distinct categories by extension, and maintains an execution audit log.

🌐 **GitHub Repo:** [github.com/abdullah-ali-338/automated-file-organizer-python](https://github.com/abdullah-ali-338/automated-file-organizer-python)

---

## ✨ Features

- **Rule-Based Classification:** Categorizes files into Documents, Images, Code, Videos, Audio, Archives, and Executables using extension-based classification.
- **Audit Logging:** Uses Python's `logging` module to track moved files, timestamps, and caught exceptions in `organizer_audit.log`.
- **Fault-Tolerant Execution:** Handles invalid directory paths, duplicate file name collisions, and permission exceptions without crashing.
- **Cross-Platform Setup:** Built exclusively with Python standard libraries (`os`, `shutil`, `logging`), requiring zero external dependencies.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Programming Style:** Procedural / Modular
- **Standard Libraries:** `os`, `shutil`, `logging`
- **Core Concepts:** File System Automation, Directory Traversal, File Classification, File Operations, Exception Handling, Logging, Path Validation, Duplicate File Handling

---

## 📁 Repository Structure

```text
FileOrganizer/
├── file_organizer.py       # Main automation and classification logic
├── organizer_audit.log     # Execution and error audit log
└── README.md               # Documentation
