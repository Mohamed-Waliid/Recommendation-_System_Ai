import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Load the Dataset
file_path = "./Career Dataset.xlsx"  

# Debug: Print current working directory
print("Current working directory:", os.getcwd())

try:
    data = pd.read_excel(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    print("Please ensure the file is in the correct location.")
    raise

# Step 2: Preprocessing
# Convert "User Skills" into a Bag-of-Words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['Skills'])

# Encode "Track" as labels
y = data['Track']

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: Make Predictions
def recommend_track(user_skills):
    """Predict the track based on user skills."""
    user_skills_vectorized = vectorizer.transform([user_skills])
    prediction = model.predict(user_skills_vectorized)
    return prediction[0]

# Example Usage
example_skills = input("Enter your skills: ")
recommended_track = recommend_track(example_skills)
print(f"Recommended Track for '{example_skills}': {recommended_track}")
