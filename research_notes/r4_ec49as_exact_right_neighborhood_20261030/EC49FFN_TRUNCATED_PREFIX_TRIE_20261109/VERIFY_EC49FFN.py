#!/usr/bin/env python3
"""Exact EC49FFM last-three-signed-X6-step truncation for one-key low four-colour DP.
Original BRC model pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Run from sibling research directories with Python 3 (no third-party packages).
"""
from collections import defaultdict
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FFJ_NATIVE_PREFIX_TRIE_20261109'))
from BRC_ORIGINAL_MODEL_EC49FFJ import candidates,native
from VERIFY_EC49FFJ_TRIE import admissible_keys,merge,INF
SIG=(1,2,4,8)

def solve(h,key):
    children=[{}];term=[0];count=0
    L=2*(sum(key)-1)
    for word,s in candidates(h,key):
        if s not in SIG:continue
        count+=1
        prefix=native(word)
        assert len(prefix)==L
        node=0
        for step in prefix[:L-3]:
            nxt=children[node].get(step)
            if nxt is None:
                nxt=len(children);children[node][step]=nxt
                children.append({});term.append(0)
            node=nxt
        bit=1<<SIG.index(s)
        if term[node] and term[node]!=bit:
            raise AssertionError(('colour collision',h,key,node))
        term[node]=bit
    assert count>0
    dp=[None]*len(children)
    for p in range(len(children)-1,-1,-1):
        vec=[INF]*16;vec[0]=0
        if term[p]:vec[term[p]]=0
        for ch in children[p].values():vec=merge(vec,dp[ch])
        dp[p]=vec
    assert dp[0][15]<INF
    return {'h':h,'key':list(key),'low_words':count,
            'truncated_nodes':len(children),'truncated_min':dp[0][15],
            'native_full_min':dp[0][15]+12}

def main():
    rows=[];per=[]
    for h in range(2,10):
        keys=list(admissible_keys(h))
        curr=[solve(h,key) for key in keys]
        mincost=min(x['native_full_min'] for x in curr)
        expected=28 if h==2 else 34 if h==3 else 4*h+16
        assert mincost==expected,(h,mincost,expected)
        per.append({'h':h,'key_count':len(keys),'low_words':sum(x['low_words'] for x in curr),
                    'truncated_nodes':sum(x['truncated_nodes'] for x in curr),
                    'min_cost':mincost})
        rows+=curr
        print('H',h,'keys',len(keys),'nodes',per[-1]['truncated_nodes'],'minimum',mincost,flush=True)
    assert len(rows)==200 and sum(r['low_words'] for r in rows)==781882
    d={'schema':'EC49FFN_TRUNCATED_NATIVE_SIGNED_TRIE_V1','status':'EXACT_INTEGER_PASS',
       'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
       'exact_identity':'C_opt(native full four-colour)=C_opt(truncated to L-3)+12',
       'key_count':len(rows),'low_words':sum(r['low_words'] for r in rows),
       'per_window':per,'rows':rows}
    dest=Path(__file__).with_name('EXACT_REPORT_EC49FFN.json')
    dest.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    print('SUMMARY',json.dumps({k:d[k] for k in ('key_count','low_words','status')}),flush=True)
if __name__=='__main__':main()
