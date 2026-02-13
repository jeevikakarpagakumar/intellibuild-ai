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

### 
