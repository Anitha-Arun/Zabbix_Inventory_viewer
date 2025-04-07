
# 🚀 Zabbix Inventory Viewer

A sleek and user-friendly web interface built with **Flask** to display **Zabbix host inventory** grouped by host groups.  
Designed for teams to get clear visibility into device inventories — beautifully and efficiently.

---

## 🎯 Features

- 🔍 Filter devices by Zabbix Host Group
- 🧾 View cleanly formatted inventory fields
- 💼 Custom field names (e.g., `site_notes` becomes `Site Owner`)
- 🎨 Fully responsive and styled with a white background and Apexon branding
- 🖼 Logo (`Apexon.png`) smartly placed for a professional look

---

## 📌 Requirements

- 🐍 Python 3.7 or above
- 🧰 Flask and Requests (`pip install flask requests`)
- 🌐 Access to the Zabbix Server with API enabled
- ✅ Run this app on the **Zabbix server itself** (recommended) or a system with access to Zabbix API

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```--
git clone https://github.com/your-username/zabbix-inventory-viewer.git
cd zabbix-inventory-viewer
```

2. **Install Dependencies**

```--
pip install -r requirements.txt
```

Or manually:


pip install flask requests
```

3. **Configure your Zabbix API settings** inside `app.py`:

```python
ZABBIX_URL = 'http://<your-zabbix-server>/zabbix'
ZABBIX_USER = 'Admin'
ZABBIX_PASSWORD = '-'
```

4. **Run the App**


python app.py
```

Then open your browser and go to:

```
http://localhost:5000
```

---

## 📁 Project Structure

```
├── app.py                    # Flask application
├── templates/
│   └── zabbix.html           # Beautiful HTML page with filters and table
├── static/
│   └── images/
│       └── Apexon.png        # Logo used as branding
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🛠 Optional: Using `zabbix_sender`

If you plan to push data using Zabbix sender:

```--
sudo apt install zabbix-sender
```

Example command:

```--
zabbix_sender -z <ZABBIX_SERVER_IP> -s "<HOST_NAME>" -k custom.key -o "Some value"
```

---

## 🖼 UI Preview

![image](https://github.com/user-attachments/assets/46b23a94-58f9-46a1-a873-8d3f02239a76)


---

## 👨‍💻 Author

Built with ❤️ by [Anitha Damarla]
Email:anithadamarla0313@gmail.com

Feel free to contribute or suggest improvements!

```

---

Let me know if you want this exported as `README.md` or want to include badges or license info too!
