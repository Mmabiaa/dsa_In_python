"""
description: this hook is called after completing the test session, calculates & shows the tests pass rate   
run: pytest DSA/Tests/ -v -c DSA/Config/pytest.ini
"""
import pytest

def pytest_sessionfinish(session):
    total = session.testscollected 
    failed = session.testsfailed
    passed = total - failed
    pass_rate = (passed / total * 100) if total != 0 else 0
    print(f"\nTests Pass Rate: {pass_rate:.2f}%")