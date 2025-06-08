#testing code
from backend.diff import compare_documents
from backend.llm import analyze_change
import time

changes = compare_documents('data/Text_v1.txt', 'data/Text_v2.txt')
for i, change in enumerate(changes):
    if change["type"] in ("added", "modified"):
        print(f"Analyzing change {i+1}/{len(changes)}...")
        analysis = analyze_change(change)
        change.update(analysis)
        time.sleep(0.5)  

for change in changes:
    print("\n----------------------------")
    print(f"Change Type: {change['type']}")
    if 'old' in change:
        print(f"OLD:\n{change['old']}")
    if 'new' in change:
        print(f"NEW:\n{change['new']}")
    if 'change_summary' in change:
        print(f"Summary: {change['change_summary']}")
    if 'change_type' in change:
        print(f"LLM Label: {change['change_type']}")
