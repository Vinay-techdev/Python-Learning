# 📘 Chapter 08 – File I/O (Input/Output)

Files allow Python programs to store data permanently on a storage device, unlike RAM, which is volatile and loses all data when the program ends.

---

## 1. What is a File?

- A file is data stored on a storage device.
- Python can read from or write to a file.
- RAM → volatile (data lost after program ends)
- HDD / SSD → non-volatile (data persists forever)

### Types of Files

- Text files – .txt, .csv, .log, etc.
- Binary files – .jpg, .png, .exe, etc.

---

## 2. File Operations

# Opening a File
```python
file = open("example.txt", "r")  # open file in read mode
```

# Reading from a File
```python
content = file.read()        # read entire file
line = file.readline()       # read one line at a time
lines = file.readlines()     # read all lines as list
```

# Writing to a File
```python
file = open("example.txt", "w")  # write mode
file.write("Hello, Python!\n")
file.writelines(["Line 1\n", "Line 2\n"])
```

# Closing a File
```python
file.close()   # always close after operation
```
---

# 3. Modes of Opening a File


| Mode | Description                        |
| ---- | ---------------------------------- |
| `r`  | Read (default)                     |
| `w`  | Write (creates file or overwrites) |
| `a`  | Append (adds to existing file)     |
| `+`  | Read & Write                       |
| `rb` | Read Binary                        |
| `rt` | Read Text (default)                |


---

# 4. Using with Statement

- Automatically handles closing the file, no need for file.close().

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# file automatically closed here
```

---

# 🏋️ Practice Set – File I/O

- Q1. Create a text file and write content
- Q2. Read the entire content of a file
- Q3. Read all lines into a list
- Q4. Append new content to a file
- Q5. Copy content from one file to another
- Q6. Count number of lines in a file

# ✅ Key Takeaways

- Files are used to store data permanently.
- Always choose the correct mode (r, w, a, etc.) depending on the operation.
- Use with statement to avoid forgetting to close files.