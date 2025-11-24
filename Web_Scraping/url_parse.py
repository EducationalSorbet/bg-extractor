def urlparse(url):
    # Initialize components to store the parsed results
    scheme = ""
    netloc = ""
    path = ""
    query = ""
    fragment = ""


    # Step 1: Extract the scheme (protocol)
    if "://" in url:
        scheme, url = url.split("://", 1) # Split at '://', scheme is before it, the rest is the URL
    
    # Step 2: Extract the netloc (domain)
    if "/" in url:
        netloc, url = url.split("/", 1) # Everything before the first slash in the netloc
    else:
        netloc = url # If no slash , the entire URL is just the netloc
    
    # Step 3: Extract the path (after domain but before query/fragment)
    if "?" in url:
        path, url = url.split("/", 1) # Split at '?', path is before it
    elif "#" in url:
        path, url = url.split("#", 1) # Split at '#', path is before it
    else:
        path = url # If no '?' or '#', everything left is the path
        url = "" # No query or fragment
    
    # Step 4: Extract the query string (if present)
    if "?" in url:
        query, url = url.split("#", 1) if "#" in url else (url, "") # Query if before '#' or end of URL
    
    # Step 5: Extract the fragment (if present)
    if "#" in url:
        fragment = url.split("#", 1)[1] # Everything after '#' is the fragment

    # Return the paarsed URL components
    return {
        "Scheme": scheme,
        "netloc": netloc,
        "path": path,
        "query": query,
        "fragment": fragment
    }
