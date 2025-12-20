import re
from urllib.parse import urlparse

def is_local(path):
    if not path:
        return False
    parsed = urlparse(path)
    return parsed.scheme == "" and not path.startswith("//")

def extract_tables(sql):
    tables = set()
    patterns = [
        r'FROM\s+([a-zA-Z_][\w]*)',
        r'JOIN\s+([a-zA-Z_][\w]*)',
        r'INTO\s+([a-zA-Z_][\w]*)',
        r'UPDATE\s+([a-zA-Z_][\w]*)'
    ]
    for p in patterns:
        for m in re.findall(p, sql, re.IGNORECASE):
            tables.add(m)
    return list(tables)

def assetmap(code):
    results = []
    lines = code.splitlines()

    for i, line in enumerate(lines, start=1):

        # CSS
        for p in re.findall(r'<link[^>]+href=["\'](.*?)["\']', line):
            results.append({"type": "CSS", "path": p, "line": i})

        # JS
        for p in re.findall(r'<script[^>]+src=["\'](.*?)["\']', line):
            results.append({"type": "JS", "path": p, "line": i})

        # IMAGE
        for p in re.findall(r'<img[^>]+src=["\'](.*?)["\']', line):
            results.append({"type": "IMAGE", "path": p, "line": i})

        # LINK (a href)
        for p in re.findall(r'<a[^>]+href=["\'](.*?)["\']', line):
            results.append({
                "type": "LINK",
                "path": p.split("?")[0],
                "line": i
            })

        # PHP include / require
        for _, p in re.findall(
            r'(include|require|include_once|require_once)\s*\(?\s*[\'"](.*?)[\'"]',
            line
        ):
            results.append({"type": "PHP_INCLUDE", "path": p, "line": i})

        # SQL tables
        if any(k in line.upper() for k in ["SELECT", "INSERT", "UPDATE", "DELETE"]):
            for t in extract_tables(line):
                results.append({"type": "DB_TABLE", "table": t, "line": i})

    return results
