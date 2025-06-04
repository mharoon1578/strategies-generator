import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from prompts import strategy_prompt

st.title("Psychological Business Strategy Generator")
st.markdown("""
Get smart strategies using **psychology, behavioral economics, and persuasion**.
Provide your business type and target audience. Optionally, add extra context or details.
""")

GROQ_API_KEY = st.text_input(
    "Enter your Groq API Key",
    type="password",
    placeholder="Paste your Groq API key here",
    help="Get your API key from https://developer.groq.com",
)

business_type = st.text_input(
    "What kind of business is it?",
    placeholder="e.g. SaaS for freelancers",
    help="Briefly describe your business model or product."
)

target_audience = st.text_input(
    "Who is the target audience?",
    placeholder="e.g. Gen Z creators, B2B CMOs",
    help="Define the primary audience you're targeting."
)

extra_context = st.text_area(
    "Optional Details (Context, goals, pain points, etc.)",
    height=150,
    placeholder="Add anything specific you'd like the strategy to consider...",
    help="This can include brand values, pain points, growth stage, etc."
)

if st.button("Generate Strategies"):
    if not GROQ_API_KEY:
        st.warning("⚠️ Please enter your Groq API key to proceed.")
    elif not business_type.strip() or not target_audience.strip():
        st.warning("⚠️ Business type and target audience are required.")
    else:
        llm = ChatGroq(
            temperature=0.7,
            model_name="mistral-saba-24b",
            groq_api_key=GROQ_API_KEY
        )
        chain = LLMChain(llm=llm, prompt=strategy_prompt)

        with st.spinner("Generating psychology-driven strategies..."):
            try:
                response = chain.run(
                    business_type=business_type,
                    target_audience=target_audience,
                    extra_context=extra_context or ""
                )
                st.subheader("Strategic Insights")
                st.markdown(response)
            except Exception as e:
                st.error(f"❌ Error: {e}")
