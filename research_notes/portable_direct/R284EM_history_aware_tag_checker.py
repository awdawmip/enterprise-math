#!/usr/bin/env python3
"""R284EM frozen Port: exact temporal-observer confusability checker.
Run beside R284CO_spectral_witness_checker.py; Python standard library only.
"""
import json
from pathlib import Path
from collections import Counter
from R284CO_spectral_witness_checker import FROZEN_SHA, arcs, words, dist

N, EMAX = 1 << 16, 8656
G = (0, 65, 1, 64)
EDGES = tuple((a,b) for a in range(4) for b in range(a+1,4))
EXPECTED2 = {(0,1):60,(0,2):9394,(0,3):9526,(1,2):9289,(1,3):9421,(2,3):60}
EXPECTED4 = {(0,1):60,(0,2):9432,(0,3):9564,(1,2):9327,(1,3):9459,(2,3):60}
COUNTS2 = {(0,1):16384,(0,2):14,(0,3):14,(1,2):14,(1,3):14,(2,3):16384}
COUNTS4 = {(0,1):16384,(0,2):8,(0,3):8,(1,2):8,(1,3):8,(2,3):16384}

def tag(i):
    return ((i>>12)&1) | (((i>>14)&1)<<1)

def main():
    x, aa = words(), arcs()    # words checks the immutable frozen SHA256
    assert len(x)==N and len(aa)==64
    f = [max(dist(v,a) for a in aa) for v in x]
    order = sorted(range(N), key=lambda i:(f[i],i))
    mind=[{},{}]; witness=[{},{}]; counts=[Counter(),Counter()]
    same=[0,0]; tested=0
    for pos,i in enumerate(order):
        q=pos-1
        while q>=0 and f[i]-f[order[q]]<=2*EMAX:
            j=order[q];tested+=1
            a,b=sorted((tag(i),tag(j)));pair=(a,b)
            d2=max(abs(f[i]-f[j]),abs(f[i^65]-f[j^65]))
            d4=max(d2,abs(f[i^1]-f[j^1]),abs(f[i^64]-f[j^64]))
            for z,d in enumerate((d2,d4)):
                if d<=2*EMAX:
                    counts[z][pair]+=1
                    if a==b: same[z]+=1
                    elif d<mind[z].get(pair,10**30):
                        mind[z][pair]=d
                        witness[z][pair]=[min(i,j),max(i,j)]
            q-=1
    assert tested==308913
    assert same==[0,0]
    assert mind==[EXPECTED2,EXPECTED4]
    assert [dict(c) for c in counts]==[COUNTS2,COUNTS4]
    # Omitted pairs have first-coordinate gap > 17312; all minima above
    # are < 17312, hence no omitted pair can improve one or be confusable.
    def graph(e, mins):
        return {ab for ab in EDGES if mins[ab]<=2*e}
    for mins,threshold in ((mind[0],4697),(mind[1],4716)):
        for e in range(0,30):
            assert graph(e,mins)==set()
        for e in range(30,threshold):
            g=graph(e,mins)
            assert g and g.issubset({(0,1),(1,2),(2,3)})
        for e in range(threshold,EMAX+1):
            assert {(0,1),(0,2),(1,2)}.issubset(graph(e,mins))
    for k in range(6):
        def c(a,b):
            return (a,)*(k+1)+(b,)*(k+1)+(a^b,)*k
        cc=[c(a,b) for a,b in ((0,0),(1,0),(0,1),(1,1))]
        assert len(cc[0])==3*k+2
        assert all(sum(u!=v for u,v in zip(cc[a],cc[b]))>=2*k+1
                   for a,b in EDGES)
    out={
      'schema':'R284EM_HISTORY_AWARE_TAG_RESOURCE_CERTIFICATE_V1',
      'pinned_source_commit':'acba2d8667903434aaa2a10720f43637fcc2421b',
      'pinned_source_git_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
      'frozen_residue_sha256':FROZEN_SHA,
      'state_count':N,'arc_count':64,'port_offsets':list(G),
      'numeric_error_max':EMAX,'exhaustive_candidate_pairs':tested,
      'same_label_confusable_pairs_at_max_error':same,
      'two_port':{'min_cross_label_linf':{f'{a}-{b}':mind[0][(a,b)] for a,b in EDGES},
                  'confusable_pair_counts':{f'{a}-{b}':counts[0][(a,b)] for a,b in EDGES},
                  'witnesses':{f'{a}-{b}':witness[0][(a,b)] for a,b in EDGES},
                  'triangle_onset_integer_error':4697},
      'four_port':{'min_cross_label_linf':{f'{a}-{b}':mind[1][(a,b)] for a,b in EDGES},
                   'confusable_pair_counts':{f'{a}-{b}':counts[1][(a,b)] for a,b in EDGES},
                   'witnesses':{f'{a}-{b}':witness[1][(a,b)] for a,b in EDGES},
                   'triangle_onset_integer_error':4716},
      'optimal_storage':{
        'two_port':'n=0 if E<=29; n=2k+1 if 30<=E<=4696; n=3k+2 if 4697<=E<=8656',
        'four_port':'n=0 if E<=29; n=2k+1 if 30<=E<=4715; n=3k+2 if 4716<=E<=8656'},
      'arithmetic':'exact integers',
      'review':'NOT_REVIEWED'
    }
    Path(__file__).with_name('R284EM_history_aware_tag_certificate.json').write_text(
        json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','candidate_pairs':tested,
                      'two_port':out['two_port']['min_cross_label_linf'],
                      'four_port':out['four_port']['min_cross_label_linf']},sort_keys=True))

if __name__=='__main__':
    main()
