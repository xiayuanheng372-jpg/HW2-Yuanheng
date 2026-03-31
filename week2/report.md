# Report: Week 2 GenAI Workflow

## Business Use Case

This prototype automates the first draft of customer support replies for an e-commerce company. When a customer submits a message — whether a complaint, question, or request — the system generates a professional, empathetic draft reply for a support agent to review and send. The goal is to reduce the time agents spend on routine, repetitive replies and allow them to focus on complex or escalated cases.

## Model Choice

The prototype uses **Llama 3.1 8B Instant** via the Groq API. Groq was chosen because it offers a free tier with no regional restrictions, fast inference, and an OpenAI-compatible API that made integration straightforward. Google Gemini (the originally recommended model) was unavailable due to free-tier quota restrictions. Llama 3.1 8B Instant produced fluent, well-structured replies suitable for a customer support context.

## Baseline vs. Final Design

**Version 1 (baseline):** The initial system instruction produced replies that were polite and relevant, but too long for practical use. In Case 5 (return policy question), the model fabricated a specific "30-day return policy" with confidence — a clear hallucination with no factual basis.

**Version 2:** Adding a 150-word limit and a conciseness instruction significantly shortened replies without losing helpfulness. The hallucination in Case 5 persisted, however, because the instruction to "not guess" was too vague.

**Version 3 (final):** Replacing the vague instruction with an explicit rule — "NEVER state specific policy details unless provided" — and supplying a safe fallback phrase ("I'd be happy to look into that for you") eliminated the hallucination in Case 5. The model now deflects policy questions appropriately rather than inventing answers.

## Where the Prototype Still Fails

The prototype still requires human review in several situations. Even in Version 3, the model occasionally provides overly generic responses to edge cases (e.g., "I'm not happy") that may feel dismissive if sent without personalization. The pairing instructions in Case 3 are plausible but not specific to any actual product — an agent must verify accuracy before sending. More broadly, the system has no access to real order data, customer history, or company policy documents, which limits its usefulness to draft assistance only.

## Deployment Recommendation

This prototype is **not ready for autonomous deployment** but shows clear value as a draft-assist tool. I would recommend deploying it in a human-in-the-loop configuration: the model generates a draft, and a support agent reviews, edits, and sends it. Before deployment, the system should be connected to real policy documents and order data to reduce hallucination risk, and the prompt should be tested against a larger, more diverse evaluation set. With those additions, this workflow could meaningfully reduce agent workload while maintaining reply quality.
