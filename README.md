
# Celebrity_Search

Integration of Openai in any project using Langchain.

For demonstration purpose we use streamlit library to create a small project. We create it in two phase :-


## Phase 1

- Integration of Openai model with our project in which we can search by celebrity name and it will provide us the information about the celebrity using the openai model.

## Phase 2

- This phase focus on LLMchains, buffer memory and prompt templates.
## Run Locally

Clone the project

```bash
  git clone https://github.com/Nirbhay09Singh/Celebrity_Search
```

Go to the project directory

```bash
  cd Celebrity_Search
```

You need Python version-3.8 or above.

Install all the required libraries

```bash
  pip install -r requirement.txt
```

Go to the openai website, get an api key and paste it in the constant.py

Now, you can run phase-1

```bash
  streamlit run phase_1.py
```

Or run phase-2

```bash
  streamlit run phase_2.py
```