import os
import sys

# Ensure the project root is on sys.path so \"from main import app\" works when this
# file is executed from the api/ directory on Vercel.
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from main import app as fastapi_app  # noqa: E402

# Export only the ASGI application for Vercel's Python runtime auto-detection.
# Avoid exporting a non-class `handler` object which can confuse the runtime's
# detection logic and trigger issubclass TypeError.
app = fastapi_app
