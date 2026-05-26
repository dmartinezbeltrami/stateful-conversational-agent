# 🧠 Stateful Conversational Agent

A tool-using conversational AI agent with persistent memory, multi-step tool execution, reset support, and local JSON-based memory storage.

---

## 🚀 Overview

This project implements a **stateful conversational AI agent** capable of:
- Maintaining conversational memory across sessions
- Executing multiple tools dynamically
- Performing deterministic time arithmetic
- Handling multi-step tool orchestration loops
- Persisting conversation history locally
- Resetting and limiting memory safely
- Supporting multi-turn contextual reasoning

The project focuses on **reliability-oriented architecture**, combining:
- structured tool orchestration
- persistent state management
- deterministic execution tools
- conversational continuity
- modular design

---

## 🛠️ Tech Stack

- Python
- OpenAI API
- Tool calling / function calling
- JSON persistence
- Stateful conversational workflows
- Deterministic execution tools
- Prompt engineering

---

## 🎯 Features

### ✅ Persistent Conversational Memory

The agent stores conversations locally and automatically reloads them when restarted.

Example:

```text
User:
What time will it be in 3 hours?

Agent:
In 3 hours, the time will be 20:15:55 on May 25, 2026.

User:
And 2 hours after that?

Agent:
Two hours after that, the time will be 22:15:55 on May 25, 2026.
```

The agent understands contextual references such as:
```text
"after that"
```
even across multiple turns.

---

### 🧠 Stateful Memory System

Conversation history is maintained internally:
```python
self.messages
```
The memory system:
- loads automatically on startup
- saves automatically after interactions
- persists between sessions
- supports reset functionality
- limits conversation history size

---

### 🔧 Multi-Tool Orchestration

The agent dynamically selects and executes tools depending on user intent.

Implemented tools:

- calculator
- current time retrieval
- deterministic time arithmetic

Example workflow:
```text
User:
What time will it be in 30 minutes?
```
Execution chain:
```text
get_current_time
→ add_time
→ final response
```
---

### 🔁 Multi-Step Tool Execution Loop

The agent supports iterative execution loops:
```text
reason
→ tool call
→ observe result
→ additional tool call
→ final answer
```

This enables:
- chained reasoning
- dynamic execution flows
- contextual tool orchestration

---

### Deterministic Time Arithmetic

The project separates:

- semantic reasoning (LLM)
- deterministic computation (Python tools)
Example:
```text
What time was it 2 days, 3 hours and 15 seconds ago?
```
The agent uses structured time arithmetic instead of relying on approximate LLM reasoning.

---

### 🧹 Memory Reset Support

Users can reset the conversation state:
```text
reset
```
This clears:
- in-memory history
- persisted conversation history

---

### 📦 Memory History Limiting

The memory system automatically limits stored conversation history to prevent:
- unbounded context growth
- excessive token usage
- degraded model performance

---

## 📂 Project Structure
```
stateful-conversational-agent/
│
├── app/
│   ├── agent.py          # Core conversational + orchestration logic
│   ├── tools.py          # Tool definitions + deterministic execution
│   ├── memory.py         # Persistent memory system
│   ├── prompts.py        # System prompts
│   ├── config.py         # Model + debug settings
│   └── main.py           # CLI interface
│
├── data/
│   └── conversation_memory.json
│
├── run.py                # Entry point
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/dmartinezbeltrami/stateful-conversational-agent.git
cd stateful-conversational-agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate it

Windows (PowerShell):
```bash
.\venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Add your API key

Create a .env file:
```text
OPENAI_API_KEY=your_api_key_here
```

### 6. Run the agent
```bash
python run.py
```
---
## 🧪 Demo

### Input
```text
What time will it be in 4 days, 1 hour, 77 minutes and 3 seconds?
```

### Tool Execution
```text
get_current_time
→ add_time
→ final response
```

### Output
```text
The time will be 2026-05-27 at 03:00:02 in 4 days, 1 hour, 77 minutes, and 3 seconds from now.
```
---

### Persistent Memory Example

Session 1:
```text
User:
What time will it be in 2 hours?
```
Application closes.

Session 2:
```text
User:
What did I ask you first?
```
Output:
```text
User:
You first asked what time it would be in 2 hours.
```

## 🧠 Key Concepts Demonstrated

- Stateful AI agent architecture
- Persistent conversational memory
- Multi-tool orchestration
- Iterative execution loops
- Deterministic execution tools
- Conversational continuity
- Local persistence systems
- Tool routing
- Context-aware reasoning
- Reliability-focused AI engineering
- Separation of concerns

---

## 🔒 Security

- API keys are stored in .env
- .env is excluded via .gitignore
- Persisted memory is stored locally
- No secrets are hardcoded into the repository

---

## 📈 Future Improvements

Possible future extensions:
- Vector database memory
- Retrieval-Augmented Generation (RAG)
- Autonomous planner/executor loops
- Multi-agent orchestration
- Web interface
- Streaming responses
- Database-backed persistence
- Semantic memory retrieval
- Long-term memory summarization

---

## 🧳 Portfolio Value

This project demonstrates:
- Production-style AI engineering patterns
- Stateful conversational architecture
- Multi-step orchestration workflows
- Persistent memory systems
- Tool-based deterministic execution
- Reliability-oriented LLM integration
- Modular system architecture

---

## 🧩 Architecture Highlights

- Conversational memory persists across sessions
- Tool orchestration loop supports chained execution
- Deterministic Python tools handle exact computations
- Persistent memory system reloads automatically on startup
- Reset functionality safely clears local memory state
- Memory limiting prevents uncontrolled context growth
- Multi-turn reasoning enables contextual continuity

---

## 👤 Author

Built by Diego Martínez Beltrami  
AI Engineer focused on Computer Vision, Edge AI, and Agentic Systems.