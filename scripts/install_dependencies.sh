#!/bin/bash
exec > >(tee /tmp/install.log) 2>&1
set -e  # Exit immediately on error

echo ">>> Installing dependencies..."

cd /home/ubuntu/paws

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ">>> Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo ">>> Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ">>> Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo ">>> Installing Python packages from requirements.txt..."
pip install -r requirements.txt

echo ">>> Dependency installation completed successfully."
