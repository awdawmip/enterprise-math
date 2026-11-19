"""All modular jet contents and lossless readouts of 4,096 frozen 24-step histories."""
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
import runpy

import numpy as np


SOURCE = 'experiments/x6_rotation_path_tensor_jet_two_cycle_20260906/check_two_cycle_tensor_jet.py'
DIGEST = 'dc9926ce1cd1aa4c2f89f1ef1b8d5acee05c76ab51b392faaf58d40cb413b169'
PANEL = {4: ('XXXZXZ','XXYZYZ','XXXYXY'), 2: ('XXXXXXXZ','XXXXXXYZ','XXXXXXXY')}


def cycles(source):
    result = []
    for w in source['WORDS']:
        steps = source['cycle_steps'](w)
        assert len(steps) == 12 and [sum(x) for x in zip(*steps)] == [0,0,0]
        result.append([(next(i for i,v in enumerate(s) if v), sum(s)) for s in steps])
    return result


def local_levels(words, depth):
    # Row w, column the base-three axis word. Update from the previous position.
    levels = [np.zeros((64,3**k),dtype=np.int32) for k in range(depth+1)]
    levels[0][:] = 1
    for row,word in enumerate(words):
        for pos,(axis,sgn) in enumerate(word):
            for k in range(min(depth,pos+1),0,-1):
                levels[k][row,axis::3] += sgn*levels[k-1][row]
    assert not levels[1].any()
    return levels


def layer(depth, rows, levels):
    a, b = rows//64, rows%64
    result = levels[depth][a]+levels[depth][b]
    for i in range(2,depth-1):
        term = levels[i][a,:,None]*levels[depth-i][b,None,:]
        result += term.reshape(len(rows),-1)
    return result


def raw_rank_code(word):
    code = 0
    for a in word:
        code = 3*code+'XYZ'.index(a)
    return code


def panel_check(diffs, modulus):
    # A column mask lists every unresolved pair that this actual component separates.
    masks = {int.from_bytes(np.packbits(v,bitorder='little').tobytes(),'little')
             for v in (diffs%modulus!=0).T}
    masks.discard(0)
    maximal = [v for v in masks if not any(v!=w and v&w==v for w in masks)]
    full = (1<<len(diffs))-1
    selected = [raw_rank_code(word) for word in PANEL[modulus]]
    assert np.any(diffs[:,selected]%modulus != 0,axis=1).all()
    assert all((v|w)!=full for v in maximal for w in maximal)
    return dict(unresolved_pairs=len(diffs), fixed_panel=PANEL[modulus], minimum_fixed=3,
                nonzero_masks=len(masks), maximal_masks=len(maximal),
                maximal_coverage=sorted(v.bit_count() for v in maximal))


def fiber_hist(left,right):
    # The tested pairs form disjoint cliques; a vertex has fiber size 1+degree.
    sizes = np.bincount(left,minlength=4096)+np.bincount(right,minlength=4096)+1
    n = Counter(map(int,sizes))
    assert all(count%size==0 for size,count in n.items())
    return dict(sorted((size,count//size) for size,count in n.items()))


def census(levels):
    left,right=np.triu_indices(4096,1)
    left,right=left.astype(np.int32),right.astype(np.int32)
    content=np.zeros(len(left),dtype=np.int32)
    rows,panels={},{}
    total=comb(4096,2)
    for k in range(2,9):
        active=np.unique(np.r_[left,right])
        key=np.zeros(4096,dtype=np.int32)
        key[active]=np.arange(len(active))
        data=layer(k,active,levels)
        if k in (6,8):
            modulus=4 if k==6 else 2
            collision=content%modulus==0
            panels[modulus]=panel_check(data[key[left[collision]]]-data[key[right[collision]]],modulus)
        batch=max(32,200000//3**k)
        for i in range(0,len(left),batch):
            b=slice(i,i+batch)
            diff=data[key[left[b]]]-data[key[right[b]]]
            content[b]=np.gcd(content[b],np.gcd.reduce(diff,axis=1))
        multiplicities=Counter(map(int,content))
        multiplicities[1]+=total-len(content)
        hist={}
        for m in (0,2,3,4,5):
            collision=(content==0 if m==0 else content%m==0)
            hist[m]=fiber_hist(left[collision],right[collision])
        rows[k]=dict(content=dict(sorted(multiplicities.items())),fibers=hist,
                     class_counts={m:sum(counts.values()) for m,counts in hist.items()})
        remaining=content!=1
        left,right,content=left[remaining],right[remaining],content[remaining]
    assert not len(content)
    assert [rows[d]['class_counts'][0] for d in (2,3,4,5)]==[125,729,3860,4096]
    return rows,panels


def coefficient(steps,target,modulus=None):
    counts=[1]+[0]*len(target)
    positions=[[i for i in reversed(range(len(target))) if 'XYZ'.index(target[i])==a]
               for a in range(3)]
    for axis,sign in steps:
        for i in positions[axis]:
            counts[i+1]+=sign*counts[i]
            if modulus:
                counts[i+1]%=modulus
    return counts[-1]


def witnesses(words):
    result={}
    for m,a,b,t in [(0,72,513,'XXXZX'),(4,9,576,'XXXZXZ'),(2,0,585,'XXXXXXXZ')]:
        paths=[words[x//64]+words[x%64] for x in (a,b)]
        stored=[]
        for path in paths:
            prefix=[np.zeros(3**k,dtype=np.int32) for k in range(len(t))]
            prefix[0][0]=1
            for axis,sign in path:
                for k in range(len(t)-1,0,-1):
                    prefix[k][axis::3]+=sign*prefix[k-1]
            stored.append(prefix)
        prefix_contents=[int(np.gcd.reduce(x-y)) for x,y in zip(*stored)]
        assert all(c==0 if m==0 else c%m==0 for c in prefix_contents)
        values=[coefficient(path,t) for path in paths]
        assert values[0]!=values[1] and (not m or (values[0]-values[1])%m)
        result[m]=dict(branch_words=[format(a,'012b'),format(b,'012b')],coordinate=t,values=values,prior_layer_contents=prefix_contents)
    for a in range(8):
        b=8*a+a
        history=words[b]*2
        assert [coefficient(history,word*4,2) for word in ('XY','YZ','ZX')]==list(map(int,format(a,'03b')))
    return result


def repetition(words):
    # Verify the exact leading coordinate with literal signed subsequences.
    verified=0
    for p,s,L in product((2,3,5,7),range(1,5),range(1,17)):
        q=p**s
        v=0
        x=L
        while x%p==0:
            v+=1
            x//=p
        k=p**max(v-s+1,0)
        delta=(coefficient(words[32]*L,'XY'*k,q)-coefficient(words[0]*L,'XY'*k,q))%q
        assert delta==(-1)**k*comb(L,k)%q and delta!=0
        assert all(comb(L,i)%q==0 for i in range(1,k))
        verified+=1
    return verified


def split_examples(words):
    result=[]
    for m,d,left_exponent,right_exponent in ((6,5,4,3),(10,6,4,5),(30,5,4,15),(60,5,8,15)):
        first=words[0]*left_exponent
        second=words[32]*right_exponent
        values=[]
        for history in (first+second,second+first):
            a=[np.zeros(3**k,dtype=np.int32) for k in range(d+1)]
            a[0][0]=1
            for axis,sign in history:
                for k in range(d,0,-1):
                    a[k][axis::3]=(a[k][axis::3]+sign*a[k-1])%m
            values.append(a)
        assert first[0]!=second[0]
        assert all(np.array_equal(a,b) for a,b in zip(*values))
        result.append([m,d,left_exponent,right_exponent])
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    repo=parser.parse_args().repo
    src=repo/SOURCE
    assert sha256(src.read_bytes()).hexdigest()==DIGEST
    words=cycles(runpy.run_path(str(src)))
    assert max(comb(24,d) for d in range(9))<2**31
    levels=local_levels(words,8)
    rows,panels=census(levels)
    one={}
    for m in (0,2,3,4,5):
        keys=[b'']*64
        class_counts=[]
        for data in levels[1:5]:
            keys=[key+(row%m if m else row).tobytes() for key,row in zip(keys,data)]
            class_counts.append(len(set(keys)))
        one[m]=class_counts
    assert one[2]==[1,8,8,64]
    result=dict(source=SOURCE,source_sha256=DIGEST,histories=4096,pairs=comb(4096,2),
                by_degree=rows,single_cycle_by_degree=one,fixed_repairs=panels,sharp_component_witnesses=witnesses(words),
                all_single_cycle_integer_top_axis_words=len({tuple(a for a,_ in w) for w in words}),
                repetition_prime_power_cases=repetition(words),split_prime_power_examples=split_examples(words))
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
