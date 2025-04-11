from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# -------------------------------
# Academic Article Search using CrossRef
# -------------------------------
def search_academic(query, rows=5):
    url = "https://api.crossref.org/works"
    params = {"query": query, "rows": rows}
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    
    data = response.json()
    results = []
    for item in data.get("message", {}).get("items", []):
        title = item.get("title", ["No Title"])[0]
        authors = []
        for author in item.get("author", []):
            given = author.get("given", "")
            family = author.get("family", "")
            full_name = f"{given} {family}".strip()
            if full_name:
                authors.append(full_name)
        published = item.get("issued", {}).get("date-parts", [[None]])[0][0]
        doi = item.get("DOI", "")
        url_link = item.get("URL", "")
        
        results.append({
            "title": title,
            "authors": authors,
            "published": published,
            "doi": doi,
            "url": url_link,
            "type": "academic"
        })
    
    return results

def generate_bibtex(entry):
    key = entry["title"][:10].replace(" ", "_").replace("{", "").replace("}", "")
    authors = " and ".join(entry["authors"]) if entry["authors"] else "Unknown"
    
    bibtex = (
        f"@article{{{key},\n"
        f"  title={{ {entry['title']} }},\n"
        f"  author={{ {authors} }},\n"
        f"  year={{ {entry['published'] if entry['published'] else 'Unknown'} }},\n"
        f"  url={{ {entry['url']} }}\n"
        f"}}"
    )
    return bibtex

# -------------------------------
# News Article Search using NewsAPI
# -------------------------------
def search_news(query, rows=5):
    NEWS_API_KEY = "5671956c374a43e699defd6923b1b02c"  # Replace with your NewsAPI key
    url = "https://newsapi.org/v2/everything"
    params = {"q": query, "pageSize": rows, "apiKey": NEWS_API_KEY, "language": "en"}
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    
    data = response.json()
    articles = []
    for item in data.get("articles", []):
        articles.append({
            "title": item.get("title", "No Title"),
            "source": item.get("source", {}).get("name", "Unknown"),
            "publishedAt": item.get("publishedAt", "Unknown"),
            "description": item.get("description", ""),
            "url": item.get("url", ""),
            "type": "news"
        })
    return articles

# -------------------------------
# Wikipedia Article Search using MediaWiki API
# -------------------------------
def search_wikipedia(query, rows=5):
    """
    Search Wikipedia articles based on a query.
    This function uses the MediaWiki API to obtain a list of matching article titles and snippets.
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": rows,
    }
    
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    
    data = response.json()
    search_results = data.get("query", {}).get("search", [])
    results = []
    for item in search_results:
        title = item.get("title", "No Title")
        snippet = item.get("snippet", "")
        pageid = item.get("pageid", "")
        # Construct the article URL from the page ID
        url_link = f"https://en.wikipedia.org/?curid={pageid}"
        results.append({
            "title": title,
            "snippet": snippet,
            "url": url_link,
            "type": "wikipedia"
        })
    return results

# -------------------------------
# Flask Routes
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_type = request.form.get("searchType") or "academic"  # default to academic
        query = request.form.get("query")
        num_results = int(request.form.get("numResults", 5))
        
        results = []
        if search_type == "academic":
            results = search_academic(query, rows=num_results)
            for result in results:
                result["bibtex"] = generate_bibtex(result)
        elif search_type == "news":
            results = search_news(query, rows=num_results)
        elif search_type == "wikipedia":
            results = search_wikipedia(query, rows=num_results)
        else:
            results = []
        
        return render_template("results.html", query=query, search_type=search_type, results=results)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
