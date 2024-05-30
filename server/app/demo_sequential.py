import requests

# Define the URLs
urls = [
    "http://localhost:5057/api/test",
    "http://localhost:5057/api/test",
    "http://localhost:5057/api/test",
    "http://localhost:5057/api/test",
]


# Function to make a GET request
def make_request(url):
    response = requests.get(url)
    return response.text


# Run the requests sequentially
def run_requests_sequentially(urls):
    results = []
    for url in urls:
        result = make_request(url)
        results.append(result)
    return results


# Run the requests
results = run_requests_sequentially(urls)

# Print the results
for i, result in enumerate(results):
    print(f"Result of request {i+1}:\n{result}\n")
