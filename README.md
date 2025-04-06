# Password_Checker

This is a simple web application built using **Flask** that allows users to check the strength of a password based on several criteria. The app provides instant feedback on whether the entered password is strong or weak, and if weak, offers specific suggestions for improvement.

## 🚀 Features

- Checks for:
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character
- User-friendly UI with real-time feedback
- Error message for empty passwords
- Styled using responsive HTML/CSS

## 🛠️ Tech Stack

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**

## 📁 Project Structure

. ├── app.py # Main Flask application ├── templates │ └── index.html # Frontend HTML template


## 🧪 Password Strength Criteria

A password is considered **strong** if it contains:

- ✅ At least 8 characters  
- ✅ One uppercase letter  
- ✅ One lowercase letter  
- ✅ One digit  
- ✅ One special character

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sainathislavath/Password_Checker.git
cd Password_Checker

### Install Dependencies

pip install flask

### Run the file

python app.py

### Open in Browser

http://127.0.0.1:5000