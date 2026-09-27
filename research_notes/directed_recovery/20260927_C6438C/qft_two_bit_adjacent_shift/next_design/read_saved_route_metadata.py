"""Stdlib I/O only: classify saved lengths; never import scientific modules."""
from pathlib import Path
import gzip
import hashlib
import json
from collections import Counter

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / 'sep27-qft-two-bit-adjacent-shift'
RAW_PIN = 'a084a16fa26a9a2143729620ba3f2fdc1331579ae16087a5f3ddcce199a96d82'
GZIP_PIN = '385295e9a5581ce762761f24d0d5c25e32f9bc06d645f32fbaecbdffd75b8294'
SOURCE_PIN = 'bee8a702062dfb16a75139a63b6c52b9451a02834a5b3033f5d52fcaebff9c6e'
COST_PIN = 'f8b4e67fdaa4d300680a38b0a02d6babc76b1a686f65c75d01d1c8fa0f34bd2c'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    compressed = (OLD / 'ADJACENT_SHIFT_RESULTS.json.gz').read_bytes()
    assert digest(compressed) == GZIP_PIN
    raw = gzip.decompress(compressed)
    assert digest(raw) == RAW_PIN
    assert digest((OLD / 'adjacent_shift.py').read_bytes()) == SOURCE_PIN
    assert digest((OLD / 'ADJACENT_COST_READBACK.json').read_bytes()) == COST_PIN
    payload = json.loads(raw)
    assert payload['status'] == 'PASS'
    cases = []
    all_counts = Counter()
    old_requests = 0
    proposed_setups = 0
    proposed_bundles = 0
    for case in payload['cases']:
        counts = Counter()
        requests = case['certificate']['requests']
        old_requests += len(requests)
        assert case['all_residues_equal'] is True
        for request in requests:
            assert request['complete'] is True
            for progression in request['progressions']:
                n = progression['n']
                assert type(n) is int and n >= 0
                route = 'empty' if n == 0 else 'singleton' if n == 1 else 'multiple'
                counts[route] += 1
                all_counts[route] += 1
                assert progression['empty'] is (n == 0)
        balanced = case['inputs']['R'] == 1
        old_tables = 4 * (counts['singleton'] + counts['multiple'])
        new_tables = 0 if balanced else 4 * counts['multiple']
        proposed_setups += int(not balanced)
        proposed_bundles += int(not balanced and counts['multiple'] > 0)
        cases.append({'inputs': case['inputs'], 'saved_length_classes': dict(counts),
            'whole_query_balanced_route': balanced, 'old_top_level_table_calls': old_tables,
            'proposed_top_level_table_calls': new_tables})
    result = {'status': 'PASS_METADATA_ONLY', 'scientific_execution': False,
        'scientific_answers_recomputed': False, 'source_sha256': SOURCE_PIN,
        'raw_sha256': RAW_PIN, 'gzip_sha256': GZIP_PIN, 'cost_readback_sha256': COST_PIN,
        'reader_sha256': digest(Path(__file__).read_bytes()), 'cases': cases,
        'saved_length_classes': dict(all_counts), 'old_requests': old_requests,
        'old_top_level_table_calls': sum(c['old_top_level_table_calls'] for c in cases),
        'proposed_top_level_table_calls': sum(c['proposed_top_level_table_calls'] for c in cases),
        'observer_layout': 'one fresh observer per historical tuple, unchanged',
        'proposed_scale_setups': proposed_setups,
        'proposed_lazy_coefficient_bundles': proposed_bundles,
        'interpretation': 'counterfactual route counts from saved lengths; no digit or timing prediction'}
    output = ROOT / 'SAVED_ROUTE_METADATA.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status','old_requests','old_top_level_table_calls',
        'proposed_top_level_table_calls','proposed_scale_setups','proposed_lazy_coefficient_bundles')}))

if __name__ == '__main__':
    main()
