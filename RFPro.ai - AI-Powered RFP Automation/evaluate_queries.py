import pandas as pd
from answering import query_rag_with_varag  # ✅ Import from above file

# ✅ Load CSV of questions
CSV_PATH = r"E:\All My Projects\Capstone\Capstone\GenAI_RFP_Question_Data_Input_Jun_2024_25.xlsx - Sample 25 RFP Questions.csv"
df = pd.read_csv(CSV_PATH)

results = []

# ✅ Run through all questions
for i, row in df.iterrows():
    q = row['Question']
    print(f"\n🔹 [{i+1}/{len(df)}] Question: {q}")
    answer, _ = query_rag_with_varag(q)
    results.append({"Question": q, "Answer": answer})

# ✅ Save output
df_out = pd.DataFrame(results)
df_out.to_csv("rag_answers_output2.csv", index=False)
print("\n✅ Results saved to rag_answers_output.csv")
