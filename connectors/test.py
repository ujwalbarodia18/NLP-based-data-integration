# import spacy

# # # load the pre-trained model with word embeddings
# nlp = spacy.load(
#     'E:/en_core_web_md-3.0.0/en_core_web_md-3.0.0/en_core_web_md/en_core_web_md-3.0.0')


# # def preprocess_text(text):
# #     """Preprocess text by removing stop words, punctuation, and converting to lowercase."""
# #     doc = nlp(text.lower())
# #     tokens = [
# #         token.text for token in doc if not token.is_stop and not token.is_punct]
# #     return " ".join(tokens)


# attr1 = "custname"
# attr2 = "cname"
# # print(preprocess_text(attr1))

# # preprocessed_attr1 = preprocess_text(attr1)
# # preprocessed_attr2 = preprocess_text(attr2)

# similarity_score = nlp(attr1).similarity(nlp(attr2))
# print(similarity_score)
# similarity_score = nlp(preprocessed_attr1).similarity(nlp(preprocessed_attr2))

# print(f"Similarity score between {attr1} and {attr2}: {similarity_score}")

# from nltk.corpus import wordnet
# import nltk
# nltk.download('wordnet')


# def get_word_similarity_score(word1, word2):
#     synset1 = wordnet.synsets(word1)
#     synset2 = wordnet.synsets(word2)
#     if synset1 and synset2:
#         wup_similarities = []
#         for s1 in synset1:
#             for s2 in synset2:
#                 wup_similarities.append(s1.wup_similarity(s2))
#         if wup_similarities:
#             return max(wup_similarities)
#     return 0


# word1 = 'car'
# word2 = 'vehicle'
# similarity_score = get_word_similarity_score(word1, word2)
# print(f"Similarity score between '{word1}' and '{word2}': {similarity_score}")

from difflib import SequenceMatcher

# Define two words
word1 = 'customerid'
word2 = 'customername'

# Compute the similarity ratio
similarity_ratio = SequenceMatcher(None, word1, word2).ratio()

# Print the similarity ratio
print(
    f"The similarity ratio between '{word1}' and '{word2}' is {similarity_ratio}")
