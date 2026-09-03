import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ResearchStartupTransportTests(unittest.TestCase):
    def test_runtime_consumers_do_not_import_deleted_v1_scheduler(self):
        for relative in (
            "research_control_dispatch.py",
            "tools/research_lane_dispatch.py",
            "tools/research_lane_claims.py",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertNotIn("research_scheduler", text, relative)

    def test_canonical_dispatch_emits_nonblocking_startup_transport(self):
        text = (ROOT / "research_control_dispatch.py").read_text(encoding="utf-8")
        self.assertIn("ENTERPRISE_MATH_RESEARCH_STARTUP_TRANSPORT_V1", text)
        self.assertIn("INJECTED_CONTEXT_ONLY_DO_NOT_REMOTE_SEARCH_OR_FETCH_FOR_TASK_START", text)
        self.assertIn('result["startup_transport"] = dict(STARTUP_TRANSPORT)', text)


if __name__ == "__main__":
    unittest.main()
