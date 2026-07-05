# 🤖 AI Leading Assistant

An **AI-powered Lead Management Assistant** built with **Django**, **HTML**, and **CSS** that helps users analyze and manage customer leads efficiently. By leveraging **Google's Gemini 2.5 Flash** model through the **Google AI Studio API**, the application intelligently evaluates reported problems and provides actionable insights.

---

## 📌 Features

* 🤖 AI-powered lead analysis using **Gemini 2.5 Flash**
* 📝 Automatically generates a concise summary of the reported problem
* 🚨 Assigns a priority level based on the issue's severity
* 💡 Suggests the next recommended action for the user
* 📋 Store and manage lead information
* 👀 View AI-generated insights for each lead
* 🎨 Clean and user-friendly interface

---

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3

### AI Integration

* Google AI Studio
* Google GenAI Python SDK
* Gemini 2.5 Flash

### Database

* SQLite3

---

## ⚙️ How It Works

1. A user submits a lead or describes a problem.
2. The application sends the information to **Gemini 2.5 Flash** using the **Google AI Studio API**.
3. The AI analyzes the input and returns:

   * 📌 Problem Summary
   * 🚨 Priority Level
   * 💡 Recommended Next Action
4. The generated insights are displayed to the user and can be stored for future reference.

---

## 📂 Project Structure

```text
AI-Leading-Assistant/
│── ai_automation/
│── automation_ai/
│── templates/
│── static/
│── manage.py
│── requirements.txt
│── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Prit0911/AILeadingAssistant.git
```

### 2. Navigate to the project directory

```bash
cd AILeadingAssistant
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Create a `.env` file in the project root and add your Google AI Studio API key:

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key
```

> **Important:** Never commit your `.env` file or API key to GitHub. Add `.env` to your `.gitignore` file.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open your browser

Visit:

```text
http://127.0.0.1:8000/
```

---

## 🧠 AI Output

For every submitted lead, the AI generates:

* **Problem Summary** – A concise overview of the issue.
* **Priority Level** – High, Medium, or Low based on the urgency.
* **Recommended Next Action** – Practical suggestions for handling the lead or resolving the issue.

---

## 🚀 Future Improvements

* User authentication and role-based access
* Lead history and analytics dashboard
* Search and filter functionality
* Export reports as PDF or Excel
* Email notifications
* Integration with CRM platforms
* Support for multiple AI models
* Conversation history for each lead
* Cloud database (PostgreSQL)
* Docker deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is intended for learning, experimentation, and portfolio purposes. Feel free to use, modify, and improve it.

---

## 👨‍💻 Author : Prit Gajjar

Developed with ❤️ using **Django**, **Google AI Studio**, and **Gemini 2.5 Flash**.
