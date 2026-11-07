"""Historical migration and current P000 contract stay distinct and fail closed."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    'coordinate_migration', ROOT / 'tools/apply_coordinate_address_contract.py')
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)

# Verbatim axioms object from P000 at 7035c8011938aa0baffbb22f3827322053f520d5.
# That commit's actual CI failed at the former historical-hash assertion:
# https://github.com/awdawmip/enterprise-math/actions/runs/37033653345
OCTOBER_2_AXIOMS = {
    'REALITY_DIMENSION': 7,
    'ENTERPRISE_SPACE_DIMENSION': 6,
    'ENTERPRISE_TIME_DIMENSION': 1,
    'REALITY_DECOMPOSITION': '6D_SPACE_PLUS_1D_TIME',
    'ENTERPRISE_SPACE_KIND': 'DISCRETE_CELL_SPACE',
    'NATIVE_SPATIAL_AXIS_COUNT': 6,
    'NATIVE_SPATIAL_AXES_PAIRWISE_ENTERPRISE_ORTHOGONAL': True,
    'ENTERPRISE_NATIVE_RIGHT_ANGLE_DEGREES': 120,
    'NATIVE_PRIMITIVE_DIRECTION_DOMAIN': 'SIGNED_NATIVE_SPATIAL_AXES',
    'OFF_NATIVE_AXIS_APPARENT_SEGMENT_IS_PRIMITIVE': False,
    'OFF_NATIVE_AXIS_APPARENT_SEGMENT_REPRESENTATION': 'COMPOSITE_NATIVE_PATH',
    'OFF_NATIVE_AXIS_OBSERVER_MANIFESTATION': 'JITTER_OR_MULTIPATH',
    'PRIMITIVE_STABLE_FORCE_ARITY': 3,
    'PRIMITIVE_TWO_FORCE_BALANCE_ALLOWED': False,
    'PRIMITIVE_BALANCE_KIND': 'TRIADIC_CLOSURE_E',
    'CANONICAL_EQUAL_QUANTUM_BALANCE_NATIVE_ANGLE_DEGREES': 120,
    'APPARENT_TWO_FORCE_EQUILIBRIUM_IS_PRIMITIVE': False,
    'APPARENT_TWO_FORCE_EQUILIBRIUM_REQUIRES_TRIADIC_LIFT': True,
    'CURRENT_THREE_AXIS_MODEL': 'RESTRICTED_STATE_OR_OBSERVER_WITHIN_HEARTBEAT_X6',
    'ENTERPRISE_GEOMETRY_PRIMARY_TRANSFORMATION': 'ROTATION',
    'TIME_ROLE': 'TRACE_AND_ORDER_OF_RELATIONAL_CHANGE',
    'ENTERPRISE_NATIVE_PLANE_EXISTS': False,
    'ALL_RESEARCH_BASIS': 'HEARTBEAT_WORLD_NATIVE_X6',
    'TIME_MODELING': 'AS_NEEDED_SEPARATELY_TYPED',
}


class P000MigrationContractTests(unittest.TestCase):
    def setUp(self):
        self.source_text = (ROOT / migration.P000_MIGRATION_FIXTURE).read_text(encoding='utf-8')
        self.source = json.loads(self.source_text)
        self.manifest = json.loads((ROOT / migration.MANIFEST).read_text(encoding='utf-8'))
        self.migrated = migration.patch_json(
            'p000_reality_foundation.json', copy.deepcopy(self.source))
        self.current = copy.deepcopy(self.migrated)
        self.current['axioms'] = copy.deepcopy(OCTOBER_2_AXIOMS)

    def validate(self, current=None, **kwargs):
        migration.check_p000_contract(
            self.manifest, self.source_text,
            self.current if current is None else current, **kwargs)

    def test_verified_historical_source_and_result_hashes(self):
        self.assertEqual(migration.digest(self.source_text),
                         '5cfb95062fb9787df8b2ecf56d50458c8f8a477fda5f56964f72b1c79eafbc29')
        self.assertEqual(migration.objhash(self.source['axioms']),
                         '6696af428ca12ac84ec6162aed78a3108dd56342f0a3dfa5272a0d7079d6fd56')
        self.assertEqual(migration.digest(json.dumps(
            self.migrated, ensure_ascii=False, indent=2) + '\n'),
            'fc90294183b9b500957fd7e892a67a7b8825acdec949343574a68551118c420a')
        self.assertNotEqual(self.source, self.migrated)
        self.assertEqual(self.source['axioms'], self.migrated['axioms'])

    def test_october_2_revision_is_accepted_but_not_the_old_hash(self):
        self.assertEqual(migration.objhash(OCTOBER_2_AXIOMS),
                         '6871575e3e420101f5ad9643503a13fcf9dce2a30b40fa21ecfe209b694419e4')
        self.assertNotEqual(migration.objhash(OCTOBER_2_AXIOMS),
                            self.manifest['p000_axioms_sha256'])
        self.validate()

    def test_current_checkout_is_the_same_explicit_revision(self):
        current = json.loads((ROOT / 'p000_reality_foundation.json').read_text(encoding='utf-8'))
        migration.require_same_json(current['axioms'], OCTOBER_2_AXIOMS,
                                    'CURRENT_CHECKOUT_DIFFERS_FROM_REVIEWED_REVISION')
        self.validate(current)

    def test_historical_replay_remains_exact_and_separate(self):
        self.validate(self.migrated, historical_replay=True)
        with self.assertRaisesRegex(ValueError, 'P000_HISTORICAL_REPLAY_CHANGED'):
            self.validate(historical_replay=True)
        with self.assertRaisesRegex(ValueError, 'EXPLICIT_REVISION_REBASE'):
            self.validate(self.migrated)

    def test_every_current_axiom_value_is_protected(self):
        for key, value in OCTOBER_2_AXIOMS.items():
            current = copy.deepcopy(self.current)
            current['axioms'][key] = (not value if isinstance(value, bool)
                                      else value + 1 if isinstance(value, int)
                                      else value + '_CHANGED')
            with self.subTest(axiom=key), self.assertRaisesRegex(
                    ValueError, 'EXPLICIT_REVISION_REBASE'):
                self.validate(current)

    def test_boolean_integer_substitution_is_rejected(self):
        for key, value in [('ENTERPRISE_TIME_DIMENSION', True),
                           ('ENTERPRISE_NATIVE_PLANE_EXISTS', 0)]:
            current = copy.deepcopy(self.current)
            current['axioms'][key] = value
            with self.subTest(axiom=key), self.assertRaisesRegex(
                    ValueError, 'EXPLICIT_REVISION_REBASE'):
                self.validate(current)

    def test_added_removed_or_restored_axioms_are_rejected(self):
        for operation in ('add_unknown', 'remove_existing', 'restore_plane'):
            current = copy.deepcopy(self.current)
            if operation == 'add_unknown':
                current['axioms']['UNREVIEWED_AXIOM'] = True
            elif operation == 'remove_existing':
                del current['axioms']['TIME_MODELING']
            else:
                current['axioms']['ENTERPRISE_PLANE_NATIVE_DIMENSION'] = 6
            with self.subTest(operation=operation), self.assertRaisesRegex(
                    ValueError, 'EXPLICIT_REVISION_REBASE'):
                self.validate(current)

    def test_source_fixture_and_manifest_are_not_rebaselined(self):
        with self.assertRaisesRegex(ValueError, 'SOURCE_BYTES_CHANGED'):
            migration.check_p000_contract(self.manifest, self.source_text + '\n', self.current)
        with self.assertRaisesRegex(ValueError, 'SOURCE_BYTES_CHANGED'):
            migration.check_p000_contract(self.manifest, json.dumps(self.current), self.current)
        for field in ('source_main', 'p000_axioms_sha256'):
            manifest = copy.deepcopy(self.manifest)
            manifest[field] = 'changed'
            with self.subTest(field=field), self.assertRaises(ValueError):
                migration.check_p000_contract(manifest, self.source_text, self.current)
        for field in ('before_sha256', 'after_sha256'):
            manifest = copy.deepcopy(self.manifest)
            manifest['updated_surfaces'][0][field] = 'changed'
            with self.subTest(field=field), self.assertRaises(ValueError):
                migration.check_p000_contract(manifest, self.source_text, self.current)

    def test_missing_or_duplicate_manifest_entry_is_rejected(self):
        for duplicate in (False, True):
            manifest = copy.deepcopy(self.manifest)
            item = manifest['updated_surfaces'].pop(0)
            if duplicate:
                manifest['updated_surfaces'].extend([item, copy.deepcopy(item)])
            with self.subTest(duplicate=duplicate), self.assertRaisesRegex(
                    ValueError, 'ENTRY_MUST_BE_UNIQUE'):
                migration.check_p000_contract(manifest, self.source_text, self.current)

    def test_axiom_changing_migration_is_rejected(self):
        changed = copy.deepcopy(self.migrated)
        changed['axioms']['ENTERPRISE_SPACE_DIMENSION'] = 5
        with mock.patch.object(migration, 'patch_json', return_value=changed):
            with self.assertRaisesRegex(ValueError, 'MIGRATION_CHANGED_AXIOMS'):
                self.validate()

    def test_non_axiom_migration_drift_is_rejected(self):
        changed = copy.deepcopy(self.migrated)
        changed['coordinate_address_scope']['crossing_forces_increment'] = True
        with mock.patch.object(migration, 'patch_json', return_value=changed):
            with self.assertRaisesRegex(ValueError, 'RESULT_BYTES_CHANGED'):
                self.validate()

    def test_marker_noop_cannot_hide_current_address_drift(self):
        for field in self.current['coordinate_address_scope']:
            current = copy.deepcopy(self.current)
            current['coordinate_address_scope'][field] = 'BROKEN'
            # Demonstrate why the old marker-only idempotence gate is insufficient.
            self.assertIs(migration.patch_json('p000_reality_foundation.json', current), current)
            with self.subTest(field=field), self.assertRaisesRegex(
                    ValueError, 'CURRENT_ADDRESS_FIELD_CHANGED'):
                self.validate(current)
        current = copy.deepcopy(self.current)
        current['coordinate_address_contract'] = 'unregistered.json'
        with self.assertRaisesRegex(ValueError, 'CURRENT_ADDRESS_FIELD_CHANGED'):
            self.validate(current)

    def test_current_typed_address_and_origin_are_protected(self):
        for field in self.current['typed_semantics']['final_cell_address']:
            current = copy.deepcopy(self.current)
            current['typed_semantics']['final_cell_address'][field] = 'BROKEN'
            with self.subTest(field=field), self.assertRaisesRegex(
                    ValueError, 'CURRENT_ADDRESS_TYPING_CHANGED'):
                self.validate(current)
        current = copy.deepcopy(self.current)
        current['typed_semantics']['native_coordinate_origin']['scope'] = 'DISPLAY_ORIGIN'
        with self.assertRaisesRegex(ValueError, 'CURRENT_RAW_ORIGIN_SCOPE_CHANGED'):
            self.validate(current)

    def test_current_address_companion_is_protected(self):
        for operation in ('remove', 'duplicate', 'change'):
            current = copy.deepcopy(self.current)
            items = current['mandatory_companion_contracts']
            item = next(x for x in items if x['contract_id'] == 'FINAL_CELL_ADDRESS_CONSTRAINT')
            if operation == 'remove':
                items.remove(item)
            elif operation == 'duplicate':
                items.append(copy.deepcopy(item))
            else:
                item['scope'] = 'OPTIONAL'
            with self.subTest(operation=operation), self.assertRaisesRegex(
                    ValueError, 'CURRENT_ADDRESS_COMPANION_CHANGED'):
                self.validate(current)

    def test_every_current_address_invariant_is_protected(self):
        address_invariants = [item for item in self.migrated['machine_invariants']
                              if item not in self.source['machine_invariants']]
        self.assertEqual(len(address_invariants), 8)
        for item in address_invariants:
            current = copy.deepcopy(self.current)
            current['machine_invariants'].remove(item)
            with self.subTest(invariant=item), self.assertRaisesRegex(
                    ValueError, 'CURRENT_ADDRESS_INVARIANTS_CHANGED'):
                self.validate(current)

    def test_validation_does_not_mutate_its_inputs(self):
        before = copy.deepcopy((self.manifest, self.source_text, self.current))
        self.validate()
        self.assertEqual((self.manifest, self.source_text, self.current), before)

    def test_check_stdout_preserves_field_with_accurate_scope(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'tools/apply_coordinate_address_contract.py'), '--check'],
            cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = json.loads(result.stdout)
        self.assertFalse(result['p000_axioms_unchanged'])
        self.assertEqual(result['p000_axioms_unchanged_scope'],
                         'CURRENT_AXIOMS_VS_HISTORICAL_MIGRATION')
        self.assertTrue(result['p000_migration_axioms_preserved'])
        self.assertEqual(result['p000_validation_scope'], 'CURRENT_CONTRACT')
        self.assertEqual(result['p000_current_revision'], migration.P000_CURRENT_REVISION)

    def test_packaged_fixture_supports_historical_replay_from_another_cwd(self):
        # No --apply call: verify the historical read/transform/check path only.
        with tempfile.TemporaryDirectory(prefix='em-p000-replay-') as tmp:
            package = Path(tmp) / 'checkout'
            for path in ('tools/apply_coordinate_address_contract.py',
                         migration.P000_MIGRATION_FIXTURE, migration.MANIFEST):
                target = package / path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / path, target)
            code = (
                'import json,runpy,sys; m=runpy.run_path(sys.argv[1]); '
                's=m["read"](m["P000_MIGRATION_FIXTURE"]); '
                'manifest=json.loads(m["read"](m["MANIFEST"])); '
                'p=m["patch_json"]("p000_reality_foundation.json",json.loads(s)); '
                'm["check_p000_contract"](manifest,s,p,historical_replay=True)'
            )
            result = subprocess.run(
                [sys.executable, '-c', code,
                 str(package / 'tools/apply_coordinate_address_contract.py')],
                cwd=tmp, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
