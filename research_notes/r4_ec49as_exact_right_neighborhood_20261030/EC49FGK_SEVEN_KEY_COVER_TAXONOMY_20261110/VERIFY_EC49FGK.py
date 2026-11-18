#!/usr/bin/env python3
"""EC49FGK: exact classification of complete raw-cache-key covers for the frozen 24-label BRC problem.
Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
DFA and positive key equations: frozen_model.py Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.
"""
from collections import defaultdict
from pathlib import Path
import json

OPS = 'acdefg'
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
     (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
     (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
REQ = {2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
       6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
LABELS = [(h,s) for h,ss in REQ.items() for s in ss]
ALL = (1 << len(LABELS)) - 1
IDX = {label:i for i,label in enumerate(LABELS)}

def candidate_labels(h,key):
    x,y,z = key
    a,b,f,g = z-1, x+y-h-1, h+1-y-2*z, h+1-x
    if min(a,b,f,g) < 0:
        return set(), 0
    labels=set();count=0
    for c in range(b+1):
        quotas=[a,c,b-c,z,f,g]
        def visit(depth,state):
            nonlocal count
            if depth==h:
                sig=SIG[state]
                if sig in REQ[h]:
                    labels.add((h,sig));count+=1
                return
            for i in range(len(OPS)):
                if quotas[i]>0 and T[state][i]!=8:
                    quotas[i]-=1
                    visit(depth+1,T[state][i])
                    quotas[i]+=1
        visit(0,0)
    return labels,count

def catalogue():
    out={};word_count=0
    for h in REQ:
        # These finite bounds follow from nonnegative a,b,f,g.
        for x in range(1,h+2):
            for y in range(h+2):
                for z in range(1,(h+1)//2+1):
                    labels,num=candidate_labels(h,(x,y,z))
                    if labels:
                        k=(x,y,z)
                        out[k]=out.get(k,0)|sum(1<<IDX[t] for t in labels)
                        word_count+=num
    return out,word_count

def cover_counts(keys,nmax=7):
    dp=[defaultdict(int) for _ in range(nmax+1)]
    dp[0][0]=1
    for m in keys.values():
        for k in range(nmax,0,-1):
            for used,n in list(dp[k-1].items()):
                dp[k][used|m]+=n
    return [d[ALL] for d in dp], [len(d) for d in dp]

def main():
    keys,word_count=catalogue()
    assert len(keys)==94 and word_count==178850
    counts,states=cover_counts(keys)
    assert counts==[0,0,0,0,0,16,2004,108434],counts
    without=dict(keys);without.pop((3,1,1))
    fewer,_=cover_counts(without)
    assert fewer[7]==1956
    assert [k for k,m in keys.items() if m & (1<<IDX[(2,16)])]==[(3,0,1)]
    assert [k for k,m in keys.items() if m & (1<<IDX[(2,32)])]==[(2,1,1)]
    out=Path(__file__).resolve().parent
    with (out/'EC49FGK_key_masks.txt').open('w',encoding='utf8') as f:
        for (x,y,z),mask in sorted(keys.items()):
            f.write(f'{x} {y} {z} {mask}\n')
    report={'schema':'EC49FGK_ORIGINAL_24_LABEL_KEY_COVER_V1',
      'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'frozen_model_blob':'7e97065ac9a0ff70435b92ee2f4bd718c9bf1859',
      'candidate_words':word_count,'legal_raw_keys':len(keys),
      'cover_count_exactly_k_keys':{str(i):v for i,v in enumerate(counts)},
      'dp_distinct_union_states':states,
      'forced_keys_all_finite_covers':[[3,0,1],[2,1,1]],
      'seven_key_covers_without_3_1_1':fewer[7],
      'seven_key_covers_with_3_1_1':counts[7]-fewer[7],
      'scope':'Complete raw-key support combinations; no native-prefix cost optimization.'}
    with (out/'EXACT_REPORT_EC49FGK.json').open('w',encoding='utf8') as f:
        json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
    print('PASS exact_cover_count k=5,6,7:',counts[5:8])
    print('PASS seven_without_3_1_1:',fewer[7])
    print('PASS catalogue:',len(keys),'keys,',word_count,'matching words')

if __name__=='__main__':main()
