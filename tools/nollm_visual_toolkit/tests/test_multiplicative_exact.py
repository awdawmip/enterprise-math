from __future__ import annotations
import importlib.util
import math
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplicative as m
from nollm_visual_toolkit.certified_hex import certified_population


def frozen():
    path=ROOT/'evidence/migration06/frozen_multiplicative.py'
    spec=importlib.util.spec_from_file_location('m06_frozen_multiplicative',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


class MultiplicativeExactMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=frozen()

    def test_legacy_build_field_old_payload_unchanged(self):
        for count,scheme,scale in [(16,'valuation',1),(257,'mixed',.5),(257,'spiral',1.5),(257,'radial',2)]:
            cfg=m.config(count,scheme,scale)
            got=m.build_field(cfg);old=self.old.build_field(self.old.config(count,scheme,scale))
            self.assertEqual(got,old)

    def test_exact_source_is_explicit_and_unreduced(self):
        f=m.build_field(m.config(64,scale=.5),cell_scale=(50,100))
        self.assertEqual(f['cell_scale_source'],{'numerator':'50','denominator':'100','unreduced':True})
        self.assertEqual(f['cell_membership_exact']['scale'],{'numerator':'50','denominator':'100'})

    def test_boundary_witness_old_float_vs_declared_tie(self):
        cfg=m.config(16,scale=.5,overrides={'3':16384})
        legacy=m.build_field(cfg)
        exact=m.build_field(cfg,cell_scale=(1,2))
        self.assertEqual(legacy['records'][3]['coord'],[0,1])
        self.assertEqual(exact['records'][3]['coord'],[-1,1])
        self.assertEqual(exact['records'][3]['cell_status'],'CERTIFIED_TIE')

    def test_base_kernel_tie_is_adapted_to_legacy_lexicographic_semantics(self):
        # n=4 has phase pi/2 when prime 2 is assigned tick 8192.
        cfg=m.config(16,scale=.5,overrides={'2':8192})
        f=m.build_field(cfg,cell_scale=(1,2))
        c=f['cell_membership_exact']['certificates'][4]
        self.assertEqual(c['base_certificate']['cell'],['0','1'])
        self.assertEqual(c['cell'],['-1','1'])
        self.assertEqual(f['records'][4]['coord'],[-1,1])
        self.assertEqual(c['tie_rule'],m.LEXICOGRAPHIC_CELL_TIE_RULE)

    def test_exact_path_never_calls_legacy_lattice_quantizer(self):
        old=m.lattice_point
        m.lattice_point=lambda *_: (_ for _ in ()).throw(AssertionError('legacy quantizer called'))
        try:
            f=m.build_field(m.config(128,'mixed'),cell_scale=(1,1))
            self.assertEqual(f['cell_membership_exact']['status'],'CERTIFIED_ALL')
        finally:m.lattice_point=old

    def test_population_record_matches_existing_kernel(self):
        for scheme in ('valuation','mixed','spiral','radial'):
            cfg=m.config(256,scheme)
            f=m.build_field(cfg,cell_scale=(3,2))
            phi=[None]+[r['phase'] for r in f['records'][1:]]
            base=certified_population(phi,3,2,include_certificates=True)
            got=f['cell_membership_exact']
            self.assertEqual(got['phase_source_sha256'],base['phase_source_sha256'])
            self.assertEqual(got['base_certifier_schema'],base['schema'])
            self.assertEqual([c['base_certificate'] for c in got['certificates']],base['certificates'])
            self.assertEqual([r['coord'] for r in f['records']],
                             [None if c['cell'] is None else [int(v) for v in c['cell']] for c in got['certificates']])

    def test_low_budget_unresolved_is_not_guessed(self):
        f=m.build_field(m.config(512,'mixed'),cell_scale=(1,1),cell_bits=8,cell_max_bits=8)
        rec=f['cell_membership_exact']
        self.assertEqual(rec['status'],'UNRESOLVED_BOUNDARY')
        ids=[int(x) for x in rec['unresolved_identities']]
        self.assertTrue(ids)
        self.assertTrue(all(f['records'][n]['coord'] is None for n in ids))
        s=m.statistics(f)
        self.assertIsNone(s['occupied_hex_centers']);self.assertIsNone(s['collision_groups'])
        self.assertEqual(s['unresolved_cell_identities'],[str(n) for n in ids])
        with self.assertRaises(ValueError):m.hex_data(f)

    def test_exact_cv_squared_reconstructs_from_integer_counts(self):
        f=m.build_field(m.config(1024,'valuation'),cell_scale=(1,1))
        s=m.statistics(f,8,32)
        for counts,key in [([sum(b[j] for b in s['grid']) for j in range(32)],'angular_cv_squared_exact'),
                           ([v for b in s['grid'] for v in b],'area_sector_cv_squared_exact')]:
            total=sum(counts);num=len(counts)*sum(v*v for v in counts)-total*total;den=total*total
            self.assertEqual(s[key]['numerator'],str(num));self.assertEqual(s[key]['denominator'],str(den))
        self.assertEqual(s['approximate_metrics_role'],'OMITTED_FROM_EXACT_OBSERVER')

    def test_legacy_statistics_old_fields_unchanged(self):
        cfg=m.config(1024,'valuation')
        new=m.statistics(m.build_field(cfg));old=self.old.statistics(self.old.build_field(self.old.config(1024,'valuation')))
        self.assertEqual(new,old)

    def test_legacy_multiplication_and_hex_data_objects_unchanged(self):
        cfg=m.config(1024,'mixed',scale=1.5)
        new=m.build_field(cfg);old=self.old.build_field(self.old.config(1024,'mixed',scale=1.5))
        for a,b in ((0,7),(1,17),(5,7),(31,19)):
            self.assertEqual(m.multiplication(new,a,b),self.old.multiplication(old,a,b))
        self.assertEqual(m.hex_data(new),self.old.hex_data(old))

    def test_exact_display_error_and_rounded_error_omitted_not_mixed(self):
        f=m.build_field(m.config(256,'valuation',scale=2),cell_scale=(1,1))
        self.assertIsNone(m.statistics(f)['max_display_quantization_error'])
        d=m.multiplication(f,5,7)
        self.assertIsNone(d['rounded_relative_error'])
        self.assertEqual(d['approximate_metrics_role'],'OMITTED_FROM_EXACT_OBSERVER')

    def test_invalid_cell_scale_is_rejected_without_float_inference(self):
        for value in ((1,0),(0,1),(True,1),(1,2.0),[1,2],(1,),None):
            if value is None:
                self.assertEqual(set(m.build_field(m.config(16))),{'config','spf','prime_phase','records'})
            else:
                with self.assertRaises(ValueError):m.build_field(m.config(16),cell_scale=value)


if __name__=='__main__':unittest.main(verbosity=2)
