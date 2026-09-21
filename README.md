# 🏎️ Formula 1 REST API (`f1-api`)

An enterprise-grade, high-performance RESTful API built with **FastAPI** providing comprehensive Formula 1 historical data, season standings, race weekend telemetry, starting grids, lap progressions, and strategic performance analytics from 1950 to modern seasons.

---

## 📌 Data Source & ETL Pipeline

The relational database powering this API is extracted, transformed, and loaded using the dedicated **F1 Race Data ETL Pipeline**:

🔗 **ETL Pipeline Repository**: [https://github.com/Cobalttt2311/f1-race-data](https://github.com/Cobalttt2311/f1-race-data)

> **Note**: Before running this API, ensure that your PostgreSQL database has been initialized and populated by running the ETL pipeline from the repository above.

---

## 🏗️ Architecture & Design Pattern

The API is architected using the **Controller-Service-Repository (CSR)** Clean Architecture pattern to ensure strict separation of concerns, maintainability, and scalability:

```text
f1-api/
├── controllers/          # API Routers & HTTP Request Handlers (FastAPI Routers)
│   ├── analytics_controller.py
│   ├── circuits_controller.py
│   ├── constructors_controller.py
│   ├── drivers_controller.py
│   ├── races_controller.py
│   ├── seasons_controller.py
│   └── standings_controller.py
├── services/             # Business Logic Layer & Data Transformations
├── repositories/         # Database Access Layer (Direct PostgreSQL queries via Psycopg2)
├── models/               # Pydantic Schemas & DTOs (Data Transfer Objects)
├── core/                 # App Settings & Database Connection Pool
│   ├── config.py
│   └── database.py
├── utils/                # Standardized JSON response envelopes & status messages
├── Formula_1_API.postman_collection.json # Ready-to-import Postman Collection
├── main.py               # Application entrypoint & middleware configuration
├── requirements.txt      # Python dependencies
└── .env.example          # Environment variables template
```

### Key Architectural Highlights:
* **Standardized JSON Envelope**: All endpoints return unified response structures (`{ "status": true, "message": "...", "data": [...] }`).
* **Optimized Raw SQL**: Database operations use direct, index-optimized SQL via `psycopg2` and `RealDictCursor` for low latency responses.
* **CORS Enabled**: Out-of-the-box support for web clients, frontends, and mobile apps.

---

## ⚙️ Prerequisites

* **Python**: `3.10` or higher
* **PostgreSQL Database**: Version 14, 15, or 16 (Local or Cloud instance such as Supabase / AWS RDS)
* Populated tables from the [f1-race-data ETL Pipeline](https://github.com/Cobalttt2311/f1-race-data)

---

## 🚀 Installation & Setup

### 1. Clone or Open the Repository
```bash
cd f1-api
```

### 2. Create and Activate Virtual Environment
* **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **Linux / macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory by copying `.env.example`:

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Edit `.env` to match your PostgreSQL credentials:
```env
DB_USER=postgres
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=formula_one
```

---

## ▶️ Running the API Server

Start the server locally using **Uvicorn** with hot-reload:

```bash
uvicorn main:app --reload --port 8000
```

Once started, the API will be available at:
* **Base URL**: `http://127.0.0.1:8000`
* **Health Check**: `http://127.0.0.1:8000/`

---

## 📖 Interactive API Documentation

FastAPI provides automated, interactive API documentation out of the box:

* **Swagger UI (Interactive)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
  *Explore and execute API calls directly from your browser.*
* **ReDoc (Specification)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  
  *Clean, human-readable API reference.*

---

## 📡 API Endpoints Overview

All endpoints are versioned under the `/api/v1` prefix.

### 1. Seasons (`/api/v1/seasons`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/seasons` | List all historical seasons (1950 - present) |
| `GET` | `/api/v1/seasons/{year}/circuits` | Circuits hosted in a specific season |
| `GET` | `/api/v1/seasons/{year}/drivers` | Drivers who competed in a specific season |
| `GET` | `/api/v1/seasons/{year}/constructors` | Constructors in a specific season |
| `GET` | `/api/v1/seasons/{year}/lineups` | Driver lineups per constructor for a season |
| `GET` | `/api/v1/seasons/{year}/winners` | Grand Prix winners of a season |
| `GET` | `/api/v1/seasons/{year}/pole-sitters` | Pole position sitters across a season |

### 2. Standings (`/api/v1/standings`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/standings/drivers/latest` | Latest driver championship standings |
| `GET` | `/api/v1/standings/constructors/latest` | Latest constructor championship standings |
| `GET` | `/api/v1/standings/drivers?year={year}` | Driver standings filtered by season |
| `GET` | `/api/v1/standings/constructors?year={year}` | Constructor standings filtered by season |

### 3. Races & Race Weekends (`/api/v1/races`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/races/calendar?year={year}` | Race calendar schedule with session dates and times |
| `GET` | `/api/v1/races/{year}/{round_no}/practice-schedule` | Practice session schedules (FP1, FP2, FP3) |
| `GET` | `/api/v1/races/{year}/sprint-schedule` | Sprint race schedules for a season |
| `GET` | `/api/v1/races/{year}/{round_no}/results` | Full Grand Prix race classification & points |
| `GET` | `/api/v1/races/{year}/{round_no}/qualifying` | Q1, Q2, Q3 qualifying timing data |
| `GET` | `/api/v1/races/{year}/{round_no}/sprint` | Sprint race classification results |
| `GET` | `/api/v1/races/{year}/{round_no}/pit-stops` | Pit stop telemetry (stop number, lap, duration) |
| `GET` | `/api/v1/races/{year}/{race_id}/starting-grid` | Official starting grid positions |
| `GET` | `/api/v1/races/{year}/{round_no}/lap-chart` | Lap-by-lap driver positions (P1–P22) |

### 4. Drivers & Constructors (`/api/v1/drivers`, `/api/v1/constructors`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/drivers` | Directory of all Formula 1 drivers |
| `GET` | `/api/v1/drivers/{driver_id}/profile` | Driver career profile, podiums, wins, and championship titles |
| `GET` | `/api/v1/constructors` | Directory of all Formula 1 constructors |

### 5. Circuits (`/api/v1/circuits`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/circuits` | List of all Grand Prix circuits and coordinates |
| `GET` | `/api/v1/circuits/{circuit_id}/history` | Historical winners and pole sitters for a circuit |

### 6. Strategy & Performance Analytics (`/api/v1/analytics`)
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/analytics/biggest-movers` | Drivers with greatest positions gained during a race |
| `GET` | `/api/v1/analytics/pit-stop-efficiency` | Team pit stop durations and rankings |
| `GET` | `/api/v1/analytics/pole-to-win-rate` | Pole position conversion rate to race victory |
| `GET` | `/api/v1/analytics/high-dnf-circuits` | Circuits with highest retirement rates |
| `GET` | `/api/v1/analytics/deep-grid-wins` | Historic wins started from deep on the grid |
| `GET` | `/api/v1/analytics/most-laps-led` | Most laps led by driver and season |
| `GET` | `/api/v1/analytics/fastest-speeds` | Highest trap speeds recorded |
| `GET` | `/api/v1/analytics/all-time-winners` | All-time race victory leaderboard |
| `GET` | `/api/v1/analytics/teammate-qualifying` | Head-to-head teammate qualifying duel comparison |
| `GET` | `/api/v1/analytics/driver-form` | Rolling form and points over recent races |
| `GET` | `/api/v1/analytics/points-progression` | Cumulative points progression race-by-race |
| `GET` | `/api/v1/analytics/constructor-one-twos` | Constructor 1-2 finish history |
| `GET` | `/api/v1/analytics/youngest-winners` | Youngest race winners in F1 history |
| `GET` | `/api/v1/analytics/circuit-masters` | Drivers with the most wins at specific circuits |

---

## 🧪 Testing with Postman

A pre-configured Postman Collection is included in the root directory:

📁 **`Formula_1_API.postman_collection.json`**

### Quick Steps:
1. Open **Postman**.
2. Click **Import** in the top-left corner.
3. Drag and drop `Formula_1_API.postman_collection.json`.
4. Set your environment variable `baseUrl` to `http://127.0.0.1:8000` (or use the default pre-set requests).
5. Execute requests across all modules to verify endpoints and response structures.

---

## 👨‍💻 Author

**Made by Cobalt**

* Data Pipeline & Ingestion: [f1-race-data ETL](https://github.com/Cobalttt2311/f1-race-data)
