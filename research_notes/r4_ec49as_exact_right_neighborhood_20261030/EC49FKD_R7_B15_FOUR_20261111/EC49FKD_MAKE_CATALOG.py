#!/usr/bin/env python3
"""Regenerate original 178850-row signed BRC word catalogue for the exact trie."""
import os,sys
from pathlib import Path
R=Path(__file__).resolve().parent
D=Path(os.environ.get('EC49FKB_INPUT_DIR',R.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
sys.path.insert(0,str(D))
import EC49FGW_RADIUS5_SCREEN as g
assert g.PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
n=0
with (R/'FJR_CATALOG.tsv').open('w') as f:
 for lab,w in g.all_words():
  k=g.raw_key(w)
  f.write(f'{lab[0]}\t{lab[1]}\t{k[0]}\t{k[1]}\t{k[2]}\t{w}\n')
  n+=1
assert n==178850
print('EC49FKD_CATALOG_PASS',n)
