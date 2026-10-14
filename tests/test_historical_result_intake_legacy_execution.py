"""Exact old RR65 bytes in isolated temporary roots; no scientific replay or role grant."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest import mock
from control_plane import research_historical_result_intake as h
from control_plane import research_result_records_impl as impl

REPO=Path(__file__).resolve().parents[1]

class ExactLegacyExecutionEvidenceTests(unittest.TestCase):
    def setUp(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);self.root=Path(temp.name)
        self.contract=json.loads((REPO/h.CONTRACT).read_text())
        self.target=next(r for r in self.contract['targets'] if r['historical_result_id']=='RR-65F19B398F4D33FEAE9C')
        self.old=json.loads((REPO/self.target['result_pin']['path']).read_text())
        paths={self.target[k]['path'] for k in ('result_pin','execution_pin','publication_pin','taskbook_pin')}
        paths.update(r['path'] for r in self.old['output_manifest'])
        for rel in paths:
            p=self.root/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(REPO/rel,p)
        self.write(h.CONTRACT,self.contract)
        self.er=json.loads((self.root/self.target['execution_pin']['path']).read_text())
        self.pub=json.loads((self.root/self.target['publication_pin']['path']).read_text())
        self.before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def write(self,path,value):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value)+'\n')

    def evidence(self,target=None,er=None,old=None,pub=None):
        return h._execution_evidence(self.root,target or self.target,old or self.old,er or self.er,pub or self.pub)

    def test_actual_raw_science_accepts_only_explicit_profile_preserving_bytes_unknown_and_no_alias(self):
        target=h._target(self.root,self.target['task_id'],self.target['publication_id'],self.target['historical_result_id'])
        old,outputs=h._science(self.root,target)
        self.assertEqual(old,self.old);self.assertEqual(len(outputs),5)
        self.assertNotIn(old['execution_record_id'],impl.execution_map(self.root))
        errors={e.split(': ',1)[-1] for e in impl.audit_result_record(old,None,self.root)}
        self.assertEqual(errors,{'unknown execution record'})
        self.assertEqual(self.before,{str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()})
        self.assertEqual(target['historical_authentication_status'],'UNKNOWN_NO_RECOVERED_AUTHENTICATED_SERVER_ENVELOPES')
        self.assertFalse((self.root/h.INTAKE_ROOT).exists())

    def test_without_explicit_profile_same_raw_record_remains_rejected(self):
        target=copy.deepcopy(self.target);target.pop('historical_execution_evidence')
        with self.assertRaisesRegex(h.HistoricalIntakeError,'execution identity mismatch'):h._science(self.root,target)

    def test_target_must_be_source_allowlisted_not_caller_profile(self):
        contract=copy.deepcopy(self.contract);contract['targets']=[r for r in contract['targets'] if r['historical_result_id']!=self.target['historical_result_id']];self.write(h.CONTRACT,contract)
        with self.assertRaisesRegex(h.HistoricalIntakeError,'no exact Source-approved intake scope'):
            h._target(self.root,self.target['task_id'],self.target['publication_id'],self.target['historical_result_id'])

    def test_profile_unknown_schema_or_fields_rejected(self):
        for field,value in [('schema','OTHER'),('historical_identifier_field','id'),('absent_fields',['execution_record_id']),('taskbook_binding_basis','INFER_FROM_NAME'),('extra',True)]:
            target=copy.deepcopy(self.target);target['historical_execution_evidence'][field]=value
            with self.subTest(field=field),self.assertRaises(h.HistoricalIntakeError):self.evidence(target=target)

    def test_profile_cannot_restore_auth_or_alias_even_false_like_integer(self):
        for field,value in [('execution_authentication_restored',True),('canonical_execution_alias_created',True),('execution_authentication_restored',0),('canonical_execution_alias_created',0)]:
            target=copy.deepcopy(self.target);target['historical_execution_evidence'][field]=value
            with self.subTest(field=field,value=value),self.assertRaises(h.HistoricalIntakeError):self.evidence(target=target)
        target=copy.deepcopy(self.target);target['historical_authentication_status']='AUTHENTICATED'
        with self.assertRaisesRegex(h.HistoricalIntakeError,'cannot restore historical authentication'):self.evidence(target=target)

    def test_backfilled_execution_fields_are_rejected_even_when_value_matches(self):
        for field,value in [('execution_record_id',self.old['execution_record_id']),('taskbook_blob_sha1',self.old['taskbook_blob_sha1'])]:
            er={**self.er,field:value}
            with self.subTest(field=field),self.assertRaisesRegex(h.HistoricalIntakeError,'exact missing execution fields'):self.evidence(er=er)

    def test_wrong_legacy_id_branch_or_path_is_rejected(self):
        for field,value in [('record_id','ER-FOREIGN'),('execution_branch_base','a'*40)]:
            with self.subTest(field=field),self.assertRaises(h.HistoricalIntakeError):self.evidence(er={**self.er,field:value})
        target=copy.deepcopy(self.target);target['execution_pin']['path']='research_execution_records/ER-FOREIGN.json'
        with self.assertRaisesRegex(h.HistoricalIntakeError,'identity mismatch'):self.evidence(target=target)

    def test_missing_er_taskbook_is_not_inferred_without_independent_exact_path_and_bytes(self):
        with self.assertRaisesRegex(h.HistoricalIntakeError,'path binding'):self.evidence(pub={**self.pub,'taskbook_path':'research_tasks/other.md'})
        with self.assertRaisesRegex(h.HistoricalIntakeError,'byte binding'):self.evidence(pub={**self.pub,'taskbook_blob_sha1':'sha1:'+'a'*40})
        p=self.root/self.target['taskbook_pin']['path'];p.write_bytes(p.read_bytes()+b'\n')
        with self.assertRaisesRegex(h.HistoricalIntakeError,'byte binding'):self.evidence()

    def test_full_science_rejects_original_or_output_byte_drift_before_any_write(self):
        paths=[self.target['execution_pin']['path'],self.old['return_path']]
        for rel in paths:
            p=self.root/rel;raw=p.read_bytes();p.write_bytes(raw+b'\n')
            with self.subTest(path=rel),mock.patch.object(h.tx,'commit') as commit,self.assertRaisesRegex(h.HistoricalIntakeError,'byte drift'):
                h._science(self.root,self.target)
            commit.assert_not_called();p.write_bytes(raw)

    def test_actual_ordinary_execution_map_and_unapproved_audit_errors_stay_blocking(self):
        with mock.patch.object(impl,'execution_map',return_value={self.old['execution_record_id']:copy.deepcopy(self.er)}):
            with self.assertRaisesRegex(h.HistoricalIntakeError,'cannot be imported or aliased'):h._science(self.root,self.target)
        with mock.patch.object(impl,'audit_result_record',return_value=['RR: unknown execution record','RR: unapproved defect']):
            with self.assertRaisesRegex(h.HistoricalIntakeError,'unapproved failure'):h._science(self.root,self.target)

    def test_exact_claim_author_task_and_branch_evidence_cannot_be_rebound(self):
        for field,value in [('task_id','RS-OTHER'),('publication_id','TP2-OTHER'),('claim_id','other-claim'),('researcher_id','EM-OTHER'),('execution_branch','research/other')]:
            changed={**self.er,field:value};self.write(self.target['execution_pin']['path'],changed)
            target=copy.deepcopy(self.target);target['execution_pin']=h.pin(self.root,self.target['execution_pin']['path'])
            message='historical publication scope mismatch' if field in ('task_id','publication_id') else 'historical execution-linked field mismatch: '+field
            with self.subTest(field=field),self.assertRaisesRegex(h.HistoricalIntakeError,message):h._science(self.root,target)
            (self.root/self.target['execution_pin']['path']).write_bytes(self.before[self.target['execution_pin']['path']])

    def test_existing_pcf_governance_authority_does_not_authorize_this_target(self):
        from tests.test_historical_result_intake import HistoricalIntakeTests
        fixture=HistoricalIntakeTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        with self.assertRaisesRegex(h.HistoricalIntakeError,'GOV task does not authorize this historical target'):
            h._authority(fixture.context,fixture.root,governance=self.target['authorizing_governance_task_id'])

if __name__=='__main__':unittest.main()
