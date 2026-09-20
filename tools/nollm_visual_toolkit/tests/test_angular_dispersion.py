"""Exact-oracle and real-consumer tests for migration slice 01.

Fraction and floating operations below are independent TEST oracles, never
native implementation paths. Only the explicit legacy readout is approximate.
"""
from __future__ import annotations

import builtins
from dataclasses import FrozenInstanceError
from fractions import Fraction
from itertools import product
import json
import math
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from nollm_visual_toolkit.angular_dispersion import AngularDispersion
from nollm_visual_toolkit import multiplication_lab as lab


class AngularDispersionTests(unittest.TestCase):
    def test_uniform_and_concentrated_histograms(self):
        for bins in (2, 3, 64, 256):
            uniform = AngularDispersion((7,) * bins)
            self.assertEqual(uniform.numerator, 0)
            concentrated = AngularDispersion((17,) + (0,) * (bins - 1))
            self.assertEqual(concentrated.compare_ratio(bins - 1, 1), 0)

    def test_known_one_sixth_keeps_raw_source(self):
        exact = AngularDispersion((1, 2, 3))
        self.assertEqual((exact.numerator, exact.denominator), (6, 36))
        self.assertEqual(exact.compare_ratio(1, 6), 0)
        readout = exact.readout(10)
        self.assertEqual((readout.scaled_value, readout.residual_numerator), (1, 24))
        self.assertEqual(readout.residual_denominator, 360)

    def test_enumerated_histograms_against_independent_variance_oracle(self):
        cases = 0
        for bins in range(2, 6):
            for counts in product(range(4), repeat=bins):
                total = sum(counts)
                if not total:
                    continue
                exact = AngularDispersion(counts)
                mean = Fraction(total, bins)
                oracle = sum((Fraction(c) - mean) ** 2 for c in counts) / bins / mean**2
                self.assertEqual(Fraction(exact.numerator, exact.denominator), oracle)
                self.assertGreaterEqual(exact.numerator, 0)
                self.assertLessEqual(exact.numerator, (bins - 1) * exact.denominator)
                for scale in (1, 10, 257):
                    readout = exact.readout(scale)
                    trace = readout.trace
                    self.assertEqual(trace.reconstruct(), scale * exact.numerator)
                    self.assertEqual(trace.collapsed_numerator, trace.denominator * trace.quotient)
                    self.assertTrue(0 <= trace.remainder < exact.denominator)
                    rebuilt = Fraction(trace.quotient, scale) + Fraction(trace.remainder, scale * exact.denominator)
                    self.assertEqual(rebuilt, oracle)
                cases += 1
        self.assertEqual(cases, 1356)

    def test_all_comparison_pairs(self):
        observations = [AngularDispersion(c) for c in product(range(3), repeat=3) if sum(c)]
        pairs = 0
        for left in observations:
            for right in observations:
                a = Fraction(left.numerator, left.denominator)
                b = Fraction(right.numerator, right.denominator)
                self.assertEqual(left.compare_value(right), (a > b) - (a < b))
                pairs += 1
        self.assertEqual(pairs, 676)

    def test_same_value_preserves_distinct_sources(self):
        first = AngularDispersion((1, 2, 3))
        scaled = AngularDispersion((2, 4, 6))
        permuted = AngularDispersion((3, 2, 1))
        for other in (scaled, permuted):
            self.assertEqual(first.compare_value(other), 0)
            self.assertNotEqual(first, other)
        self.assertNotEqual(first.as_record(), scaled.as_record())

    def test_large_inputs_and_scale_are_exact(self):
        exact = AngularDispersion((10**220 + 7, 10**219 + 3, 0))
        scale = 10**160 + 1
        result = exact.readout(scale)
        self.assertEqual(result.trace.reconstruct(), exact.numerator * scale)
        self.assertEqual(result.source.denominator, exact.denominator)
        self.assertTrue(0 <= result.trace.remainder < exact.denominator)

    def test_float_alias_does_not_merge_values(self):
        n = 2**80
        left = AngularDispersion((n, 1))
        right = AngularDispersion((n + 1, 1))
        self.assertEqual(float(Fraction(left.numerator, left.denominator)), float(Fraction(right.numerator, right.denominator)))
        self.assertEqual(left.compare_value(right), -1)

    def test_zero_and_exact_grid_residual(self):
        for exact, scale in ((AngularDispersion((1, 1)), 10), (AngularDispersion((1, 2, 3)), 6)):
            result = exact.readout(scale)
            self.assertEqual(result.residual_numerator, 0)

    def test_snapshot_and_frozen_state(self):
        counts = [1, 2, 3]
        exact = AngularDispersion.from_counts(counts)
        counts[0] = 100
        self.assertEqual(exact.counts, (1, 2, 3))
        with self.assertRaises(FrozenInstanceError):
            exact.numerator = 0
        record = exact.as_record()
        record['counts'][0] = '100'
        self.assertEqual(exact.counts, (1, 2, 3))

    def test_invalid_histograms_rejected_without_coercion(self):
        for counts in ((), (0,), (0, 0), (-1, 2), (True, 1), (1.0, 2), ('1', 2), (None, 2), [1, 2], '12', None):
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                AngularDispersion(counts)
        for counts in ({1, 2}, iter([1, 2]), '12', None):
            with self.assertRaises(ValueError):
                AngularDispersion.from_counts(counts)

    def test_invalid_scale_and_threshold(self):
        exact = AngularDispersion((1, 2))
        for scale in (0, -1, True, 1.0, '10', None):
            with self.subTest(scale=scale), self.assertRaises(ValueError):
                exact.readout(scale)
        for n, d in ((-1, 1), (True, 1), (1.0, 1), (1, 0), (1, -1), (1, True), (1, 1.0)):
            with self.assertRaises(ValueError):
                exact.compare_ratio(n, d)
        with self.assertRaises(TypeError):
            exact.compare_value(Fraction(1, 2))

    def test_json_round_trip_preserves_large_integers_and_trace(self):
        exact = AngularDispersion((2**100 + 1, 7, 3))
        record = json.loads(json.dumps(exact.as_record(scale=10**40)))
        self.assertEqual(tuple(map(int, record['counts'])), exact.counts)
        self.assertEqual(int(record['numerator']), exact.numerator)
        trace = record['readout']['trace']
        self.assertEqual(trace['evaluation_kind'], 'BRC_DIVISION_EVALUATION')
        self.assertEqual(int(trace['numerator']), int(trace['denominator']) * int(trace['quotient']) + int(trace['remainder']))
        def visit(value):
            if isinstance(value, dict):
                for child in value.values(): visit(child)
            elif isinstance(value, list):
                for child in value: visit(child)
            else:
                self.assertTrue(value is None or isinstance(value, str), repr(value))
        visit(record)

    def test_no_readout_means_no_materialization(self):
        with patch.object(AngularDispersion, 'readout', side_effect=AssertionError('must not materialize')):
            record = AngularDispersion((1, 2)).as_record()
        self.assertIsNone(record['readout'])

    def test_real_diagnostics_consumes_new_exact_module(self):
        spf = lab.smallest_factors(256)
        phi = lab.phases(spf, lab.prime_phases(spf))
        result = lab.diagnostics(phi, bins=7, exact_scale=10**12)
        expected = AngularDispersion.from_counts(result['angular_counts'])
        self.assertEqual(result['angular_cv_squared_exact'], expected.as_record(scale=10**12))
        self.assertEqual(result['angular_cv_role'], 'LEGACY_FLOAT_DISPLAY_NOT_EXACT_EVIDENCE')
        self.assertIn('not a native/proven', result['quantizer'])
        self.assertEqual(result['population'], result['occupied_cells'] + result['excess_identities_if_collapsed'])
        oracle = float(Fraction(expected.numerator, expected.denominator))
        self.assertAlmostEqual(result['angular_cv']**2, oracle)

    def test_default_diagnostics_is_source_only_and_data_unchanged(self):
        spf = lab.smallest_factors(16)
        phi = lab.phases(spf, lab.prime_phases(spf))
        snapshot = list(phi)
        result = lab.diagnostics(phi)
        self.assertEqual(phi, snapshot)
        self.assertIsNone(result['angular_cv_squared_exact']['readout'])
        self.assertEqual(sum(result['angular_counts']), 15)

    def test_invalid_exact_scale_rejected_before_geometry(self):
        for scale in (0, -1, True, 1.0, '10'):
            with patch.object(lab, 'rounded_hex', side_effect=AssertionError('too late')):
                with self.assertRaises(ValueError):
                    lab.diagnostics([None, 0], exact_scale=scale)

    def test_standalone_symbolic_path_without_enterprise_math(self):
        # Load only the exact module: do not replace the production initializer.
        module_path = Path(sys.modules[AngularDispersion.__module__].__file__).resolve()
        code = '''import importlib.util, sys
p=sys.argv[1]
spec=importlib.util.spec_from_file_location("standalone_dispersion",p)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
x=m.AngularDispersion((1,2,3));assert x.compare_ratio(1,6)==0;assert x.as_record()["readout"] is None
try:x.readout(10)
except RuntimeError as e:assert "No approximate fallback" in str(e)
else:raise AssertionError("BRC must not be available in isolated process")
'''
        result = subprocess.run([sys.executable, '-I', '-S', '-c', code, str(module_path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_transitive_missing_dependency_is_not_hidden(self):
        original_import = builtins.__import__
        def missing(name, *args, **kwargs):
            if name == 'enterprise_math.exact_arithmetic':
                raise ModuleNotFoundError('missing transitive module', name='unrelated_dependency')
            return original_import(name, *args, **kwargs)
        with patch('builtins.__import__', side_effect=missing):
            with self.assertRaises(ModuleNotFoundError) as caught:
                AngularDispersion((1, 2)).readout(10)
        self.assertEqual(caught.exception.name, 'unrelated_dependency')


if __name__ == '__main__':
    unittest.main(verbosity=2)
