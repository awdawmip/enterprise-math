from __future__ import annotations

import hashlib
import json
import unittest

import mpmath

from nollm_visual_toolkit import certified_hex as c


M32 = 1 << 32


class CertifiedHexPhase32Tests(unittest.TestCase):
    def test_default_carrier_is_backward_compatible(self):
        for tick in (0, 1, 2, 123, 16384, 32768, 49152, 65535):
            self.assertEqual(c.phase_bounds(tick, 64), c.phase_bounds(tick, 64, 65536))
        source = c.PolarSource(3, 16384, 1, 2)
        self.assertEqual(source.as_record()['phase_modulus'], '65536')
        self.assertEqual(source.locate(), c.PolarSource(3, 16384, 1, 2, 65536).locate())

    def test_phase32_bounds_enclose_high_precision_oracle(self):
        mpmath.mp.dps = 140
        scale = mpmath.mpf(2) ** 96
        # Exact cardinals are tested separately: transcendental oracles may return
        # tiny nonzero residues for values that are exactly zero.
        for tick in (1, 2, 3, 123456789, M32 // 4 - 1, M32 // 4 + 1,
                     M32 // 2 + 1, 3 * M32 // 4 + 1, M32 - 2, M32 - 1):
            cosine, sine = c.phase_bounds(tick, 96, M32)
            angle = 2 * mpmath.pi * tick / M32
            x, y = mpmath.cos(angle), mpmath.sin(angle)
            self.assertLessEqual(mpmath.mpf(cosine.lo) / scale, x)
            self.assertGreaterEqual(mpmath.mpf(cosine.hi) / scale, x)
            self.assertLessEqual(mpmath.mpf(sine.lo) / scale, y)
            self.assertGreaterEqual(mpmath.mpf(sine.hi) / scale, y)

    def test_phase32_cardinals_keep_shared_radical_ties(self):
        expected = {
            0: ('CERTIFIED_INTERIOR', ['1', '0']),
            M32 // 4: ('CERTIFIED_TIE', ['-1', '1']),
            M32 // 2: ('CERTIFIED_INTERIOR', ['-1', '0']),
            3 * M32 // 4: ('CERTIFIED_TIE', ['0', '-1']),
        }
        for tick, (status, cell) in expected.items():
            record = c.PolarSource(3, tick, 1, 2, M32).locate()
            self.assertEqual(record['status'], status)
            self.assertEqual(record['cell'], cell)
            self.assertEqual(record['source']['phase_modulus'], str(M32))
            self.assertTrue(c.verify_cell_record(record))

    def test_phase32_population_and_exact_diagnostics(self):
        phi = [None] + [(n * 2654435761) % M32 for n in range(1, 1024)]
        population = c.certified_population(phi, 1, 1, phase_modulus=M32,
                                            initial_bits=64, max_bits=192)
        self.assertEqual(population['status'], 'CERTIFIED_ALL')
        self.assertEqual(population['phase_modulus'], str(M32))
        self.assertEqual(population['population'], '1024')
        self.assertEqual(population['unresolved_identities'], [])
        payload = json.dumps([None if v is None else str(v) for v in phi],
                             separators=(',', ':')).encode()
        self.assertEqual(population['phase_source_sha256'], hashlib.sha256(payload).hexdigest())
        result = c.exact_diagnostics(phi, 1, 1, bins=64, readout_scale=10**12,
                                     phase_modulus=M32)
        counts = [0] * 64
        for tick in phi[1:]:
            counts[tick * 64 // M32] += 1
        self.assertEqual(result['angular_counts'], counts)
        self.assertEqual(result['cell_membership_exact']['phase_modulus'], str(M32))

    def test_phase32_noncardinal_replay(self):
        record = c.PolarSource(65535, 0xDEADBEEF, 3, 2, M32).locate(
            initial_bits=64, max_bits=192)
        self.assertIsNotNone(record['cell'])
        self.assertTrue(c.verify_cell_record(record))
        tampered = json.loads(json.dumps(record))
        tampered['source']['phase_modulus'] = '65536'
        self.assertFalse(c.verify_cell_record(tampered))

    def test_invalid_phase_modulus_rejected_before_execution(self):
        for modulus in (0, 1, 3, 6, (1 << 32) + 1, 1 << 33, True, 4.0):
            with self.subTest(modulus=modulus):
                with self.assertRaises(ValueError):
                    c.phase_bounds(0, 64, modulus)
        with self.assertRaises(ValueError):
            c.PolarSource(1, 4, phase_modulus=4)
        with self.assertRaises(ValueError):
            c.certified_population([None, 0], 1, 1, phase_modulus=12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
