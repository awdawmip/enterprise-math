"""Independent native-X6 94 versus 109 signed-prefix comparison."""
import json
from EC49FEG_CERTIFY import WITNESS, pref, key, end, sig, audit_witness
W94={'2':['de','ed','ce','ec'],'3':['feg','gef'],
'4':['fegg','gefg'],'5':['feggd','feggc','gefgd','gefgc'],
'6':['fegggf','gefggf'],'7':['fegggfg','gefggfg'],
'8':['fegggfgd','fegggfgc','gefggfgd','gefggfgc'],
'9':['fegggfggf','gefggfggf']}
def audit_general(W):
    nodes=set();keys=set()
    for hs,words in W.items():
        h=int(hs)
        assert all(any(sig(w)&m for w in words) for m in (18,20,33,40))
        for w in words:
            assert len(w)==h and end(w)==(2,0,0,0,0,0)
            nodes.update(pref(w));keys.add(key(w))
    return len(nodes),sorted(keys)
def frontier(W):
    nodes=set();out=[]
    for h in range(2,10):
        words=W[str(h)]
        pp=set().union(*(pref(w) for w in words))
        added=len(pp-nodes);nodes|=pp
        out.append({'h':h,'keys':sorted({key(w) for w in words}),
                    'quota':len(words),'added':added,'total':len(nodes)})
    return out
c94,k94=audit_general(W94)
c109,k109=audit_witness(WITNESS)
f94,f109=frontier(W94),frontier(WITNESS)
assert c94==94 and c109==109 and len(k94)==len(k109)==5
assert k94==[(3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1)]
assert [z['added'] for z in f94]==[28,14,4,16,6,4,16,6]
assert [z['added'] for z in f109]==[26,9,4,16,6,24,18,6]
assert [z['quota'] for z in f94]==[4,2,2,4,2,2,4,2]
assert [z['quota'] for z in f109]==[4,2,2,4,2,4,4,2]
assert {sig(w) for w in W94['7']}=={16,32}
assert {sig(w) for w in WITNESS['7']}=={1,2,4,8}
print(json.dumps({'source_94':'EC49FDN rank 2200, 22 words',
                  'source_109':'EC49FEG, 24 words',
                  '94_keys':k94,'109_keys':k109,
                  '94_prefix_count':c94,'109_prefix_count':c109,
                  '94_frontier':f94,'109_frontier':f109,
                  'early_94_minus_109':7,'late_94_minus_109':-22,
                  'global_94_minus_109':-15},indent=2))
