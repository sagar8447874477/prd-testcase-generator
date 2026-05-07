# 🧪 PRD to Test Case Generator

## 📌 Project Overview

This project is an AI-assisted web application that converts Product Requirement Documents (PRDs) into structured QA test cases.

The goal of the system is to reduce the manual effort required by QA engineers when creating repetitive test documentation from PRDs. Instead of writing every test case manually, the tool generates an initial draft containing:

* Test Case ID
* Scenario
* Preconditions
* Steps
* Expected Result
* Priority (P0/P1/P2)
* Test Type (Functional / Edge / Negative)

The application supports both:

* `.txt` files
* `.pdf` PRD documents

and is deployed as a Streamlit web application.

---

# ⚙️ Technologies Used

| Technology             | Purpose                          |
| ---------------------- | -------------------------------- |
| Python                 | Core programming language        |
| Streamlit              | Web application framework        |
| pdfplumber             | Extract text from PDF PRDs       |
| Regex / NLP heuristics | Requirement extraction           |
| GitHub                 | Version control and code hosting |
| Streamlit Cloud        | Free deployment platform         |

---

# 🧠 Initial Architecture (Local LLM-Based Approach)

The first implementation used a local Large Language Model (LLM) to generate test cases intelligently from PRDs.

## 📦 Model Used

The project initially used:

```python
google/flan-t5-base
```

through Hugging Face Transformers.

This is an instruction-tuned transformer model designed for text generation and structured NLP tasks.

---

# ❓ Why FLAN-T5 Was Chosen

The model was selected because:

* it works locally without paid APIs
* it performs well on instruction-following tasks
* it can generate structured outputs
* it is lightweight compared to larger LLMs

The idea was to prompt the model like a QA engineer.

Example prompt structure:

```text
You are a QA engineer.

Generate structured test cases from the following PRD.

Include:
- happy paths
- edge cases
- negative cases
```

The model would then generate QA-style outputs dynamically.

---

# ⚠️ Problems Faced with Local LLM Approach

Although the architecture worked conceptually, several practical problems occurred during implementation:

## 1. Heavy Dependencies

The local LLM approach required:

* `transformers`
* `torch`

These packages are large and system-dependent.

---

## 2. Windows + Python Compatibility Issues

During execution, the system encountered:

```text
ImportError: DLL load failed while importing _C
```

This happened because:

* PyTorch DLLs were not compatible with the local Python 3.12 environment
* local Torch installation failed repeatedly

---

## 3. Deployment Complexity

The local LLM approach also introduced:

* large model downloads
* slow startup time
* memory-heavy execution
* deployment instability on free hosting platforms

---

# 🔄 Final Architecture (Lightweight NLP-Based System)

To make the application stable, deployable, and beginner-friendly, the architecture was redesigned.

Instead of relying on a transformer model, the final system uses:

* lightweight NLP heuristics
* regex-based requirement extraction
* template-driven test generation

This removed all heavy ML dependencies while still producing structured QA outputs.

---

# 🧠 Final Working Flow (Step-by-Step)

## Step 1 — Upload PRD

The user uploads:

* `.txt`
* or `.pdf`

through the Streamlit UI.

---

## Step 2 — Extract Text

### For TXT files

The system reads plain text directly.

### For PDF files

The system uses:

```python
pdfplumber
```

to extract textual content page-by-page.

---

## Step 3 — Requirement Extraction

The PRD text is split into individual requirement-like statements using:

* periods (`.`)
* line breaks (`\n`)

Example:

```text
Users should be able to log in
Forgot password should work
System should lock account after 5 failed attempts
```

becomes a list of requirements.

This is handled using regex-based parsing.

---

## Step 4 — Test Case Expansion

For every extracted requirement, the system automatically generates:

### ✅ Functional Test Case

Checks expected/happy path behavior.

### ⚠️ Edge Test Case

Checks boundary conditions and unusual inputs.

### ❌ Negative Test Case

Checks invalid behavior and error handling.

---

# 🧪 Example

## Requirement

```text
Users should be able to log in using email and password
```

## Generated Functional Test

```text
Scenario:
Validate login using valid credentials
```

## Generated Edge Case

```text
Validate login with empty password
```

## Generated Negative Case

```text
Validate login using invalid credentials
```

---

# 🎯 Why This Architecture Was Chosen

The lightweight NLP approach was selected because it provides:

## ✅ Advantages

* easy deployment
* no GPU required
* no paid APIs
* low memory usage
* stable execution
* faster response time

---

## ⚠️ Tradeoff

The system is less intelligent than a true LLM and may:

* miss implicit requirements
* generate generic outputs
* require human review

However, for this assignment, reliability and deployability were prioritized over advanced generation quality.

---

# 🧑‍💻 Human QA Workflow Integration

This tool is designed to assist QA engineers, not replace them.

The expected workflow is:

```text
PM writes PRD
↓
Tool generates draft test cases
↓
QA engineer reviews/edit/adds missing cases
↓
Final QA plan created
```

This reduces repetitive documentation work while keeping humans in control.

---

# 🚀 Features Implemented

* Upload PRDs
* PDF + TXT support
* Structured test case generation
* Functional / Edge / Negative cases
* Download generated output
* Simple web UI
* Fully local execution
* No paid APIs

---

# ⚠️ Current Limitations

The current system:

* depends on PRD clarity
* uses heuristic parsing
* does not deeply understand semantics
* may generate repetitive outputs

Complex workflows or implicit requirements may still require manual QA effort.

---

# 📈 Future Improvements

Future versions could include:

## 1. Smaller Local LLMs

Use lightweight models such as:

* TinyLlama
* Phi
* DistilGPT

for better reasoning without large dependencies.

---

## 2. Requirement Coverage Checker

Verify:

* every requirement has at least one test case
* no requirement is missed

---

## 3. Structured Export Formats

Export directly to:

* Excel
* TestRail
* Zephyr

---

## 4. Better NLP Understanding

Use:

* embeddings
* semantic similarity
* requirement classification

to improve test quality.

---

# ☁️ Deployment

The project is deployed using:

* GitHub (repository hosting)
* Streamlit Cloud (free deployment)

Whenever code is updated on GitHub, Streamlit automatically redeploys the application.

---

# 🧠 Key Learning

The project demonstrated that:

* practical system design
* deployment stability
* workflow understanding

are often more important than using large AI models.

A simpler and reliable system is usually better than a complex but unstable architecture.

---
