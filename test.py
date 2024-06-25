import requests

# Test Case 1: Fetch a Random Poem
response = requests.get("https://poetrydb.org/random")
assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
data = response.json()
assert isinstance(data, list) and len(data) == 1, "Expected a single poem in the list"
poem = data[0]
assert "title" in poem, "Expected 'title' field in the response"
assert "author" in poem, "Expected 'author' field in the response"
assert "lines" in poem, "Expected 'lines' field in the response"
assert isinstance(poem["lines"], list) and all(isinstance(line, str) for line in poem["lines"]), "Expected 'lines' to be a list of strings"
print("Test Case 1 passed")

# Test Case 2: Search Poems by Author
response = requests.get("https://poetrydb.org/author/Emily%20Dickinson")
assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
data = response.json()
assert isinstance(data, list), "Expected a list of poems"
for poem in data:
    assert "title" in poem, "Expected 'title' field in the response"
    assert "author" in poem, "Expected 'author' field in the response"
    assert poem["author"] == "Emily Dickinson", f"Expected author to be 'Emily Dickinson', but got {poem['author']}"
    assert "lines" in poem, "Expected 'lines' field in the response"
    assert isinstance(poem["lines"], list) and all(isinstance(line, str) for line in poem["lines"]), "Expected 'lines' to be a list of strings"
print("Test Case 2 passed")