# Validation — 2026-11-08

## Passed locally

- Python 3.14.2: 14 storage/access tests, 8 asynchronous lifecycle tests, 3 distribution checks: **25 passed**.
- Lifecycle tests required execution outside the Windows sandbox, where asyncio initially stalled. They use HA test doubles and never connect to a real HA instance.
- JavaScript syntax checked with `node --check`.
- Packaging script parses Python/JSON/YAML, checks source hashes and excludes cache, environments, recordings and secrets.
- All 14 original component files other than manifest.json are byte-for-byte unchanged from local version 0.3.1. SOURCE.json records individual hashes.
- Added English config-form translation and two original brand icons. Manifest changes are version, metadata and sorted dependencies only.

## Not run / pending

- Full pytest HTTP/config-flow suite: HA, pytest and aiohttp are not installed in the available Windows development environment. No packages were installed. WSL inventory returned access denied.
- HACS action and hassfest: workflows supplied, not executed on GitHub. Repository links point to the proposed repository, which has not been published by this task.
- Installation via Marketplace, fresh HA setup, update from 0.3.1 and regression on HA 2026.11: pending a test instance. Minimum 2026.10.3 is the existing target, not proof of compatibility with all newer versions.
- Current Nabu Casa and reverse-proxy middleware behavior: not retested end-to-end.
- Complete English recorder/entity/notification UI: not implemented; existing Czech runtime UI deliberately preserved.

The owner previously confirmed successful browser and P4 recordings with the project's existing version. That is historical runtime evidence, not a test of this new distribution package. Nothing was deployed, flashed or published. Do not claim Marketplace approval or a passing GitHub validation until those checks actually run.
