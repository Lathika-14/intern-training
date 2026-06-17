pip notes:
   * pip is Python's default package manager.
   * Used to install, update, and remove packages.
   * Downloads packages from PyPI.
   * Easy to use and widely supported.
commands:
    pip install requests
    pip uninstall requests
    pip list
    pip freeze > requirements.txt
    deactivate

uv notes:    
   * uv is a fast Python package and environment manager.
   * Can replace pip and venv workflows.
   * Much faster than pip for installing packages.
   * Supports virtual environments and dependency management.
commands:
    python -m uv venv
    python -m uv pip install requests
    python -m uv pip list
    python -m uv pip freeze > requirements.txt    
    deactivate
    
