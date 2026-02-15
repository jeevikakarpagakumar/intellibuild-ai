# Design Of StoryCode

## 1. Design Goals
StoryCode has the following goals:

- **Human centric understanding:** Prioritizes explanations that help users undertstand the *why* in code not just *what* it does
- **Explainability-first AI:** Ensures all AI-generated insights are interpretable and given with evidence
- **Learning and Productivity balance:** Supports both educational use and real-world developer workflow
- **Modular Architecture:** Enable easy extension to new languages, platforms and IDE integrations

## 2. System Overview
StoryCode is a pipeline based AI system that transforms legacy codebases into narrative explainations.
It integrates **static code analysis**, **version history analysis**, and **code review extraction** to construct the evolution of codebase into a human understandable story
The system ingests a Git repository, processes code, infers developer intent and generates narratives at multiple abstraction levels for different users

## 3. High-Level Architecture
The architecture is divided into 4 logical layers:

1. **Input Layer**
Handles repository ingestion and authentication

2. **Analysis Layer**
Extracts structural and historical portions from code, commits and reviews

3. **AI reasoning Layer**
Infers intent, identifies risks and generates narratives

4. **Presentation Layer**
Displayes story based explanation through interactive UI

## 4. Component Level Design

### 4.1 Repository Ingestion Module

- Accepts local or remote Git repositories
- Handles authentication of private repositories
- Ensures all repository data is processed in-memory or in temporary storage 

### 4.2 Code Parsing Module

- Parses source code so as to identify modules, classes and functions
- Builds an abstract representation of codebase
- Designed to be language adaptive

### 4.3 Commit History Analyzer

- Extracts chronological commit data
- Maps commits to its code regions
- Identifies frequency and density of changes across files and functions

### 4.4 Code Review Extractor

- Extracts review comments and discussions from CR platforms
- Associates review feedback with specific commits and files
- Identifies recurring concerns such as security, performance or readability

### 4.5 Change Classification Module

- Classifies code changes into:
    - Feature additions
    - Bug fixes
    - Refactors
- Uses hybrid approach combining rule-based heuristics and lightweight ML models
- Supports multilabel classification where required

 ### 4.6 Intent Inference Engine
- Infers why changes were made using
    - Commit messages
    - Change patterns
    - Code review discussions
- Explicitly models uncertainty and avoids overconfident conclusions
- Outputs structured intent signals for narrative generation

### 4.7 Narrative Generation Module
- Uses a large language model to convert structured signals into stories
- Ensures chronological and logical coherence
- Adapts explanation depth based on abstraction level:
    - Beginner: motivations and high level evolution
    - Intermediate: design decisions and tradeoffs
    - Expert: technical rationale and risks
- Avoids hallucination by grounding narratives in extracted evidence

### 4.8 Risk Analysis Module
- Identifies fragile code regions using:
  - High modification frequency
  - Repeated review concerns
  - Complexity growth over time
- Flags potential maintenance risks
- Integrates risk insights into narrative explanations

## 5. AI Design Decisions

StoryCode adopts a **hybrid AI design**:

- Deterministic analysis (parsing, metrics) is performed before AI reasoning
- LLMs are used only at the final narrative stage
- This separation:
  - Improves explainability
  - Reduces hallucination
  - Enables traceability of insights

Uncertainty is explicitly communicated in outputs to maintain user trust

## 6. Data Flow Design

1. Repository is ingested by the system
2. Code structure, commit history, and review data are extracted
3. Changes are classified and aggregated chronologically
4. Developer intent and risk signals are inferred
5. Narrative explanations are generated
6. Results are rendered in the user interface

This linear data flow simplifies debugging and scalability

## 7. Abstraction Level Control

StoryCode supports three abstraction levels:

- Beginner: 
  Focuses on story, motivation, and high-level evolution
- Intermediate: 
  Explains design decisions, trade-offs, and architectural shifts
- Expert:
  Provides technical reasoning, performance implications, and risk areas

This design supports both learning and professional use cases

## 8. UI / UX Design Rationale

The user interface is designed to minimize cognitive load:

- Timeline-based navigation for evolution tracking
- Expandable story sections for progressive disclosure
- Clear labeling of uncertainty and assumptions
- Minimalistic layout focused on narrative flow

The UI emphasizes understanding over technical verbosity

## 9. Design Constraints and Trade-offs

- Initial support is limited to a small number of languages and platforms
- Review data availability depends on repository access permissions
- Narrative depth is balanced against response time

These trade-offs are acceptable within hackathon constraints and allow future refinement

## 10. Extensibility and Future Design

The modular architecture enables:
- IDE integrations (e.g., VS Code)
- Support for additional languages and review platforms
- Team-level knowledge mapping
- Predictive insights into future maintenance risks

StoryCode is designed to evolve alongside user needs

## 11. Summary

StoryCode’s design prioritizes **human understanding, explainable AI, and real-world usability
By integrating code, history, and reviews into narrative explanations, the system bridges the gap between technical logic and human intent

---