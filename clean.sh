echo "🧹 Usuwanie plików cache..."

find . -type d -name '__pycache__' -exec rm -r {} + 2>/dev/null
find . -type d -name '.pytest_cache' -exec rm -r {} + 2>/dev/null
find . -type d -name '.mypy_cache' -exec rm -r {} + 2>/dev/null
find . -type d -name '.streamlit/cache' -exec rm -r {} + 2>/dev/null
find . -type d -name '.ipynb_checkpoints' -exec rm -r {} + 2>/dev/null

echo "✅ Gotowe: cache usunięte."