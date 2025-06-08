import streamlit as st
from backend.diff import compare_documents
from backend.llm import analyze_change
import tempfile
import time

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


st.title("Regulatory Change Analyzer")
file1 = st.file_uploader("Upload OLD version", type="txt")
file2 = st.file_uploader("Upload NEW version", type="txt")

if st.button("Analyze Changes") and file1 and file2:
    with tempfile.NamedTemporaryFile(delete=False) as tmp1, tempfile.NamedTemporaryFile(delete=False) as tmp2:
        tmp1.write(file1.read())
        tmp2.write(file2.read())
        tmp1_path = tmp1.name
        tmp2_path = tmp2.name

    st.info("Comparing documents...")
    changes = compare_documents(tmp1_path, tmp2_path)
    limited_changes = [c for c in changes if c["type"] in ("added", "modified")][:30]

    analyzed_changes = []
    for i, change in enumerate(limited_changes):
        st.write(f"Analyzing change {i+1}/{len(limited_changes)}...")
        analysis = analyze_change(change)
        change.update(analysis)
        analyzed_changes.append(change)
        time.sleep(0.1)

    st.success("Done analyzing!")
    for change in analyzed_changes:
        with st.expander(f"{change['change_summary']}"):
            st.write(f"**Change Type:** {change['change_type']}")
            if "old" in change:
                st.markdown("**Old Text:**")
                st.code(change["old"])
            if "new" in change:
                st.markdown("**New Text:**")
                st.code(change["new"])
