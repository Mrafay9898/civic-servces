# AI Smart Civic Services Platform 🏙️

A complete, production-ready **AI-Powered Civic Complaint Management** web application designed for hackathons and real-world urban service monitoring.

---

## 📌 Problem Statement & Objective
Municipal centers are flooded daily with unstructured complaint descriptions (emails, forms, phone calls) regarding infrastructure issues like pothole-ridden roads, flickering lights, or bursting water lines. Manually sorting, assigning departments, and prioritizing these tickets is slow, expensive, and error-prone.

**Our Objective:** Create an intelligent civic platform where citizens submit plain-text problems, and a localized AI pipeline instantly categorizes, prioritizes, summarizes, and routes the issues to responsible departments for rapid resolution.

---

## ⚡ Features
- **Citizen Portal:** Easy form submission with location detection and optional photo upload.
- **AI Analysis Reporting:** Immediate category, priority, and summary responses displayed on screen.
- **Admin Dashboard:** Aggregated KPI cards (Total, Open, In Progress, Resolved, Critical) and modern data visualization plots (Seaborn/Matplotlib donut charts, category histograms, and submission trends).
- **Complaint Console:** Rich administrative data grid featuring text searching and advanced filtering (by status, location, category, and department).
- **Interactive Action System:** Interactive options to re-assign departments, update work statuses, and delete logs with persistent SQLite sync.
- **Mathematical Analytics:** Deep-dive statistics page detailing resolution time averages, standard deviations, quartiles, IQR, and statistical outlier fences.
- **AI Sandbox Sandbox:** Dedicated playground to test arbitrary complaints, inspect real-time performance matrix confusion plots, and trigger on-the-fly model retraining.
- **Explainable AI (XAI) Page:** Educates administrators on TF-IDF representation, Logistic Regression, and model boundaries.

---

## 🧠 AI Features
The platform incorporates three distinct AI features:
1. **Complaint Classification:** Uses a **TF-IDF (1,2-ngram) Vectorizer + Logistic Regression** model to predict issue categories (`Road`, `Water`, `Waste`, `Electricity`, `Drainage`, `Safety`, `Other`).
2. **Priority Estimation:** Uses a **TF-IDF + Logistic Regression** model to predict urgency levels (`Low`, `Medium`, `High`, `Critical`).
3. **Actionable Summarization (Local Fallback):** Computes normalized sentence-importance scores using word-frequency metrics (ignoring standard English stopwords) to extract a punchy summary (e.g. *"Burst water line on Main St"*), avoiding expensive API calls.
4. **Self-Healing Integration:** If serialized models are not found on system launch, the application dynamically triggers training to self-heal.

---

## 🛠️ Technology Stack
- **Frontend & Routing:** Streamlit (Custom styled with responsive CSS injections)
- **Backend OOP Core:** Python 3.11
- **Database System:** SQLite 3
- **Machine Learning & NLP:** Scikit-Learn
- **Data Structuring & Analysis:** Pandas, NumPy
- **Visual Analytics:** Matplotlib, Seaborn

---

## 🗺️ System Architecture
```text
ai-smart-civic-services/
│
├── app.py                     # Streamlit Main App & Theme Router
├── requirements.txt           # Python Dependencies
├── README.md                  # Project Documentation
├── .gitignore                 # Track Ignored Files
│
├── data/
│   └── civic_complaints.csv   # Synthesized Training Corpus
│
├── models/
│   ├── category_model.pkl     # Logistic Regression Category Model
│   ├── priority_model.pkl     # Logistic Regression Priority Model
│   └── vectorizer.pkl         # Fit TF-IDF Feature Extractor
│
├── database/
│   └── civic_services.db      # Live SQLite Database File
│
├── src/
│   ├── complaint.py           # Complaint OOP Model
│   ├── citizen.py             # Citizen Model
│   ├── department.py          # Department Map & Routing Config
│   ├── complaint_manager.py   # Business Process Coordinator
│   ├── ai_analyzer.py         # ML Prediction & Extractive Summary engine
│   ├── database_manager.py    # SQLite CRUD Engine & Preloaded Demo Data
│   ├── statistics_manager.py  # Advanced Mathematical Computations
│   └── pages/                 # Modular Frontend Screens
│       ├── home.py
│       ├── submit_complaint.py
│       ├── my_complaints.py
│       ├── admin.py
│       ├── management.py
│       ├── analytics.py
│       ├── ai_testing.py
│       └── about.py
│
├── ml/
│   ├── train_models.py        # Dataset synthesizer & Training pipeline
│   └── evaluate_models.py     # Evaluation & metrics compiler
│
└── assets/
    └── uploads/               # Saved Citizen Image Uploads
```

---

## 📊 Database Design
The SQLite database stores records inside the `complaints` table using the following columns:
- `complaint_id` (TEXT, PK): Unique 8-digit randomized UUID.
- `description` (TEXT): Detailed plain-text ticket description.
- `category` (TEXT): Classified problem area.
- `priority` (TEXT): Estimated ticket urgency.
- `location` (TEXT): Reported physical location.
- `status` (TEXT): Open / Assigned / In Progress / Resolved.
- `assigned_department` (TEXT): Target department.
- `ai_output` (TEXT): JSON dump of prediction confidence values.
- `summary` (TEXT): Actionable summary string.
- `image_path` (TEXT): Link to local uploaded asset.
- `created_at` (TEXT): Created timestamp.
- `updated_at` (TEXT): Updated timestamp.

---

## 🚀 Setup & Execution

### 1. Installation
Clone the repository, open your terminal inside the workspace directory, and install requirements:
```bash
pip install -r requirements.txt
```

### 2. Model Training & Evaluation
Generate the training dataset and train the ML classifiers:
```bash
python ml/train_models.py
```
To review F1-scores, precision, and recall metrics, run:
```bash
python ml/evaluate_models.py
```

### 3. Launching the App
Run the local Streamlit development server:
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser. The database will automatically initialize and populate itself with 10 realistic demo complaints on its first run, allowing dashboards and analytics to be immediately functional.

---

## ☁️ Deployment Instructions
The platform is fully optimized for containerization and Render/Heroku deployments:
- No hardcoded API secrets (no external API dependencies).
- Automatically initializes missing database schemas.
- Incorporates auto-training fallbacks if models are not present.
- Compatible with WSGI and standard Streamlit deployment steps. Create a standard Web Service on Render and point the start command to:
  ```bash
  streamlit run app.py --server.port $PORT
  ```

---

## ⚠️ Limitations & Future Improvements
- **Limited Vocabulary:** Accuracy depends on vocabularies inside the training CSV. Very odd descriptions may result in incorrect classification.
- **Spelling Errors:** Standard TF-IDF is sensitive to typos. A future update could add character n-grams or embeddings (like Word2Vec/BERT) for spelling tolerance.
- **Multilingual Support:** Currently optimized for English descriptions only.
