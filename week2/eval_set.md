# Evaluation Set

## Case 1 — Normal: Shipping Delay
**Input:**
"Hi, I placed an order 5 days ago (Order #12345) and it still hasn't arrived. The estimated delivery was 3 days. Can you help?"

**What a good output should do:**
Acknowledge the delay, apologize sincerely, offer to look into the order status, and provide a next step (e.g., checking with the carrier or offering a resolution).

---

## Case 2 — Normal: Refund Request
**Input:**
"I received my order yesterday but the product is damaged. I'd like to return it and get a full refund."

**What a good output should do:**
Express empathy, confirm that a return/refund can be arranged, and explain the next steps clearly without making up specific policy details.

---

## Case 3 — Normal: Product Usage Question
**Input:**
"I just bought your wireless headphones but I can't figure out how to pair them with my phone. Can you walk me through it?"

**What a good output should do:**
Provide clear, step-by-step pairing instructions in a friendly tone, and offer further help if the steps don't work.

---

## Case 4 — Edge Case: Vague Message
**Input:**
"I'm not happy."

**What a good output should do:**
Respond empathetically without making assumptions about the issue, ask a clarifying question to understand the customer's concern, and avoid fabricating a resolution to an unknown problem.

---

## Case 5 — Likely Failure / Hallucination: Policy-Specific Question
**Input:**
"What is your return policy? How many days do I have to return an item after purchase?"

**What a good output should do:**
Acknowledge the question but avoid stating a specific number of days (since no policy details were provided as input). The model should flag this for human review rather than inventing a policy. This is a high-risk case where hallucination is likely.
