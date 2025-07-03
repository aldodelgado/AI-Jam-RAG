# 🧠 AI Jam RAG PR Automation System

This project provides a fully automated Pull Request (PR) resolution workflow using a Python-based Retrieval-Augmented Generation (RAG) system. It integrates with GitHub Actions, OpenAI's GPT-4, and `llm-prompt-semantic-diff` for intelligent, semantic-aware code modification and review.

---

## 🔁 Workflow Overview

1. **Issue Handling**
   - Retrieves the latest open GitHub Issue as the root instruction.

2. **Contextual Prompt Generation**
   - Scans the repository for relevant files to inject context into the LLM prompt.

3. **Patch Generation + SED Loop**
   - Uses GPT to generate a patch.
   - Applies it to a clean Git branch.
   - Validates with:
     - ✅ Semantic diffing (`llm-prompt-semantic-diff`)
     - ✅ Unit tests (`pytest`)
     - ✅ Linting (`flake8`)
   - If any step fails, retries (Synthesize → Execute → Debug loop).

4. **Automated PR Review**
   - Reviews PRs via GitHub Action with optional semantic or checklist validation.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `issue_handler.py` | Gets the latest GitHub issue. |
| `prompt_context_builder.py` | Locates and extracts file context for patch generation. |
| `change_applier.py` | Handles patch generation, validation, and push. |
| `pr_reviewer.py` | Posts comments on PRs for review results. |
| `Dockerfile` | Sandboxed CI container. |
| `.github/workflows/rag_automation.yml` | CI automation pipeline. |

---

## 🚀 Setup

### 1. Clone and install

```bash
git clone https://github.com/aldodelgado/AI-Jam-RAG.git
cd AI-Jam-RAG
pip install -r requirements.txt
