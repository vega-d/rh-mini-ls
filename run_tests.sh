#!/bin/bash

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "Error: pytest is not installed. Please install it using 'pip install pytest'."
    exit 1
fi

# Check if the tests.py file exists
if [ ! -f tests.py ]; then
    echo "Error: tests.py file not found in the current directory. Did you clone the repo correctly?"
    exit 1
fi

# Execute pytest on tests.py
echo "Running tests in tests.py..."
pytest tests.py

# Capture the exit status of pytest
EXIT_STATUS=$?

# Check if pytest ran successfully
if [ $EXIT_STATUS -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above."
fi

# Exit with the same status as pytest
exit $EXIT_STATUS
