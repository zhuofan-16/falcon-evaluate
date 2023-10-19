import pandas as pd
import numpy as np
import warnings
from .evaluate import FalconEvaluator
warnings.filterwarnings("ignore")


class ModelScoreSummary:
    """_summary_

    This class is used to generate the summary of the scores generated by the models

        # Example usage:

        model_score_summary = ModelScoreSummary(df)

        summary_df = model_score_summary.execute_summary()

        print(summary_df)

    """
    def __init__(self, data: pd.DataFrame):

        self.data = data

        cols_to_drop = ['prompt', 'reference']

        self.models = [ x for x in self.data.columns if x not in cols_to_drop]  # Update the list of model identifiers as per your dataset

    def safe_eval(self, x):
        """
        Safely evaluate the expression and return the result.
        If an error occurs, it logs the error message and returns None.
        """
        try:
            return eval(x)
        except Exception as e:
            print(f"Error evaluating '{x}': {e}")
            return None

    def extract_scores(self, column_name):

        return self.data[column_name].apply(self.safe_eval)


    def generate_summary(self,score_keys):

        summary_df = pd.DataFrame(columns=['Model'] + score_keys )

        self.models_sel_cols = [col for col in self.data.columns if '-Scores' in col]

        print(self.models_sel_cols )

        for model in self.models_sel_cols:
            average_scores = {'Model': model}
            text_scores = self.extract_scores(f"{model}")

            for key in score_keys:
                valid_scores = text_scores.apply(lambda x: x.get(key, None) if x else None).dropna()
                if valid_scores.empty:
                    print(f"No valid scores found for model {model}, key {key}")

                average_scores[key] = valid_scores.mean()

            summary_df = summary_df.append(average_scores, ignore_index=True)

        return summary_df


    def execute_summary(self):

        evaluator = FalconEvaluator(self.data)

        evaluation_results = evaluator.evaluate()

        #print(evaluation_results)

        #model_score_summary = ModelScoreSummary(evaluation_results)

        #score_keys=['bleu_score', 'jaccard_similarity', 'cosine_similarity', 'semantic_similarity']

        #summary_df = model_score_summary.generate_summary(score_keys)

        #print(summary_df)

        return evaluation_results

"""
# Usage example:
# Ideally user will pass this dataframe as input "prompt" &  "reference" columns are mandatory and rest of the columns are model generated outputs

df = pd.DataFrame({
    'prompt': [
        "What is the capital of France?", 
        "What is the capital of Germany?",
        "What is the capital of Italy?",
        "What is the capital of Spain?",
        "What is the capital of Portugal?",
        "What is the capital of Greece?",
        "What is the capital of Poland?",
        "What is the capital of Belgium?",
        "What is the capital of Netherlands?",
        "What is the capital of Austria?"
    ],
    'reference': [
        "The capital of France is Paris.",
        "The capital of Germany is Berlin.",
        "The capital of Italy is Rome.",
        "The capital of Spain is Madrid.",
        "The capital of Portugal is Lisbon.",
        "The capital of Greece is Athens.",
        "The capital of Poland is Warsaw.",
        "The capital of Belgium is Brussels.",
        "The capital of Netherlands is Amsterdam.",
        "The capital of Austria is Vienna."
    ],
    'Model A': [
        "Paris is the capital of France.",
        "Berlin is Germany’s capital.",
        "Rome is the capital of Italy.",
        "Madrid is the capital of Spain.",
        "Lisbon is the capital of Portugal.",
        "Athens is the capital of Greece.",
        "Warsaw is the capital of Poland.",
        "Brussels is the capital of Belgium.",
        "Amsterdam is the capital of Netherlands.",
        "Vienna is the capital of Austria."
    ],
    'Model B': [
        "Capital of France is Paris.",
        "Germany’s capital city is Berlin.",
        "Italy's capital city is Rome.",
        "Spain's capital is Madrid.",
        "Portugal's capital is Lisbon.",
        "Capital of Greece is Athens.",
        "Poland’s capital city is Warsaw.",
        "Capital city of Belgium is Brussels.",
        "Netherlands has Amsterdam as its capital.",
        "Capital of Austria? It's Vienna."
    ],
    'Model C': [
        "Capital of France was Paris.",
        "Germany’s capital city is not Berlin.",
        "Was Rome the capital of Italy?",
        "Madrid, Spain's capital?",
        "Is Lisbon the main city of Portugal?",
        "Athens might be the capital of Greece.",
        "Warsaw was the main city of Poland.",
        "Isn’t Brussels the heart of Belgium?",
        "Amsterdam, known as the Netherlands' capital.",
        "Vienna stands as Austria's capital."
    ],
})

# Below codes to be converted into a function in above class

model_score_summary = ModelScoreSummary(df)
result = model_score_summary.execute_summary()
print(result)
"""