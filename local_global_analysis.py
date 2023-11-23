import math
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]
def tokenize(document):
    return document.split()
def term_frequency(term, document):
    tokens = tokenize(document)
    return tokens.count(term)
def inverse_document_frequency(term, documents):
    num_documents_with_term = sum(1 for document in documents if term in tokenize(document))
    return math.log(len(documents) / (1 + num_documents_with_term))
def tf_idf(term, document, documents):
    tf = term_frequency(term, document)
    idf = inverse_document_frequency(term, documents)
    return tf * idf
query = "this document"
query_tokens = tokenize(query)
document_scores = []
for doc in documents:
    score = sum(tf_idf(term, doc, documents) for term in query_tokens)
    document_scores.append((doc, score))
document_scores.sort(key=lambda x: x[1], reverse=True)
print("Ranked Documents (Global Analysis):")
for doc, score in document_scores:
    print(f"Document: {doc}, Score: {score}")
document_index = 1  
document = documents[document_index]
term_scores = []
for term in query_tokens:
    score = tf_idf(term, document, documents)
    term_scores.append((term, score))
