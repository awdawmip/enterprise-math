"""Derive an explicit original-CF driver; no hybrid import or runtime patch."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
source=ROOT.parent/'integration'/'complete_factorization.py'
target=ROOT/'cf_universal_factorization.py'
text=source.read_text(encoding='utf-8')
pairs=[
 ('from general_streaming import GeneralStreamingProgram, ROOT',
  "sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'integration'))\nfrom general_streaming import GeneralStreamingProgram, ROOT"),
 ('def factor_integer(N, rng, phase_provider, *, failure_bits=16, max_attempts=None, base_provider=None):',
  'def factor_integer_cf_universal(N, rng, *, failure_bits=16, max_attempts=None, base_provider=None):'),
 ('    phase_provider(t) returns (bank, dim, error_certificate), whose\n    terminal_TV_bound is a uniform whole-instrument bound to ideal Shor.',
  '    The pinned complete K33 phase provider and original CF postprocessor\n    have an all-width positive support proof. Ideal TV remains a separate bound.'),
 ("    if not integer(N) or N < 2: raise ValueError('integer N >= 2 required')",
  "    phase_provider = certified_phase_provider\n    if not integer(N) or N < 2: raise ValueError('integer N >= 2 required')"),
 ('        gamma = F(1, 8 * n) - epsilon',
  "        B = 2*t + 128*sum(t-m+1 for m in range(3, min(t,32)+1))\n        support_exponent = 2*B + 1\n        spectral_gamma = F(1, 1 << support_exponent)\n        tv_gamma = F(1, 8*n) - epsilon\n        gamma = max(spectral_gamma, tv_gamma)"),
 ('        # Lack of a useful conservative bound does not prevent an actual run.\n        # Its stopping budget and missing guarantee are made explicit.',
  '        # The spectral support bound is positive for every finite width.\n        # An explicit budget override can still weaken the probability guarantee.'),
 ("            'per_attempt_success_lower_bound': str(max(F(0), gamma)),",
  "            'per_attempt_success_lower_bound': str(gamma),\n            'original_cf_support_certificate': {\n                'algorithm': 'Complete fixed K33 words and unchanged sparse CF-only postprocessor',\n                'proof': 'ROOT_CF_ALL_WIDTH_SUCCESS.md',\n                'postprocessing_extension': False,\n                'retained_modes': dim,\n                'per_round_full_ideal_operator_bound': '185/4294967296',\n                'terminal_dyadic_denominator_exponent_upper_bound': B,\n                'uniform_success_dyadic_denominator_exponent': support_exponent,\n                'cases': ['odd_part_1_first_active_bit', 'odd_part_3_nearest_CF_history', 'odd_part_above_3_cyclotomic_norm'],\n                'chosen_bound': 'IDEAL_TV' if tv_gamma >= spectral_gamma else 'SPECTRAL_DYADIC',\n                'no_all_scale_ideal_distribution_accuracy_claim': True},"),
]
for old,new in pairs:
    if text.count(old)!=1:raise AssertionError((old,text.count(old)))
    text=text.replace(old,new)
if text.count('BRC_RECURSIVE_FACTORIZATION_V1')!=2:raise AssertionError('schema count')
text=text.replace('BRC_RECURSIVE_FACTORIZATION_V1','BRC_CF_UNIVERSAL_FACTORIZATION_V1')
text='# Fixed K33 / original CF-only variant with an explicit all-width support bound.\n'+text
assert 'hybrid' not in text.lower()
assert 'attempt = factor_attempts(value, t, R, rng, factory, bases=bases)' in text
target.write_text(text,encoding='utf-8')
manifest={'source':'../integration/complete_factorization.py','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'result':target.name,'result_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'replacements':[{'old':a,'new':b} for a,b in pairs],
 'schema_replacement':'BRC_RECURSIVE_FACTORIZATION_V1 -> BRC_CF_UNIVERSAL_FACTORIZATION_V1',
 'factor_attempts_call_unchanged':True,'postprocessing_extension':False,'runtime_monkeypatch':False}
(ROOT/'CF_DRIVER_DERIVATION.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('explicit original-CF driver generated')
