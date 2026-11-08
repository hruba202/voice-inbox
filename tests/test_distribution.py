"""Release contract: preserve identity and ship only the intended integration."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
COMPONENT = ROOT / "custom_components" / "voice_inbox"

class DistributionTests(unittest.TestCase):
    def test_metadata(self):
        manifest = json.loads((COMPONENT / "manifest.json").read_text())
        hacs = json.loads((ROOT / "hacs.json").read_text())
        self.assertEqual(manifest["domain"], "voice_inbox")
        self.assertEqual(manifest["version"], "0.3.2")
        self.assertTrue(manifest["config_flow"])
        self.assertEqual(manifest["codeowners"], ["@hruba202"])
        self.assertEqual(hacs["homeassistant"], "2026.10.3")
        self.assertNotIn("voip_stack", manifest["dependencies"])
        self.assertEqual([p.name for p in (ROOT / "custom_components").iterdir() if p.is_dir() and p.name != "__pycache__"], ["voice_inbox"])

    def test_translations_and_brand(self):
        base = json.loads((COMPONENT / "strings.json").read_text(encoding="utf-8"))
        english = json.loads((COMPONENT / "translations/en.json").read_text(encoding="utf-8"))
        czech = json.loads((COMPONENT / "translations/cs.json").read_text(encoding="utf-8"))
        self.assertEqual(base, english)
        self.assertEqual(set(base["config"]["error"]), set(czech["config"]["error"]))
        self.assertEqual((COMPONENT / "brand/icon.png").read_bytes()[:8], b"\x89PNG\r\n\x1a\n")

    def test_upload_and_storage_contract(self):
        text = (COMPONENT / "const.py").read_text()
        self.assertIn('URL = "/api/voice_inbox/upload"', text)
        self.assertIn('EVENT_SAVED = "voice_inbox_saved"', text)
        self.assertIn("MAX_FILES = 100", text)
        self.assertIn("MAX_SECONDS = 60", text)

if __name__ == "__main__":
    unittest.main()
