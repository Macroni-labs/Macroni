"""Entry point used when building the app with PyInstaller."""
import os
import sys

# ---------------------------------------------------------------------------
# PyObjC framework modules (Quartz, AppKit, CoreFoundation, HIServices, …)
# cannot be loaded from PyInstaller's bundled archive. PyObjC bridge modules
# such as _coregraphics expect to be imported from their installed package
# location, not from PyInstaller's flat bundle directory. Find the venv's
# site-packages by walking up from the executable and add it to sys.path so
# PyObjC is imported from there, not from PyInstaller's archive.
# ---------------------------------------------------------------------------
_exe_dir = os.path.dirname(os.path.abspath(sys.executable))
_search = _exe_dir
for _ in range(8):
    _candidate = os.path.join(_search, '.venv', 'lib', 'python3.14', 'site-packages')
    if os.path.isdir(_candidate):
        if _candidate not in sys.path:
            sys.path.insert(0, _candidate)
        break
    _parent = os.path.dirname(_search)
    if _parent == _search:
        break
    _search = _parent

from macro_recorder.__main__ import main

if __name__ == "__main__":
    main()
