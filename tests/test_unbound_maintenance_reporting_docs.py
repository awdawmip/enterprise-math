"""Reporting text only; executable authorization checks keep their own tests."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MaintenanceReportingDocs(unittest.TestCase):
    def test_optional_diagnostics_cannot_grant_parent_completion(self):
        en = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.en.md").read_text()
        zh = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md").read_text()
        self.assertIn("Diagnostic unavailability cannot prohibit an honest blocker report or establish parent completion", en)
        self.assertIn("不需要先提交 `pre_final`", zh)
        self.assertIn("不自动赋予正式任务／父目标完成权", zh)
        for text in (en, zh):
            self.assertIn("formal_task_completion_checked=false", text)

    def test_bilingual_reporting_exception_retains_actual_formal_bindings(self):
        en = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.en.md").read_text()
        zh = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md").read_text()
        self.assertIn("No eight-field self-declaration or remote request is required", en)
        self.assertIn("不是回复许可", zh)
        for text in (en, zh):
            for token in ("CLAIM", "publication", "owner/lease", "CAS", "authorized=false"):
                self.assertIn(token, text)
        self.assertIn("cannot be dropped or relabeled", en)
        self.assertIn("不能删去既有研究绑定", zh)

    def test_optional_bridge_hint_is_not_the_formal_completion_api(self):
        en = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.en.md").read_text()
        zh = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md").read_text()
        self.assertIn("Current formal operation contracts still apply when those operations are actually called", en)
        self.assertIn("实际调用正式操作时仍按其当前合同核验", zh)
        for text in (en, zh):
            for field in ("--formal-task-completion", "formal_task_completion_checked=false", "pre_final {}"):
                self.assertIn(field, text)

    def test_admission_description_has_no_fixed_five_request_ceiling(self):
        en = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.en.md").read_text()
        zh = (ROOT / "docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md").read_text()
        self.assertNotIn("maximum five unfinished requests", en)
        self.assertNotIn("每个 conversation 最多 5 个未结束请求", zh)
        self.assertIn("no fixed five-request admission ceiling", en)
        self.assertIn("不设固定五槽接纳上限", zh)
        for text in (en, zh):
            self.assertIn("WAITING_RESOURCE", text)
            self.assertIn("reconcile", text)


if __name__ == "__main__":
    unittest.main()
