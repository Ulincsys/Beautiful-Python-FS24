import json, requests

def search_mods(query):
    # https://docs.modrinth.com/api-spec
    api_url = "https://api.modrinth.com/v2/{}"
    endpoint = "search"
    
    facets = [["categories:fabric"], ["project_type:mod"]]
    
    # :eyes:
    p = {
        "facets": json.dumps(facets),
        "query": query
    }
    
    response = requests.get(api_url.format(endpoint), params = p)
    
    print(response.url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 400:
        print(response.json())
    else:
        print(response.status_code)

results = search_mods("enough items")

print(f"{results['total_hits']} results, {results['limit']} results per page, on page: {results['offset'] + 1}")

for i, result in enumerate(results["hits"]):
    print(f"{i}: {result['title']}")
    print(f"\tAuthor: {result['author']}")
    print(f"\tCategories: {result['categories']}")
    print(f"\tLatest supported version: {result['versions'][-1]}")
