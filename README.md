# AI Agent Course — Setup Guide

Welcome! This repository contains hands-on labs for learning how to build **AI Agents** — from calling an LLM for the first time, to multi-agent workflows, tool calling, and persistent memory.

This guide assumes **no prior experience** with Python, virtual environments, or API keys. Follow each step in order.

---

## What You Will Need

| Item | Notes |
|------|--------|
| **Computer** | macOS, Windows, or Linux |
| **Cursor** | Free code editor — download at [cursor.com](https://cursor.com) |
| **Internet** | Required to install tools and call AI APIs |
| **OpenAI account** | Required for most labs — [platform.openai.com](https://platform.openai.com) |
| **Credit card** | Some API providers require billing setup (OpenAI, Anthropic, etc.) |

Optional accounts (needed for specific labs later):

- [Anthropic](https://console.anthropic.com) — Claude models (Module 2)
- [Google AI Studio](https://aistudio.google.com) — Gemini models (Module 2)
- [MailerSend](https://www.mailersend.com/) — email notifications (Modules 3, 4, 6)
- [Serper](https://serper.dev) — web search (Modules 5, 6)
- [LangSmith](https://langsmith.com) — tracing for LangGraph (Module 6)

---

## Course Structure

Work through the modules in order:

| # | Module | Folder | What you learn |
|---|--------|--------|----------------|
| 1 | Foundations | `1_foudations/` | Call OpenAI, chain prompts |
| 2 | AI Models | `2_ai_models/` | Compare providers, structured output |
| 3 | Resume Chatbot | `3_resume_chatbot/` | Gradio UI, tool calling, email |
| 4 | OpenAI Agents SDK | `4_open_ai_sdk/` | Agents, tools, handoffs |
| 5 | CrewAI | `5_crew_ai/` | Multi-agent crews |
| 6 | LangGraph | `6_langgraph/` | Graphs, memory, checkpointing |

**Setup notebooks** (run these first):

- `setup/1_extensions.ipynb` — install Cursor extensions & select Python kernel
- `setup/2_api_key_setup.ipynb` — verify your API keys

---

## Step 1 — Install Python (via uv)

We use **[uv](https://docs.astral.sh/uv/)** to manage Python and packages. It is fast and handles virtual environments for you.

### macOS / Linux

Open **Terminal** and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen Terminal, then verify:

```bash
uv --version
```

### Windows

Open **PowerShell** and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen PowerShell, then verify:

```powershell
uv --version
```

> **Alternative:** If the commands above do not work, install uv with pip:
> ```bash
> pip install uv
> ```

---

## Step 2 — Open the Project in Cursor

1. Download or clone this repository to your computer.
2. Open **Cursor**.
3. Go to **File → Open Folder** and select the `course-ai-agent` folder.
4. You should see folders like `1_foudations`, `setup`, `2_ai_models`, etc. in the left sidebar.

---

## Step 3 — Create a Virtual Environment

A **virtual environment** (`.venv`) keeps this project's packages separate from other Python projects.

Open the **integrated terminal** in Cursor:

- **View → Terminal**, or press `` Ctrl+` `` (Windows/Linux) / `` Cmd+` `` (Mac)

Make sure you are in the project root (the folder that contains `requirements.txt`), then run:

```bash
uv venv --python 3.12
```

This creates a `.venv` folder in the project. The project expects **Python 3.12** (see `.python-version`).

### Activate the virtual environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

When active, your terminal prompt should show `(.venv)` at the beginning.

---

## Step 4 — Install Python Libraries

With the virtual environment activated, install all lab dependencies:

```bash
uv pip install -r requirements.txt
```

This may take a few minutes. When finished, you should see packages like `openai`, `gradio`, `langgraph`, and `crewai` installed.

> **Tip:** If you get an error, make sure Step 3 completed successfully and `(.venv)` is visible in your terminal.

---

## Step 5 — Install Cursor Extensions

You need two extensions to run the `.ipynb` lab notebooks:

1. In Cursor, open the **Extensions** panel:
   - **View → Extensions**, or press `Cmd+Shift+X` (Mac) / `Ctrl+Shift+X` (Windows)
2. Search for **`Python`** → install **Python** by **ms-python**
3. Search for **`Jupyter`** → install **Jupyter** by **Microsoft**

Or follow the guided notebook: open `setup/1_extensions.ipynb` and read the instructions at the top.

---

## Step 6 — Select the Python Kernel

Every notebook needs to know which Python to use.

1. Open any lab notebook (e.g. `1_foudations/1_lab1.1.ipynb`).
2. Click **Select Kernel** in the top-right of the notebook.
3. Choose **Python Environments**.
4. Select **`.venv (Python 3.12.x)`** — it should point to this project's virtual environment.

If `.venv` does not appear:

1. **Mac:** Cursor menu → **Settings → VS Code Settings** (not Cursor Settings)
   **Windows:** **File → Preferences → VS Code Settings**
2. Search for **`venv`**
3. In **Path to folder with a list of Virtual Environments**, enter your project root path, e.g.:
   - Mac: `/Users/yourname/path/to/course-ai-agent`
   - Windows: `C:\Users\yourname\path\to\course-ai-agent`
4. Reopen the notebook and try **Select Kernel** again.

---

## Step 7 — Create Your `.env` File

API keys and personal settings are stored in a `.env` file. This file is **never committed to git** — it stays on your machine only.

### Copy the template

**macOS / Linux:**

```bash
cp .env.example .env
```

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**Windows (Command Prompt):**

```cmd
copy .env.example .env
```

You can also do this manually: duplicate `.env.example` in the file explorer and rename the copy to `.env`.

### Fill in your values

Open `.env` in Cursor and replace the empty values. Example:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxx
YOUR_NAME=Your Name
YOUR_EMAIL=you@example.com
```

### What each variable is for

| Variable | Required when | How to get it |
|----------|---------------|---------------|
| `OPENAI_API_KEY` | **Most labs** | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |
| `YOUR_NAME` | Module 3+ | Your display name (any text) |
| `YOUR_EMAIL` | Module 3+ | Your email for test notifications |
| `ANTHROPIC_API_KEY` | Module 2 | [console.anthropic.com](https://console.anthropic.com) |
| `GOOGLE_API_KEY` | Module 2 | [aistudio.google.com/api-keys](https://aistudio.google.com/api-keys) |
| `MAILER_SEND_API_TOKEN` | Modules 3, 4, 6 | [app.mailersend.com/domains](https://app.mailersend.com/domains) → Manage → Generate token |
| `MAILER_SEND_DOMAIN` | Modules 3, 4, 6 | The domain shown on MailerSend Domains page |
| `SERPER_API_KEY` | Modules 5, 6 | [serper.dev](https://serper.dev) → sign up → API key |
| `LANGSMITH_API_KEY` | Module 6 | [langsmith.com](https://langsmith.com) → Tracing → Generate API Key |
| `LANGSMITH_PROJECT` | Module 6 | Any project name you create in LangSmith |
| `LANGSMITH_TRACING` | Module 6 | Keep as `true` |
| `LANGSMITH_ENDPOINT` | Module 6 | Keep as `https://api.smith.langchain.com` |

> You do **not** need every key on day one. Start with `OPENAI_API_KEY` and add others when you reach that module.

Detailed API key walkthrough: open `setup/2_api_key_setup.ipynb`.

---

## Step 8 — Verify Everything Works

1. Open `setup/2_api_key_setup.ipynb`
2. Select the `.venv` kernel (Step 6)
3. Run each cell top to bottom (`Shift+Enter`)
4. You should see messages like:
   ```
   OpenAI API Key exists and begins sk-proj-
   ```

Then run your first lab:

1. Open `1_foudations/1_lab1.1.ipynb`
2. Run all cells top to bottom
3. You should get a response from GPT (e.g. the answer to `2+2`)

If that works — you are ready to start the course!

---

## Step 9 — Module 5 (CrewAI) Extra Setup

Module 5 lives in `5_crew_ai/` and uses its own project config. After completing Steps 1–8:

```bash
cd 5_crew_ai
uv pip install crewai[tools]
crewai install
```

Make sure your `.env` file is in the **project root** (one level above `5_crew_ai/`) and includes `OPENAI_API_KEY` and `SERPER_API_KEY`.

Run the crew from the `5_crew_ai` folder:

```bash
crewai run
```

See `5_crew_ai/README.md` for more details.

---

## How to Run a Lab Notebook

1. Open the `.ipynb` file in Cursor
2. Confirm the kernel is **`.venv (Python 3.12.x)`**
3. Run cells **top to bottom** using `Shift+Enter`
4. Read the **Introduction** and **Lab Structure** at the top of each notebook before coding

---

## Troubleshooting

### `Import Error` or `ModuleNotFoundError`

- Make sure the `.venv` kernel is selected (Step 6)
- Re-run: `uv pip install -r requirements.txt` with the venv activated

### `OpenAI API Key not set`

- Check that `.env` exists in the project root (same folder as `requirements.txt`)
- Check that `OPENAI_API_KEY=sk-...` has no spaces around `=`
- Restart the notebook kernel: click **Restart** in the notebook toolbar, then re-run cells

### `.venv` not showing in kernel list

- Follow the venv path fix in Step 6
- Run `uv venv --python 3.12` again from the project root

### Gradio URL does not open

- Look for a line like `Running on local URL: http://127.0.0.1:7860` in the cell output
- Click the link or paste it into your browser

### MailerSend email fails

- Complete MailerSend setup in Lab 3.2 (Part 2) before Modules 4 or 6
- Verify `MAILER_SEND_API_TOKEN` and `MAILER_SEND_DOMAIN` in `.env`

### LangGraph / LangSmith traces missing

- Complete LangSmith setup in `6_langgraph/6_lab1.ipynb` (Part 1)
- Copy all `LANGSMITH_*` variables from LangSmith into `.env`

---

## Project Layout

```
course-ai-agent/
├── .env.example          ← template — copy to .env
├── .env                  ← your secrets (create this, never commit)
├── requirements.txt      ← Python packages for all labs
├── setup/
│   ├── 1_extensions.ipynb
│   └── 2_api_key_setup.ipynb
├── 1_foudations/         ← Module 1 labs
├── 2_ai_models/          ← Module 2 labs
├── 3_resume_chatbot/     ← Module 3 labs
├── 4_open_ai_sdk/        ← Module 4 labs
├── 5_crew_ai/            ← Module 5 crew project
└── 6_langgraph/          ← Module 6 labs
```

---

## Quick Start Checklist

Use this checklist on your first day:

- [ ] Install [Cursor](https://cursor.com)
- [ ] Install [uv](https://docs.astral.sh/uv/) (`uv --version` works)
- [ ] Open project folder in Cursor
- [ ] Run `uv venv --python 3.12`
- [ ] Activate venv (`source .venv/bin/activate`)
- [ ] Run `uv pip install -r requirements.txt`
- [ ] Install **Python** and **Jupyter** extensions
- [ ] Copy `.env.example` → `.env`
- [ ] Add `OPENAI_API_KEY` to `.env`
- [ ] Select `.venv` kernel in a notebook
- [ ] Run `setup/2_api_key_setup.ipynb` — keys verified
- [ ] Run `1_foudations/1_lab1.1.ipynb` — first LLM response works

Happy building!
