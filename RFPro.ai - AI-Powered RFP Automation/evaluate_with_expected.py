import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# ✅ Paths to your files
predicted_path =r"E:\Capstone\rag_answers_output.csv"
expected_path = r"E:\Capstone\Capstone\rfp_expected_answers_filled.csv"

# ✅ Load both files
pred_df = pd.read_csv(predicted_path)
exp_df = pd.read_csv(expected_path)

# ✅ Safety check
if "Question" not in pred_df.columns or "Answer" not in pred_df.columns:
    raise Exception("Your rag_answers_output.csv must have 'Question' and 'Answer' columns.")

if "Question" not in exp_df.columns or "Expected Answer Snippet" not in exp_df.columns:
    raise Exception("Your rfp_expected_answers.csv must have 'Question' and 'Expected Answer Snippet' columns.")

# ✅ Match each question and compare answers
results = []
pass_count = 0

for i, row in pred_df.iterrows():
    question = row["Question"]
    actual_answer = str(row["Answer"]).lower()

    # Find matching expected answer
    match = exp_df[exp_df["Question"] == question]

    if not match.empty:
        expected_answer = str(match.iloc[0]["Expected Answer Snippet"]).lower()
        score = fuzz.partial_ratio(actual_answer, expected_answer)
        passed = score >= 70  # ✅ Pass if ≥ 70% similarity

        results.append({
            "Question": question,
            "Expected": expected_answer,
            "Predicted": actual_answer,
            "Score": score,
            "Passed": "✅" if passed else "❌"
        })

        if passed:
            pass_count += 1
    else:
        results.append({
            "Question": question,
            "Expected": "❌ Not found in expected list",
            "Predicted": actual_answer,
            "Score": 0,
            "Passed": "❌"
        })

# ✅ Save results
results_df = pd.DataFrame(results)
results_df.to_csv("evaluation_results.csv", index=False)

accuracy = (pass_count / len(results)) * 100
print(f"\n🎯 Evaluation Complete — Accuracy: {accuracy:.2f}%")
print("📁 Results saved to evaluation_results.csv")
