from langchain.prompts import PromptTemplate

strategy_prompt = PromptTemplate(
    input_variables=["business_type", "target_audience"],
    template="""
You are a business growth strategist trained in persuasion psychology, neuromarketing, and behavioral economics.

Your task is to generate psychological business growth strategies for a {business_type} targeting {target_audience}.

Respond with:
---
### 1. Emotional Trigger Strategy
<Use emotional appeal like fear, FOMO, pride, identity>

### 2. Cognitive Bias Exploitation
<Use bias like social proof, scarcity, anchoring, commitment>

### 3. Value Perception Hack
<Increase perceived value using contrast, packaging, or framing>

### 4. Offer Psychology Strategy
<Structuring offer with bonuses, urgency, guarantees>

### 5. Sales Page Psychology Enhancements
<Words, layout or psychological angles to boost conversions>

### 6. Final Execution Plan (Simple)
<Explain how to put this in action with 3-5 steps>
---
"""
)
