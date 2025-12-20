# 🔍 AssetMap

**AssetMap** is a lightweight code analysis tool designed to scan a project and list all assets referenced in the source code.  
It helps developers quickly understand dependencies, resource usage, and file relationships within a codebase.

---

## 🎯 Project Objective

The primary objectives of AssetMap are:

- 📁 Identify all assets referenced in a project  
- 🔗 Provide a clear mapping of links and dependencies  
- 🧩 Simplify maintenance and refactoring tasks  
- ⏱️ Reduce time spent on manual asset tracking  

---

## 📌 What AssetMap Detects

AssetMap currently detects:

- 🔗 Internal file links  
- 🖼️ Image references  
- 📜 Script and stylesheet references  
- 🧩 PHP `include` and `require` statements  
- 📂 Module and relative path dependencies  

---

## 💡 Why AssetMap?

In real-world projects:

- Assets are scattered across multiple files  
- Broken or unused assets are hard to detect  
- Manual inspection is slow and error-prone  

✅ **AssetMap automates this process** by extracting asset references and presenting them in a single, consolidated view.

---

## 🛠️ Tech Stack

- **Backend:** PHP  
- **Frontend:** HTML, CSS  
- **Server:** Apache (XAMPP)  
- **Version Control:** Git  

---

## 🗂️ Project Structure

assetmap/
│
├── modules/ # Feature-based modules
├── assets/ # Static assets
├── temp/ # Temporary / test files
├── config/ # Configuration files
└── README.md


---

## ⚙️ How It Works

1. 📄 Scans source files line by line  
2. 🔍 Detects asset references such as:
   - Links  
   - Images  
   - Includes  
3. 🧾 Records each asset with:
   - File name  
   - Line number  
   - Asset path  
4. 📊 Displays results in a readable format  

---

## ✅ Current Features

- 🔍 Asset extraction from source code  
- 📍 Line-level reference tracking  
- 🧹 Organized output for easy analysis  

---

## 🧪 Use Cases

- 🧠 Understanding legacy projects  
- 🛠️ Debugging missing or broken assets  
- 🚀 Preparing projects for deployment  
- 🧹 Code cleanup and refactoring  
- 📘 Learning project asset flow  

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
2.Move the project to your local server directory (for example, htdocs)
3.Start Apache using XAMPP
4.Open in browser

📝 Update Log

⚠️ Always append new updates below. Do not modify older entries.

🔹 Version 1.0

Initial release

Basic asset scanning implemented

🔹 Version 1.1

Improved detection accuracy

Added line-number tracking

🤝 Contribution

Contributions, suggestions, and improvements are welcome.
Feel free to fork the repository and submit a pull request.
