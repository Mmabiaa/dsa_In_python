"""
description: test basic trie functionalities 
run this test file: pytest DSA/Tests/test_trie.py -v -c DSA/Config/pytest.ini
"""
import pytest
from Data_Structures.Trie.main import Trie, TrieNode 

@pytest.fixture
def word_input():
    return "hello"

def test_creation():
    # test trie node creation
    trie_node = TrieNode()
    assert trie_node
    assert trie_node.children == {}
    assert trie_node.is_end_of_word == False
    assert isinstance(trie_node, TrieNode)
    # test trie creation
    trie = Trie()
    assert isinstance(trie, Trie)
    assert isinstance(trie.root, TrieNode)

def test_insert(word_input):
    trie = Trie()
    trie.insert(word_input)
    curr = trie.root
    for letter in word_input:
        assert letter in curr.children
        curr = curr.children[letter]
    assert curr.is_end_of_word

def test_search(word_input):
    trie = Trie()
    trie.insert(word_input)
    assert trie.search(word_input) == True
    assert trie.search("world") == False

def test_starts_with(word_input, prefix="he"):
    trie = Trie()
    trie.insert(word_input)
    assert trie.starts_with(prefix) == True
    assert trie.starts_with("ll") == False

def test_delete_word_input(word_input):
    trie = Trie()
    trie.insert(word_input)
    assert trie.search(word_input) == True
    trie.delete(word_input)
    assert trie.search(word_input) == False


 