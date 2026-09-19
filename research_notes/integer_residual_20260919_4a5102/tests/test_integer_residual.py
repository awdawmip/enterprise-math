"""Independent rational oracles use Fraction constructed ONLY from integer pairs."""
import ast
from dataclasses import replace
from decimal import Decimal
from fractions import Fraction
import hashlib
from math import isqrt
from pathlib import Path
import random
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
sys.path.insert(0, str(ROOT / 'tools'))
from enterprise_math.exact_arithmetic import DivisionExpr, RootExpr, brc_scaled_evaluate
from enterprise_math.integer_residual import (
    IntegerResidual, NativeProjection6, Origin, PhaseLabel,
    RationalInterval, RootResidual, SignedDivisionSource,
)
from audit_numeric_surface import scan_file

COUNTS = {}

def hit(name):
    COUNTS[name] = COUNTS.get(name, 0) + 1


def observed_value(state):
    return Fraction(state.quotient * state.denominator + state.remainder,
                    state.denominator * state.scale)


class IntegerResidualTests(unittest.TestCase):
    def test_01_original_sources_are_byte_identical(self):
        expected = {'core.py': 'cdb8ace10e4cc8bba13b70f4da306313efb24819',
                    'division.py': 'bf0b1a6b6aeccc94578d11509c5bcd12ff930cb5',
                    'exact_arithmetic.py': '35ea95b0916494b83a92386e3e313928362dd79e'}
        for name, sha in expected.items():
            b = (ROOT / 'src/enterprise_math' / name).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest(), sha)

    def test_02_exhaustive_signed_reconstruction(self):
        for n in range(-40, 41):
            for d in range(1, 18):
                for s in (1, 2, 3, 7, 10, 256, 10**9):
                    state = SignedDivisionSource.from_pair(n, d).readout(s)
                    self.assertEqual(observed_value(state), Fraction(n, d))
                    self.assertEqual(state.quotient, (n*s)//d)
                    self.assertEqual(state.remainder, (n*s)%d)
                    self.assertEqual(state.exact_at_scale, (n*s)%d == 0)
                    self.assertTrue(state.enclosure().contains(state.source))
                    hit('signed_reconstruction')

    def test_03_refinement_semigroup(self):
        for n in range(-25, 26):
            for d in range(1, 14):
                x = SignedDivisionSource.from_pair(n, d, label='refinement').readout(7)
                for a,b in ((1,1), (2,3), (3,5), (10,10), (17,19)):
                    self.assertEqual(x.refine(a).refine(b), x.refine(a*b))
                    self.assertEqual(x.refine(a*b), x.rescale(7*a*b))
                    hit('refinement_semigroup')

    def test_04_exact_arithmetic_oracle(self):
        values = [(n,d) for n in range(-6,7) for d in range(1,8)]
        for n,d in values:
            for m,e in values:
                x = SignedDivisionSource.from_pair(n,d,label='left').readout(7)
                y = SignedDivisionSource.from_pair(m,e,label='right').readout(13)
                self.assertEqual(observed_value(x.add(y)), Fraction(n,d)+Fraction(m,e))
                self.assertEqual(observed_value(x.multiply(y)), Fraction(n,d)*Fraction(m,e))
                self.assertEqual(x.source.compare_value(y.source), (n*e > m*d)-(n*e < m*d))
                self.assertEqual(x.add(y).source.origin.parents, (x.source.origin,y.source.origin))
                hit('arithmetic_pair')

    def test_05_random_large_integer_oracle(self):
        rng = random.Random(20260919)
        for _ in range(500):
            n = rng.getrandbits(512) * rng.choice((-1,1))
            m = rng.getrandbits(512) * rng.choice((-1,1))
            d, e = rng.getrandbits(384)+1, rng.getrandbits(384)+1
            x, y = SignedDivisionSource.from_pair(n,d).readout(10**20), SignedDivisionSource.from_pair(m,e).readout(17)
            self.assertEqual(observed_value(x.add(y)), Fraction(n,d)+Fraction(m,e))
            self.assertEqual(observed_value(x.multiply(y)), Fraction(n,d)*Fraction(m,e))
            self.assertEqual(x.refine(31), x.rescale(31*10**20))
            hit('large_integer_pair')

    def test_06_negative_floor_is_not_truncation(self):
        x = SignedDivisionSource.from_pair(-1,7).readout(10)
        self.assertEqual((x.quotient,x.remainder,x.denominator),(-2,4,7))
        self.assertEqual(observed_value(x),Fraction(-1,7))

    def test_07_structural_equality_is_not_value_equality(self):
        x,y = SignedDivisionSource.from_pair(2,4),SignedDivisionSource.from_pair(1,2)
        self.assertNotEqual(x,y)
        self.assertNotEqual(x.origin,y.origin)
        self.assertEqual(x.value_key(),y.value_key())
        self.assertEqual(x.compare_value(y),0)

    def test_08_input_provenance_is_not_dropped(self):
        x,y = SignedDivisionSource.from_pair(1,2,label='path-A'),SignedDivisionSource.from_pair(1,2,label='path-B')
        self.assertNotEqual(x,y)
        self.assertEqual(x.value_key(),y.value_key())
        self.assertNotEqual(x.add(y),y.add(x))
        self.assertEqual(x.add(y).value_key(),y.add(x).value_key())

    def test_09_zero_does_not_erase_input_carrier(self):
        x,y = SignedDivisionSource.from_pair(0,3),SignedDivisionSource.from_pair(0,7)
        self.assertNotEqual(x,y)
        self.assertEqual(x.value_key(),(0,1))
        self.assertEqual(y.value_key(),(0,1))
        self.assertEqual(x.readout().remainder,0)

    def test_10_reciprocal_and_negation(self):
        for n in range(-25,26):
            for d in range(1,14):
                x = SignedDivisionSource.from_pair(n,d)
                self.assertEqual(x.negate().value_key(),(-Fraction(n,d).numerator, Fraction(n,d).denominator))
                if n:
                    y = x.reciprocal().readout(11)
                    self.assertEqual(observed_value(y),1/Fraction(n,d))
                    self.assertEqual(x.multiply(x.reciprocal()).value_key(),(1,1))
                else:
                    with self.assertRaises(ZeroDivisionError): x.reciprocal()
                hit('reciprocal_negation')

    def test_11_approximate_inputs_are_rejected(self):
        for bad in (True,False,1.0,0.1,complex(1,0),Decimal('1'),Fraction(1,2),'1',None):
            with self.assertRaises((TypeError,ValueError)): SignedDivisionSource.from_pair(bad,1)
            with self.assertRaises((TypeError,ValueError)): SignedDivisionSource.from_pair(1,bad)
            with self.assertRaises((TypeError,ValueError)): SignedDivisionSource.from_pair(1,7).readout(bad)

    def test_12_invalid_scale_denominator_rejected(self):
        for d in (0,-1,-10):
            with self.assertRaises(ValueError): SignedDivisionSource.from_pair(1,d)
        x = SignedDivisionSource.from_pair(1,7).readout()
        for scale in (0,-1):
            with self.assertRaises(ValueError): x.refine(scale)
            with self.assertRaises(ValueError): x.rescale(scale)

    def test_13_forged_reconstruction_rejected(self):
        x = SignedDivisionSource.from_pair(1,7).readout(10)
        with self.assertRaises(ValueError): replace(x, quotient=2)
        with self.assertRaises(ValueError): replace(x, remainder=7)
        with self.assertRaises(ValueError): replace(x, scale=100)

    def test_14_root_exhaustive_polynomial_certificate(self):
        for n in range(151):
            for p in range(1,8):
                for s in (1,2,7,10,64):
                    state = RootResidual.evaluate(n,p,s)
                    k,r = state.readout.trace.root_index,state.polynomial_residual
                    self.assertEqual(n*s**p,k**p+r)
                    self.assertLessEqual(k**p,n*s**p)
                    self.assertLess(n*s**p,(k+1)**p)
                    self.assertEqual(state.refine(3).readout,RootResidual.evaluate(n,p,s*3).readout)
                    if p == 2: self.assertEqual(k,isqrt(n*s*s))
                    hit('root_polynomial_certificate')

    def test_15_root_residual_is_not_linear_tail(self):
        state = RootResidual.evaluate(2,scale=10)
        self.assertEqual((state.readout.trace.root_index,state.polynomial_residual),(14,4))
        self.assertEqual(state.enclosure(),RationalInterval(14,15,10))
        self.assertEqual(state.compare_to_rational(SignedDivisionSource.from_pair(14,10)),1)
        self.assertEqual(state.compare_to_rational(SignedDivisionSource.from_pair(15,10)),-1)
        self.assertEqual(state.compare_to_rational(SignedDivisionSource.from_pair(18,10)),-1)

    def test_16_perfect_roots_and_zero(self):
        for n,p,expected in ((0,2,0),(9,2,3),(27,3,3),(1,5,1),(7,1,7)):
            x = RootResidual.evaluate(n,p,10)
            self.assertEqual(x.polynomial_residual,0)
            self.assertEqual(x.enclosure(),RationalInterval(10*expected,10*expected,10))
            self.assertEqual(x.compare_to_rational(SignedDivisionSource.from_pair(expected)),0)
            self.assertEqual(x.compare_to_rational(SignedDivisionSource.from_pair(-1)),1)

    def test_17_forged_root_certificate_rejected(self):
        x = RootResidual.evaluate(2,scale=10)
        bad = replace(x.readout,trace=replace(x.readout.trace,remainder=5))
        with self.assertRaises(ValueError): RootResidual(bad)
        with self.assertRaises(TypeError): RootResidual(DivisionExpr(2,1))

    def test_18_interval_overlap_is_unknown(self):
        self.assertEqual(RationalInterval(1,2,3).relation(RationalInterval(1,2,3)),'UNKNOWN')
        self.assertEqual(RationalInterval(1,1,2).relation(RationalInterval(2,2,4)),'EQ')
        self.assertEqual(RationalInterval(1,2,3).relation(RationalInterval(2,3,3)),'UNKNOWN')
        self.assertEqual(RationalInterval(1,2,3).relation(RationalInterval(3,4,3)),'LT')
        self.assertEqual(RationalInterval(3,4,3).relation(RationalInterval(1,2,3)),'GT')

    def test_19_interval_arithmetic_contains_exact_values(self):
        for n in range(-10,11):
            for m in range(-10,11):
                for s in (1,3,16):
                    a,b = SignedDivisionSource.from_pair(n,7),SignedDivisionSource.from_pair(m,11)
                    x,y = a.readout(s).enclosure(),b.readout(s).enclosure()
                    self.assertTrue(x.add(y).contains(a.add(b)))
                    self.assertTrue(x.multiply(y).contains(a.multiply(b)))
                    hit('interval_arithmetic')

    def test_20_phase_equivalence_retains_winding(self):
        a,b = PhaseLabel(SignedDivisionSource.from_pair(1,4)),PhaseLabel(SignedDivisionSource.from_pair(5,4))
        self.assertTrue(a.same_phase(b))
        self.assertNotEqual(a,b)
        self.assertEqual((a.turns.readout().quotient,b.turns.readout().quotient),(0,1))
        self.assertTrue(a.add(a).same_phase(PhaseLabel(SignedDivisionSource.from_pair(1,2))))
        self.assertTrue(PhaseLabel(SignedDivisionSource.from_pair(-1,4)).same_phase(PhaseLabel(SignedDivisionSource.from_pair(3,4))))

    def test_21_native_depth_and_path_are_not_erased(self):
        a = NativeProjection6((2,0,0,0,0,0),4,10,'path-A')
        b = NativeProjection6((1,0,0,0,0,0),2,11,'path-B')
        self.assertNotEqual(a,b)
        self.assertEqual(tuple(x.source.value_key() for x in a.observe()),tuple(x.source.value_key() for x in b.observe()))
        self.assertNotEqual(a.observe(),b.observe())
        with self.assertRaises(ValueError): NativeProjection6((1,2,3),4,10,'path')
        with self.assertRaises(TypeError): NativeProjection6((1.0,0,0,0,0,0),4,10,'path')

    def test_22_large_integer_boundary_not_float(self):
        x = SignedDivisionSource.from_pair(2**60+1)
        y = SignedDivisionSource.from_pair(2**60)
        self.assertEqual(x.compare_value(y),1)
        self.assertEqual(float(2**60+1),float(2**60))  # historical failure witness only

    def test_23_binary_lift_cannot_recover_decimal_source(self):
        binary_ratio = Fraction(0.1)  # quarantine demonstration, never core input
        exact_decimal = Fraction(1,10)
        self.assertNotEqual(binary_ratio,exact_decimal)
        self.assertEqual(Fraction(*float(0.1).as_integer_ratio()),binary_ratio)
        with self.assertRaises(TypeError): SignedDivisionSource.from_pair(0.1)

    def test_24_json_readout_uses_integer_strings(self):
        import json
        x = SignedDivisionSource.from_pair(2**200+1,7).readout(10**80)
        rec = json.loads(json.dumps(x.transport_record()))
        for field in ('source_n','source_d','scale','quotient','remainder'):
            self.assertIsInstance(rec[field],str)
        self.assertEqual(int(rec['scale'])*int(rec['source_n']),int(rec['source_d'])*int(rec['quotient'])+int(rec['remainder']))
        self.assertEqual(rec['provenance_scope'],'SCALAR_READOUT_ONLY')

    def test_25_ast_bounded_math_surface_is_clean(self):
        # This regression covers only the frozen source slice, never the whole repo.
        paths = [ROOT/'src/enterprise_math'/name for name in
                 ('core.py', 'division.py', 'exact_arithmetic.py', 'integer_residual.py')]
        for path in paths:
            result = scan_file(path)
            self.assertEqual(result['findings'],[],(path,result))

    def test_26_ast_true_division_is_review_not_automatically_float(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/'example.py'
            path.write_text('from fractions import Fraction\nx = Fraction(1, 3) / Fraction(2, 5)\n')
            scan = scan_file(path)
            self.assertTrue(scan['exact_rational_import_present'])
            self.assertEqual([f['severity'] for f in scan['findings']],['REVIEW'])

    def test_27_ast_detects_float_math_aliases(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/'example.py'
            path.write_text('from math import sqrt as rt\nimport numpy as np\nx=1e-12\ny=rt(2)\nz=np.array([1],dtype="float64")\n')
            rules = {f['rule'] for f in scan_file(path)['findings']}
            self.assertEqual(rules,{'APPROXIMATE_NUMERIC_LITERAL','ANALYTIC_APPROXIMATION_CALL','APPROXIMATE_DTYPE'})

    def test_28_scale_change_roundtrip_has_no_information_loss(self):
        x = SignedDivisionSource.from_pair(-31,17,label='rescale').readout(13)
        self.assertEqual(x.rescale(3).rescale(13),x)
        self.assertEqual(x.rescale(2).rescale(10).rescale(13),x)

    def test_29_types_cannot_be_interchanged(self):
        root = RootResidual.evaluate(2)
        div = SignedDivisionSource.from_pair(1,7).readout()
        with self.assertRaises(TypeError): div.add(root)
        with self.assertRaises(TypeError): PhaseLabel(root)
        with self.assertRaises(TypeError): RationalInterval(0,1,1).contains(root)

    def test_30_reciprocal_seven_residue_cycle(self):
        state = SignedDivisionSource.from_pair(1,7,label='reciprocal-7').readout()
        digits, residues = [], [state.remainder]
        for _ in range(6):
            prior = state
            state = state.refine(10)
            digits.append(state.quotient - 10 * prior.quotient)
            residues.append(state.remainder)
            hit('reciprocal_cycle_step')
        self.assertEqual(digits,[1,4,2,8,5,7])
        self.assertEqual(residues,[1,3,2,6,4,5,1])
        self.assertNotEqual(state, SignedDivisionSource.from_pair(1,7,label='reciprocal-7').readout())
        self.assertEqual(observed_value(state),Fraction(1,7))

    def test_31_residual_refinement_matches_modular_powers(self):
        # Finite exact identity, not a fast period finder or a Shor simulation.
        for modulus in (7,15,21,35,77):
            for base in (2,3,5,10):
                state = SignedDivisionSource.from_pair(1,modulus).readout()
                for step in range(1,21):
                    state = state.refine(base)
                    self.assertEqual(state.remainder,pow(base,step,modulus))
                    self.assertEqual(modulus*state.quotient+state.remainder,base**step)
                    hit('modular_power_refinement')


if __name__ == '__main__':
    unittest.main()
