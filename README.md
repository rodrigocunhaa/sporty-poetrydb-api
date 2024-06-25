# sporty-poetrydb-api

## Test Cases

| Test Case | Description | Steps | Expected Result | Validation Description |
|-----------|-------------|-------|-----------------|------------------------|
| 1         | Fetch a Random Poem | Send a GET request to `https://poetrydb.org/random` | Receive a JSON response with a random poem containing fields: `title`, `author`, and `lines`. | Verify status code is 200. Ensure JSON response contains `title`, `author`, and `lines` fields. Validate `lines` is a list of strings. |
| 2         | Search Poems by Author | Send a GET request to `https://poetrydb.org/author/Emily%20Dickinson` | Receive a JSON array of poems by Emily Dickinson with fields: `title`, `author`, and `lines`. | Verify status code is 200. Ensure JSON array contains poems with `title`, `author`, and `lines` fields. Validate `author` is "Emily Dickinson" and `lines` is a list of strings. |

## Validation Description

- **Status Code**: Verifying the HTTP status code ensures that the request was successful (`200 OK`), indicating the API responded as expected.
- **JSON Structure**: Checking for specific fields (`title`, `author`, `lines`) in the JSON response ensures that the API provides the necessary poem details.
- **Data Type Checks**: Validating that `lines` is a list of strings ensures the integrity of the poem's textual content, confirming it can be processed correctly by downstream applications.