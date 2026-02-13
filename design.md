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
