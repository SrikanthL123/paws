import sys
import site

# Add your app's directory to the path
sys.path.insert(0, '/home/ubuntu/paws')

# Add virtualenv's site-packages
site.addsitedir('/home/ubuntu/paws/venv/lib/python3.12/site-packages')

from app import app as application
