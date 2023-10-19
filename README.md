<div align="center">
  <img src="img/Falcon_Evaluate.png" alt="Falcon Evaluate Logo">
</div>

# Falcon Evaluate

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/travis/user/repo.svg)](https://github.com/Praveengovianalytics/falcon_evaluate)
[![GitHub issues](https://img.shields.io/github/issues/Praveengovianalytics/falcon-evaluate)](https://github.com/Praveengovianalytics/falcon-evaluate/issues)
[![GitHub release](https://img.shields.io/github/release/Praveengovianalytics/falcon-evaluate)](https://github.com/Praveengovianalytics/falcon-evaluate/releases)

<h4 align="center">
    <p>
        <a href="#shield-installation">Installation</a> |
        <a href="#fire-quickstart">Quickstart</a> |
    <p>
</h4>

Falcon Evaluate
==============================

Falcon Evaluate is an open-source Python library designed to simplify the process of evaluating and validating open source LLM models such as llama2,mistral ,etc. This library aims to provide an easy-to-use toolkit for assessing the performance, bias, and general behavior of LLMs in various natural language understanding (NLU) tasks.


# Falcon Evaluate - A Language Model Validation Library

## Overview
Falcon Evaluate is an open-source Python library designed to simplify the process of evaluating and validating Language Models (LLMs) such as GPT-3.5 and other similar models. This library aims to provide an easy-to-use toolkit for assessing the performance, bias, and general behavior of LLMs in various natural language understanding (NLU) tasks.

## :shield: Installation

```bash
pip install falcon_evaluate -q
```


if you want to install from source

```bash
git clone https://github.com/Praveengovianalytics/falcon_evaluate && cd falcon_evaluate
pip install -e .
```


## :fire: Quickstart

###  Google Colab notebook

- [Get start with falcon_evaluate](https://colab.research.google.com/drive/1h9E0Q5Fema9TkOiv0asyaSaHin1R0UN5?usp=sharing)

```python
# Example usage

!pip install falcon_evaluate -q

from falcon_evaluate.fevaluate_results import ModelScoreSummary
import pandas as pd
import nltk
nltk.download('punkt')

df = pd.DataFrame({
    'prompt': [
        "What is the capital of France?"
    ],
    'reference': [
        "The capital of France is Paris."
    ],
    'Model A': [
        "Paris is the capital of France.
    ],
    'Model B': [
        "Capital of France is Paris."
    ],
    'Model C': [
        "Capital of France was Paris."
    ],
})

model_score_summary = ModelScoreSummary(df)
result = model_score_summary.execute_summary()
print(result)

```

# Model Evaluation Results

The following table shows the evaluation results of different models when prompted with a question. Various scoring metrics such as BLEU score, Jaccard similarity, Cosine similarity, and Semantic similarity have been used to evaluate the models. Additionally, composite scores like Falcon Score have also been calculated.

## Evaluation Data

| Prompt                         | Reference                     |
|--------------------------------|-------------------------------|
| What is the capital of France? | The capital of France is Paris.|

## Model A Evaluation

#### Readability and Complexity

- ARI: 2.7
- Flesch-Kincaid Grade Level: 2.9

#### Language Modeling Performance

- Perplexity: 112.17

#### Text Toxicity

- Toxicity Level: 0.09

#### Text Similarity and Relevance

- BLEU: 0.64
- Cosine Similarity: 0.85
- Semantic Similarity: 0.99
- Jaccard Similarity: 0.71

#### Information Retrieval

- Precision: 0.83
- Recall: 0.71
- F1-Score: 0.77

## Falcon Score (Model A)

## Evaluation Categories Metrics

Below are the computed metrics categorized under different evaluation categories:

### Readability and Complexity

- Arithmetic Mean: 1.65
- Weighted Sum: 1.65
- Geometric Mean: 1.59
- Harmonic Mean: 1.53
- T-Statistic: 2.12
- P-Value: 0.28
- F-Score: 0.00
- Z-Score Normalization: [-1.00, 1.00]

### Language Modeling Performance

- Arithmetic Mean: 19.45
- Weighted Sum: 19.45
- Geometric Mean: 19.45
- Harmonic Mean: 19.45
- T-Statistic: NaN
- P-Value: NaN
- F-Score: 0.00
- Z-Score Normalization: [NaN]

### Text Toxicity

- Arithmetic Mean: 0.046
- Weighted Sum: 0.046
- Geometric Mean: 0.046
- Harmonic Mean: 0.046
- T-Statistic: NaN
- P-Value: NaN
- F-Score: 0.00
- Z-Score Normalization: [NaN]

### Text Similarity and Relevance

- Arithmetic Mean: 0.67
- Weighted Sum: 0.67
- Geometric Mean: 0.00
- Harmonic Mean: 0.00
- T-Statistic: 1.29
- P-Value: 0.29
- F-Score: 0.00
- Z-Score Normalization: [-1.67, 0.82, 0.73, 0.11]

### Information Retrieval

- Arithmetic Mean: 0.77
- Weighted Sum: 0.77
- Geometric Mean: 0.77
- Harmonic Mean: 0.77
- T-Statistic: 11.23
- P-Value: 0.01
- F-Score: 0.77
- Z-Score Normalization: [1.25, -1.19, -0.06]


## Model B Evaluation

| Response                    | Scores |
|-----------------------------|--------|
| Capital of France is Paris. |  |

## Model A Evaluation scores

### Readability and Complexity:
- **ARI**: 2.7
- **Flesch-Kincaid Grade Level**: 2.9

### Language Modeling Performance:
- **Perplexity**: 112.17

### Text Toxicity:
- **Toxicity Level**: 0.09

### Text Similarity and Relevance:
- **BLEU**: 0.64
- **Cosine Similarity**: 0.85
- **Semantic Similarity**: 0.99
- **Jaccard Similarity**: 0.71

### Information Retrieval:
- **Precision**: 0.83
- **Recall**: 0.71
- **F1-Score**: 0.77

### Kindly refer the google colab notebook for more details

## Key Features

1. **Benchmarking:** Falcon Evaluate provides a set of pre-defined benchmarking tasks commonly used for evaluating LLMs, including text completion, sentiment analysis, question answering, and more. Users can easily assess model performance on these tasks.

2. **Custom Evaluation:** Users can define custom evaluation metrics and tasks tailored to their specific use cases. Falcon Evaluate provides flexibility for creating custom test suites and assessing model behavior accordingly.

3. **Interpretability:** The library offers interpretability tools to help users understand why the model generates certain responses. This can aid in debugging and improving model performance.

4. **Scalability:** Falcon Evaluate is designed to work with both small-scale and large-scale evaluations. It can be used for quick model assessments during development and for extensive evaluations in research or production settings.

## Use Cases
- Model Development: Falcon Evaluate can be used during the development phase to iteratively assess and improve the performance of LLMs.
- Research: Researchers can leverage the library to conduct comprehensive evaluations and experiments with LLMs, contributing to advancements in the field.
- Production Deployment: Falcon Evaluate can be integrated into NLP pipelines to monitor and validate model behavior in real-world applications.

## Getting Started
To use Falcon Evaluate, users will need Python and dependencies such as TensorFlow, PyTorch, or Hugging Face Transformers. The library will provide clear documentation and tutorials to assist users in getting started quickly.

## Community and Collaboration
Falcon Evaluate is an open-source project that encourages contributions from the community. Collaboration with researchers, developers, and NLP enthusiasts is encouraged to enhance the library's capabilities and address emerging challenges in language model validation.

## Project Goals
The primary goals of Falcon Evaluate are to:
- Facilitate the evaluation and validation of Language Models.
- Promote transparency and fairness in AI by detecting and mitigating bias.
- Provide an accessible and extensible toolkit for NLP practitioners and researchers.

## Conclusion
Falcon Evaluate aims to empower the NLP community with a versatile and user-friendly library for evaluating and validating Language Models. By offering a comprehensive suite of evaluation tools, it seeks to enhance the transparency, robustness, and fairness of AI-powered natural language understanding systems.



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── falcon_evaluate    <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io




--------