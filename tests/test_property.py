import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from tasks import search_tasks
from hypothesis import given, strategies as st

@given(st.lists(st.dictionaries(keys=st.sampled_from(["title", "description"]), values=st.text(), max_size=2)),
       st.text())
def test_search_does_not_crash(tasks, query):
    try:
        search_tasks(tasks, query)
    except Exception as e:
        assert False, f"Search raised an exception: {e}"

@given(st.text())
def test_empty_task_list_returns_empty(query):
    assert search_tasks([], query) == []

@given(st.text())
def test_query_in_title(query):
    task = {"title": query, "description": ""}
    results = search_tasks([task], query)
    assert task in results

@given(st.text())
def test_query_in_description(query):
    task = {"title": "", "description": query}
    results = search_tasks([task], query)
    assert task in results

@given(st.text())
def test_case_insensitive_search(query):
    task = {"title": query.upper(), "description": ""}
    results = search_tasks([task], query.lower())
    assert task in results
