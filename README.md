# 🏷️ KOE Inventory Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange)
![QR Code](https://img.shields.io/badge/QR--Code-8.2-yellow)

A modern QR-code based asset tracking system that allows quick access to equipment information by scanning QR codes with mobile devices.

## ✨ Core Features

### 🏷️ QR Code Management
- **Dynamic QR Generation** - Automatic QR code creation for all assets
- **Mobile-Friendly Links** - QR codes direct to responsive web pages
- **Batch QR Creation** - Generate multiple QR codes at once

### 🔐 Asset Tracking
- **Real-time Asset Information** - Instant access to equipment details
- **Assignment Tracking** - Monitor who has which equipment
- **Status Monitoring** - Active, inactive, and maintenance statuses

### 🗄️ Data Management
- **MySQL Database** - Reliable data storage for assets and employees
- **Environment Variables** - Secure configuration management
- **Data Integrity** - Foreign key relationships and constraints

### 📱 User Experience
- **Responsive Design** - Works perfectly on desktop and mobile
- **Instant Access** - Scan QR code → See asset info in seconds
- **Clean Interface** - Professional and easy-to-read asset cards

### ⚙️ Admin Features
- **Asset Management** - Add, edit, and track equipment
- **Employee Assignment** - Assign assets to team members
- **Category Organization** - Categorize assets by type and department

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MySQL Server

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/mervetas/koe-inventory.git
cd koe-inventory
```
2. **Backend Setup:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```
3. **Configure Environment:**
```bash
# Create .env file from example
cp .env.example .env

# Edit .env file with your settings:
BASE_URL=http://your_local_ip:5000/asset/
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=koe_inventory
DB_PORT=3306
```
4. **Database Setup:**
```bash
# Initialize database with sample data
python populate_mysql.py
```
5. **Generate QR Codes:**
```bash
# Create QR codes for all assets
python qr_generator.py
```
6. **Run Application:**
```bash
# Start Flask development server
python app.py
```
7. **Access the System:**
Web Interface: http://localhost:5000/asset/asset-1
Mobile Access: http://your_local_ip:5000/asset/asset-1
Health Check: http://localhost:5000/health

## 📁 Project Structure
```text
koe-inventory/
├── app.py                    # Main Flask application
├── qr_generator.py           # QR code generation script
├── populate_mysql.py         # Database initialization
├── requirements.txt          # Python dependencies
├── README.md  
├── .env.example              # Environment configuration template
├── .gitignore                # Git ignore rules
├── LICENSE                   # MIT License
│
├── templates/                # HTML templates
│   └── asset.html           # Asset information page
│
└── qrs/                     # Generated QR codes (auto-created)
    ├── KOE-001.png
    ├── KOE-002.png
    └── ...
    
```
## 🏗️ Database Schema
### Assets Table
asset_id, tag, name, type, serial, status, assigned_to

### Employees Table
employee_id, full_name, department, email

## 🔧 Configuration
### Environment Variables
BASE_URL - Base URL for QR code links
DB_HOST - MySQL database host
DB_USER - MySQL username
DB_PASS - MySQL password
DB_NAME - Database name
DB_PORT - MySQL port
### Network Setup
For mobile access, ensure:
Phone and computer are on same WiFi network
Firewall allows port 5000
Correct IP address in BASE_URL

## 🎯 Usage Examples
Scan QR Code - Use phone camera to scan asset QR
View Information - See asset details, assigned person, status
Manage Assets - Update assignments and status via database

## 👨‍💻 About the Project
This project was developed to solve asset tracking challenges by providing instant access to equipment information through QR codes. The system eliminates manual lookups and provides real-time asset status to authorized personnel.

## 📞 Contact
Merve Taş
GitHub: mervetas
Project Repository: https://github.com/mervetas/koe-inventory

## ⚠️ Usage Notice
This project is shared for learning and portfolio purposes. Unauthorized commercial use, redistribution, or claiming ownership of this code is strictly prohibited. If you find this useful, please provide proper credit to Merve Taş.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.