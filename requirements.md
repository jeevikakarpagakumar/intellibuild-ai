# Requirements Specifications For StoryCode

## 1. Introduction

### 1.1 Purpose 
This document defines functional, non-functional, technical, AI-specific and User requirements for **StoryCode**, an AI-powered system that explains legacy codebases as human readable stories. The goal is to help developers and students understand, learn codebases by focusing on *why* code exists rather than only *what* it does

### 1.2 Scope
StoryCode analyzes source code, version control history and code reviews to generate narrative and explain the evolution, intent and design decision behind legacy code. This system is intended to help students, developers and teams to work with complex codes or undocumented codebases.

---

## 2. Functional Requirements

### 2.1 Repository Input

- The system shall accept a repository (Git/private) as input
- The repository may be local or remote

### 2.2 Source Code Parsing

- The system shall parse source code files to identify modules, classes and functions
- The system shall construct an internal hierarchial structure representing the codebase
- The system shall support the programming language 

### 2.3 Version History Extraction

- The system shall extract commit history from repository
- The system shall associate code changes with corresponding commits
- The system shall preserve the order of changes

### 2.4 Code Review Extraction

- The system shall extract code review data 
- Sources may include pull requests, merge requests and review comments
- The system shall review comments with relevant code changes
- The system shall identify recurring concerns raised during reviews

### 2.5 Change classification

- The system shall classify code changes into following categories:
    - Feature additions
    - Bug fixes
    - Refactoring changes
- The system shall allow changes to belong to multiple categories if present

### 2.6 Intent interface

- The system shall infer possible developer intent behind code changes
- Intent interface shall be based on:
    - Commit messages
    - Code diffs
    - Code change frequencies
    - Code review discussions
- The system shall indicate uncertainities where intent cannot be inferred confidently

### 2.7 Narrative Generation

- The system shall generate a chronological narrative explaining the evolution of selected codebase
- The narrative shall integrate insights from commits and code reviews
- The system shall discuss motivations, tradeoffs and concerns raised during development

### 2.8 Abstraction Level Control

- The system shall support multiple explanation levels:
    - High level story
    - Design Focus explanation
    - Detailed technical rationale
- User shall be able to switch between abstraction levels

---

## 3. Non-Functional Requirements

### 3.1 Usability

- The system shall present explanations in clear, concise and readable language
- The interface shall be usable by developers onboarding

### 3.2 Performance

- The system shall design narratives within a reasonable time for small and medium size repositories
- The sstem shall provide progressive feedback during analysis

### 3.3 Scalability

- The system shall handle increasing repository sizes with acceptable performance dip
- The system shall accept incremental analysis if possible

### 3.4 Reliability

- The system shall produce consistent explanations for same repository state
- Analysis failures shall be handled gracefully

### 3.5 Explainability

- The system shall explain why conclusions were drawn, including references to commits or reviews
- Uncertain inferences shall be explicitly clear

---

## 4. Technical Requirements

### 4.1 Backend
- The system shall be implemented using a Python based backend
- The system shall use Git integration libraries to analyze repository history

### 4.2 Code Review Integration
- The system shall support extraction of review data via APIs or repository metadata
- Initial implementations may focus on a single platform 
- Review extraction shall respect access permissions and privacy constraints

### 4.3 AI Components
- A large language model shall be used for narrative generation
- Machine learning techniques may be used for:
  - Change classification
  - Intent inference
  - Review theme clustering

### 4.4 Frontend
- The system shall provide a web based user interface
- The interface shall display:
  - Narrative explanations
  - Evolution timelines
  - Review-informed insights

### 4.5 Storage
- The system shall use temporary storage for repository analysis
- Repository and review data shall not be stored permanently without user consent


---

## 5. Data Requirements

### 5.1 Input Data

- Source code files from repository
- Git commit metadata including author, timestamp and messages
- Code diffs between commits
- Code review comments 

### 5.2 Privacy and Security

- The system shall not use private repositories
- The analysis must occur only with user's discretion 

---

## 6. AI and Model Requirements

### 6.1 Narrative Coherance

- Generated narratives shall be logically coherant and in chronological order
- Narratives must be consistent

### 6.2 Fabrication Avoidance

- The AI shall not fabricate events, decisions not supported by data
- The system shall prefer explanatopms when evidence is available

### 6.3 Adaptivity

- The AI shall adapt explanation based on user selected abstraction
- The AI shall support iterative explanations

---

## 7. User Requirements

### 7.1 Students

- The system shall help students understand real-time legacy codebases

### 7.2 Developers

- The system shall reduce onboarding time for new developers and developers new to the assigned codebase

### 7.3 Team 

- The system shall reduce understanding time of codebases with inadequate design documents

---

## 8. Success Criteria

- Users report improved understanding of legacy code based on timely feedback
- Reduced time to comprehend selected modules

---

## 9. Conclusion

StoryCode prioritises **human understanding** over purely technical completeness. This system focuses on learning, productivity and explainable AI