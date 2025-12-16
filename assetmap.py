from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import os

def is_local(path):
    if not path:
        return False
    parsed = urlparse(path)
    return parsed.scheme == "" and not path.startswith("//")

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""

# ---------------- CSS ----------------

def extract_css_assets(css_code):
    urls = re.findall(r'url\((.*?)\)', css_code)
    assets = []
    for url in urls:
        clean = url.strip('\'" ')
        if is_local(clean):
            assets.append(clean)
    return assets

def process_css(css_path, root, visited, tree):
    full = os.path.join(root, css_path)
    if full in visited or not os.path.isfile(full):
        return

    visited.add(full)
    tree[css_path] = []

    code = read_file(full)
    for asset in extract_css_assets(code):
        tree[css_path].append(asset)

# ---------------- JS ----------------

def extract_js_assets(js_code):
    imports = re.findall(
        r'(?:import\s+.*?\s+from\s+|import\s+)(["\'])(.*?)\1',
        js_code
    )
    requires = re.findall(
        r'require\((["\'])(.*?)\1\)',
        js_code
    )
    assets = []
    for _, path in imports + requires:
        if is_local(path):
            assets.append(path)
    return assets

def process_js(js_path, root, visited, tree):
    full = os.path.join(root, js_path)
    if full in visited or not os.path.isfile(full):
        return

    visited.add(full)
    tree[js_path] = []

    code = read_file(full)
    for dep in extract_js_assets(code):
        tree[js_path].append(dep)
        process_js(dep, root, visited, tree)

# ---------------- PHP ----------------

def extract_php_assets(php_code):
    assets = []

    # include / require
    includes = re.findall(
        r'(include|include_once|require|require_once)\s*\(?\s*[\'"](.*?)[\'"]\s*\)?',
        php_code
    )
    assets.extend([m[1] for m in includes if is_local(m[1])])

    # header("Location: ...")
    redirects = re.findall(
        r'header\s*\(\s*[\'"]Location:\s*([^\'"]+)',
        php_code
    )
    for r in redirects:
        path = r.split("?")[0]
        if path.endswith(".php"):
            assets.append(path)

    return assets


def process_php(php_path, root, visited, tree):
    full = os.path.join(root, php_path)
    if full in visited or not os.path.isfile(full):
        return

    visited.add(full)
    tree[php_path] = []

    code = read_file(full)
    for dep in extract_php_assets(code):
        tree[php_path].append(dep)
        process_php(dep, root, visited, tree)

# ---------------- MAIN ----------------

def assetmap(code, project_root="."):
    soup = BeautifulSoup(code, "html.parser")

    tree = {}
    visited = set()

    # HTML
    for tag in soup.find_all("link", href=True):
        if is_local(tag["href"]):
            process_css(tag["href"], project_root, visited, tree)

    for tag in soup.find_all("script", src=True):
        if is_local(tag["src"]):
            process_js(tag["src"], project_root, visited, tree)

    for tag in soup.find_all("img", src=True):
        if is_local(tag["src"]):
            tree[tag["src"]] = []

    # Inline PHP (if pasted)
    if "<?php" in code:
        tree["inline_php"] = []
        for dep in extract_php_assets(code):
            tree["inline_php"].append(dep)
            process_php(dep, project_root, visited, tree)

    return tree
