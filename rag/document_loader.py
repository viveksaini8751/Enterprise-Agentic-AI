def load_csv(file_path):

    documents = []

    with open(file_path, "r", encoding="utf-8-sig") as file:

        # Skip header
        next(file)

        for row_number, line in enumerate(file, start=1):

            line = line.strip()

            if not line:
                continue

            parts = line.rsplit(",", 2)

            if len(parts) != 3:
                continue

            text = parts[0].strip()
            label = parts[1].strip()
            word_count = parts[2].strip()

            documents.append({
                "id": row_number,
                "text": text,
                "label": label,
                "word_count": word_count
            })

    return documents


if __name__ == "__main__":

    documents = load_csv("data/company-document-text.csv")

    print("CSV Successfully Loaded!")
    print("Total Documents:", len(documents))

    print("\nFirst 3 Documents:\n")

    for document in documents[:3]:

        print(document["text"])
        print("Label:", document["label"])
        print("Word Count:", document["word_count"])
        print("-" * 50)