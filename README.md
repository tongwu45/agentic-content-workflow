# agentic-content-workflow
A multi-step LLM workflow for generating, critiquing, refining, and adapting product content across channels
# Agentic Content Workflow

A multi-step LLM workflow for generating, critiquing, refining, and adapting product content across channels.

## Overview

This project explores how AI workflows can support growth, discovery, and distribution work. Instead of generating content in one step, the system uses multiple agent-style stages to transform product information into clearer, more trustworthy, and more platform-appropriate content.

The workflow is designed to simulate the kind of work involved in AI-native growth roles, where the goal is not just to write content, but to build repeatable systems that improve messaging quality over time.

## Why I Built This

I built this project to demonstrate how LLM-based workflows can be used for:
- product messaging
- content generation
- automated critique and revision
- cross-platform adaptation
- lightweight feedback loops

This project is especially inspired by roles focused on growth, discovery, and distribution for AI products.

## What the Workflow Does

The system takes a structured product input and runs it through several stages:

1. **Strategy Agent**  
   Identifies the target audience, user pain points, key message, and trust angles.

2. **Generator Agent**  
   Creates first-draft content for multiple channels.

3. **Critic Agent**  
   Reviews the draft for clarity, trustworthiness, specificity, empathy, and platform fit.

4. **Refiner Agent**  
   Revises the content using the critic’s feedback.

5. **Platform Adapter Agent**  
   Adapts the refined content into formats suitable for different channels.

6. **Logger**  
   Saves prompts, outputs, and workflow results for review.

## Workflow Diagram

```mermaid
flowchart TD
    A[Product Input JSON] --> B[Strategy Agent]
    B --> C[Generator Agent]
    C --> D[Critic Agent]
    D --> E[Refiner Agent]
    E --> F[Platform Adapter Agent]
    F --> G[Logger]
    G --> H[Streamlit Demo UI]
