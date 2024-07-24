#!/bin/bash

# Default installation path
INSTALL_PATH="$HOME/.local/bin"
SCRIPT_NAME="mini-ls"

# Function to display help
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --help         Display this help message."
    echo "  --path PATH    Specify the installation path (default: $HOME/.local/bin)."
    echo "  --uninstall    Uninstall mini-ls from the specified path."
    echo ""
    echo "This script installs or uninstalls mini-ls.py into/from the specified directory."
}

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --help)
            show_help
            exit 0
            ;;
        --path)
            if [[ -n "$2" ]]; then
                INSTALL_PATH="$2"
                shift 2
            else
                echo "Error: --path requires an argument."
                exit 1
            fi
            ;;
        --uninstall)
            UNINSTALL=true
            shift
            ;;
        *)
            echo "Error: Unknown option '$1'."
            show_help
            exit 1
            ;;
    esac
done

# If uninstall option is specified
if [[ "$UNINSTALL" == true ]]; then
    # Check if the script exists in the installation path
    if [[ -f "$INSTALL_PATH/$SCRIPT_NAME" ]]; then
        rm "$INSTALL_PATH/$SCRIPT_NAME"
        echo "$SCRIPT_NAME has been uninstalled from $INSTALL_PATH."
    else
        echo "Error: $SCRIPT_NAME not found in $INSTALL_PATH."
    fi
    exit 0
fi

# Check if mini-ls.py exists in the current directory
if [[ ! -f "mini-ls.py" ]]; then
    echo "Error: mini-ls.py not found in the current directory. Did you clone the repo correctly?"
    exit 1
fi

# Create the installation directory if it doesn't exist
mkdir -p "$INSTALL_PATH"

# Copy mini-ls.py to the installation path
cp mini-ls.py "$INSTALL_PATH/$SCRIPT_NAME"

# Make the script executable
chmod +x "$INSTALL_PATH/$SCRIPT_NAME"

# Output success message
echo "mini-ls.py has been installed to $INSTALL_PATH/$SCRIPT_NAME"
echo "You can run it by typing '$SCRIPT_NAME' in your terminal."
