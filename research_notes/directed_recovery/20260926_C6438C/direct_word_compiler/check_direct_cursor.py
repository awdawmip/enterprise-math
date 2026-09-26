"""Bounded negative controls for the new direct-construction cursor only."""
from copy import deepcopy
import gzip
import hashlib
import json
from pathlib import Path
import construct_direct_word as direct
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent
saved = direct.read(ROOT/'DIRECT_WORD_PARTIAL.json.gz')
rows = []

def rejected(name, value):
    start = len(CALLS)
    try:
        direct.build(pair_budget=0, previous=value)
    except ValueError as exc:
        rows.append({'case': name, 'rejected': True, 'reason': str(exc),
                     'actual_core_calls': len(CALLS)-start})
    else:
        raise AssertionError(name+' was accepted')

bad = deepcopy(saved)
bad['request']['tolerance'] = '1/8'
rejected('target_budget_substitution', bad)
bad = deepcopy(saved)
bad['status'] = 'CERTIFIED'
rejected('false_completed_cursor', bad)
bad = deepcopy(saved)
bad['four_square_search']['records'][0]['observed_pair_sum'] = 1
rejected('changed_observed_pair_sum', bad)

result = {'status': 'AUTHOR_ACTUAL_BOUNDED_NEGATIVE_CONTROLS_NOT_ADMITTED',
          'checks': rows, 'source': direct.source_binding(),
          'actual_core_call_count': len(CALLS), 'native_core_calls': CALLS,
          'scope': 'new direct-constructor cursor rejection; no ideal reference or Shor execution'}
raw = direct.compiler.packed(result)
(ROOT/'DIRECT_CURSOR_NEGATIVE_CONTROLS.json.gz').write_bytes(gzip.compress(raw, mtime=0))
summary = {k:v for k,v in result.items() if k != 'native_core_calls'}
summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
(ROOT/'DIRECT_CURSOR_NEGATIVE_CONTROLS.summary.json').write_text(
    json.dumps(summary, indent=2)+'\n', encoding='utf-8')
print(json.dumps(summary))
