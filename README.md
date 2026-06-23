# 🏥 MediBot — AI Health Assistant

> An intelligent health chatbot powered by **Groq API** and **Llama 3.1** for instant medical guidance, symptom analysis, and wellness support.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-green.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-red.svg)
![Status](https://img.shields.io/badge/Status-Live-brightgreen.svg)

**[🌐 Try Live](https://dr-med-ten.vercel.app)** | **[📚 Documentation](#-documentation)** | **[🚀 Quick Start](#-quick-start)**

---

## 📋 Overview

**MediBot** is a production-ready AI health assistant designed to provide accurate, safe, and compassionate health information. Whether you need symptom analysis, medication details, nutrition guidance, or wellness tips — MediBot delivers instant, intelligent responses powered by advanced AI.

### 🎯 Perfect For:
- 👨‍⚕️ Healthcare students and professionals
- 👥 General users seeking health information
- 🏥 Clinics and wellness centers
- 📱 Mobile-first healthcare experiences

---

## ✨ Key Features

### 🤖 **Intelligent Chat Engine**
- Real-time conversation with Llama 3.1 8B model
- Context-aware responses with conversation history
- Multiple chat modes: General, Symptoms, Medications
- Smooth typing indicators and streaming responses

### 🛠️ **Comprehensive Health Tools**
- **BMI Calculator** — Calculate and track body mass index
- **Symptom Checker** — Analyze symptoms with AI
- **Quick Questions** — Pre-curated common health queries
- **Daily Health Targets** — Steps, water, sleep, calories tracker
- **Emergency Numbers** — Quick access to critical contacts (Pakistan)

### 🎨 **Premium User Experience**
- Modern glassmorphism design with blur effects
- Dark medical theme (optimized for eye comfort)
- Fully responsive (desktop, tablet, mobile)
- Smooth animations and micro-interactions
- Fast load times and optimized performance

### 🔒 **Safety & Compliance**
- Medical disclaimer on every interaction
- Content filtering for harmful queries
- Secure API key management
- HIPAA-aware design principles

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Backend** | Flask 3.0.3 (Python) |
| **AI/LLM** | Llama 3.1 8B via Groq API |
| **Styling** | Custom CSS + Design Tokens |
| **Typography** | Clash Display, Satoshi (Google Fonts) |
| **Deployment** | Vercel (Serverless) |
| **Version Control** | Git + GitHub |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Git
- Free Groq API Key ([Get one here](https://console.groq.com))

### Local Development

1. **Clone Repository**
```bash
git clone https://github.com/Nauman804/DR-MED.git
cd DR-MED
```

2. **Create Virtual Environment**
```bash
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Environment Variables**
Create `.env` file in root:
```env
GROQ_API_KEY=sk-proj-your-api-key-here
```

5. **Run Development Server**
```bash
python app.py
```

Access at: **`http://localhost:5000`**

---

## 📚 Documentation

### Project Structure
```
DR-MED/
├── app.py                 # Flask application & API routes
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (gitignored)
├── .gitignore             # Git ignore configuration
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   ├── app.js             # Frontend logic & API calls
│   └── style.css          # Styling & responsive design
└── README.md              # This file
```

### API Endpoints

#### `POST /chat`
Send a health-related message and receive AI response.

**Request:**
```json
{
  "message": "What are symptoms of flu?",
  "history": [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"}
  ]
}
```

**Response:**
```json
{
  "reply": "Flu symptoms typically include...",
  "safe_flag": false
}
```

---

## 🌐 Live Deployment

### Vercel
MediBot is deployed on Vercel for production use.

**Live URL:** [https://dr-med-ten.vercel.app](https://dr-med-ten.vercel.app)

**Deployment Configuration:**
- Auto-deploy on GitHub push
- Environment variables configured in Vercel dashboard
- SSL/TLS enabled
- CDN for global distribution

### Deploy Your Own
1. Fork this repository
2. Create Vercel account ([vercel.com](https://vercel.com))
3. Connect GitHub repository
4. Add `GROQ_API_KEY` in environment variables
5. Deploy (automatic on push)

---

## 💡 Usage Guide

### Chat Modes
- **General** — Ask any health-related question
- **Symptoms** — Describe symptoms for AI analysis
- **Medications** — Get dosage and side effects information

### Quick Tools

**BMI Calculator:**
1. Enter weight (kg) and height (cm)
2. Click "Calculate BMI"
3. View category (Underweight, Normal, Overweight, Obese)

**Symptom Checker:**
1. Select symptoms from the right panel
2. Click "Ask MediBot"
3. Get AI-powered symptom analysis

**Emergency Numbers (Pakistan):**
- Rescue: 1122
- Ambulance: 115
- Umang Helpline: 0311-7786264
- Edhi Foundation: 115

---

## 🔧 Configuration

### Groq API Setup

Get your free API key:
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up (free account)
3. Generate API key
4. Add to `.env` file

**Free Tier Limits:**
- 30 requests/minute
- 500K tokens/month
- No credit card required

---

## 📊 Performance & Analytics

- **Load Time:** < 2 seconds
- **API Response:** 1-3 seconds (Groq)
- **Mobile Optimization:** 100% responsive
- **Browser Support:** Chrome, Firefox, Safari, Edge

---

## 🐛 Known Limitations

⚠️ **Important Notes:**
- Medical advice is **informational only** — always consult a licensed doctor
- Chat history stored **locally** (clears on page refresh)
- Maximum **600 characters** per message
- Voice input requires browser support (Chrome, Edge)
- Not suitable for emergency medical situations

---

## 🔐 Security & Privacy

✅ **Safety Measures:**
- No user data stored on servers
- API keys never logged
- Conversation history in browser only
- HTTPS/SSL enabled
- Content filtering for harmful queries
- Medical disclaimer on every interaction

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit changes:** `git commit -m "Add amazing feature"`
4. **Push to branch:** `git push origin feature/amazing-feature`
5. **Open Pull Request**

---

## 📝 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Creator

**Nauman Gokboru**

- 🎓 BS Artificial Intelligence | Superior University, Lahore
- 💼 Full Stack AI Developer
- 🔗 GitHub: [@Nauman804](https://github.com/Nauman804)

---

## 📧 Support & Feedback

- Open [GitHub Issues](https://github.com/Nauman804/DR-MED/issues) for bug reports
- Start [Discussions](https://github.com/Nauman804/DR-MED/discussions) for feature requests
- Contact via GitHub for questions

---

⭐ **If you found MediBot helpful, please star this repository!** ⭐

---

*Made with ❤️ by Nauman Gokboru*  
*Last Updated: June 2026*