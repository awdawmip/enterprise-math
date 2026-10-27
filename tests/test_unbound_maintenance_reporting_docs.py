"""Reporting text only; executable authorization checks keep their own tests."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MaintenanceReportingDocs(unittest.TestCase):
    def test_optional_diagnostics_cannot_grant_parent_completion(self):
        en = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.en.md').read_text()
        zh = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md').read_text()
        self.assertIn('Diagnostic unavailability cannot prohibit an honest blocker report or establish parent completion', en)
        self.assertIn('诊断服务不可用不阻止如实报告，不能据此称父目标已完成', zh)

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

    def test_formal_api_shape_remains_required_when_called(self):
        en = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.en.md').read_text()
        zh = (ROOT / 'docs/CHATGPT_ORDINARY_CONTROL.zh-CN.md').read_text()
        self.assertIn('When calling a formal or optional diagnostic API', en)
        self.assertIn('实际调用正式或可选诊断 API 时', zh)
        for text in (en, zh):
            for field in ('parent_liveness', 'executable_next_actions', 'continuation_lease_active'):
                self.assertIn(field, text)

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
