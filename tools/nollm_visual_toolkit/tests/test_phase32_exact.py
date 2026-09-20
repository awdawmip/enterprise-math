from __future__ import annotations
import importlib.util
import json
import math
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import phase32_lab as m


def frozen():
    path=ROOT/'evidence/migration17/frozen_phase32_lab.py'
    spec=importlib.util.spec_from_file_location('m17_frozen_phase32_lab',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod


class Phase32ExactMigrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=frozen()

    def test_legacy_objects_unchanged(self):
        for count,mode,pitch in ((64,'golden',1),(256,'hash',.5),(256,'spiral',1.5)):
            cfg=dict(count=count,mode=mode,pitch=pitch,a=min(5,count-1),b=min(7,count-1))
            new=m.build(cfg); old=self.old.build(cfg)
            self.assertEqual(new,old)
            self.assertEqual(m.metrics(new),self.old.metrics(old))
            self.assertEqual(m.multiplication(new,new['config']['a'],new['config']['b']),
                             self.old.multiplication(old,old['config']['a'],old['config']['b']))
            self.assertEqual(m.hex_data(new),self.old.hex_data(old))

    def test_exact_pitch_is_explicit_unreduced_and_not_inferred_from_float(self):
        a=m.build(dict(count=128,pitch=.25),cell_pitch=(2,2))
        b=m.build(dict(count=128,pitch=8),cell_pitch=(2,2))
        self.assertEqual(a['cell_pitch_source'],{'numerator':'2','denominator':'2','unreduced':True})
        self.assertEqual(a['cell_membership_exact'],b['cell_membership_exact'])
        self.assertNotEqual(a['config']['pitch'],b['config']['pitch'])
        self.assertEqual(a['cell_membership_exact']['certifier_scale'],{'numerator':'2','denominator':'2'})
        self.assertEqual(a['cell_precision'],{'initial_bits':64,'max_bits':192})

    def test_float_boundary_witness_uses_declared_lexicographic_tie(self):
        cfg=dict(count=16,pitch=2,overrides={'3':m.DEN//4})
        legacy=m.build(cfg)
        exact=m.build(cfg,cell_pitch=(2,1))
        self.assertEqual(m.quantize(m.position(legacy,3),2),(0,1))
        cert=exact['cell_membership_exact']['certificates'][3]
        self.assertEqual(cert['status'],'CERTIFIED_TIE')
        self.assertEqual(cert['cell'],['-1','1'])
        self.assertEqual(cert['tie_rule'],'MINIMUM_EUCLIDEAN_DISTANCE_THEN_AXIAL_LEXICOGRAPHIC')

    def test_base_certifier_tie_is_adapted_not_substituted(self):
        cfg=dict(count=16,pitch=2,overrides={'2':m.DEN//8})
        exact=m.build(cfg,cell_pitch=(2,1))
        cert=exact['cell_membership_exact']['certificates'][4]
        self.assertEqual(cert['status'],'CERTIFIED_TIE')
        self.assertEqual(cert['base_certificate']['cell'],['0','1'])
        self.assertEqual(cert['cell'],['-1','1'])
        self.assertNotEqual(cert['tie_rule'],cert['base_certifier_tie_rule'])

    def test_exact_build_never_calls_phase32_display_geometry(self):
        old_position,old_quantize=m.position,m.quantize
        old_sqrt,old_sin,old_cos=m.math.sqrt,m.math.sin,m.math.cos
        forbidden=lambda *a,**k: (_ for _ in ()).throw(AssertionError('display float called'))
        try:
            m.position=m.quantize=forbidden
            m.math.sqrt=m.math.sin=m.math.cos=forbidden
            field=m.build(dict(count=128,mode='golden'),cell_pitch=(1,1))
        finally:
            m.position,m.quantize=old_position,old_quantize
            m.math.sqrt,m.math.sin,m.math.cos=old_sqrt,old_sin,old_cos
        self.assertEqual(field['cell_membership_exact']['status'],'CERTIFIED_ALL')
        self.assertEqual(field['cell_membership_exact']['phase_modulus'],str(m.DEN))

    def test_exact_metrics_never_call_float_geometry(self):
        field=m.build(dict(count=512,mode='hash'),cell_pitch=(1,1))
        old_position,old_quantize=m.position,m.quantize
        old_sqrt,old_sin,old_cos=m.math.sqrt,m.math.sin,m.math.cos
        forbidden=lambda *a,**k: (_ for _ in ()).throw(AssertionError('display float called'))
        try:
            m.position=m.quantize=forbidden
            m.math.sqrt=m.math.sin=m.math.cos=forbidden
            stats=m.metrics(field,readout_scale=10**12)
        finally:
            m.position, m.quantize=old_position,old_quantize
            m.math.sqrt,m.math.sin,m.math.cos=old_sqrt,old_sin,old_cos
        self.assertIsNone(stats['angular_cv']);self.assertIsNone(stats['equal_area_cv'])
        self.assertEqual(stats['approximate_metrics_role'],'OMITTED_FROM_EXACT_OBSERVER')
        self.assertEqual(sum(stats['angular_counts']),511)
        self.assertEqual(sum(stats['equal_area_counts']),511)

    def test_exact_cv_squared_reconstructs_from_counts(self):
        field=m.build(dict(count=1024,mode='golden',sectors=31,rings=7),cell_pitch=(3,2))
        stats=m.metrics(field,readout_scale=10**9+7)
        for counts,key in ((stats['angular_counts'],'angular_cv_squared_exact'),
                           (stats['equal_area_counts'],'equal_area_cv_squared_exact')):
            total=sum(counts); num=len(counts)*sum(x*x for x in counts)-total*total; den=total*total
            rec=stats[key]
            self.assertEqual(rec['counts'],[str(x) for x in counts])
            self.assertEqual(rec['numerator'],str(num));self.assertEqual(rec['denominator'],str(den))
            self.assertEqual(rec['readout']['scale'],str(10**9+7))
        self.assertEqual(stats['occupied_cells']+stats['collision_excess'],1023)

    def test_exact_multiplication_is_integer_only_and_preserves_counterexample(self):
        exact=m.build(dict(count=256,mode='spiral'),cell_pitch=(1,1))
        old_position,old_quantize=m.position,m.quantize
        forbidden=lambda *a,**k: (_ for _ in ()).throw(AssertionError('display geometry called'))
        try:
            m.position=m.quantize=forbidden
            result=m.multiplication(exact,2,2)
            zero=m.multiplication(exact,0,23)
        finally:m.position,m.quantize=old_position,old_quantize
        self.assertEqual(result['phase_defect_uint32'],m.GOLDEN)
        self.assertEqual(result['omega_defect'],0)
        self.assertIsNone(result['continuous_relative_error']);self.assertIsNone(result['rounded_relative_error'])
        self.assertEqual(result['approximate_metrics_role'],'OMITTED_FROM_EXACT_OBSERVER')
        self.assertIsNone(zero['phase_defect_uint32']);self.assertIsNone(zero['continuous_relative_error'])
        self.assertIn('absorbing',zero['zero_rule'])

    def test_exact_hex_data_keeps_all_ids_without_pixels(self):
        field=m.build(dict(count=256,mode='hash'),cell_pitch=(1,2))
        data=m.hex_data(field)
        self.assertEqual(data['schema'],'NOLLM_VISUAL_DATA_V2');self.assertEqual(len(data['records']),256)
        self.assertEqual(data['metadata']['cell_pitch_source'],{'numerator':'1','denominator':'2','unreduced':True})
        self.assertEqual(data['metadata']['typing'],'A2_CERTIFIED_INTEGER_RESIDUAL_OBSERVER_NOT_NATIVE_X6')
        self.assertNotIn('config',data['metadata']);self.assertNotIn('pitch',data['metadata']['phase_source'])
        self.assertEqual(data['metadata']['cell_precision'],{'initial_bits':64,'max_bits':192})
        for n,r in enumerate(data['records']):
            self.assertEqual(r['id'],str(n));self.assertEqual(r['n'],n)
            self.assertFalse(any(k.startswith('ideal') for k in r['fields']))
            self.assertEqual(r['fields']['phase_denominator'],m.DEN)
        def floats(x):
            if isinstance(x,float): return True
            if isinstance(x,dict): return any(floats(v) for v in x.values())
            if isinstance(x,list): return any(floats(v) for v in x)
            return False
        self.assertFalse(floats(data))

    def test_low_budget_unresolved_is_retained_and_not_exported(self):
        field=m.build(dict(count=512,mode='hash'),cell_pitch=(1,1),cell_bits=8,cell_max_bits=8)
        pop=field['cell_membership_exact'];self.assertEqual(pop['status'],'UNRESOLVED_BOUNDARY')
        self.assertTrue(pop['unresolved_identities'])
        stats=m.metrics(field)
        self.assertIsNone(stats['occupied_cells']);self.assertIsNone(stats['collision_excess']);self.assertIsNone(stats['max_cell_multiplicity'])
        self.assertEqual(stats['unresolved_cell_identities'],pop['unresolved_identities'])
        with self.assertRaises(ValueError):m.hex_data(field)

    def test_exact_actual_schedules_match_legacy_cells_in_finite_matrix(self):
        for mode in ('golden','hash','spiral'):
            for n,d in ((1,2),(1,1),(3,2)):
                cfg=dict(count=1024,mode=mode,pitch=n/d)
                old=m.build(cfg); exact=m.build(cfg,cell_pitch=(n,d))
                self.assertEqual(exact['cell_membership_exact']['status'],'CERTIFIED_ALL')
                new_cells=[tuple(map(int,c['cell'])) for c in exact['cell_membership_exact']['certificates']]
                old_cells=[m.quantize(m.position(old,i),n/d) for i in range(1024)]
                self.assertEqual(new_cells,old_cells)
                a=m.metrics(old);b=m.metrics(exact)
                self.assertEqual((b['occupied_cells'],b['collision_excess'],b['max_cell_multiplicity']),
                                 (a['occupied_cells'],a['collision_excess'],a['max_cell_multiplicity']))

    def test_invalid_exact_pitch_and_readout_options_fail_closed(self):
        for value in ((0,1),(1,0),(True,1),(1,2.0),[1,2],(1,)):
            with self.subTest(value=value),self.assertRaises(ValueError):
                m.build(dict(count=16),cell_pitch=value)
        legacy=m.build(dict(count=16))
        with self.assertRaises(ValueError):m.build(dict(count=16),cell_bits=8,cell_max_bits=8)
        with self.assertRaises(ValueError):m.metrics(legacy,readout_scale=None)
        with self.assertRaises(ValueError):m.metrics(legacy,readout_scale=7)


if __name__=='__main__':unittest.main(verbosity=2)
