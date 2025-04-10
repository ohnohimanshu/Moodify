from transformers import pipeline

# Load emotion classification model
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def detect_moods_from_text(text):
    # Use the classifier to get emotion scores
    results = classifier(text)
    # Sort emotions by score in descending order and get the top 3
    top_moods = sorted(results[0], key=lambda x: x['score'], reverse=True)[:3]
    return [mood['label'] for mood in top_moods]
