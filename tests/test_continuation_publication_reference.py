"""Execute the real packet function with isolated state providers and real pins."""
import copy,hashlib,json,tempfile,unittest
from datetime import datetime,timezone
from pathlib import Path
from unittest.mock import patch

COMMIT='a'*40
PID='TP2-'+'A'*20
TASK='T-PUBLICATION-REF'


class ProgressReferenceTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
  self.record={'task_id':TASK,'publication_id':PID,'taskbook_path':'taskbook.md'}
  self.definition={'task_id':TASK,'last_progress_ref':PID,'last_progress_at':'2026-11-01T00:00:00+00:00'}
  self.state={**self.definition,'dispatch_state':'NEEDS_DISPATCH','claim_id':None,'last_claim_id':None,'last_claim_comment_id':None}
  self.metadata={};self.pubpath=f'research_task_records/{TASK}/{PID}.json'
  for name,body in [('taskbook.md','isolated taskbook'),(self.pubpath,json.dumps(self.record)),('proof.txt','unchanged proof')]:
   p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
  blobs={str(p.relative_to(self.root)):hashlib.sha1(b'blob '+str(len(p.read_bytes())).encode()+b'\0'+p.read_bytes()).hexdigest() for p in self.root.rglob('*') if p.is_file()}
  self.manifest={'schema':'ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1','source_commit':COMMIT,'blobs':blobs}
  (self.root/'EM_SOURCE_BLOBS.json').write_text(json.dumps(self.manifest))
  (self.root/'EM_CONTINUATION_WRITE_SANDBOX.json').write_text(json.dumps({'schema':'ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1','source_commit':COMMIT,'isolated':True}))
 def packet(self):
  from control_plane import research_continuation as continuation, research_source_firewall
  from tools import research_dispatch, research_task_records, research_result_records, research_taskbook
  with patch.object(continuation, '_definition', return_value=copy.deepcopy(self.definition)), \
       patch.object(continuation, 'checkpoint_frontier', return_value={'state':'NOT_FOUND','source_artifacts':[],'execution_authorized':False}), \
       patch.object(continuation, 'current_normative_context', return_value={}), \
       patch.object(continuation, '_route', return_value={'execution_authorized':False}), \
       patch.object(research_dispatch, 'reduce_definition', return_value=copy.deepcopy(self.state)), \
       patch.object(research_task_records, 'current_records', return_value={TASK:copy.deepcopy(self.record)}), \
       patch.object(research_result_records, 'task_result_state', return_value=None), \
       patch.object(research_taskbook, 'split_taskbook', return_value=(copy.deepcopy(self.metadata),'')), \
       patch.object(research_source_firewall, 'validate_config', side_effect=lambda value:value):
   return continuation.continuation_packet(TASK,root=self.root,events=[],now=datetime(2026,11,9,tzinfo=timezone.utc),source_commit=COMMIT)
 def test_fresh_publication_ID_resolves_without_claim_or_work_authority(self):
  value=self.packet();self.assertEqual(value['artifact_errors'],[])
  self.assertEqual(value['progress_reference_readback']['pin']['path'],self.pubpath)
  self.assertEqual(value['progress_reference_readback']['original_reference'],PID)
  self.assertEqual(value['progress_reference_readback']['historical_work_status'],'UNKNOWN_NOT_ESTABLISHED_BY_CURRENT_READBACK')
  self.assertIsNone(value['continuation_seed']);self.assertEqual(value['takeover_readiness']['state'],'NO_LIVE_CLAIM')
  self.assertEqual([p['path'] for p in value['source_artifacts']].count(self.pubpath),1)
 def test_tampered_publication_bytes_still_fail_immutable_verification(self):
  (self.root/self.pubpath).write_text('tampered bytes')
  value=self.packet();self.assertTrue(value['artifact_errors']);self.assertIsNone(value['progress_reference_readback'])
 def test_publication_missing_from_manifest_still_has_errors(self):
  del self.manifest['blobs'][self.pubpath];(self.root/'EM_SOURCE_BLOBS.json').write_text(json.dumps(self.manifest))
  value=self.packet();self.assertTrue(value['artifact_errors']);self.assertIsNone(value['progress_reference_readback'])
 def test_other_publication_ID_is_not_silently_assumed_current(self):
  self.state['last_progress_ref']='TP2-'+'B'*20
  value=self.packet();self.assertIn(self.state['last_progress_ref'],[e['path'] for e in value['artifact_errors']]);self.assertIsNone(value['progress_reference_readback'])
 def test_real_file_reference_keeps_its_hash_checked_path(self):
  self.definition['last_progress_ref']=self.state['last_progress_ref']='proof.txt'
  value=self.packet();self.assertEqual(value['artifact_errors'],[]);self.assertEqual(value['progress_reference_readback']['pin']['path'],'proof.txt')
 def test_blind_firewall_without_publication_allowance_still_withholds_readback(self):
  self.metadata['source_firewall']={'allowed_source_pins':[]}
  value=self.packet();self.assertTrue(value['source_access_policy']['restricted']);self.assertIsNone(value['progress_reference_readback']);self.assertIsNone(value['continuation_seed'])
 def test_explicit_firewall_allowance_resolves_same_verified_record(self):
  self.metadata['source_firewall']={'allowed_source_pins':[{'commit':COMMIT,'path':self.pubpath,'blob_sha1':self.manifest['blobs'][self.pubpath]}]}
  value=self.packet();self.assertTrue(value['source_access_policy']['restricted']);self.assertEqual(value['progress_reference_readback']['pin']['path'],self.pubpath);self.assertIsNone(value['continuation_seed'])
 def test_prior_claim_input_seed_keeps_existing_unfinished_work_semantics(self):
  self.state.update(last_claim_id='CL-PRIOR',last_claim_comment_id=17)
  value=self.packet();self.assertEqual(value['continuation_seed']['completed_units'],[]);self.assertFalse(value['continuation_seed']['completed_research_units_verified'])
  self.assertEqual(value['continuation_seed']['previous_claim_id'],'CL-PRIOR')

 def test_reference_readback_does_not_relax_recovery_seed_conditions(self):
  self.state.update(last_claim_id='CL-PRIOR',last_claim_comment_id=17)
  for changes in ({'last_claim_comment_id':None},{'last_claim_comment_id':True},
                  {'last_claim_comment_id':0},{'last_claim_comment_id':-1},
                  {'dispatch_state':'COMPLETE'},{'claim_id':'CL-LIVE','last_owner_activity_at':'2026-11-08T00:00:00+00:00'},
                  {'last_progress_at':None},{'last_progress_at':'2026-11-02T00:00:00+00:00'}):
   with self.subTest(changes=changes):
    previous=copy.deepcopy(self.state);self.state.update(changes)
    try:
     value=self.packet();self.assertIsNone(value['continuation_seed'])
     self.assertEqual(value['artifact_errors'],[])
     self.assertEqual(value['progress_reference_readback']['pin']['path'],self.pubpath)
    finally:self.state=previous

if __name__=='__main__':unittest.main()
