
# Psychological Business Strategy Maker

A Streamlit app that generates actionable, psychology-driven business strategies using the Groq API powered by the **mistral-saba-24b** language model.

---

## Features

* Input your **business type** and **target audience**.
* Optionally add **detailed context** or goals.
* Enter your Groq API key directly in the app UI.
* Receive tailored strategy suggestions based on psychological principles.
* Instantly see AI-powered insights to boost persuasion, sales, and engagement.

---

## Getting Started

### Prerequisites

* Python 3.8+
* Groq API key (get one at [https://developer.groq.com](https://developer.groq.com))
* Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mharoon1578/strategies-generator.git
   cd psychological-strategy-maker
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Run the App

```bash
streamlit run app.py
```

---

## How to Use

1. Open the app in your browser (`http://localhost:8501` by default).
2. Fill in your **business type** (e.g., SaaS tool, consulting agency).
3. Enter your **target audience** (e.g., small business owners, Gen Z, real estate agents).
4. Optionally provide **extra context** like goals, market, or pain points.
5. Paste your **Groq API key** in the input box.
6. Click the **Generate Strategy** button.
7. View a set of personalized, psychological strategies powered by AI.

---

## Important Notes

* The app requires a valid **Groq API key** to function.
* Your inputs are sent securely to Groq's API and are not stored.
* You don’t need to configure `.env` — just paste your key into the app UI.

---

## File Structure

```
├── app.py                  # Main Streamlit app logic
├── prompts.py              # Contains the prompt for generating strategies
├── requirements.txt        # Dependency list
├── README.md               # This file
└── .env.example            # Example environment file (optional)
```

---

## Dependencies

* streamlit
* langchain
* langchain\_groq
* python-dotenv

---

## License

MIT License

---

## Contact

For questions, suggestions, or issues, feel free to open an issue or reach out to me at **[mharoon1578@gmail.com](mailto:mharoon1578@gmail.com)**.
