import requests
import concurrent.futures

urls = [
    "http://localhost:5057/api/test",
    "http://localhost:5057/api/test",
    "http://localhost:5057/api/test",
    "http://localhost:5057/api/test",
]


def make_request(url):
    response = requests.get(url)
    return response.text


# Use ThreadPoolExecutor to run requests simultaneously
def run_requests_simultaneously(urls):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Start the requests
        futures = [executor.submit(make_request, url) for url in urls]
        # Collect the results as they complete
        results = [
            future.result() for future in concurrent.futures.as_completed(futures)
        ]
    return results


results = run_requests_simultaneously(urls)

# Print the results
for i, result in enumerate(results):
    print(f"Result of request {i+1}:\n{result}\n")
