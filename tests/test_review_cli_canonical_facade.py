"""Isolated CLI/import regression for the canonical review facade.

Copies only the actual repository CLI, quarantine installer/read reducer and
three frozen historical records into a temporary fixture, then executes fresh
Python -I script/import processes. Unrelated authority layers are fixture doubles.
The active-DA boundary stops before review construction: no live authorization,
review admission, transaction persistence or follow-up completion is proved.
No network, full-repository copy, persistent fixture output or external path is used.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
RID = 'RR-A4EBF925BE07691C8C16'
TASK = 'RS-PERFECT-PRIME-AP-BINOMIAL-CAUCHY-LAYER-COFACTOR-POSITIVITY'
OLD_DR = 'DR-9986FE430DB065EA8EF2'
NEW_DR = 'DR-6FAD20D6377588C9CBB2'
RESULT_PATH = f'research_result_records/{TASK}/{RID}.json'
OLD_PATH = f'research_result_reviews/{RID}/{OLD_DR}.json'
NEW_PATH = f'research_result_reviews/{RID}/{NEW_DR}.json'
FIRST_ERROR = 'the first immutable review becomes operational immediately and requires --followup-spec'
SECOND_ERROR = 'a second-or-later review reopens exact-set review authority'

BASE_DOUBLE = '''
import json
from pathlib import Path
from types import SimpleNamespace
ROOT = Path(__file__).resolve().parents[1]
class ResultRecordError(ValueError): pass
TERMINAL_DISPOSITIONS = {'ACCEPTED','REJECTED','PARKED','CLOSED','SUPERSEDED'}
ALL_DISPOSITIONS = TERMINAL_DISPOSITIONS | {'RETURN_TO_OWNER','REQUEST_REPLICATION','REQUEST_REVISION'}
DESTINATION_CLASSES = {'NONE','FOLLOWUP_TASK'}
_parallel = SimpleNamespace()
def rows(relative, key, root):
    out = []
    for p in sorted((root / relative).glob('*/*.json')):
        row = json.loads(p.read_text()); row[key] = p.relative_to(root).as_posix(); out.append(row)
    return out
def iter_results(root=ROOT): return rows('research_result_records','_record_path',root)
def iter_reviews(root=ROOT): return rows('research_result_reviews','_review_path',root)
_RAW_ITER_RESULTS = iter_results
def task_result_state(*args, **kwargs): return {}
def audit(root=ROOT): return []
def _now(value): return value or '2026-10-12T19:00:00+00:00'
def legacy_main():
    import sys
    if sys.argv[1].startswith('fixture-raise-'):
        from tools import research_result_records as public
        name = sys.argv[1].removeprefix('fixture-raise-')
        errors = {'ResultRecordError': public.ResultRecordError,
                  'DriverFollowupError': public._followup_impl.DriverFollowupError,
                  'DriverAuthorityError': public._driver_authority.DriverAuthorityError,
                  'ResultControlReplacementError': public._result_replacements.ResultControlReplacementError,
                  'ImmutableCandidateValidationError': public._candidate_validation.ImmutableCandidateValidationError,
                  'ImmutableWriteTransactionError': public._write_tx.ImmutableWriteTransactionError}
        raise errors[name]('FIXTURE_DOMAIN_EXCEPTION_' + name)
    raise ResultRecordError('FIXTURE_LEGACY_NON_REVIEW_MAIN')
_impl = SimpleNamespace(main=legacy_main, command_freeze=None)
main = legacy_main
'''

DRIVER_DOUBLE = '''
import inspect, json, sys
class DriverAuthorityError(ValueError): pass
def require_active_driver(*args, **kwargs):
    caller = inspect.currentframe().f_back
    writer = caller.f_globals
    from tools import research_result_records as public
    import research_review_evidence as evidence
    record = {'writer_module': writer['__name__'],
              'writer_review_ids': sorted(r['review_id'] for r in writer['iter_reviews']()),
              'reader_review_ids': sorted(r['review_id'] for r in public.iter_reviews()),
              'reader_state': evidence.state('RR-A4EBF925BE07691C8C16')['review_state'],
              'spec_loaded': caller.f_locals.get('spec') is not None,
              'shared_result_error_class': writer['ResultRecordError'] is public.ResultRecordError,
              'writer_function_uses_public_globals': writer is vars(public)}
    print('FIXTURE_OBSERVATION ' + json.dumps(record,sort_keys=True), file=sys.stderr)
    raise DriverAuthorityError('FIXTURE_STOP_BEFORE_REVIEW_CONSTRUCTION')
'''

STORE_DOUBLE = '''
from pathlib import Path
ROOT = Path(__file__).resolve().parent
class ReviewEvidenceError(ValueError): pass
TERMINAL_DISPOSITIONS = {'ACCEPTED','REJECTED','PARKED','CLOSED','SUPERSEDED'}
ALL_DISPOSITIONS = TERMINAL_DISPOSITIONS | {'RETURN_TO_OWNER','REQUEST_REPLICATION','REQUEST_REVISION'}
def intakes(root=ROOT): return {}
def reference_passes(root=ROOT): return {}
def syntheses(root=ROOT): return {}
def _id(value,label): return value
def review_set_hash(ids): return 'fixture-exact-set-' + '-'.join(sorted(ids))
'''

OTHER_DOUBLES = {
    'control_plane/research_historical_result_intake.py': '',
    'control_plane/immutable_write_transaction.py': 'class ImmutableWriteTransactionError(ValueError): pass\ndef commit(*args,**kwargs): raise AssertionError("FIXTURE_FORBIDS_REVIEW_WRITE")\n',
    'control_plane/research_immutable_candidate_validation.py': 'class ImmutableCandidateValidationError(ValueError): pass\ndef require_valid_review_candidate(*args,**kwargs): raise AssertionError("FIXTURE_FORBIDS_REVIEW_CANDIDATE")\n',
    'control_plane/research_result_authority_fault_isolation.py': 'def operational_results(rows,root,**kwargs): return rows\ndef operational_reviews(rows,root): return rows\n',
    'control_plane/research_continuation_write_authority.py': 'def operational(rows,kind,root): return rows\n',
    'control_plane/research_continuation.py': 'class ContinuationError(ValueError): pass\ndef require_review_authority(*args,**kwargs): return None\n',
    'research_driver_followup.py': 'class DriverFollowupError(ValueError): pass\nRESULT_CONTINUATION_DECISION = "RESULT_ACCEPTED_TASK_OPEN_CONTINUATION"\n',
    'research_driver_followup_guard.py': '',
    'research_result_control_replacements.py': 'class ResultControlReplacementError(ValueError): pass\ndef replacement_edges(*args,**kwargs): return {}\n',
    'control_plane/research_control_bootstrap.py': 'from control_plane import research_driver_review_authority_fault_isolation as isolation\ndef install(root): isolation.install(root)\n',
}


def write(root, relative, content):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}


class CanonicalReviewCliTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # These are immutable existing repository records, never live authority.
        # Hash-check all three before using their bytes as local fixture inputs.
        expected = {
            RESULT_PATH: (3516, 'dd0c8f552c510d930b1ccf798db8582813fcea3ed19c81f3a4ca69a9ac7aa58b'),
            OLD_PATH: (1096, '158118750f33040075a5b94c2e86466c454270ac2a0fcd2770a6369de6f8de5a'),
            NEW_PATH: (2170, '7449359817b7c153968dd37b4c742fc86e1270ad01e872cf4978a50a0135038d'),
        }
        for relative, (size, digest) in expected.items():
            data = (REPO / relative).read_bytes()
            assert len(data) == size, relative
            assert hashlib.sha256(data).hexdigest() == digest, relative

    def fixture(self, active_new=False):
        temp = tempfile.TemporaryDirectory(prefix='em-cli-facade-regression-')
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        write(root, 'tools/__init__.py', '')
        write(root, 'control_plane/__init__.py', '')
        write(root, 'control_plane/research_result_records_compat_runtime.py', BASE_DOUBLE)
        write(root, 'research_driver_authority.py', DRIVER_DOUBLE)
        write(root, 'research_review_evidence_store.py', STORE_DOUBLE)
        for relative, content in OTHER_DOUBLES.items(): write(root, relative, content)
        for relative in ['control_plane/research_driver_review_authority_fault_isolation.py',
                         'control_plane/research_review_evidence_store.py',
                         'research_review_evidence.py', RESULT_PATH, OLD_PATH]:
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / relative, destination)
            self.assertEqual((REPO / relative).read_bytes(), destination.read_bytes())
        shutil.copyfile(REPO / 'tools/research_result_records.py', root / 'tools/research_result_records.py')
        self.assertEqual((REPO / 'tools/research_result_records.py').read_bytes(),
                         (root / 'tools/research_result_records.py').read_bytes())
        addendum = json.loads((REPO / 'control_plane/driver_review_authority_quarantine_addendum_20260904.json').read_text())
        exact = [r for r in addendum['entries'] if r['review_id'] == OLD_DR]
        self.assertEqual(1, len(exact))
        # Feed the exact frozen quarantine entry through the real validator/filter;
        # unrelated registry entries and the full Source bootstrap are excluded.
        write(root, 'research_driver_review_authority_quarantines.json', json.dumps({
            'schema': addendum['schema'], 'status': addendum['status'], 'entries': exact}))
        write(root, 'fixture-spec.json', '{}')
        if active_new: shutil.copyfile(REPO / NEW_PATH, root / NEW_PATH)
        write(root, 'invoke_imported.py', '''import sys\nfrom pathlib import Path\nsys.path.insert(0,str(Path(__file__).resolve().parent))\nfrom tools import research_result_records as records\nsys.argv=[str(Path(__file__).parent/'tools/research_result_records.py'),*sys.argv[1:]]\ntry:\n    raise SystemExit(records.canonical_main())\nexcept (records.ResultRecordError,records._driver_authority.DriverAuthorityError) as exc:\n    print('ERROR:',exc)\n    raise SystemExit(1)\n''')
        return root

    def run_cli(self, active_new=False, spec=False, imported=False, non_review=False):
        root = self.fixture(active_new)
        before = hashes(root)
        argv = [sys.executable, '-I', str(root / ('invoke_imported.py' if imported else 'tools/research_result_records.py'))]
        if non_review: argv.append(non_review if isinstance(non_review,str) else 'fixture-non-review')
        else:
            argv += ['review','--result-id',RID,'--driver-id','EM-DVR-FIXTURE',
                     '--disposition','ACCEPTED','--review-path','fixture-report.md',
                     '--destination-class','NONE','--reviewer-session-id','fixture-session',
                     '--reviewer-contribution-ids-json','[]']
            if spec: argv += ['--followup-spec','fixture-spec.json']
        proc = subprocess.run(argv, cwd=root, capture_output=True, text=True, timeout=10)
        self.assertEqual(before, hashes(root), 'Fixture canonical records/source must not be changed')
        self.assertEqual(1, proc.returncode, proc.stdout + proc.stderr)
        self.assertNotIn('Traceback', proc.stderr)
        observations = [json.loads(line.removeprefix('FIXTURE_OBSERVATION '))
                        for line in proc.stderr.splitlines() if line.startswith('FIXTURE_OBSERVATION ')]
        value = {'active_new':active_new,'spec':spec,'imported':imported,
                 'non_review':non_review,'returncode':proc.returncode,'stdout':proc.stdout,
                 'stderr':proc.stderr,'observations':observations,'fixture_all_bytes_unchanged':True}
        return value

    def test_actual_script_executes_the_public_canonical_command(self):
        value = self.run_cli(spec=True)
        self.assertIn('FIXTURE_STOP_BEFORE_REVIEW_CONSTRUCTION', value['stdout'])
        observation = value['observations'][0]
        self.assertEqual('tools.research_result_records', observation['writer_module'])
        self.assertTrue(observation['writer_function_uses_public_globals'])
        self.assertTrue(observation['shared_result_error_class'])

    def test_first_review_still_requires_followup_spec(self):
        value = self.run_cli(spec=False)
        self.assertIn(FIRST_ERROR, value['stdout'])
        self.assertEqual([], value['observations'])

    def test_script_and_import_share_the_empty_filtered_review_set(self):
        for imported in [False, True]:
            with self.subTest(imported=imported):
                value = self.run_cli(spec=True, imported=imported)
                self.assertIn('FIXTURE_STOP_BEFORE_REVIEW_CONSTRUCTION', value['stdout'])
                observation = value['observations'][0]
                self.assertEqual('tools.research_result_records', observation['writer_module'])
                self.assertEqual([], observation['writer_review_ids'])
                self.assertEqual([], observation['reader_review_ids'])
                self.assertEqual('NO_REVIEW', observation['reader_state'])
                self.assertTrue(observation['spec_loaded'])
                self.assertTrue(observation['shared_result_error_class'])
                self.assertTrue(observation['writer_function_uses_public_globals'])

    def test_valid_existing_review_remains_visible_as_single_review(self):
        for imported in [False, True]:
            with self.subTest(imported=imported):
                value = self.run_cli(active_new=True, imported=imported)
                self.assertIn('FIXTURE_STOP_BEFORE_REVIEW_CONSTRUCTION', value['stdout'])
                observation = value['observations'][0]
                self.assertEqual([NEW_DR], observation['writer_review_ids'])
                self.assertEqual([NEW_DR], observation['reader_review_ids'])
                self.assertEqual('SINGLE_REVIEW_FLOW', observation['reader_state'])
                self.assertFalse(observation['spec_loaded'])

    def test_later_review_still_rejects_inline_followup(self):
        for imported in [False, True]:
            with self.subTest(imported=imported):
                value = self.run_cli(active_new=True, spec=True, imported=imported)
                self.assertIn(SECOND_ERROR, value['stdout'])
                self.assertEqual([], value['observations'])

    def test_non_review_preserves_legacy_delegation(self):
        value = self.run_cli(non_review=True)
        self.assertIn('FIXTURE_LEGACY_NON_REVIEW_MAIN', value['stdout'])

    def test_all_public_domain_exceptions_are_caught(self):
        for name in ['ResultRecordError','DriverFollowupError','DriverAuthorityError',
                     'ResultControlReplacementError','ImmutableCandidateValidationError',
                     'ImmutableWriteTransactionError']:
            with self.subTest(error=name):
                value = self.run_cli(non_review='fixture-raise-' + name)
                self.assertIn('FIXTURE_DOMAIN_EXCEPTION_' + name, value['stdout'])

if __name__ == '__main__': unittest.main(verbosity=2)
