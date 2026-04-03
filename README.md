# 🚀 Paytm Reconcile AI (Voice-Based Billing & Payment System)

A full-stack AI-powered system that converts **voice input into structured bills**, generates **UPI QR codes**, and performs **automatic payment reconciliation**.

---

## 🧠 Project Overview

Paytm Reconcile AI is designed to simulate a **real-world retail billing + payment flow** using voice commands.

👉 Speak your order → system generates bill → QR → payment → auto-match.

---

## 🔥 Key Features

* 🎤 **Real-Time Voice Billing**

  * Uses browser speech recognition (no file upload needed)
  * Converts speech → structured bill instantly

* 🧾 **Smart Bill Generation**

  * Extracts items and total using NLP parsing
  * Supports mixed Hindi-English inputs (e.g., *“ek chai 2 samosa”*)

* 🔳 **UPI QR Code Generation**

  * Generates scannable QR for payment
  * Embeds item metadata in QR

* 💳 **Payment Matching Engine**

  * Matches payments to bills using:

    * Amount similarity
    * Timestamp proximity
    * Heuristic scoring logic

* 📊 **Bill Status Tracking**

  * Check if bill is **pending / paid / matched**

---

## 🏗️ Architecture

```text
Frontend (HTML/CSS/JS)
        ↓
FastAPI Backend (API Layer)
        ↓
Service Layer
(Speech → Parser → Billing → QR → Matching)
        ↓
SQLite Database
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

### Frontend

* HTML, CSS, JavaScript
* Web Speech API (Live Voice Input)

### Utilities

* QRCode (UPI generation)
* Regex-based NLP parser

---

## 📁 Project Structure

```text
paytm-reconcile-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── deps.py
│   │
│   ├── services/
│   │   ├── speech.py
│   │   ├── parser.py
│   │   ├── billing.py
│   │   ├── qr.py
│   │   ├── payment.py
│   │   ├── matching.py
│   │   └── reconcile.py
│   │
│   ├── routes/
│   │   ├── voice.py
│   │   ├── bill.py
│   │   ├── payment.py
│   │   └── status.py
│
├── frontend/
│   ├── index.html
│   ├── voice.html
│   ├── bill.html
│   ├── status.html
│   ├── style.css
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/REDDIDIVAKARSAI/paytm_hack.git
cd paytm_hack
```

---

### 2️⃣ Setup Backend

```bash
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

### 3️⃣ Run Backend

```bash
uvicorn app.main:app --reload
```

👉 API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 4️⃣ Run Frontend

```bash
cd frontend
python -m http.server 5500
```

👉 Open:

```
http://localhost:5500
```

---

## 🧪 How to Use

### 🎤 Voice Billing Flow

1. Go to **Voice Billing**
2. Click **Start**
3. Speak:

   ```
   2 chai ek samosa 50
   ```
4. Click **Stop**
5. System will:

   * Parse speech
   * Create bill
   * Generate QR

---

### 📝 Manual Billing Flow

1. Enter items + total
2. Generate bill
3. QR appears instantly

---

### 📊 Status Check

1. Enter Bill ID
2. Check whether:

   * Pending
   * Paid

---

## ⚙️ Core Logic (Matching Engine)

The system uses a scoring mechanism:

* Exact amount match → +70
* Small difference → +50
* Time proximity → +20
* Single candidate → +10

👉 Ensures reliable reconciliation of payments.

---

## ⚠️ Limitations

* Uses rule-based NLP (not ML-based)
* No real UPI payment confirmation (simulation only)
* Speech recognition depends on browser (Chrome recommended)

---

## 🚀 Future Improvements

* 🤖 LLM-based NLP (Bedrock / OpenAI)
* 🔔 Webhook-based payment confirmation
* ☁️ Cloud deployment (AWS / Render)
* 📱 Mobile app version
* 📊 Admin dashboard

---

## 🎯 Use Cases

* Small retail shops
* Street vendors
* Voice-first POS systems
* Smart billing assistants

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
