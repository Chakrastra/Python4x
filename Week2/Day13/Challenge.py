import pandas as pd
data = {
    'Name': ['Ram','Shyam', 'Rohit', 'Mohit'],
    'Age': [21, 40, 32, 28],
    'Score': [90, 94, 68, 92]
}

df = pd.DataFrame(data)

avg_age = df['Age'].mean()

max_score = df['Score'].max()

print(f"Average Age is: {avg_age}\n Maximum Score is: {max_score}")