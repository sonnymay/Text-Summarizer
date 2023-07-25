import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')  # Download the Punkt sentence tokenizer
nltk.download('stopwords')  # Download stopwords

def summarize(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    
    # Calculate frequency distribution
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1
    
    # Calculate sentence scores
    sentences = sent_tokenize(text)
    sentence_scores = dict()
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq
                else:
                    sentence_scores[sentence] = freq
                    
    # Get the N highest-scoring sentences. Let's use the average sentence score as the threshold.
    avg_score = int(sum(sentence_scores.values()) / len(sentence_scores))
    summary = [sentence for sentence, score in sentence_scores.items() if score > avg_score]
    return ' '.join(summary)

# Example usage:
text = """
The Industrial Revolution, which took place from the 18th to 19th centuries, was a period during which predominantly agrarian, rural societies in Europe and America became industrial and urban. Prior to the Industrial Revolution, which began in Britain in the late 1700s, manufacturing was often done in people’s homes, using hand tools or basic machines. Industrialization marked a shift to powered, special-purpose machinery, factories and mass production. The iron and steel industry spawned new construction materials, the railroads connected the country and the discovery of oil provided a new source of fuel. The invention of the telegraph, telephone, radio and computer set the stage for this unprecedented integration of capabilities.
"""
summary = summarize(text)
print(summary)
