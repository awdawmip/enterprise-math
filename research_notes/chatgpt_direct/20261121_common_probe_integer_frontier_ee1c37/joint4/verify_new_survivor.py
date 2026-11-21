"""Direct exact native, coverage, star and modular checks of the new survivor."""
from pathlib import Path
from hashlib import sha256
import argparse
import importlib.util
import json
import sys


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--witness', type=Path, required=True)
    p.add_argument('--prior-cuts', type=Path, required=True)
    p.add_argument('--delivery', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    sys.path.insert(0, str(a.prior_cuts))
    from modular_fibers import scan
    from joint_axes import scan_joint
    spec = importlib.util.spec_from_file_location('native_original_verifier', a.delivery/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    data = a.witness.read_bytes(); doc = json.loads(data)
    bad, pair = native.observation_tables(); known = {}
    result = {'witness_sha256': sha256(data).hexdigest(), 'frame': doc['frame'],
              'native': native.verify_one(a.witness, bad, pair, known),
              'native_unique_classes': len(known), 'modular_checks': [],
              'arithmetic': 'integer and rational', 'review_status': 'NOT_REVIEWED'}
    for q in (2, 3, 4, 5):
        check = scan(doc, q, exact=True)
        assert check['violating_dp_minima'] == 0
        result['modular_checks'].append(check)
    result['two_coordinate_mod3'] = scan_joint(doc, 3, exact=True)
    assert result['two_coordinate_mod3']['violating_dp_minima'] == 0
    result['all_checks_passed'] = True
    a.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['modular_checks', 'two_coordinate_mod3']}))


if __name__ == '__main__':
    main()
