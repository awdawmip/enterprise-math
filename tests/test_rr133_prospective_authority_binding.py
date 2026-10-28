"""Control-only synthetic fixtures; never authorize a real Source/native write.

Catalog lookup is isolated from unrelated repository history. Real V2 taskbook
preflight, canonical ER map/ID, raw evidence, DA validation, server-comment receipt
replay, strict RR/DR audits, packet validator and successor checks all execute.
No scientific checker or claim endpoint is called.
"""
import base64
import copy
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import shutil
import sys
import unittest
from unittest import mock

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
sys.path.insert(0, str(BASE / 'tests'))
import test_followup_current_publisher as publisher_fixture
from test_followup_current_publisher import CURRENT, SESSION, authorization, write_json
import research_driver_followup as followup
import research_driver_followup_guard as guard
import research_driver_authority as authority
from control_plane import research_prospective_result_authority_binding as binding
from control_plane import research_result_records_impl as results
from control_plane import research_continuation_write_authority as receipts
from control_plane import research_driver_followup_fault_isolation as isolation
from control_plane import research_driver_followup_transaction as transaction
from control_plane import research_result_authority_fault_isolation as result_isolation
from control_plane import research_task_integrity_fault_isolation as task_integrity
from control_plane import research_task_semantic_integrity_fault_isolation as semantic
from control_plane import research_task_record_audit_fault_isolation as historical_tasks
from control_plane import research_control_bootstrap as bootstrap
from tools import research_task_records as tasks, research_taskbook as books
from tools import research_execution_records as executions, research_dispatch as dispatch

SOURCE_TIME = '2026-10-14T18:00:00+00:00'
CLAIM_TIME = '2026-10-14T18:01:00+00:00'
FROZEN = '2026-10-14T18:02:00+00:00'
REVIEWED = '2026-10-14T18:03:00+00:00'
PUBLISHED = '2026-10-14T18:04:00+00:00'
CREATED = '2026-10-14T18:05:00+00:00'
RESEARCHER = 'EM-TEST-NEW133'


class RR133BindingTests(unittest.TestCase):
    def setUp(self):
        self.fixture = publisher_fixture.CurrentPublisherBindingTests('runTest')
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        for patch in reversed(self.fixture.patches): patch.stop()
        self.fixture.patches = []
        # CI may install the real operational selectors before this fixture.
        # Preserve the nonempty semantic registry and its exact source pins;
        # do not replace current_records or weaken the production validator.
        semantic_payload = json.loads((BASE / semantic.QUARANTINE_FILE).read_text())
        self.assertTrue(semantic_payload['quarantines'])
        self.assertTrue(all(row['task_id'] not in {binding.SOURCE_TASK, binding.COVERAGE_TASK}
                            for row in semantic_payload['quarantines']))
        self.copy(semantic.QUARANTINE_FILE)
        for row in semantic_payload['quarantines']:
            for field in ('record_path', 'taskbook_path', 'source_taskbook_path'):
                self.copy(row[field])
        for folder in ['research_result_records', 'research_result_reviews']:
            shutil.rmtree(self.root / folder)
        for pin in binding.OLD_PINS: self.copy(pin['path'])
        for name, key, value in [(result_isolation.QUARANTINE_FILE, 'result_id', binding.OLD_RESULT),
                                 (isolation.QUARANTINE_FILE, 'packet_id', binding.OLD_PACKET)]:
            data = json.loads((BASE / name).read_text())
            data['entries'] = [row for row in data['entries'] if row[key] == value]
            write_json(self.root / name, data)
        data=json.loads((BASE/'research_execution_record_audit_quarantines.json').read_text())
        data['quarantines']=[row for row in data['quarantines'] if row['execution_record_id']==binding.OLD_EXECUTION]
        write_json(self.root/'research_execution_record_audit_quarantines.json',data)
        for relative in ['research_taskbook_policy.json', 'research_taskbook_contract.json',
                         'research_driver_followup_legacy_reviews.json']:
            self.copy(relative)
        write_json(self.root / receipts.CUTOVER, {'schema':'ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1','records':{}})
        self.source = self.make_generation(binding.SOURCE_TASK, binding.SOURCE_PUBLICATION, 'SOURCE_GEN2_FIXTURE.md', SOURCE_TIME)
        self.new_return = self.root / 'research_returns/rr133-fixture/return.md'
        self.new_return.parent.mkdir(parents=True)
        self.new_return.write_text('Synthetic evidence-custody return, not a scientific claim or real authority.\n')
        self.custody_path = self.new_return.parent / 'RR133_PROSPECTIVE_EVIDENCE_MANIFEST.json'
        write_json(self.custody_path, {'schema':'ENTERPRISE_MATH_RR133_PROSPECTIVE_EVIDENCE_CUSTODY_V2',
                                     'historical_request':binding.REQUEST,'historical_pins':binding.OLD_PINS,
                                     'historical_contributor_ids':['EM-NCASDIST1-3F7A91']})
        self.execution = {'record_schema':executions.SCHEMA, 'task_id':binding.SOURCE_TASK,
            'publication_id':self.source['publication_id'], 'claim_id':'fixture-rr133-gen2',
            'researcher_id':RESEARCHER, 'theorem_owner':'fixture owner (no real claim)',
            'execution_branch':'fixture/rr133-gen2', 'execution_branch_base':'a'*40,
            'taskbook_path':self.source['taskbook_path'], 'taskbook_blob_sha1':self.source['taskbook_blob_sha1'],
            'owner_lease_minutes':120, 'prepared_at':SOURCE_TIME,
            'allowed_outputs':['research_returns/rr133-fixture/**']}
        self.execution['execution_record_id'] = executions.execution_record_id(binding.SOURCE_TASK,
            self.source['publication_id'], self.execution['claim_id'], RESEARCHER, self.execution['execution_branch'])
        self.execution_path = f"research_execution_records/{binding.SOURCE_TASK}/{self.execution['execution_record_id']}.json"
        write_json(self.root/self.execution_path, self.execution)
        self.result = results.freeze_result(execution_record_id=self.execution['execution_record_id'],
            return_path=self.new_return, output_paths=[self.custody_path], owner_head='b'*40,
            terminal_verdict='NEGATIVE_BOUNDARY', hard_target_disposition='Fixture only', unresolved_residue='Parent OPEN',
            method_harvest='RESULT_ONLY', independence_status='SHARED_AMBIENT_CONTEXT_DISCLOSED',
            source_exposure_status='NONBLIND_DISCLOSED', next_control_plane_recommendation='Review exact frozen science; parent OPEN',
            frozen_at=FROZEN, root=self.root)
        self.result['_record_path'] = receipts.record_path(self.result, 'RESULT')
        self.claim = {'schema':dispatch.EVENT_SCHEMA, 'event':'CLAIM', 'task_id':binding.SOURCE_TASK,
            'publication_id':self.source['publication_id'], 'claim_id':self.execution['claim_id'],
            'researcher_id':RESEARCHER, 'session_id':'MCP-rr133-gen2-fixture', 'lease_minutes':120}
        self.comment = {'id':99000133,'issue_url':dispatch.GITHUB_ISSUE_URL,'user':{'login':'owner','id':7},
            'author_association':'OWNER','created_at':CLAIM_TIME,'updated_at':CLAIM_TIME,'body':json.dumps(self.claim)}
        self.save_result()
        artifact = self.root/'driver_reviews/rr133_fixture_review.md'
        artifact.write_text('Synthetic independent exact-evidence review fixture.\n')
        self.review = results.review_result(result=self.result, driver_id=CURRENT, disposition='ACCEPTED',
            review_path=artifact, destination_class='FOLLOWUP_TASK', destination_ref_or_none=binding.COVERAGE_TASK,
            reviewed_at=REVIEWED, root=self.root)
        self.review.update(driver_authority_record_id=authorization()['authority_record_id'],
            driver_authority_source_comment_id=901, reviewer_contribution_ids=[])
        self.review['_review_path'] = receipts.record_path(self.review, 'REVIEW')
        self.save_review()
        # Canonical catalogs are the only substituted boundary, not their
        # underlying raw source, receipts, ER map, authority or exact-set pins.
        self.catalogs = [mock.patch.object(followup, 'result_map', side_effect=lambda root:{self.result['result_id']:self.result}),
            mock.patch.object(followup,'review_map',side_effect=lambda root:{self.review['review_id']:self.review_view()}),
            mock.patch.object(guard,'authority_map',side_effect=lambda root:{self.review['review_id']:self.review_view()})]
        for patch in self.catalogs:
            patch.start(); self.addCleanup(patch.stop)
        self.coverage = self.make_generation(binding.COVERAGE_TASK, binding.OLD_PUBLICATION, 'COVERAGE_GEN2_FIXTURE.md', PUBLISHED)
        self.packet = self.build()
        self.save_packet()
        self.old_packet = json.loads((self.root/f'research_driver_followups/{binding.OLD_REVIEW}/{binding.OLD_PACKET}.json').read_text())
        self.task_pin = isolation.quarantine_rows(self.root)[binding.OLD_PACKET]['derived_task_publications'][0]
        self.row = isolation.quarantine_rows(self.root)[binding.OLD_PACKET]

    @contextmanager
    def installed_semantic_selector(self):
        # Exercise the real installer and validators, then restore only its
        # five process-global attributes, including originally absent flags.
        from control_plane import research_task_records_impl as task_core
        flag = '_task_semantic_integrity_fault_isolation_installed'
        absent = object()
        saved = [(module, name, getattr(module, name, absent)) for module, name in (
            (task_core, 'current_records'), (tasks, 'current_records'),
            (dispatch, 'merged_definitions'), (task_core, flag), (dispatch, flag))]
        try:
            semantic.install(self.root)
            yield
        finally:
            for module, name, value in reversed(saved):
                if value is absent:
                    if hasattr(module, name):
                        delattr(module, name)
                else:
                    setattr(module, name, value)

    def copy(self, relative):
        dest=self.root/relative;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(BASE/relative,dest)

    def add_history_compatibility(self):
        # Existing typed audit isolation, not a new heading alias mechanism.
        row = {'task_id': 'RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY', 'publication_id': 'TP2-5D9C21A7B40E683F1C52', 'record_path': 'research_task_records/RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY/TP2-5D9C21A7B40E683F1C52.json', 'record_blob_sha1': 'sha1:1eb4fe4825ff1ff4eeac929ba72fb5a277614c2e', 'taskbook_path': 'research_tasks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_20260903.md', 'taskbook_blob_sha1': 'sha1:7be6bca90aeb7b1e8222090ea6e22797f9e96f8c', 'allowed_task_record_audit_errors': ['mandatory body section is missing or empty: Frozen inputs and scope', 'mandatory body section is missing or empty: Hard target and required outputs', 'mandatory body section is missing or empty: Research value to preserve', 'mandatory body section is missing or empty: Success, kill, and return criteria'], 'quarantine_id': 'TRAQ-NCDIST-5D9C-SUPERSEDED-GEN1-20261014', 'state': 'NONOPERATIONAL_IMMUTABLE_RECORD_INTEGRITY_FAULT', 'nonoperational_basis': 'DIRECTLY_SUPERSEDED_SAME_TASK', 'allowed_publication_envelope_errors': [], 'operational': False, 'history_preserved': True, 'working_truth_granted': False, 'foundation_authority_granted': False, 'canonical_promotion_granted': False, 'successor_triggered': False, 'operational_publication_selected': False, 'reason': 'Only after actual direct same-Task Gen2 publication, migrate this exact former current-only Taskbook integrity row to immutable historical audit isolation. Preserve original record/body bytes and all four strict heading errors; no Result/review/DFU or mathematical authority is restored.'}
        write_json(self.root/historical_tasks.QUARANTINE_FILE,{'schema':historical_tasks.SCHEMA,'status':'ACTIVE','quarantines':[row]})
        bootstrap._install_operational_audit_views(self.root)

    def make_generation(self, task, old_id, filename, timestamp):
        old=json.loads((self.root/f'research_task_records/{task}/{old_id}.json').read_text())
        meta,body=books.split_taskbook((self.root/old['taskbook_path']).read_text())
        if task==binding.SOURCE_TASK:
            body=binding.source_generation_body(body,old['research_value'])
            meta['origin_kind']='DRIVER_ROADMAP'
        path=self.root/'research_tasks'/filename;path.write_text(books.render_taskbook(meta,body))
        new=tasks.build_record(meta,path=path,publisher_role='RESEARCH_DRIVER',publisher_id=CURRENT,
            research_value=old['research_value'],published_at=timestamp,supersedes_publication_id=old_id,root=self.root)
        write_json(self.root/f"research_task_records/{task}/{new['publication_id']}.json",new)
        return new

    def save_result(self):
        raw={k:v for k,v in self.result.items() if not k.startswith('_') and k!='write_authorization'}
        book={'taskbook_content_base64':base64.b64encode((self.root/self.source['taskbook_path']).read_bytes()).decode()}
        raw['write_authorization']=receipts.build_receipt(raw,'RESULT',{
            'source_commit':'c'*40,'authorized_at':FROZEN,'server_comments':[self.comment],
            'task_definition':receipts._canonical_frozen_definition(self.source,book),**book,
            'principal':{'claim_id':raw['claim_id'],'researcher_id':raw['researcher_id'],
                         'session_id':'MCP-rr133-gen2-fixture','ownership_epoch':99000133}})
        self.result['write_authorization']=raw['write_authorization'];write_json(self.root/self.result['_record_path'],raw)

    def save_review(self):
        raw={k:v for k,v in self.review.items() if not k.startswith('_') and k!='write_authorization'}
        raw['result_record_sha256']='sha256:'+hashlib.sha256((self.root/self.result['_record_path']).read_bytes()).hexdigest()
        raw['write_authorization']=receipts.build_receipt(raw,'REVIEW',{'source_commit':'d'*40,'authorized_at':REVIEWED,
            'authority_observed_through_comment_id':901,'principal':{'driver_id':CURRENT,'session_id':SESSION,
                                                        'authority_record_id':authorization()['authority_record_id']}})
        self.review.update(raw);write_json(self.root/self.review['_review_path'],raw)

    def review_view(self):
        return {**self.review,'review_authority_id':self.review['review_id'],'review_authority_kind':'IMMUTABLE_REVIEW',
                'source_review_ids':[self.review['review_id']]}

    def build(self):
        gates=[{'gate':g,'decision':'REQUIRED' if g=='MATHEMATICAL_CONTINUATION' else 'NOT_REQUIRED',
                'reason':'Explicit synthetic fixture gate; no real review decision','evidence_refs':[]} for g in followup.GATES]
        for gate in gates:
            if gate['gate']=='EXTERNAL_PRIOR_ART_DUPLICATION':
                gate.update(decision='SATISFIED_BY_REVIEWED_RESULT',evidence_refs=[self.review['review_path']])
        return followup.build_packet(review_id=self.review['review_id'],decision='TASK_SET_PUBLISHED',gate_decisions=gates,
            task_publications=[{'task_id':binding.COVERAGE_TASK,'publication_id':self.coverage['publication_id'],
                                'task_role':'MATHEMATICAL_CONTINUATION'}],driver_id=CURRENT,created_at=CREATED,
            publishing_driver_id=CURRENT,publisher_session_id=SESSION,
            prospective_result_authority_binding=binding.REQUEST,root=self.root)

    def save_packet(self):
        path=self.root/f"research_driver_followups/{self.packet['review_id']}/{self.packet['packet_id']}.json"
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(transaction._packet_bytes(self.packet))

    def check(self):
        isolation._validate_independent_successor(self.task_pin,self.row,self.old_packet,
            {self.coverage['publication_id']},self.root)

    def test_exact_two_gen2_native_chain_and_old_bytes_preserved(self):
        self.assertIsNone(receipts.receipt_error(self.result,'RESULT',self.root))
        self.assertIsNone(receipts.receipt_error(self.review,'REVIEW',self.root))
        self.assertEqual([],results.audit_result_record(self.result,self.execution,self.root))
        self.assertIn(self.execution['execution_record_id'],results.execution_map(self.root))
        self.check()
        transaction._validate_packet_candidate(self.packet,self.root,persisted=True)
        for pin in binding.OLD_PINS:self.assertEqual(pin,binding._pin(self.root,pin['path']))
        self.assertFalse(self.packet[binding.FIELD]['historical_authority_restored'])

    def test_bootstrapped_semantic_selector_preserves_current_source_and_excludes_bad_head(self):
        with self.installed_semantic_selector():
            selected = tasks.current_records(self.root)
            self.assertEqual(self.source['publication_id'], selected[binding.SOURCE_TASK]['publication_id'])
            quarantines = semantic.validated_quarantines(self.root)
            self.assertTrue(quarantines)
            self.assertTrue(set(quarantines).isdisjoint(selected))
            self.assertEqual((BASE / semantic.QUARANTINE_FILE).read_bytes(),
                             (self.root / semantic.QUARANTINE_FILE).read_bytes())

    def test_bootstrapped_semantic_selector_still_rejects_pinned_source_drift(self):
        with self.installed_semantic_selector():
            row = next(iter(semantic.validated_quarantines(self.root).values()))
            path = self.root / row['source_taskbook_path']
            path.write_bytes(path.read_bytes() + b'\n')
            with self.assertRaisesRegex(semantic.TaskSemanticIntegrityIsolationError,
                                        'source taskbook blob drift'):
                tasks.current_records(self.root)

    def test_binding_absent_preserves_old_result_and_source_equality(self):
        self.packet.pop(binding.FIELD);self.save_packet()
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError,'changed the reviewed target'):self.check()

    def test_request_unknown_extra_wrong_target_rejected(self):
        for value in [None,{**binding.REQUEST,'extra':True},{**binding.REQUEST,'historical_result_id':'RR-OTHER'}]:
            with self.subTest(value=value),self.assertRaises(followup.DriverFollowupError):binding.validate_request(value)

    def test_closed_binding_type_and_extra_pin_tamper_rejected(self):
        for change in [{'historical_authority_restored':0},{'extra':'unexpected'},{'new_packet_id':'DFU-OTHER'}]:
            altered=copy.deepcopy(self.packet);altered[binding.FIELD].update(change)
            with self.subTest(change=change),self.assertRaisesRegex(followup.DriverFollowupError,'closed binding'):
                followup.validate_packet(altered,self.root)

    def test_science_original_byte_drift_rejected(self):
        path=self.root/binding.OLD_PINS[1]['path'];path.write_bytes(path.read_bytes()+b'\n')
        with self.assertRaisesRegex(followup.DriverFollowupError,'historical evidence byte drift'):self.check()

    def test_wrong_execution_and_wrong_source_publication_rejected(self):
        for field,value in [('execution_record_id',binding.OLD_EXECUTION),('publication_id',binding.SOURCE_PUBLICATION)]:
            with self.subTest(field=field):
                original=copy.deepcopy(self.result);self.result[field]=value;self.save_result();self.save_review()
                with self.assertRaises(followup.DriverFollowupError):self.build()
                self.result=original;self.save_result();self.save_review()

    def test_payload_receipt_forgery_and_old_authority_rejected(self):
        self.result['write_authorization']['principal']['ownership_epoch']=7
        write_json(self.root/self.result['_record_path'],{k:v for k,v in self.result.items() if not k.startswith('_')})
        self.save_review()
        with self.assertRaisesRegex(followup.DriverFollowupError,'RESULT existing write authority failed'):self.build()

    def test_legacy_exemption_cannot_replace_current_native_receipt(self):
        pin=binding._pin(self.root,self.result['_record_path'])
        write_json(self.root/receipts.CUTOVER,{'schema':'ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1',
            'records':{pin['path']:{k:v for k,v in pin.items() if k!='path'}}})
        with self.assertRaisesRegex(followup.DriverFollowupError,'legacy exemption'):self.build()

    def test_same_task_rr_without_exact_custody_or_old_attribution_rejected(self):
        custody=json.loads(self.custody_path.read_text());custody['historical_contributor_ids']=[]
        write_json(self.custody_path,custody);self.refresh_manifest_receipts()
        with self.assertRaisesRegex(followup.DriverFollowupError,'closed historical evidence manifest'):self.build()

    def test_historical_author_cannot_review_a_fresh_native_rr_that_did_not_inherit_its_actor_ids(self):
        self.assertNotIn('contributor_ids',self.result)
        self.review['reviewer_contribution_ids']=json.loads(self.custody_path.read_text())['historical_contributor_ids']
        self.save_review()
        self.assertIsNone(receipts.receipt_error(self.review,'REVIEW',self.root))
        with self.assertRaisesRegex(followup.DriverFollowupError,'preserved historical scientific authors'):self.build()

    def test_reused_science_cannot_be_declared_blind(self):
        self.result['source_exposure_status']='BLIND_RAW_FROZEN'
        self.save_result();self.save_review()
        with self.assertRaisesRegex(followup.DriverFollowupError,'nonblind disclosure'):self.build()

    def test_foreign_publisher_session_rejected(self):
        altered=copy.deepcopy(self.packet);altered['materialization_publisher']['session_id']='MCP-foreign'
        with self.assertRaisesRegex(followup.DriverFollowupError,'session'):binding.expected_binding(altered,self.root)

    def test_duplicate_dfu_cannot_publish_same_successor(self):
        duplicate=copy.deepcopy(self.packet);duplicate['packet_id']='DFU-DUPLICATE'
        write_json(self.root/f"research_driver_followups/{self.packet['review_id']}/DFU-DUPLICATE.json",duplicate)
        with self.assertRaisesRegex(isolation.DriverFollowupIsolationError,'one exact native follow-up'):self.check()


    def refresh_manifest_receipts(self):
        self.result['output_manifest']=results.build_output_manifest([self.custody_path,self.new_return],self.execution,self.root)
        self.save_result();self.save_review()

    def test_custody_extra_missing_path_escape_and_wrong_hash_rejected_after_resigning_new_outputs(self):
        original=json.loads(self.custody_path.read_text())
        cases=[]
        extra=copy.deepcopy(original);extra['unexpected']=True;cases.append(extra)
        missing=copy.deepcopy(original);missing['historical_pins'].pop();cases.append(missing)
        escaped=copy.deepcopy(original);escaped['historical_pins'][0]['path']='../private';cases.append(escaped)
        changed=copy.deepcopy(original);changed['historical_pins'][0]['sha256']='0'*64;cases.append(changed)
        duplicate=copy.deepcopy(original);duplicate['historical_pins'].append(duplicate['historical_pins'][0]);cases.append(duplicate)
        for value in cases:
            with self.subTest(value=value):
                write_json(self.custody_path,value);self.refresh_manifest_receipts()
                with self.assertRaisesRegex(followup.DriverFollowupError,'closed historical evidence manifest mismatch'):self.build()

    def test_arbitrary_same_task_current_rr_without_custody_is_not_authority(self):
        self.result['output_manifest']=results.build_output_manifest([self.new_return],self.execution,self.root)
        self.save_result();self.save_review()
        self.assertIsNone(receipts.receipt_error(self.result,'RESULT',self.root))
        with self.assertRaisesRegex(followup.DriverFollowupError,'unique native evidence manifest'):self.build()

    def test_source_and_coverage_scopes_cannot_be_narrowed_or_replaced(self):
        for record in [self.source,self.coverage]:
            path=self.root/record['taskbook_path'];original=path.read_bytes()
            for transform in [lambda text:text.replace('## Hard target and required outputs','## Hard target and required outputs\n\nCustody PASS is sufficient.',1),
                              lambda text:text.replace('## Success, kill, and return criteria','## Success, kill, and return criteria\n\nOnly control completion is required.',1)]:
                with self.subTest(task=record['task_id']):
                    path.write_text(transform(original.decode()))
                    with self.assertRaisesRegex(followup.DriverFollowupError,'exact frozen scope'):self.build()
                    path.write_bytes(original)

    def test_wrong_generation_predecessor_and_origin_rejected(self):
        for record in [self.source,self.coverage]:
            path=self.root/f"research_task_records/{record['task_id']}/{record['publication_id']}.json"
            for change in [{'publication_generation':3},{'publication_generation':True},{'supersedes_publication_id':'TP2-OTHER'}]:
                with self.subTest(change=change):
                    write_json(path,{**record,**change})
                    with self.assertRaisesRegex(followup.DriverFollowupError,'direct Gen2'):self.build()
                    write_json(path,record)
        path=self.root/self.source['taskbook_path'];original=path.read_text()
        path.write_text(original.replace('"origin_kind": "DRIVER_ROADMAP"','"origin_kind": "MAINTENANCE"'))
        with self.assertRaisesRegex(followup.DriverFollowupError,'exact frozen scope'):self.build()

    def test_old_generation_intent_and_unauthorized_claim_server_actor_rejected(self):
        old=self.execution['publication_id'];self.execution['publication_id']=binding.SOURCE_PUBLICATION
        write_json(self.root/self.execution_path,self.execution)
        self.assertIsNotNone(receipts.receipt_error(self.result,'RESULT',self.root))
        self.execution['publication_id']=old;write_json(self.root/self.execution_path,self.execution)
        self.comment['user']['login']='unauthorized';self.save_result();self.save_review()
        with self.assertRaisesRegex(followup.DriverFollowupError,'RESULT existing write authority failed'):self.build()

    def test_nonaccepted_and_noncurrent_exact_review_authority_rejected(self):
        self.review['disposition']='RETURN_TO_OWNER';self.save_review()
        with self.assertRaisesRegex(followup.DriverFollowupError,'new DR must accept'):self.build()
        self.review['disposition']='ACCEPTED';self.save_review()
        with mock.patch.object(guard,'authority_map',return_value={}):
            with self.assertRaises(followup.DriverFollowupError):self.build()

    def test_old_quarantine_cannot_be_deleted_or_edited(self):
        path=self.root/result_isolation.QUARANTINE_FILE;data=json.loads(path.read_text())
        data['entries'][0]['reason']+=' Modified.';write_json(path,data)
        with self.assertRaisesRegex(followup.DriverFollowupError,'historical quarantine row'):self.build()

    def test_bound_request_cannot_enter_unauthenticated_legacy_materializer(self):
        spec={'decision':'TASK_SET_PUBLISHED','gate_decisions':self.packet['gate_decisions'],'tasks':[],
              binding.FIELD:binding.REQUEST}
        before={p.relative_to(self.root).as_posix():p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        with self.assertRaisesRegex(transaction.DriverFollowupTransactionError,'native current publisher'):
            followup.materialize(review_id=self.review['review_id'],spec=spec,created_at=CREATED,root=self.root)
        after={p.relative_to(self.root).as_posix():p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before,after)


    def test_original_hold_is_generation_scoped_with_real_quarantine_validation(self):
        held=result_isolation.withheld_state(binding.SOURCE_TASK,binding.SOURCE_PUBLICATION,self.root)
        self.assertEqual([binding.OLD_RESULT],held['withheld_result_ids'])
        self.assertIsNone(result_isolation.withheld_state(binding.SOURCE_TASK,self.source['publication_id'],self.root))
        self.assertEqual([binding.OLD_PACKET],list(isolation.validated_quarantines(self.root)))
        self.assertEqual(4,len(tasks.audit(self.root)))
        self.add_history_compatibility()
        self.assertEqual([],tasks.audit(self.root))
        self.assertEqual([binding.OLD_RESULT],result_isolation.withheld_state(binding.SOURCE_TASK,binding.SOURCE_PUBLICATION,self.root)['withheld_result_ids'])

    def materialize_fixture(self, fail_postcheck=False):
        self.add_history_compatibility()
        (self.root/f"research_task_records/{binding.COVERAGE_TASK}/{self.coverage['publication_id']}.json").unlink()
        (self.root/self.coverage['taskbook_path']).unlink()
        (self.root/f"research_driver_followups/{self.packet['review_id']}/{self.packet['packet_id']}.json").unlink()
        old=json.loads((self.root/f'research_task_records/{binding.COVERAGE_TASK}/{binding.OLD_PUBLICATION}.json').read_text())
        meta,body=books.split_taskbook((self.root/old['taskbook_path']).read_text())
        sections=tasks._section_payloads(body)
        task_spec={key:copy.deepcopy(meta[key]) for key in ('task_id','title','owner','frontier','next_action','kind','priority','leverage',
            'identity_lane','origin_kind','task_lineage','parent_task_id','successor_gate','source_refs','dependencies')}
        task_spec.update(task_role='MATHEMATICAL_CONTINUATION',research_value=old['research_value'],
            taskbook_filename='COVERAGE_NATIVE_TRANSACTION_FIXTURE.md',supersedes_publication_id=binding.OLD_PUBLICATION,
            mother_question=sections['Mother question'],frozen_inputs_and_scope=sections['Frozen inputs and scope'],
            hard_target_and_required_outputs=sections['Hard target and required outputs'],
            research_value_to_preserve=sections['Research value to preserve'],success_kill_and_return_criteria=sections['Success, kill, and return criteria'])
        def exact_postcheck(packet,root,created):
            transaction._validate_packet_candidate(packet,root,persisted=True)
            errors=list(isolation.audit(root))
            for item in created:
                if item.path.read_bytes()!=item.content:errors.append('owned bytes drift')
            if fail_postcheck:errors.append('injected late postcheck failure')
            return errors
        # The isolated store deliberately omits unrelated global governance
        # baselines. Its exact isolation, publication, packet/publisher and all
        # owned-byte checks remain real; only that global aggregation is replaced.
        with mock.patch.object(transaction,'_candidate_post_audit',side_effect=exact_postcheck):
            return followup.materialize(review_id=self.review['review_id'],spec={
                'decision':'TASK_SET_PUBLISHED','tasks':[task_spec],'gate_decisions':self.packet['gate_decisions'],
                binding.FIELD:binding.REQUEST},created_at=CREATED,root=self.root,
                publishing_driver_id=CURRENT,publisher_session_id=SESSION)

    def test_native_transaction_wires_closed_request_and_succeeds(self):
        outcome=self.materialize_fixture()
        self.assertEqual(self.result['result_id'],outcome['result_id'])
        self.assertEqual(self.source['publication_id'],outcome['source_publication_id'])
        self.assertEqual(binding.SCHEMA,outcome[binding.FIELD]['schema'])
        self.assertEqual([],tasks.audit(self.root))
        self.assertEqual([binding.OLD_PACKET],list(isolation.validated_quarantines(self.root)))
        self.assertEqual(1,len([p for p in isolation._raw_packets(self.root) if p['review_id']==self.review['review_id']]))

    def test_late_failure_rolls_back_only_new_coverage_outputs(self):
        with self.assertRaisesRegex(transaction.DriverFollowupTransactionError,'injected late postcheck failure'):
            self.materialize_fixture(fail_postcheck=True)
        self.assertFalse((self.root/'research_tasks/COVERAGE_NATIVE_TRANSACTION_FIXTURE.md').exists())
        self.assertEqual([],list((self.root/'research_driver_followups'/self.review['review_id']).glob('*.json')))
        self.assertTrue((self.root/self.result['_record_path']).exists())
        self.assertTrue((self.root/self.source['taskbook_path']).exists())
        for pin in binding.OLD_PINS:self.assertEqual(pin,binding._pin(self.root,pin['path']))


    def test_current_only_taskbook_quarantine_requires_exact_atomic_history_migration(self):
        name='control_plane/task_integrity_quarantine_addendum_20260902.json'
        current=json.loads((BASE/name).read_text())
        # Model the exact pre-Gen2 hold; Main now retains it historically.
        # Do not require the old row to remain in the current-only registry.
        current['quarantines']=[{'task_id': 'RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY',
         'publication_id': 'TP2-5D9C21A7B40E683F1C52',
         'record_path': 'research_task_records/RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY/TP2-5D9C21A7B40E683F1C52.json',
         'record_blob_sha1': 'sha1:1eb4fe4825ff1ff4eeac929ba72fb5a277614c2e',
         'taskbook_path': 'research_tasks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_20260903.md',
         'taskbook_blob_sha1': 'sha1:7be6bca90aeb7b1e8222090ea6e22797f9e96f8c',
         'reason': 'The sole active generation is otherwise claimable and has no frozen Result, but its taskbook '
                   'bypasses the exact combined V2 section headings. Block only this task before claim; an '
                   'authorized Driver may publish a corrected superseding generation without changing its research '
                   'frontier.',
         'allowed_task_record_audit_errors': ['mandatory body section is missing or empty: Frozen inputs and scope',
                                              'mandatory body section is missing or empty: Hard target and required '
                                              'outputs',
                                              'mandatory body section is missing or empty: Research value to '
                                              'preserve',
                                              'mandatory body section is missing or empty: Success, kill, and return '
                                              'criteria'],
         'working_truth_granted': False,
         'foundation_authority_granted': False,
         'canonical_promotion_granted': False,
         'successor_triggered': False,
         'state': 'INVALID_CURRENT_TASK_PUBLICATION',
         'operational_publication_id': None,
         'isolation_scope': 'CONTROL_PLANE_ONLY'}]
        self.assertEqual(1,len(current['quarantines']))
        record=self.root/f"research_task_records/{binding.SOURCE_TASK}/{self.source['publication_id']}.json"
        new_bytes=record.read_bytes();record.unlink();write_json(self.root/name,current)
        task_integrity.install(self.root)
        self.assertEqual(binding.SOURCE_PUBLICATION,task_integrity.validated_quarantines(self.root)[binding.SOURCE_TASK]["publication_id"])
        record.write_bytes(new_bytes)
        with self.assertRaisesRegex(task_integrity.TaskIntegrityIsolationError,'one pinned active head'):
            tasks.current_records(self.root)
        current['quarantines']=[];write_json(self.root/name,current);self.add_history_compatibility()
        self.assertEqual(self.source['publication_id'],tasks.current_records(self.root)[binding.SOURCE_TASK]['publication_id'])
        self.assertEqual([],tasks.audit(self.root))
        self.assertEqual([binding.OLD_RESULT],result_isolation.withheld_state(binding.SOURCE_TASK,binding.SOURCE_PUBLICATION,self.root)['withheld_result_ids'])
        for pin in binding.OLD_PINS:self.assertEqual(pin,binding._pin(self.root,pin['path']))


class ExactExistingSourceLaunchTests(unittest.TestCase):
    """Actual immutable launch bytes, never new scientific/Native authority."""
    def setUp(self):
        self.row = isolation.quarantine_rows(BASE)[binding.SOURCE_LAUNCH_PACKET]
        self.task = self.row['derived_task_publications'][0]
        self.packet = json.loads((BASE / self.row['packet_path']).read_text())
        self.heads = {binding.SOURCE_LAUNCH_PUBLICATION}

    def validate(self, root=BASE, **changes):
        values = {'task': self.task, 'row': self.row, 'source_packet': self.packet,
                  'active_heads': self.heads, 'root': root}
        values.update(changes)
        return binding.validate_exact_source_launch_successor(**values)

    @contextmanager
    def pinned_fixture(self):
        import tempfile
        with tempfile.TemporaryDirectory(prefix='rr133-launch-pins-') as name:
            root = Path(name)
            for pin in [*binding.OLD_PINS, *binding.SOURCE_LAUNCH_PINS]:
                path = root / pin['path']; path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((BASE / pin['path']).read_bytes())
            yield root

    def test_exact_existing_roadmap_launch_does_not_invent_a_followup(self):
        self.assertTrue(self.validate())
        records = isolation._raw_packets(BASE)
        self.assertFalse(any(item.get('publication_id') == binding.SOURCE_LAUNCH_PUBLICATION
            for packet in records for item in packet.get('task_publications', [])))
        self.assertIn(binding.SOURCE_LAUNCH_PACKET, isolation.quarantine_rows(BASE))
        self.assertIn(binding.OLD_PACKET, isolation.quarantine_rows(BASE))
        self.assertIsNone(result_isolation.withheld_state(binding.SOURCE_TASK, binding.SOURCE_LAUNCH_PUBLICATION, BASE))
        self.assertIsNotNone(result_isolation.withheld_state(binding.SOURCE_TASK, binding.SOURCE_PUBLICATION, BASE))

    def test_other_task_or_other_ancestor_retains_generic_successor_route(self):
        for change in ({'task_id': binding.COVERAGE_TASK}, {'publication_id': binding.OLD_PUBLICATION}):
            with self.subTest(change=change):
                self.assertFalse(self.validate(task={**self.task, **change}))

    def test_arbitrary_same_task_gen2_gen3_or_ambiguous_head_is_rejected(self):
        for heads in ({'TP2-ARBITRARY-GEN2'}, {'TP2-GEN3'}, self.heads | {'TP2-SECOND'}, set()):
            with self.subTest(heads=heads), self.assertRaisesRegex(followup.DriverFollowupError, 'one exact existing Gen2'):
                self.validate(active_heads=heads)

    def test_old_row_or_raw_packet_cannot_be_reclassified(self):
        row = copy.deepcopy(self.row); row['operational'] = True
        with self.assertRaisesRegex(followup.DriverFollowupError, 'historical isolation row drift'):
            self.validate(row=row)
        packet = copy.deepcopy(self.packet); packet['result_id'] = binding.OLD_RESULT
        with self.assertRaisesRegex(followup.DriverFollowupError, 'source packet differs'):
            self.validate(source_packet=packet)

    def test_exact_science_launch_parent_and_identity_bytes_are_enforced(self):
        pins = [*binding.SOURCE_LAUNCH_PINS, binding.OLD_PINS[1]]
        with self.pinned_fixture() as root:
            for pin in pins:
                with self.subTest(path=pin['path']):
                    path = root / pin['path']; original = path.read_bytes()
                    path.write_bytes(original + b'\n')
                    with self.assertRaisesRegex(followup.DriverFollowupError, 'publication pin drift'):
                        self.validate(root)
                    path.write_bytes(original)

    def test_actual_root_authority_and_session_are_not_optional(self):
        active = authority.require_active_driver(binding.SOURCE_LAUNCH_DRIVER, '2026-10-15T01:41:42.436725+00:00', BASE)
        for changed in (None, {**active, 'authority_record_id': 'DA-OTHER'},
                        {**active, 'source_body': json.dumps({'session_id': 'MCP-other'})}):
            with self.subTest(value=changed is None), mock.patch.object(authority, 'require_active_driver', return_value=changed):
                with self.assertRaises(followup.DriverFollowupError):
                    self.validate()

    def test_canonical_direct_parent_authority_cannot_be_replaced_by_a_label(self):
        import research_objective_authority as parent
        for changed in ({'binding_source': 'LEGACY_UNBOUND'},
                        {'binding_source': 'TASK_PUBLICATION_DIRECT', 'objective_id': binding.SOURCE_LAUNCH_OBJECTIVE,
                         'objective_generation_id': binding.SOURCE_LAUNCH_OBJECTIVE_GENERATION, 'objective_authority_verified': False}):
            with self.subTest(changed=changed), mock.patch.object(parent, 'resolve_authoritative_task_parent_binding', return_value=changed):
                with self.assertRaisesRegex(followup.DriverFollowupError, 'direct authoritative parent tenure'):
                    self.validate()

    def test_later_valid_objective_head_keeps_recorded_time_launch_replay_valid(self):
        import os
        import tempfile
        import research_objective_authority as parent
        with tempfile.TemporaryDirectory(prefix='rr133-later-objective-', dir=BASE.parent) as name:
            root = Path(name) / 'source'
            shutil.copytree(BASE, root, copy_function=os.link, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))
            old = json.loads((root / f'research_objective_records/{binding.SOURCE_LAUNCH_OBJECTIVE}/{binding.SOURCE_LAUNCH_OBJECTIVE_GENERATION}.json').read_text())
            generation, head, receipt = parent.create_and_select(
                expected_previous_generation_id=binding.SOURCE_LAUNCH_OBJECTIVE_GENERATION,
                objective_id=binding.SOURCE_LAUNCH_OBJECTIVE, objective_status='OPEN',
                title=old['title'], scope=old['scope'], success_criteria=old['success_criteria'],
                closure_criteria=old['closure_criteria'], research_value=old['research_value'],
                publisher_id=binding.SOURCE_LAUNCH_DRIVER, created_at='2026-10-15T02:30:00+00:00', root=root)
            self.assertEqual(2, generation['generation'])
            self.assertNotEqual(binding.SOURCE_LAUNCH_OBJECTIVE_GENERATION, head['objective_generation_id'])
            self.assertTrue(self.validate(root))

    def test_cold_full_bootstrap_keeps_old_authority_isolated(self):
        import subprocess
        script = """
import research_control_dispatch
from pathlib import Path
from tools import research_task_records
from control_plane import research_result_authority_fault_isolation as held
from control_plane import research_driver_followup_fault_isolation as isolated
from control_plane import research_prospective_result_authority_binding as binding
root=Path.cwd()
current=research_task_records.current_records(root)
assert current[binding.SOURCE_TASK]['publication_id']==binding.SOURCE_LAUNCH_PUBLICATION
coverage=current[binding.COVERAGE_TASK]
assert coverage['publication_id']=='TP2-C6F364B0E01C124DB7E9'
assert coverage['publication_generation']==2
assert coverage['supersedes_publication_id']==binding.OLD_PUBLICATION
rows=isolated.validated_quarantines(root)
assert binding.OLD_PACKET in rows and binding.SOURCE_LAUNCH_PACKET in rows
assert held.withheld_state(binding.SOURCE_TASK,binding.SOURCE_PUBLICATION,root)['withheld_result_ids']==[binding.OLD_RESULT]
assert held.withheld_state(binding.SOURCE_TASK,binding.SOURCE_LAUNCH_PUBLICATION,root) is None
print('full bootstrap source launch; both old DFU rows and old Result hold preserved')
"""
        run = subprocess.run([sys.executable, '-B', '-c', script], cwd=BASE, capture_output=True, text=True, timeout=60)
        self.assertEqual(0, run.returncode, run.stdout + run.stderr)
        self.assertIn('old Result hold preserved', run.stdout)


if __name__=='__main__':unittest.main()
