"""Persist an explicit auditable variant of the certified recursive driver."""
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parent
source=ROOT.parent/'integration'/'complete_factorization.py'
target=ROOT/'universal_factorization.py'
text=source.read_text(encoding='utf-8')
pairs=[
 ('are split only by the actual sampled Shor driver or its native gcd precheck.',
  'use the actual sampled driver, explicit post-readout exponent enhancement, and native gcd precheck.'),
 ('    phase_provider(t) returns (bank, dim, error_certificate), whose\n    terminal_TV_bound is a uniform whole-instrument bound to ideal Shor.',
  '    The pinned K33 phase provider fixes the actual complete rational words.\n    The success bound combines spectral support with the optional sharper TV bound.'),
 ('from general_streaming import GeneralStreamingProgram, ROOT',
  "sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'integration'))\nfrom general_streaming import GeneralStreamingProgram, ROOT"),
 ('from general_driver import factor_attempts',
  'from general_driver import factor_attempts\nfrom hybrid_postprocess import hybrid_classical_postprocess'),
 ('def factor_integer(N, rng, phase_provider, *, failure_bits=16, max_attempts=None, base_provider=None):',
  'def factor_integer_universal(N, rng, *, failure_bits=16, max_attempts=None, base_provider=None):'),
 ("    if not integer(N) or N < 2: raise ValueError('integer N >= 2 required')",
  "    phase_provider = certified_phase_provider\n    if not integer(N) or N < 2: raise ValueError('integer N >= 2 required')"),
 ('        gamma = F(1, 8 * n) - epsilon',
  "        B = 2*t + 128*sum(t-m+1 for m in range(3, min(t,32)+1))\n        support_exponent = 2*B + 1\n        spectral_gamma = F(1, 1 << support_exponent)\n        tv_gamma = F(1, 8*n) - epsilon\n        gamma = max(spectral_gamma, tv_gamma)"),
 ('        # Lack of a useful conservative bound does not prevent an actual run.\n        # Its stopping budget and missing guarantee are made explicit.',
  '        # Spectral support is positive for every finite input width.\n        # A user budget override remains explicit and may weaken the bound.'),
 ('attempt = factor_attempts(value, t, R, rng, factory, bases=bases)',
  'attempt = factor_attempts(value, t, R, rng, factory, bases=bases, postprocess=hybrid_classical_postprocess)'),
 ("            'per_attempt_success_lower_bound': str(max(F(0), gamma)),",
  "            'per_attempt_success_lower_bound': str(gamma),\n            'universal_support_certificate': {\n                'algorithm': 'K33 complete retained words plus public AFTER-readout low-odd-part exponent verification',\n                'common_rational_space_dimension_upper_bound': 32,\n                'terminal_dyadic_denominator_exponent_upper_bound': B,\n                'uniform_success_dyadic_denominator_exponent': support_exponent,\n                'low_odd_part_max': 1023, 'all_completed_readouts_including_zero': True,\n                'chosen_bound': 'IDEAL_TV' if tv_gamma >= spectral_gamma else 'SPECTRAL_DYADIC',\n                'no_all_scale_ideal_distribution_accuracy_claim': True},"),
]
for old,new in pairs:
    if text.count(old)!=1: raise AssertionError((old,text.count(old)))
    text=text.replace(old,new)
if text.count('BRC_RECURSIVE_FACTORIZATION_V1')!=2: raise AssertionError('schema occurrences changed')
text=text.replace('BRC_RECURSIVE_FACTORIZATION_V1','BRC_UNIVERSAL_HYBRID_FACTORIZATION_V1')
text='# Explicit K33 + hybrid postprocessing variant; previous driver remains unchanged.\n'+text
target.write_text(text,encoding='utf-8')
manifest={'source':'../integration/complete_factorization.py','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'result':'universal_factorization.py','result_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'replacements':[{'old':old,'new':new} for old,new in pairs],
 'schema_replacement':'BRC_RECURSIVE_FACTORIZATION_V1 -> BRC_UNIVERSAL_HYBRID_FACTORIZATION_V1',
 'runtime_monkeypatch':False,'frozen_module_modified':False}
(ROOT/'UNIVERSAL_DRIVER_DERIVATION.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('explicit universal driver generated')
