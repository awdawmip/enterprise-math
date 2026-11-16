#!/usr/bin/env python3
"""Scoped R063 Stage3 source-line 57 optimization guard injection, not original full benchmark."""
from __future__ import annotations
import ast
import json
import sys
from collections import Counter
FRAGMENT = '''def relation_weights(p,q):
  a,b=cnt(p);c,d=cnt(q);raw,shift,target=oriented_product(a,b,c,d);total=Counter()
  for R in residual_sets(p,q):total.update(linext_word_counts(R,shift))
  assert total and all(cnt(w)==target for w in total);return tuple(sorted(total.items()))
'''
NAMESPACE={'Counter':Counter,'cnt':lambda x:(0,0),'oriented_product':lambda a,b,c,d:((0,0),0,(0,0)),'residual_sets':lambda p,q:[],'linext_word_counts':lambda R,shift:Counter()}
if len([n for n in ast.walk(ast.parse(FRAGMENT)) if isinstance(n,ast.Assert)])!=1:raise RuntimeError('source assertion count changed')
exec(compile(FRAGMENT,'<frozen-stage3-lines54-57>','exec'),NAMESPACE)
try: outcome=NAMESPACE['relation_weights']('i','j')
except AssertionError: outcome='ASSERTION_ERROR'
if __debug__:
    if outcome!='ASSERTION_ERROR': raise RuntimeError('ordinary must reject invalid empty relation')
else:
    if outcome!=(): raise RuntimeError('optimized must expose empty result bypass')
print(json.dumps({'scope':'ORIGINAL_FUNCTION_FRAGMENT_ONLY_NOT_FULL_BENCHMARK','source_commit':'69b7a90328bdb72852d47b338dedd7b276740ac9','source_blob':'4fca0c160acaa2b5d257d9bc1aefe82e1e3f4636','optimize':sys.flags.optimize,'observation':'REJECTED' if outcome=='ASSERTION_ERROR' else 'SILENT_EMPTY_TUPLE'},sort_keys=True))
