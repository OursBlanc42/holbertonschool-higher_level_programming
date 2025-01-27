#!/bin/bash

# Initialize counters
total_files=0
total_problems=0
pycodestyle_problems=0

# Iterate over all Python files in the current directory
for file in *.py; do
    total_files=$((total_files + 1))
    file_problems=0
    echo "=============================="
    echo "Checking: $file"
    echo "=============================="

    # Check module documentation
    echo -n "[MODULE] Documentation: "
    module_doc=$(python3 -c "
try:
    module = __import__('${file%.py}')
    print(module.__doc__ or 'No documentation found.')
except Exception as e:
    print(f'Error: {e}')
" 2>/dev/null)
    echo "$module_doc"
    if [[ "$module_doc" == "No documentation found." ]]; then
        file_problems=$((file_problems + 1))
    fi

    # Check class documentation
    echo "[CLASSES] Checking class documentation..."
    python3 -c "
try:
    module = __import__('${file%.py}')
    for attr in dir(module):
        obj = getattr(module, attr)
        if isinstance(obj, type):  # Check if it's a class
            doc = obj.__doc__ or 'No documentation.'
            print(f'  Class {attr}:', doc)
            if doc == 'No documentation.':
                exit(1)  # Mark as a problem
except Exception as e:
    print(f'Error: {e}')
" || file_problems=$((file_problems + 1))

    # Check function/method documentation
    echo "[FUNCTIONS] Checking function/method documentation..."
    python3 -c "
try:
    module = __import__('${file%.py}')
    for attr in dir(module):
        obj = getattr(module, attr)
        if isinstance(obj, type):  # If it's a class
            for method in dir(obj):
                if callable(getattr(obj, method)) and not method.startswith('__'):
                    doc = getattr(obj, method).__doc__ or 'No documentation.'
                    print(f'  Method {method} in {attr}:', doc)
                    if doc == 'No documentation.':
                        exit(1)  # Mark as a problem
        elif callable(obj):  # If it's a standalone function
            doc = obj.__doc__ or 'No documentation.'
            print(f'  Function {attr}:', doc)
            if doc == 'No documentation.':
                exit(1)  # Mark as a problem
except Exception as e:
    print(f'Error: {e}')
" || file_problems=$((file_problems + 1))

    # Check pycodestyle
    echo "[PYCODESTYLE] Checking PEP 8 compliance..."
    pycodestyle_output=$(python3 -m pycodestyle "$file" 2>/dev/null)
    if [[ -n "$pycodestyle_output" ]]; then
        file_problems=$((file_problems + 1))
        pycodestyle_problems=$((pycodestyle_problems + 1))
        echo "  Issues found with pycodestyle."
    else
        echo "  No issues found with pycodestyle."
    fi

    # Add file problems to total problems
    total_problems=$((total_problems + file_problems))

    if [[ $file_problems -gt 0 ]]; then
        echo "==> Problems found in $file: $file_problems issue(s)."
    else
        echo "==> No issues in $file."
    fi
    echo "=============================="
    echo
done

# Final summary
echo "=============================="
echo "Scan complete!"
echo "Files scanned: $total_files"
echo "Documentation/Function problems detected: $((total_problems - pycodestyle_problems))"
echo "Pycodestyle issues detected: $pycodestyle_problems"
echo "Total problems detected: $total_problems"
echo "=============================="

