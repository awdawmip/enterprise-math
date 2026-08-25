import io, json, pathlib, tempfile, unittest
from contextlib import redirect_stdout
from tools import research_scheduler_event as ev

class EventHelperTests(unittest.TestCase):
    def emit_event(self, argv):
        buf=io.StringIO()
        with redirect_stdout(buf): rc=ev.main(argv)
        self.assertEqual(0,rc); return json.loads(buf.getvalue())
    def test_free_publish_proposal(self):
        e=self.emit_event(["publish-proposal","--task-id","RS-FREE-X","--title","X","--publisher-id","EM-FREE-ABC123","--publisher-role","RESEARCHER","--at","2026-08-24T16:10:00+08:00","--frontier","f","--next-action","n"])
        self.assertEqual("PUBLISH",e["event"]); self.assertEqual("RESEARCHER",e["publisher_role"])
    def test_review_claim(self):
        e=self.emit_event(["review-claim","--task-id","RS-X","--reviewer-id","EM-DVR-111AAA","--review-claim-id","r1","--at","2026-08-24T16:11:00+08:00"])
        self.assertEqual("REVIEW_CLAIM",e["event"])
    def test_publish_taskbook_parses_frontmatter(self):
        with tempfile.TemporaryDirectory() as td:
            p=pathlib.Path(td)/"T.md"; p.write_text('<!-- ENTERPRISE_MATH_TASK_V1\n{"task_id":"RS-X","title":"X"}\n-->\n# X\n')
            e=self.emit_event(["publish-taskbook",str(p),"--taskbook-ref","research_tasks/T.md@abcdef1","--publisher-id","EM-DVR-111AAA","--publisher-role","RESEARCH_DRIVER","--at","2026-08-24T16:10:00+08:00"])
            self.assertEqual("RS-X",e["task_id"])
    def test_approve_binds_taskbook_content_gate(self):
        e=self.emit_event(["approve","--task-id","RS-X","--reviewer-id","EM-DVR-222BBB","--review-claim-id","r1","--taskbook-ref","research_tasks/T.md@abcdef1","--review-ref","review.md@abcdef2","--taskbook-audit","PASS","--policy-digest","sha256:1234","--at","2026-08-25T10:00:00+08:00"])
        self.assertEqual("PASS",e["taskbook_audit"]); self.assertEqual("sha256:1234",e["policy_digest"])
    def test_review_binds_semantic_route_fields(self):
        e=self.emit_event(["review","--task-id","RS-X","--reviewer-id","EM-DVR-222BBB","--review-claim-id","r1","--verdict","ACCEPT","--review-ref","driver.md@abcdef3","--method-harvest","RESULT_ONLY","--evidence-class","MIXED_INDEPENDENT_EVIDENCE","--route-disposition","CLOSE","--at","2026-08-25T10:01:00+08:00"])
        self.assertEqual("RESULT_ONLY",e["method_harvest"]); self.assertEqual("CLOSE",e["route_disposition"])
    def test_same_task_replication_verdict_is_rejected_by_emitter(self):
        with self.assertRaises(SystemExit):
            ev.main(["review","--task-id","RS-X","--reviewer-id","EM-DVR-222BBB","--review-claim-id","r1","--verdict","REQUEST_INDEPENDENT_REPLICATION","--review-ref","driver.md@abcdef3","--method-harvest","RESULT_ONLY","--evidence-class","SOURCE_ONLY","--route-disposition","PARK","--at","2026-08-25T10:01:00+08:00"])
    def test_replication_child_is_explicit(self):
        e=self.emit_event(["review","--task-id","RS-PARENT","--reviewer-id","EM-DVR-222BBB","--review-claim-id","r1","--verdict","PARK","--review-ref","driver.md@abcdef3","--method-harvest","RESULT_ONLY","--evidence-class","SOURCE_ONLY","--route-disposition","OPEN_INDEPENDENT_REPLICATION_CHILD","--child-task-id","RS-CHILD","--child-task-ref","research_tasks/CHILD.md@abcdef4","--independence-protocol","CLEAN_NEW_CONTEXT_BLIND_PACKET","--at","2026-08-25T10:01:00+08:00"])
        self.assertEqual("RS-CHILD",e["child_task_id"])
if __name__=="__main__": unittest.main()
