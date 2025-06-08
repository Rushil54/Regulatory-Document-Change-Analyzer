# Regulatory Document Change Analyzer

This project is a functional AI-powered prototype designed to help Quality Assurance and Regulatory Affairs teams compare two versions of a regulatory document and perform an initial impact analysis. It automatically identifies changes (additions, deletions, modifications) and uses a local LLM to assess their significance.

---

### 1. Problem Statement

Manually comparing regulatory documents line by line is inefficient and risky. Missing changes can lead to non-compliance and audit issues. This prototype solves that by automating:

- Change detection between versions.
- Classification and summarization of impactful changes using AI.
- A clean user interface for document upload and review.

---

### 2. Approach

#### Strategy

- Break down the task into detection + analysis phases.
- Ensure each phase is modular, testable, and scalable.

#### AI Implementation

- Uses Ollama to run open-source local LLMs `Phi-3`.
- For each added/modified section:
  - A prompt-engineered query is sent to the LLM.
  - The LLM returns a structured JSON:
    - `change_summary`: one-line summary of the change.
    - `change_type`: one of:
    - `New Requirement`
    - `Clarification of Existing Requirement`
    - `Deletion of Requirement`
    - `Minor Edit`

#### Frontend & Backend Integration

- Backend (Python):
  - Handles file parsing, change detection, LLM queries.
- Frontend (Streamlit):
  - Allows uploading "Before" and "After" documents.
  - Calls backend logic on button press.
  - Displays results clearly using interactive elements (expanders, cards).

---

### 3. Functionality (End-to-End)

- Full end-to-end working flow:
  - Upload 2 document versions
  - Detect changes
  - Analyze changes with LLM
  - Display structured output on UI

- Change Detection Logic:
    - Accurately detects:
    - Added paragraphs
    - Deleted paragraphs
    - Modified paragraphs using fuzzy similarity

---
# Project Structure

reg-doc-change-analyzer/
├── backend/
│   ├── diff.py          
│   └── llm.py           
├── frontend/
│   └── app.py           
├── data/
│   ├── text_v1.txt
│   └── text_v2.txt
├── requirements.txt
└── README.md

# Technology Stack
- Python 3
- Streamlit
- Ollama
- Open-source LLMs (Phi-3)
- difflib / fuzzy matching for comparison

# Screenshots

![Alt text](/home/rushil/Desktop/zipp/images/Screenshot from 2025-06-08 12-57-04.png)
![Alt text](/home/rushil/Desktop/zipp/images/Screenshot from 2025-06-08 13-13-46.png)


# Author
Rushil Maradugula
Pre-Final Year, CSE
Motilal Nehru National Institute of Technology


