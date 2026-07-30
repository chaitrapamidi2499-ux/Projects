import pandas as pd
from fuzzywuzzy import fuzz
from rouge_score import rouge_scorer

# ✅ Load the files
predicted_path = "rag_answers_output2.csv"
expected_path = "rfp_expected_answers_filled.csv"

pred_df = pd.read_csv(predicted_path)
exp_df = pd.read_csv(expected_path)

# ✅ Initialize scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

results = []
pass_count = 0

# ✅ Evaluate each question
for _, row in pred_df.iterrows():
    question = row["Question"]
    actual_answer = str(row["Answer"]).lower()

    match = exp_df[exp_df["Question"] == question]

    if not match.empty:
        expected_answer = str(match.iloc[0]["Expected Answer Snippet"]).lower()

        # ✅ Fuzzy score
        fuzzy_score = fuzz.partial_ratio(actual_answer, expected_answer)

        # ✅ ROUGE scores
        rouge = scorer.score(expected_answer, actual_answer)
        rouge1 = round(rouge['rouge1'].fmeasure, 3)
        rouge2 = round(rouge['rouge2'].fmeasure, 3)
        rougel = round(rouge['rougeL'].fmeasure, 3)

        # ✅ Define pass criteria (adjust if needed)
        passed = fuzzy_score >= 70 or rougel >= 0.6
        if passed:
            pass_count += 1

        results.append({
            "Question": question,
            "Expected": expected_answer,
            "Predicted": actual_answer,
            "Fuzzy Score": fuzzy_score,
            "ROUGE-1 F1": rouge1,
            "ROUGE-2 F1": rouge2,
            "ROUGE-L F1": rougel,
            "Passed": "✅" if passed else "❌"
        })
    else:
        results.append({
            "Question": question,
            "Expected": "❌ Not found in expected list",
            "Predicted": actual_answer,
            "Fuzzy Score": 0,
            "ROUGE-1 F1": 0,
            "ROUGE-2 F1": 0,
            "ROUGE-L F1": 0,
            "Passed": "❌"
        })

# ✅ Save output
results_df = pd.DataFrame(results)
results_df.to_csv("evaluation_with_rouge1.csv", index=False)

# ✅ Print summary
accuracy = (pass_count / len(results_df)) * 100
print(f"\n✅ Evaluation Complete — Accuracy: {accuracy:.2f}%")
print("📁 Saved to: evaluation_with_rouge.csv")
