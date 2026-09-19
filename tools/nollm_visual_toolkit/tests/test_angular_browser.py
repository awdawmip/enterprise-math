"""Cross-language tests of the embedded browser port against existing BRC.

These use Node for the pure kernel, not a DOM substitute for browser tests.
The migration runner separately executes the actual page in Chromium.
"""
from __future__ import annotations
import itertools
import json
import shutil
import subprocess
import unittest

from nollm_visual_toolkit.angular_dispersion import AngularDispersion
from nollm_visual_toolkit.angular_dispersion_browser import SCRIPT

NODE = shutil.which('node')


def js(expression: str, data=None):
    program = SCRIPT + '\nconst input=JSON.parse(require("fs").readFileSync(0,"utf8"));\n' + \
        'const result=(' + expression + ');\nprocess.stdout.write(JSON.stringify(result));'
    result = subprocess.run([NODE, '-e', program], input=json.dumps(data),
        text=True, capture_output=True, timeout=60, check=True)
    return json.loads(result.stdout)


@unittest.skipUnless(NODE, 'Node is required for pure JavaScript port validation')
class AngularBrowserTests(unittest.TestCase):
    def test_complete_record_matches_existing_python_brc(self):
        histograms = [list(c) for b in range(2, 6)
            for c in itertools.product(range(4), repeat=b) if sum(c)]
        histograms += [[2**80, 1], [2**80+1, 1], [2**512, 3, 5], [10**200, 10**201, 7]]
        cases = [{'counts': [str(c) for c in counts], 'scale': str(scale)}
            for counts in histograms for scale in (1, 10**6, 2**127+7)]
        actual = js('input.map(x=>NollmAngularExact.fromCounts(x.counts,x.scale))', cases)
        for case, record in zip(cases, actual):
            counts = [int(c) for c in case['counts']]
            expected = AngularDispersion.from_counts(counts).as_record(scale=int(case['scale']))
            self.assertEqual(record, expected)
        self.assertEqual(len(cases), 4080)

    def test_source_only_schema_matches_python(self):
        cases = [[1, 2, 3], [0, 3, 1], [2, 2], [1, 0, 4, 0]]
        actual = js('input.map(x=>NollmAngularExact.fromCounts(x))', cases)
        self.assertEqual(actual, [AngularDispersion.from_counts(c).as_record() for c in cases])

    def test_comparison_matches_exact_python(self):
        counts = [list(c) for c in itertools.product(range(3), repeat=3) if sum(c)]
        cases = [[a, b] for a in counts for b in counts]
        actual = js('input.map(([a,b])=>NollmAngularExact.compareCounts(a,b))', cases)
        expected = [AngularDispersion.from_counts(a).compare_value(AngularDispersion.from_counts(b)) for a,b in cases]
        self.assertEqual(actual, expected)
        self.assertEqual(len(cases), 676)

    def test_rational_thresholds(self):
        counts = [[1,2,3], [5,5], [0,1,0]]
        cases = [[c, n, d] for c in counts for n in range(10) for d in range(1,10)]
        actual = js('input.map(([c,n,d])=>NollmAngularExact.compareRatio(c,n,d))', cases)
        self.assertEqual(actual, [AngularDispersion.from_counts(c).compare_ratio(n,d) for c,n,d in cases])

    def test_phase_bins_full_modulus_and_non_dyadic_boundaries(self):
        cases = [[str(t), '65536', 64] for t in range(65536)]
        cases += [[str(t), str(m), b] for m in (1,3,7,17,100) for b in (2,3,7,64,256) for t in range(m)]
        cases += [[str(t), str(2**120+7), 256] for t in (0, 1, 2**119, 2**120+6)]
        actual = js('input.map(([t,m,b])=>NollmAngularExact.phaseBin(t,m,b))', cases)
        self.assertEqual(actual, [int(t)*b//int(m) for t,m,b in cases])
        self.assertEqual(len(cases), 66180)

    def test_reject_approximate_and_malformed_inputs(self):
        actual = js('''(()=>{
          const bad=[true,false,null,undefined,NaN,Infinity,-1,-0,0.5,9007199254740992,"","00","1.0","1e2","+1","-1"," 1",{},[]];
          return bad.map(x=>{try{NollmAngularExact.fromCounts([1,x]);return false;}catch(e){return true;}});
        })()''')
        self.assertTrue(all(actual))
        self.assertEqual(len(actual),19)

    def test_zero_population_sparse_bins_and_invalid_scale(self):
        actual = js('''(()=>{
          const f=[()=>NollmAngularExact.fromCounts([]),()=>NollmAngularExact.fromCounts([1]),
            ()=>NollmAngularExact.fromCounts([0,0]),()=>NollmAngularExact.fromCounts([1,,2]),
            ...[0,-1,true,"0","1.0",""] .map(x=>()=>NollmAngularExact.fromCounts([1,2],x)),
            ()=>NollmAngularExact.phaseBin(7,7,64),()=>NollmAngularExact.phaseBin(0,0,64),
            ()=>NollmAngularExact.phaseBin(0,7,257),()=>NollmAngularExact.phaseBin(0,7,1),
            ()=>NollmAngularExact.compareRatio([1,2],1,0)];
          return f.map(g=>{try{g();return false;}catch(e){return true;}});
        })()''')
        self.assertTrue(all(actual));self.assertEqual(len(actual),15)

    def test_keeps_source_order_and_does_not_alias_mutable_input(self):
        actual = js('''(()=>{
          const c=[1,2,3],a=NollmAngularExact.fromCounts(c);c[0]=9;
          const b=NollmAngularExact.fromCounts([3,2,1]);
          return {counts:a.counts,reverse:b.counts,equal:NollmAngularExact.compareCounts(a.counts,b.counts)};
        })()''')
        self.assertEqual(actual, {'counts':['1','2','3'],'reverse':['3','2','1'],'equal':0})

    def test_large_integer_distinction_and_no_float_math_dependency(self):
        actual = js('''(()=>{
          Math.sqrt=()=>{throw Error('float root forbidden in exact kernel');};
          const x=2n**80n,a=NollmAngularExact.fromCounts([x,1n],10n**80n),b=NollmAngularExact.fromCounts([x+1n,1n]);
          return {cmp:NollmAngularExact.compareCounts(a.counts,b.counts),
            alias:Number(a.numerator)/Number(a.denominator)===Number(b.numerator)/Number(b.denominator),
            roundtrip:JSON.parse(JSON.stringify(a)),a};
        })()''')
        self.assertEqual(actual['cmp'],-1);self.assertTrue(actual['alias'])
        self.assertEqual(actual['roundtrip'],actual['a'])

    def test_standalone_build_does_not_require_enterprise_initializer(self):
        from pathlib import Path
        import sys
        import tempfile
        toolkit = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            program = (
                "import sys,importlib.util;sys.path.insert(0,sys.argv[1]);"
                "assert importlib.util.find_spec('enterprise_math') is None;"
                "from nollm_visual_toolkit.multiplication_lab import build_lab;"
                "p=build_lab(sys.argv[2],count=16);"
                "assert 'NOLLM_ANGULAR_BIGINT_BRC_PORT_V1' in p.read_text()"
            )
            subprocess.run([sys.executable, '-I', '-c', program, str(toolkit),
                str(Path(temp)/'standalone.html')], check=True, capture_output=True,
                text=True, timeout=30)

    def test_generated_html_contains_real_exact_module(self):
        from nollm_visual_toolkit.multiplication_lab import build_lab
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as d:
            text=build_lab(Path(d)/'lab.html',count=16).read_text()
        self.assertNotIn('__ANGULAR_EXACT_SCRIPT__',text)
        self.assertIn(SCRIPT,text)
        self.assertIn("angular_cv_squared_exact:angularExact",text)
        self.assertIn("EXACT_MODULAR_PHASE_BINS",text)
        self.assertIn("APPROXIMATE_ATAN2_BINS",text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
