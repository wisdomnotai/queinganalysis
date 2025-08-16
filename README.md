# 🗳️ Solutio – Polling Station Queue Analyzer

Solutio is a **queue simulation tool** built with Python to help optimize polling booth efficiency using **M/M/c queuing theory**.  
Created by **Wisdom Alawode**, a math student at the University of Ibadan, Oyo State, Nigeria.

---

## 🧠 Mission
Support transparent and efficient elections by helping INEC and decision-makers test different polling booth configurations before deployment.

---

## 🎓 Project Overview

### 🎯 Goals
- Simulate polling station queues using M/M/c models.
- Compare multiple server (booth) configurations.
- Provide insights into wait times, queue lengths, and system utilization.

### 📲 Key Features Implemented
✅ Calculates utilization, idle probability (P₀), and probability of waiting.  
✅ Estimates average queue length (Lq), waiting time (Wq), and service time (Ws).  
✅ Handles steady-state and overloaded scenarios.  
✅ Outputs results in a clean Pandas DataFrame format.  

---

## 🛠 Built With
- **Language:** Python  
- **Libraries:** Pandas, Math  

---

## 🚀 Installation & Usage

```bash
# 1️⃣ Clone the repository
git clone https://github.com/wisdomnotai/solutio.git

# 2️⃣ Navigate into the folder
cd solutio

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the app
python app.py
