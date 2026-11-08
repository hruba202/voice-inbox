# Development

Users do not need Python, scripts or a virtual environment to install or use Voice Inbox.

For the full development tests use **Linux / WSL, Python 3.14.2**, and the packages in `requirements-test.txt` (HA Core 2026.10.3, pytest, pytest-asyncio, pytest-aiohttp). Home Assistant is not supported as a Windows installation. Nothing installs itself.

```sh
python3.14 -m venv .wsl-venv
.wsl-venv/bin/python -m pip install -r requirements-test.txt
.wsl-venv/bin/python -c "import sys, importlib.metadata as m; print(sys.version); print({p:m.version(p) for p in ('homeassistant','pytest','pytest-asyncio','pytest-aiohttp')}); assert sys.version_info >= (3,14,2)"
.wsl-venv/bin/python -m pytest -q
node --check custom_components/voice_inbox/recorder.js
```

The CI workflow runs these tests on Ubuntu. It also invokes HACS validation and hassfest; those are not equivalent to a full live HA startup.

Without third-party packages, these focused checks also run on Windows:

```sh
python -m unittest discover -s tests -p test_storage.py -v
python -m unittest discover -s tests -p test_lifecycle_standalone.py -v
python -m unittest discover -s tests -p test_distribution.py -v
```

Storage tests execute real storage/access functions. Lifecycle tests execute the actual function definitions with yielding HA test doubles. HTTP tests use real aiohttp requests but a small fake HA object; config-flow tests use HA classes with mocked methods. None alone verifies HA middleware, real Nabu Casa routing or the complete browser workflow.

Manual release checks: clean install, update from 0.3.1 preserving all sources/keys, restart with several sources, browser record/save/play, ESP upload with 201, wrong key and LAN rejection, quota warnings/rejection, unload/reload, and rollback without losing recordings. Use a disposable HA test instance for destructive quota cases.
