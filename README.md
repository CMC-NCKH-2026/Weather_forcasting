
# Weather Forecast Project

Small-scaled project for analyzing and **predicting** weather datas. Currently has a **live instance** on [https://weather.qtpc.tech](https://weather.qtpc.tech).

## What this project is about

- Goal: explore historical weather observations and build forecasting models (regression/classification) to predict future weather-related variables.
- Main components:
  - `charts/` - Contains the generated analytic charts
  - `data/` - Contains the input data for analyzing
  - `models/` - Contains the models in `joblib` format, trained with `scikit-learn` library
  - `notebooks/` - Contains Jupyter Notebooks for the project
  - `src/` - Contains Docker entrypoint and utility classes for the project
  - `templates/` - Contains the asset for the template of the website user interface
  - `app.py` - Contains the main logic code of the webserver and the entrypoint for development runs
  - `console_app.py` - Prototype console-based app for testing the model predictions
  - `Dockerfile*` - Dockerfiles for creating Linux and Windows-based Docker images for deployment
  - `wsgi.py` - Bootstrapper Python code for loading the models after starting the WSGI server (in production Docker images)

Status (90%)
------------

- Notebooks for exploration and modeling: ready-to-run (see `notebooks/`).
- Dataset: `data/weatherHistory.csv` (included), `data/processed_weather_data.csv` (after processing, also included).
- Models: `models/*.joblib` (after processing, also included)
- `app.py`: Spins up a completely working webserver that interacts with the model predictions.
- In-progress: Model predictions still need more fine-tuning for more accurate predictions.

Quickstart (Deployment)
-----------------------
The Docker image runs natively on Linux platforms (`linux/amd64` and `linux/arm64`) and Windows (`windows/amd64`, base 21H2 or later). macOS containers run through a Linux-based hypervisor.

Make sure Docker is installed. When done, run this command to have Docker automatically pull the image and run it:
```
docker run ghcr.io/cmc-nckh-2026/weather_forcasting:main
```
You may set the container environment variable `PORT` to the listening port you want to customize to instead of the default port `1515`. For example, to set the listening port to `3000`, append the argument `-e PORT=3000` to the run command.

To update the image when a new version is published, run this command to update the image:
```
docker pull ghcr.io/cmc-nckh-2026/weather_forcasting:main
```
Quickstart (Developer)
----------------------

Follow these steps to get a local development environment ready. Commands assume a POSIX shell (macOS/Linux, or Git Bash on Windows). Windows Command Prompt / PowerShell equivalents are noted where different.

1) Clone the repo (if not already done)

```bash
git clone https://github.com/CMC-NCKH-2026/Weather_forcasting
cd weather_forcast_project
```

2) Create a virtual environment and activate it

macOS / Linux (bash or zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (Command Prompt)

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Install dependencies

This repo contains a pinned dependency file named `requirements.txt`. To install the packages:

```bash
python -m pip install -r requirements.txt
```

4) Launch JupyterLab and open the notebooks (or you can run it by choosing virtual python environment)

```bash
jupyter lab
```

Open the notebooks in the `notebooks/` folder and run cells top-to-bottom.

Contributing (Team guidelines)
------------------------------

We expect team members to follow a lightweight GitHub workflow:

1. Create feature branches from `main`. It is recommended to use the naming convention `feature/<short-desc>` or `fix/<short-desc>`.
2. Keep changes small and focused: one idea per branch.
3. Add or update a notebook and include a short note in the notebook metadata or the PR description describing what changed and why.
4. Open a Pull Request (PR) targeting `main` and include:
   - A short summary of the change
   - Steps to reproduce locally (if applicable)
   - Any environment or dependency changes
5. Request one approving review from another team member before merging.
