from openai import OpenAI
import os
import json
from datetime import datetime

# Set your API key as an environment variable: export GROQ_API_KEY="your_key_here"
API_KEY = os.environ.get("GROQ_API_KEY", "")

# --- Configurable system instruction ---
SYSTEM_INSTRUCTION = """
You are a professional customer support agent for an e-commerce company.
When given a customer message, write a polite, empathetic, and helpful reply.
- Acknowledge the customer's concern
- Provide a clear next step or resolution
- Keep the tone friendly and professional
- If you do not have enough information (e.g., specific policy details), say so and ask for clarification instead of guessing
"""

def draft_reply(customer_message: str) -> str:
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=API_KEY
    )
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": customer_message}
        ]
    )
    return response.choices[0].message.content

def run_eval_set():
    eval_cases = [
        {
            "id": 1,
            "type": "Normal",
            "input": "Hi, I placed an order 5 days ago (Order #12345) and it still hasn't arrived. The estimated delivery was 3 days. Can you help?"
        },
        {
            "id": 2,
            "type": "Normal",
            "input": "I received my order yesterday but the product is damaged. I'd like to return it and get a full refund."
        },
        {
            "id": 3,
            "type": "Normal",
            "input": "I just bought your wireless headphones but I can't figure out how to pair them with my phone. Can you walk me through it?"
        },
        {
            "id": 4,
            "type": "Edge Case",
            "input": "I'm not happy."
        },
        {
            "id": 5,
            "type": "Likely Failure",
            "input": "What is your return policy? How many days do I have to return an item after purchase?"
        },
    ]

    results = []
    print("=" * 60)
    print("Customer Support Reply Generator — Evaluation Run")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    for case in eval_cases:
        print(f"\n[Case {case['id']}] Type: {case['type']}")
        print(f"Customer: {case['input']}")
        reply = draft_reply(case["input"])
        print(f"Draft Reply:\n{reply}")
        print("-" * 60)
        results.append({
            "id": case["id"],
            "type": case["type"],
            "input": case["input"],
            "output": reply
        })

    output_file = "eval_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    run_eval_set()
