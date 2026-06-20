import json

# Load sections
with open("sections.json", encoding="utf-8") as f:
    sections = json.load(f)


def retrieve(question, top_k=3):
    results = []

    query_words = question.lower().split()

    for section in sections:
        score = 0

        text = (section["title"] + " " + section["content"]).lower()

        for word in query_words:
            if word in text:
                score += 1

        results.append((score, section))

    results.sort(key=lambda x: x[0], reverse=True)

    return [item[1] for item in results[:top_k]]


question = input("Ask Question: ")

matches = retrieve(question)

for i, match in enumerate(matches, start=1):
    print("\n")
    print("=" * 60)

    print(f"Result {i}")

    print("=" * 60)

    print(match["title"])

    print()

    print(match["content"][:500])
