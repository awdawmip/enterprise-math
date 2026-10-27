"""Reporting text only; executable authorization checks keep their own tests."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MaintenanceReportingDocs(unittest.TestCase):
    def test_router_separates_optional_maintenance_from_formal_entrypoint(self):
        text = (ROOT / 'AGENTS.md').read_text()
        formal = next(line for line in text.splitlines() if line.startswith('For explicit `RESEARCH_DRIVER`'))
        self.assertNotIn('CONTROL_PLANE_MAINTENANCE', formal)
        self.assertIn('pass the original `parent_liveness`', formal)
        maintenance = next(line for line in text.splitlines() if line.startswith('For genuinely unbound'))
        self.assertIn('neither a local eight-field declaration nor a remote `pre_final` request is required', maintenance)
        self.assertIn('optional diagnostics', maintenance)
        self.assertIn('cannot be dropped or relabeled', maintenance)

    def test_bilingual_reporting_exception_retains_actual_formal_bindings(self):
        en = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.en.md').read_text()
        zh = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md').read_text()
        self.assertIn('No eight-field self-declaration or remote request is required', en)
        self.assertIn('无需为允许回复而创建八字段自报对象或远端请求', zh)
        for text in (en, zh):
            for token in ('run_request_id', 'completion_request_id', 'session_request_id', 'authorized=false'):
                self.assertIn(token, text)
        self.assertIn('cannot be dropped or relabeled', en)
        self.assertIn('不能删去既有研究绑定', zh)

    def test_runtime_explanation_reports_result_without_issuing_authority(self):
        text = (ROOT / 'docs/RESEARCH_RUNTIME_STATE_MACHINE.md').read_text()
        self.assertIn('No local eight-field declaration or remote `pre_final` request is required', text)
        self.assertIn('optional diagnostics with `authorized=false`', text)
        self.assertIn('formal task/claim/execution/activity bindings keep their original checks', text)

    def test_admission_description_has_no_fixed_five_request_ceiling(self):
        en = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.en.md').read_text()
        zh = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md').read_text()
        self.assertNotIn('maximum five unfinished requests', en)
        self.assertNotIn('每个 conversation 最多 5 个未结束请求', zh)
        self.assertIn('no fixed five-request admission ceiling', en)
        self.assertIn('不设固定五槽接纳上限', zh)
        for text in (en, zh):
            self.assertIn('WAITING_RESOURCE', text)
            self.assertIn('reconcile', text)


if __name__ == '__main__':
    unittest.main()
