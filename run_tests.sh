#!/usr/bin/env bash
# run_tests.sh — ensure your two modules are importable & run all tests

set -e

OUTFILE="test_results.txt"
echo "=== Running All Tests ===" > "$OUTFILE"

# Make sure Python will look here for deterministic_select.py and randomized_select.py
export PYTHONPATH="$(pwd)"

# Discover and run every file named test_*.py in this directory
python3 -m unittest discover -s . -p "test_*.py" -v >> "$OUTFILE" 2>&1

echo ""
echo "✅ All tests complete. See $OUTFILE for details."
