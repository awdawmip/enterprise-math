#!/usr/bin/env python3
"""Reproduce EC49FFK H9 exact four-colour signed-X6 prefix results."""
import json,sys
from pathlib import Path
here=Path(__file__).resolve().parent
sys.path.insert(0,str(here.parent/'EC49FFJ_NATIVE_PREFIX_TRIE_20261109'))
from VERIFY_EC49FFJ_TRIE import solve,admissible_keys
from BRC_ORIGINAL_MODEL_EC49FFJ import native,observed
def run(report):
    rows=json.loads(Path(report).read_text())['rows_by_z']
    expected={(x,y,int(z)):v for z,triples in rows.items() for x,y,v in triples}
    keys=list(admissible_keys(9))
    assert len(expected)==len(keys)==70 and set(expected)==set(keys)
    words=nodes=0
    for k in keys:
        r=solve(9,k)
        assert r['prefix_optimum']==expected[k],(k,r['prefix_optimum'],expected[k])
        words+=r['word_count'];nodes+=r['trie_nodes']
    assert (words,nodes)==(625050,5320558)
    winners=sorted(k for k,v in expected.items() if v==52)
    assert winners==[(x,11-x,1) for x in range(4,10)]
    for h in range(4,20):
        for x in range(4,h+1):
            r=x-3;s=h+1-x
            ws=('f'*r+'e'+'g'*s+'c','f'*r+'e'+'g'*s+'d',
                'g'+'f'*r+'e'+'g'*(s-1)+'c','g'+'f'*r+'e'+'g'*(s-1)+'d')
            assert set(observed(w) for w in ws)=={1,2,4,8}
            pref={native(w)[:i] for w in ws for i in range(1,len(native(w))+1)}
            assert len(pref)==4*h+16
    print('EXACT_PASS H9: 70 keys; 625050 words; 5320558 trie nodes; min=52 at six keys; h4..19 witnesses')
if __name__=='__main__':
    run(sys.argv[1] if len(sys.argv)>1 else str(here/'EXACT_REPORT_EC49FFK.json'))
