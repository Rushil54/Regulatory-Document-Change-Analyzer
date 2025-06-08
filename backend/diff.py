import difflib

def load_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    return paragraphs

def compare_documents(v1_path, v2_path, similarity_threshold=0.75):
    old_paragraphs = load_paragraphs(v1_path)
    new_paragraphs = load_paragraphs(v2_path)

    changes = []

    matched_old = set()
    matched_new = set()

    for i, new_para in enumerate(new_paragraphs):
        best_match_index = -1
        best_ratio = 0

        for j, old_para in enumerate(old_paragraphs):
            if j in matched_old:
                continue
            ratio = difflib.SequenceMatcher(None, new_para, old_para).ratio()
            if ratio > best_ratio:
                best_match_index = j
                best_ratio = ratio

        if best_ratio >= similarity_threshold:
            matched_old.add(best_match_index)
            matched_new.add(i)
            if best_ratio < 0.95:
                changes.append({
                    "type": "modified",
                    "old": old_paragraphs[best_match_index],
                    "new": new_para,
                })
        else:
            changes.append({
                "type": "added",
                "new": new_para,
            })

    for j, old_para in enumerate(old_paragraphs):
        if j not in matched_old:
            changes.append({
                "type": "deleted",
                "old": old_para,
            })

    return changes
