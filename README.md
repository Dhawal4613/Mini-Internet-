# Mini-Internet
This is a mini Internet which is used to use google and YouTube in terminal. I am new to git hub so please help me to learn new things and please teach me new things.

---

# 🔍 Python Web Search Launcher

A simple Python program that allows users to search **Google** or **YouTube** directly from the terminal using the default web browser.

---

## 📌 Features

* Search Google from terminal
* Search YouTube from terminal
* Uses Python’s built-in `webbrowser` module
* Beginner-friendly and easy to understand
* Works on Windows, Linux, and Android (Pydroid3)

---

## 🧠 How It Works

1. The program shows two options:

   * `1` → Google Search
   * `2` → YouTube Search
2. User selects an option.
3. User enters a search query.
4. The default browser opens with the search results.
5. The program runs continuously until manually stopped.

---

## 🛠 Requirements

* Python 3.x
* Internet connection
* Any default web browser

*No external libraries required.*

---

## ▶️ How to Run

1. Save the code in a file, for example:

   ```
   web_search.py
   ```
2. Open terminal or command prompt.
3. Run the program:

   ```
   python web_search.py
   ```
4. Follow the on-screen instructions.

---

## 📄 Sample Output

```
1. Google
2. YouTube
Enter the choice (1 or 2): 1
Enter your query on Google: Python programming
Google is opened, Sir!!
```

---

## 📂 Code Used

```python
import webbrowser as wb

print("1. Google\n2. YouTube")

while True:
    choose = input("Enter the choice (1 or 2): ")

    if choose == '1':
        query_google = input("Enter your query on Google: ")
        google = wb.open(f'https://google.com/search?q={query_google}')

        if google:
            print("Google is opened, Sir!!")
        else:
            print("Google is not opened, might be there is some ERROR!!")

    elif choose == '2':
        query_youtube = input("Enter your query on YouTube: ")
        youtube = wb.open(f'https://youtube.com/search?q={query_youtube}')

        if youtube:
            print("YouTube is opened, Sir!!")
        else:
            print("YouTube is not opened, might be there is some ERROR!!")

    else:
        print("You entered wrong option. Choose from above option.")
```

---

## 🚀 Future Improvements

* Add exit option
* Support more platforms (Wikipedia, Bing, etc.)
* Add voice input
* GUI version using Tkinter or Kivy

---

## 👨‍💻 Author

**Dhawal Bansod**
Beginner Python Developer

---
