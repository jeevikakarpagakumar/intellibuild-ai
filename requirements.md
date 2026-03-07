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

### 4.1 Frontend

- The system shall use **React.js** to build a responsive and interactive web interface
- The frontend shall support dynamic rendering of narrative explanations and timelines
- The frontend shall communicate with the backend using RESTful APIs
- The UI shall support real-time updates for analysis progress

### 4.2 Backend

- The system shall use **Python** as the primary backend language
- The backend shall be implemented using either:
    - **FastAPI** (preferred for performance and async support), or
    - **Django** (for structured and scalable API development)
- The backend shall expose REST APIs for:
    - Repository ingestion
    - Commit history extraction
    - Code review extraction
    - Narrative generation
- The backend shall handle request validation, error handling, and API authentication.

### 4.3 AI / LLM Integration

- The system shall integrate the **OpenAI API** for code to story narrative generation
- The backend shall structure repository insights before sending them to the LLM
- The system shall implement prompt control mechanisms to:
    - Reduce hallucination
    - Maintain narrative coherence
    - Control abstraction level (Beginner / Intermediate / Expert)
- The system shall handle API rate limiting and error fallback mechanisms

### 4.4 Version Control Integration

- The system shall integrate with the **GitHub API** to:
  - Fetch commit history
  - Retrieve pull requests
  - Extract code diffs
  - Extract review comments
- The system shall support OAuth based GitHub authentication
- The system shall respect repository access permissions and user scopes

### 4.5 Authentication & Authorization 

- The system shall implement **OAuth 2.0** for secure third-party authentication
- The system shall use **JWT (JSON Web Tokens)** for secure session management
- Access tokens shall be securely stored and transmitted over HTTPS
- The system shall restrict repository access based on user permissions

### 4.6 Cloud Hosting & Deployment

- The system shall be deployed on **AWS** for scalability and reliability
- The deployment environment may include:
  - AWS EC2 or ECS for backend hosting
  - AWS S3 for static frontend hosting
  - AWS RDS (optional) for metadata storage
- The system shall support horizontal scaling for increased user loadss

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