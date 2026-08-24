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
if __name__=="__main__": unittest.main()
