"""M11 actual Python consumer vs frozen M10 browser readout functions.

Node tests below are function-level VM comparisons, NOT DOM/navigation tests.
A host stub exposes only the unchanged modulus and rejects any legacy dispatch.
BRC is executed unchanged; Fraction/divmod are independent test-only oracles.
"""
from __future__ import annotations

import ast
import contextlib
import copy
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import random
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from nollm_visual_toolkit import multiplicative as m
from nollm_visual_toolkit.angular_dispersion import AngularDispersion
from nollm_visual_toolkit.angular_dispersion_browser import SCRIPT
from enterprise_math import exact_arithmetic as brc

ROOT = Path(__file__).resolve().parents[3]
BASELINE = ROOT / 'evidence/migration11/frozen_m10_multiplicative.py'
JS_READOUTS = ROOT / 'evidence/migration11/frozen_m10_browser_readouts.js'
NODE = shutil.which('node')
COUNTS = {}


def old_module():
    spec = importlib.util.spec_from_file_location('nollm_visual_toolkit._m10_readout_baseline', BASELINE)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


def node(expression, data):
    if NODE is None:
        raise RuntimeError('Node is required for M11; no silent skip')
    preamble = '''
const forbidden=()=>{throw Error('legacy/display path must not execute');};
const MulMath={M:65536,stats:forbidden,multiply:forbidden};
Math.sqrt=forbidden;Math.hypot=forbidden;Math.sin=forbidden;Math.cos=forbidden;
'''
    program = SCRIPT + '\n' + preamble + JS_READOUTS.read_text() + '''
const input=JSON.parse(require('fs').readFileSync(0,'utf8'));
process.stdout.write(JSON.stringify(''' + expression + '));'
    run = subprocess.run([NODE, '-e', program], input=json.dumps(data), text=True,
                         capture_output=True, check=True, timeout=45)
    return json.loads(run.stdout)


def transport(field):
    # No pixels, and no point certificate bulk is needed by either readout.
    return {'cell_engine': field['cell_engine'], 'config': {'count': field['config']['count']},
            'prime_phase': field['prime_phase'],
            'records': [{k: r[k] for k in ('n','phase','omega','coord')} for r in field['records']],
            'cell_membership_exact': m.cell_membership_summary(field)}


def poison_float_math():
    stack = contextlib.ExitStack()
    for name in ('sqrt', 'hypot', 'sin', 'cos', 'atan2'):
        stack.enter_context(patch('math.' + name, side_effect=AssertionError('float '+name)))
    return stack


class ExactReadoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old = old_module()
        cls.fields = {name: m.build_field(m.config(257,name), cell_scale=(1,1))
                      for name in ('valuation','mixed','spiral','radial')}
        cls.partial = m.build_field(m.config(512,'mixed'), cell_scale=(1,1),
                                   cell_bits=8, cell_max_bits=8)

    def assert_no_float(self, value):
        if isinstance(value, dict):
            for v in value.values(): self.assert_no_float(v)
        elif isinstance(value, (list, tuple)):
            for v in value: self.assert_no_float(v)
        else:
            self.assertNotIsInstance(value, float)

    def assert_reconstructs(self, record, scale):
        counts = [int(x) for x in record['counts']]
        total, bins = sum(counts), len(counts)
        mean = Fraction(total, bins)
        variance = sum((Fraction(c)-mean)**2 for c in counts) / bins
        expected = variance / (mean*mean)
        self.assertEqual(Fraction(int(record['numerator']), int(record['denominator'])), expected)
        if scale is None:
            self.assertIsNone(record['readout']); return
        rd = record['readout']; tr = rd['trace']
        n, d = int(record['numerator']), int(record['denominator'])
        q, r = divmod(scale*n, d)
        self.assertEqual((int(rd['integer']), int(rd['residual_numerator'])), (q,r))
        self.assertEqual(int(rd['residual_denominator']), scale*d)
        self.assertEqual(int(tr['numerator']), scale*n)
        self.assertEqual(int(tr['collapsed_numerator'])+int(tr['remainder']), scale*n)
        self.assertTrue(0 <= r < d)
        self.assertEqual(Fraction(q,scale)+Fraction(r,d*scale), expected)
        self.assertEqual(rd['kind'], 'INTEGER_PLUS_RATIONAL_RESIDUAL_OF_CV_SQUARED')

    def test_01_frozen_actual_source_integrity_and_unchanged_functions(self):
        raw=BASELINE.read_bytes()
        self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),
                         '6840b43d93a0eb787a5fdfd3391cf554d758a993')
        old={x.name:ast.dump(x,include_attributes=False) for x in ast.parse(raw).body
             if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))}
        new={x.name:ast.dump(x,include_attributes=False) for x in ast.parse(Path(m.__file__).read_text()).body
             if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))}
        self.assertEqual(set(old),set(new))
        changed=[name for name in old if old[name]!=new[name]]
        self.assertEqual(changed,['multiplication','statistics'])

    def test_02_exact_statistics_omit_floats_and_keep_full_schema(self):
        for field in self.fields.values():
            with poison_float_math(): result=m.statistics(field)
            self.assert_no_float(result)
            for key in ('angular_cv','area_sector_cv','iid_cv_scale','max_display_quantization_error'):
                self.assertIsNone(result[key])
            self.assertEqual(result['approximate_metrics_role'],'OMITTED_FROM_EXACT_OBSERVER')
            self.assertNotIn('iid_boundary',result)
            self.assert_reconstructs(result['angular_cv_squared_exact'],1_000_000)
            self.assert_reconstructs(result['area_sector_cv_squared_exact'],1_000_000)

    def test_03_default_stats_match_frozen_browser_complete_records(self):
        fields=list(self.fields.values())+[self.partial]
        cases=[transport(f) for f in fields]
        actual=node('input.map(f=>{const {fibers,...s}=MulExactReadouts.stats(f);return s;})',cases)
        self.assertEqual(actual,[m.statistics(f) for f in fields])
        COUNTS['complete_python_node_stats']=len(cases)

    def test_04_product_complete_records_match_browser_sampled_pairs(self):
        rng=random.Random(11002026)
        pairs=[(0,0),(0,7),(7,0),(1,1),(1,255),(255,255),(5,7)]
        pairs += [(rng.randrange(257),rng.randrange(257)) for _ in range(250)]
        cases=[{'f':transport(f),'pairs':pairs} for f in self.fields.values()]
        actual=node('input.map(x=>x.pairs.map(([a,b])=>MulExactReadouts.multiply(x.f,a,b)))',cases)
        expected=[[m.multiplication(f,a,b) for a,b in pairs] for f in self.fields.values()]
        self.assertEqual(actual,expected)
        for item in expected:self.assert_no_float(item)
        COUNTS['complete_python_node_products']=len(pairs)*len(cases)

    def test_05_zero_product_is_undefined_phase_not_measured_zero_error(self):
        f=self.fields['valuation']
        for a,b in ((0,0),(0,7),(7,0)):
            with poison_float_math(): value=m.multiplication(f,a,b)
            self.assertEqual(value['product'],0)
            for key in ('phase_defect','omega_defect','ideal_relative_error','rounded_relative_error'):
                self.assertIsNone(value[key])
            self.assertIn('undefined',value['zero_phase'])

    def test_06_products_do_not_access_pixel_scale_or_cell_coordinates(self):
        f=transport(self.fields['mixed'])
        for row in f['records']: row.pop('coord')
        with poison_float_math(), patch.object(m,'complex',side_effect=AssertionError('complex pixels'),create=True):
            value=m.multiplication(f,5,7)
        self.assertEqual(value['phase_defect'],0)
        self.assertIsNone(value['ideal_relative_error'])

    def test_07_spiral_nonclosure_is_preserved(self):
        f=self.fields['spiral']
        value=m.multiplication(f,5,7)
        self.assertNotEqual(value['phase_defect'],0)
        self.assertEqual(value['omega_defect'],0)
        self.assertEqual(value['phase_defect'],(35-5-7)*m.GOLDEN_STEP%m.PHASE_MODULUS)

    def test_08_partial_cells_preserve_exact_histograms_but_not_fake_totals(self):
        f=self.partial
        self.assertTrue(f['cell_membership_exact']['unresolved_identities'])
        with poison_float_math(): result=m.statistics(f)
        for key in ('occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber'):
            self.assertIsNone(result[key])
        self.assertEqual(sum(map(sum,result['grid'])),511)
        self.assert_reconstructs(result['area_sector_cv_squared_exact'],1_000_000)
        with self.assertRaises(ValueError):m.hex_data(f)

    def test_09_custom_histogram_dimensions_and_readout_scales(self):
        dims=[(1,1),(1,7),(3,1),(3,7),(5,33),(9,64),(2,257),(300,1)]
        scales=[None,1,10,257,10**70+19]
        f=self.fields['mixed'];cases=0
        for rings,sectors in dims:
            for scale in scales:
                with poison_float_math():r=m.statistics(f,rings,sectors,readout_scale=scale)
                self.assertEqual([len(row) for row in r['grid']],[sectors]*rings)
                self.assertEqual(sum(map(sum,r['grid'])),256)
                ordered=[0]*(rings*sectors)
                for row in f['records'][1:]:
                    band=(row['n']-1)*rings//256;sector=row['phase']*sectors//65536
                    ordered[band*sectors+sector]+=1
                self.assertEqual(r['area_sector_cv_squared_exact']['counts'],[str(c) for c in ordered])
                for key in ('angular_cv_squared_exact','area_sector_cv_squared_exact'):
                    self.assert_reconstructs(r[key],scale)
                cases+=1
        COUNTS['custom_histogram_scale_cases']=cases

    def test_10_default_custom_and_none_readout_reuse_brc(self):
        f=self.fields['valuation']
        with patch.object(brc,'brc_scaled_evaluate',wraps=brc.brc_scaled_evaluate) as evaluate:
            m.statistics(f);self.assertEqual(evaluate.call_count,2)
            m.statistics(f,readout_scale=None);self.assertEqual(evaluate.call_count,2)
            m.statistics(f,readout_scale=2**90+1);self.assertEqual(evaluate.call_count,4)
        for call in (evaluate.call_args_list[0],evaluate.call_args_list[-1]):
            self.assertIsInstance(call.args[0],brc.DivisionExpr)

    def test_11_readout_scale_cannot_change_cell_or_source_state(self):
        f=self.fields['valuation'];before=copy.deepcopy(f)
        a=m.statistics(f,readout_scale=1);b=m.statistics(f,readout_scale=2**120)
        self.assertEqual(f,before)
        self.assertEqual(a['grid'],b['grid'])
        for key in ('angular_cv_squared_exact','area_sector_cv_squared_exact'):
            x=copy.deepcopy(a[key]);y=copy.deepcopy(b[key]);x.pop('readout');y.pop('readout')
            self.assertEqual(x,y)
        a['grid'][0][0]=999999
        a['area_sector_cv_squared_exact']['counts'][0]='999999'
        self.assertEqual(f,before)

    def test_12_single_bin_extension_exact_no_padding_no_lost_denominator(self):
        counts=[1,2,63,2**200+17]
        for total in counts:
            a=AngularDispersion((total,))
            self.assertEqual((a.bins,a.population,a.numerator,a.denominator),(1,total,0,total*total))
            r=a.as_record(scale=10**80+1)
            self.assertEqual(r['counts'],[str(total)])
            self.assert_reconstructs(r,10**80+1)
        cases=[{'counts':[str(c)],'scale':str(10**80+1)} for c in counts]
        self.assertEqual(node('input.map(x=>NollmAngularExact.fromCounts(x.counts,x.scale))',cases),
                         [AngularDispersion((c,)).as_record(scale=10**80+1) for c in counts])

    def test_13_single_bin_zero_or_invalid_input_still_rejected(self):
        for counts in ((),(0,),(-1,),(True,),(1.0,),('1',)):
            with self.subTest(counts=counts),self.assertRaises(ValueError):AngularDispersion(counts)
        actual=node('''(()=>{const bad=[[],[0],[-1],[true],[0.5],[null]];
return bad.map(c=>{try{NollmAngularExact.fromCounts(c);return false;}catch(e){return true;}});})()''',None)
        self.assertTrue(all(actual))

    def test_14_integer_parameter_validation(self):
        for v in (0,-1,True,1.5,'2',None):
            for kw in ({'rings':v},{'sectors':v}):
                with self.subTest(kw=kw),self.assertRaises(ValueError):m.statistics(self.fields['mixed'],**kw)
        for v in (0,-1,True,1.0,'1000000'):
            with self.subTest(v=v),self.assertRaises(ValueError):m.statistics(self.fields['mixed'],readout_scale=v)
        legacy=m.build_field(m.config(16))
        for v in (None,1,2**90):
            with self.assertRaises(ValueError):m.statistics(legacy,readout_scale=v)

    def test_15_legacy_whole_objects_and_json_unchanged(self):
        cases=0
        for scheme,scale in itertools.product(('valuation','mixed','spiral','radial'),(.5,1,1.5)):
            cfg=m.config(257,scheme,scale);new=m.build_field(cfg);old=self.old.build_field(cfg)
            self.assertEqual(new,old)
            for dims in ((1,1),(3,1),(1,7),(3,7),(8,32)):
                a=m.statistics(new,*dims);b=self.old.statistics(old,*dims)
                self.assertEqual(a,b);self.assertEqual(json.dumps(a),json.dumps(b));cases+=1
            for a,b in ((0,7),(1,17),(5,7),(31,19),(256,256)):
                got=m.multiplication(new,a,b);want=self.old.multiplication(old,a,b)
                self.assertEqual(got,want);self.assertEqual(json.dumps(got),json.dumps(want))
            self.assertEqual(m.hex_data(new),self.old.hex_data(old))
        COUNTS['legacy_full_statistic_objects']=cases

    def test_16_cli_machine_only_real_outputs_use_new_exact_readouts(self):
        with tempfile.TemporaryDirectory() as td:
            out=Path(td)/'report.json'
            cmd=[sys.executable,'-m','nollm_visual_toolkit.multiplicative','--count','64',
                 '--cell-scale','0.50','--machine-only','--report',str(out)]
            # Existing package root and lazy BRC dependencies, no render stub.
            import os
            env=dict(os.environ,PYTHONPATH=str(ROOT/'src')+':'+str(ROOT/'tools/nollm_visual_toolkit'))
            subprocess.run(cmd,check=True,capture_output=True,text=True,env=env,timeout=30)
            data=json.loads(out.read_text())
            self.assertEqual(data['schema'],'NOLLM_MULTIPLICATIVE_REPORT_V2')
            self.assertEqual(data['cell_scale_source']['text'],'0.50')
            self.assertEqual(data['cell_membership_exact']['scale'],{'numerator':'50','denominator':'100'})
            self.assertEqual(data['html_observer_boundary'],'NOT_GENERATED_MACHINE_ONLY')
            self.assert_no_float(data['statistics'])
            self.assert_reconstructs(data['statistics']['area_sector_cv_squared_exact'],1_000_000)

    def test_17_invalid_product_labels_remain_rejected(self):
        for a,b in ((-1,3),(257,3),(True,2),(3.5,7),('3',5)):
            with self.subTest(a=a,b=b),self.assertRaises(ValueError):m.multiplication(self.fields['mixed'],a,b)

    def test_18_numerical_equality_does_not_collapse_ordered_sources(self):
        a=AngularDispersion((7,));b=AngularDispersion((14,));c=AngularDispersion((7,7))
        self.assertEqual(a.compare_value(b),0);self.assertEqual(a.compare_value(c),0)
        self.assertNotEqual(a.as_record(),b.as_record());self.assertNotEqual(a.as_record(),c.as_record())

    def test_19_residual_refinement_keeps_original_histogram(self):
        f=self.fields['mixed']
        for multiplier in (2,7,100):
            a=m.statistics(f,3,7,readout_scale=17)['area_sector_cv_squared_exact']
            b=m.statistics(f,3,7,readout_scale=17*multiplier)['area_sector_cv_squared_exact']
            qa,ra=int(a['readout']['integer']),int(a['readout']['residual_numerator'])
            qb,rb=int(b['readout']['integer']),int(b['readout']['residual_numerator'])
            d=int(a['denominator']);carry,rem=divmod(multiplier*ra,d)
            self.assertEqual(qb,multiplier*qa+carry);self.assertEqual(rb,rem)
            self.assertEqual(a['counts'],b['counts'])

    def test_20_no_pixel_reconstruction_or_function_replacement(self):
        # The exact math dependency remains the same inherited BRC implementation.
        s=(ROOT/'src/enterprise_math/exact_arithmetic.py').read_bytes()
        self.assertEqual(hashlib.sha1(b'blob '+str(len(s)).encode()+b'\0'+s).hexdigest(),
                         '35ea95b0916494b83a92386e3e313928362dd79e')
        for field in self.fields.values():
            f=copy.deepcopy(field)
            for r in f['records']:r.pop('ideal')
            with poison_float_math():result=m.statistics(f)
            self.assertEqual(result,m.statistics(field))


if __name__=='__main__': unittest.main(verbosity=2)
