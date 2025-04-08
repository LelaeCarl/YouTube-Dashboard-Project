# 🎥 YouTube Video Tracker & Analytics Dashboard

A high-performance web application that allows users to search YouTube videos by keyword or channel ID, 
store the metadata in a MySQL database, and visualize video analytics in an elegant, dashboard-style interface.

---

## ✨ Features

- 🔍 **Search Videos** via YouTube Data API v3 (by keyword or channel ID)
- 🧠 **Store Metadata** including views, likes, tags, and publish dates
- 📊 **Visual Analytics** using Chart.js (top views, tags, etc.)
- 💅 **Modern UI** with smooth animations and a YouTube-inspired design
- 🔒 Secure API key handling and config management
- 📁 Organized, scalable Flask application structure

---

## 📸 UI Preview
<img width="960" alt="image" src="https://github.com/user-attachments/assets/47898953-bbdd-4713-9752-6a060583350b" />
<img width="947" alt="image" src="https://github.com/user-attachments/assets/5ca1d17e-203f-45d2-a329-9caa20ae5521" />
<img width="731" alt="image" src="https://github.com/user-attachments/assets/c7031679-329a-440d-b7c9-cc47c8c98a47" />





---

## 🛠️ Built With

| Stack       | Description                                      |
|-------------|--------------------------------------------------|
| **Flask**   | Backend web framework                            |
| **MySQL**   | Relational database for video metadata           |
| **SQLAlchemy** | ORM for database interaction                 |
| **Chart.js**| Beautiful data visualizations                    |
| **Bootstrap 5** | Responsive front-end design framework       |
| **Inter / Roboto** | Sleek and readable typography            |

---

## 🧱 Project Structure

youtube_dashboard_project/ ├── app/ │ ├── init.py │ ├── models.py │ ├── routes.py │ ├── youtube_api.py │ ├── templates/ │ │ ├── base.html │ │ ├── index.html │ │ ├── channel.html │ │ └── analytics.html │ └── static/ │ ├── css/style.css │ └── js/scripts.js ├── config.py ├── run.py ├── init_db.py ├── requirements.txt └── README.md



---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- MySQL Server
- A valid [YouTube Data API v3 key](https://console.developers.google.com/)

---

### 🐍 Installation

```bash
git clone https://github.com/yourusername/youtube-dashboard.git
cd youtube-dashboard
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
