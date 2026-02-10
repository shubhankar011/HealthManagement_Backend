<div align="center">

# 🏥 HealthManagement Backend

### *AI-Powered Personal Health Tracking & Assistance System*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![AI](https://img.shields.io/badge/AI-Enabled-FF6F61?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/shubhankar011/HealthManagement_Backend)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**A comprehensive Python backend combining health metrics tracking, user authentication, BMI monitoring, and AI-powered health assistance**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-endpoints) • [AI Chatbot](#-ai-health-assistant) • [Contributing](#-contributing)

---

</div>

## 🎯 Overview

HealthManagement Backend is an intelligent health tracking system built with Python and Flask that combines traditional health metrics monitoring with AI-powered assistance. It provides secure user authentication, comprehensive BMI tracking with historical analysis, persistent data storage, and an integrated AI chatbot for health-related queries and guidance.

## ✨ Features

### 🤖 **AI Health Assistant** ⭐ NEW
- Intelligent chatbot for health-related queries
- Personalized health recommendations
- 24/7 virtual health guidance
- Context-aware responses based on user health data
- Natural language processing for symptom analysis

### 🔐 **Authentication System**
- Secure user registration and login
- Password encryption and hashing
- Session management with tokens
- User profile management
- Account security features

### 📊 **BMI Calculator & Tracker**
- Real-time BMI calculation
- Historical BMI logs with timestamps
- Health category classification (Underweight, Normal, Overweight, Obese)
- CSV-based log storage for persistent data
- Trend analysis and visualization support

### 💾 **Data Management**
- JSON-based user information utilities (`users_data.json`)
- CSV logging for health metrics and BMI history
- Efficient data retrieval and updates
- Scalable and modular architecture
- Data integrity validation

### 🛡️ **Security & Privacy**
- Input validation and sanitization
- Secure password handling with encryption
- Data integrity checks
- Protected endpoints with authentication
- HIPAA-compliant data handling practices

## 🏗️ System Architecture

```
HealthManagement_Backend/
│
├── ENV Folder           # Contains the modules that are necessary for this project
├── __pycache            # A cache folder
├── main.py              # Flask application entry point & routes
├── auth.py              # Authentication & authorization logic
├── BMI.py               # BMI calculation and logging system
├── manager.py           # Data management utilities & operations
├── AI_Assist.py           # AI chatbot integration & logic (NEW)
│
├── users_data.json      # User information utilities & profiles
├── info.csv             # Additional user metadata
└── bmi_logs.csv         # Historical BMI tracking data
```

## 🚀 Installation

### Prerequisites
```bash
Python 3.8 or higher
pip package manager
Flask 2.0+
```

### Quick Setup

1. **Clone the repository**
```bash
git clone https://github.com/shubhankar011/HealthManagement_Backend.git
cd HealthManagement_Backend
```

2. **Install dependencies**
```bash
pip install flask
pip install pandas              # For CSV operations
pip install bcrypt              # For password hashing
pip install python-dotenv       # For environment variables
pip install openai              # For AI chatbot (if using OpenAI)
# OR
pip install -r requirements.txt
```

3. **Configure environment variables**
```bash
# Create .env file
touch .env

# Add your API keys and configurations
echo "FLASK_SECRET_KEY=your_secret_key_here" >> .env
echo "AI_API_KEY=your_ai_api_key_here" >> .env
```

4. **Initialize the database**
```bash
python manager.py --init
```

5. **Run the application**
```bash
python main.py
```

The server will start on `http://localhost:5000`

## 💻 Usage

### User Registration
```python
POST /api/register
{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secure_password_123",
    "age": 28,
    "gender": "male"
}
```

### User Login
```python
POST /api/login
{
    "email": "john@example.com",
    "password": "secure_password_123"
}
```

### Calculate & Log BMI
```python
POST /api/calculate-bmi
Headers: { "Authorization": "Bearer <token>" }
{
    "weight": 70,    # in kg
    "height": 175    # in cm
}

Response:
{
    "bmi": 22.86,
    "category": "Normal",
    "message": "Your BMI is in the healthy range!",
    "timestamp": "2024-02-10T14:30:00"
}
```

### AI Health Assistant
```python
POST /api/chatbot
Headers: { "Authorization": "Bearer <token>" }
{
    "message": "I've been feeling tired lately and my BMI is 26. What should I do?",
    "user_id": "user_123"
}

Response:
{
    "response": "Based on your BMI of 26 (slightly overweight), fatigue could be related to...",
    "suggestions": [
        "Consider increasing physical activity",
        "Review your sleep schedule",
        "Consult with a healthcare provider for persistent fatigue"
    ]
}
```

### View BMI History
```python
GET /api/bmi-history?user_id=user_123&limit=10
Headers: { "Authorization": "Bearer <token>" }
```

## 📡 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/register` | Register new user | ❌ |
| `POST` | `/api/login` | User authentication | ❌ |
| `POST` | `/api/logout` | End user session | ✅ |
| `GET` | `/api/user-profile` | Get user information | ✅ |
| `PUT` | `/api/update-profile` | Update user details | ✅ |
| `POST` | `/api/calculate-bmi` | Calculate and log BMI | ✅ |
| `GET` | `/api/bmi-history` | Retrieve BMI logs | ✅ |
| `GET` | `/api/bmi-stats` | Get BMI statistics | ✅ |
| `POST` | `/api/chatbot` | AI health assistant | ✅ |
| `GET` | `/api/chatbot/history` | Chat conversation history | ✅ |

## 🤖 AI Health Assistant

The integrated AI chatbot provides intelligent health guidance and support:

### Capabilities
- **Symptom Analysis**: Describes symptoms and receives preliminary guidance
- **Health Tips**: Personalized recommendations based on user data
- **BMI Insights**: Context-aware advice considering current BMI and trends
- **Lifestyle Guidance**: Nutrition, exercise, and wellness suggestions
- **Medical Information**: General health information and FAQs

### How It Works
1. User sends a health-related query
2. System retrieves relevant user health data (BMI, history)
3. AI processes the query with context
4. Returns personalized, data-informed response
5. Conversation history is maintained for continuity

**Note**: The AI assistant provides general health information and guidance. Always consult healthcare professionals for medical advice and diagnosis.

## 🔧 Core Components

### `auth.py` - Authentication Module
Handles user registration, login, session management, and token-based authentication with bcrypt password hashing.

### `BMI.py` - BMI Calculator & Logger
Calculates BMI using the formula: `BMI = weight(kg) / (height(m))²`

**Health Categories:**
- **Underweight**: BMI < 18.5
- **Normal**: 18.5 ≤ BMI < 25
- **Overweight**: 25 ≤ BMI < 30
- **Obese**: BMI ≥ 30

### `manager.py` - Data Management Layer
Manages CRUD operations for user data, health metrics, and data persistence across JSON and CSV storage.

### `AI_Assist.py` - AI Integration Module ⭐ NEW
Integrates AI capabilities for natural language health assistance, context-aware responses, and conversation management.

## 🎨 Data Models

### User Information (`users_data.json`)
```json
{
    "user_id": "usr_1234567890",
    "username": "johndoe",
    "email": "john@example.com",
    "age": 28,
    "gender": "male",
    "created_at": "2024-01-15T10:30:00Z",
    "last_login": "2024-02-10T14:20:00Z",
    "profile": {
        "height": 175,
        "activity_level": "moderate"
    }
}
```

### BMI Logs (`bmi_logs.csv`)
```csv
log_id,user_id,date,weight,height,bmi,category,notes
1,usr_1234567890,2024-02-10,70,175,22.86,Normal,Feeling great
2,usr_1234567890,2024-02-03,72,175,23.51,Normal,Post-holiday
```

### Additional User Data (`info.csv`)
```csv
user_id,full_name,phone,emergency_contact,medical_conditions
usr_1234567890,John Doe,+1234567890,Jane Doe,None
```

## 🤝 Contributing

This is a forked repository. Original project by [Pratyush Kush](https://github.com/pratyush789245/HealthManagement_Backend).

### Contributors
- **Idea & Author:** [Pratyush Kush](https://github.com/pratyush789245) - Initial backend architecture
- **Maintainer & Coder:** [Shubhankar Kumar](https://github.com/shubhankar011) - AI chatbot, improved security, expanded features

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewHealthFeature`)
3. Commit your changes (`git commit -m 'Add health metric tracking'`)
4. Push to the branch (`git push origin feature/NewHealthFeature`)
5. Open a Pull Request with detailed description

### Development Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code quality
flake8 .
black .
```

## 🛣️ Roadmap

### Version 2.0 (Planned)
- [ ] Enhanced AI chatbot with medical knowledge base
- [ ] Voice-based health assistant
- [ ] Integration with wearable devices (Fitbit, Apple Watch)
- [ ] Advanced health analytics dashboard
- [ ] Mobile app (React Native)

### Version 1.5 (In Progress)
- [x] AI chatbot integration
- [ ] Multi-language support
- [ ] Export health reports (PDF)
- [ ] Appointment scheduling system

### Future Enhancements
- [ ] REST API documentation (Swagger/OpenAPI)
- [ ] JWT token refresh mechanism
- [ ] Additional health metrics (Blood Pressure, Heart Rate, Sleep)
- [ ] PostgreSQL/MongoDB database migration
- [ ] Docker containerization
- [ ] Comprehensive unit and integration tests
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] GDPR compliance features
- [ ] React/Vue.js frontend integration

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test suite
pytest tests/test_auth.py

# Run with coverage
pytest --cov=. tests/
```

## 📊 Performance

- Response time: < 200ms for most endpoints
- AI chatbot latency: 1-3 seconds (depending on query complexity)
- Supports concurrent users: 100+ (with proper deployment)
- Database query optimization: Indexed JSON and CSV operations

## 🔒 Security Features

- Password hashing with bcrypt (cost factor: 12)
- JWT token-based authentication
- CORS protection
- Input validation and sanitization
- SQL injection prevention
- Rate limiting on API endpoints
- Secure session management

## 📚 Documentation

For detailed API documentation, visit `/api/docs` when the server is running.

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact & Support

### Maintainer: Shubhankar Kumar
- 🐙 GitHub: [@shubhankar011](https://github.com/shubhankar011)
- 📧 Email: shubhankarpandey2007@outlook.com
- 🔗 LinkedIn: [Shubhankar Kumar](https://www.linkedin.com/in/shubhankar-kumar-964b74344/)
- 📱 Instagram: [@shubhankar_7002](https://www.instagram.com/shubhankar_7002/)

### Original Author: Pratyush Kush
- 🐙 GitHub: [@pratyush789245](https://github.com/pratyush789245)

### Getting Help
- 🐛 Report bugs via [GitHub Issues](https://github.com/shubhankar011/HealthManagement_Backend/issues)
- 💬 Ask questions in [Discussions](https://github.com/shubhankar011/HealthManagement_Backend/discussions)
- 📖 Read the [Wiki](https://github.com/shubhankar011/HealthManagement_Backend/wiki) for guides

---

<div align="center">

**Built with ❤️ for better health management**

*Empowering individuals to take control of their health through technology*

⭐ Star this repo if you find it helpful! | 🍴 Fork it to contribute

[![GitHub stars](https://img.shields.io/github/stars/shubhankar011/HealthManagement_Backend?style=social)](https://github.com/shubhankar011/HealthManagement_Backend)
[![GitHub forks](https://img.shields.io/github/forks/shubhankar011/HealthManagement_Backend?style=social)](https://github.com/shubhankar011/HealthManagement_Backend/fork)

</div>
