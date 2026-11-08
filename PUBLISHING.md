# Publishing checklist

This directory is the repository root. Do not upload its parent folder or the old project containing firmware and secrets.

Intended public repository: **hruba202/voice-inbox**. It has not been created or uploaded by this preparation task. If choosing another name, change both URLs in `manifest.json` and the links in README before publishing.

1. Review the proposed MIT license, ownership/credits, README and validation report.
2. Create the repository, enable Issues, set a description and topics such as `home-assistant`, `hacs`, `voice-messages`.
3. Upload the contents of this directory, including `.github` and `.gitignore`.
4. Run the Validate workflow. Fix any failing HACS, hassfest or test checks; do not ignore them. The local checks do not predict that these actions will pass.
5. Test installation through a custom repository and update from 0.3.1 on a test HA instance. Record the tested HA versions in VALIDATION.md.
6. Publish a full GitHub release `v0.3.2` only when checks pass. A Git tag alone is not a full release. Standard source-tree distribution is configured; no special ZIP asset is required by hacs.json.
7. Share the custom repository link. Later request catalog inclusion in `hacs/default` (integration category).

The installed integration contains a local `brand/icon.png`. Its acceptance by the current validator must be confirmed by the workflow; provide the corresponding Home Assistant Brands entry if required by the supported older HACS version.

Sources checked during preparation:
- https://contributors.home-assistant.io/marketplace/guides/catalog/
- https://contributors.home-assistant.io/marketplace/reference/repository-structure/
- https://contributors.home-assistant.io/marketplace/reference/hacs-json/
- https://contributors.home-assistant.io/marketplace/reference/validation/

Public catalog review is separate from custom-repository installation and is not guaranteed. Publishing or adding to the catalog does not deploy the integration to the owner's HA.
