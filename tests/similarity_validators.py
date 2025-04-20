import en_core_web_sm


def validate_output(actual_output, expected_output):
    nlp = en_core_web_sm.load()
    doc1 = nlp(actual_output)
    doc2 = nlp(expected_output)
    similarity = doc1.similarity(doc2)

    # Define the similarity threshold
    threshold = 0.8  # 0.8 is 80% similarity threshold

    if similarity >= threshold:
        return True, f"Output matches expected result. Similarity: {similarity:.2f}"
    else:
        return False, f"Output mismatch. Similarity: {similarity:.2f}"
