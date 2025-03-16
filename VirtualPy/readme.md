# Setting Up and Using a Virtual Environment in Python

## 1. Install `virtualenv`
To install `virtualenv`, run:
```sh
pip3 install virtualenv
```

## 2. Create a Virtual Environment
To create a virtual environment named `.venv`, use:
```sh
python3 -m venv .venv
```

## 3. Activate the Virtual Environment
### **For macOS/Linux:**
```sh
source .venv/bin/activate
```

### **For Windows (Command Prompt):**
```sh
.venv\Scripts\activate
```

### **For Windows (PowerShell):**
```sh
.\.venv\Scripts\Activate
```

## 4. Generate `requirements.txt`
To save installed packages to `requirements.txt`, use:
```sh
pip list > requirements.txt  # Option 1
pip freeze > requirements.txt  # Option 2 (Recommended)
```

## 5. Install Dependencies from `requirements.txt`
To install packages from `requirements.txt`, run:
```sh
pip install -r requirements.txt
```

---
These steps help you set up and manage a virtual environment efficiently in Python. 🚀

