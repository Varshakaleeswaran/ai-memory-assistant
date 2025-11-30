# ai-memory-assistant
📘 AI Memory Assistant for Zoho Cliq

A smart productivity extension that helps users save, recall, and search important notes, tasks, and messages inside Zoho Cliq using simple AI-powered commands.

🚀 Features

/remember – Save important messages or notes

/recall – Retrieve memories instantly by keyword

/summarize – AI-generated summary of long messages

/forget – Delete a saved memory

Memory Widget – View all stored memories in one place

AI Smart Search – Semantic matching for better recall

Daily Summary – Optional daily recap of saved items

🧠 How It Works

User sends commands (example: /remember Meeting at 3 PM)

Cliq Bot forwards the request to the backend (Render)

Backend processes the memory

Result is sent back to the user in Cliq

Widget displays all stored memories neatly

🏗 Architecture
Zoho Cliq Extension
   ├─ Bot
   ├─ Commands
   ├─ Widget
   └─ Webhook
       ↓
Backend (FastAPI on Render)
   ├─ Receives commands
   ├─ Stores / searches memories
   └─ Sends responses back to Cliq

🛠 Tech Stack

Zoho Cliq Developer Platform – Bot, commands, widget

FastAPI – Backend server

Render (Free Tier) – Hosting

JSON Storage – Memory database

JavaScript – Cliq action handler

📡 API Endpoint

Webhook endpoint:

https://<your-render-service>.onrender.com/webhook

📦 Project Structure
backend/
  ├── app.py
  ├── requirements.txt
  └── render.yaml

cliq-extension/
  ├── extension.json
  ├── bot/
  ├── commands/
  ├── widget/
  └── handlers/

📥 Installation

Upload extension to Zoho Cliq Developer Console

Add bot, commands, widget

Set Execution Type: Webhook

Add your Render webhook URL

Install extension to your Cliq workspace

Start chatting with the bot

👤 Commands
/remember <text>
/recall <keyword>
/summarize <text>
/forget <memory>

🎯 Why This App

Solves a real productivity problem

No need to manually search messages

AI improves speed & accuracy

Lightweight and easy to use

Not available in existing marketplace → High uniqueness

💡 Author

Developed by Varsha Kaleeswaran for Zoho Cliqtrix 2025.
