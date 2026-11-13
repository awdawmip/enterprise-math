#!/usr/bin/env python3
"""R749SMN. Exact validation of adaptive Walsh observation-tree rank.
No external dependencies: all probabilities are fractions; F2 masks are integers.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def rank(rows):
    a = [[F(v) for v in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0]); r = 0
    for j in range(n):
        k = next((i for i in range(r, m) if a[i][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        p = a[r][j]
        a[r] = [v / p for v in a[r]]
        for i in range(r+1, m):
            if a[i][j]:
                v = a[i][j]
                a[i] = [z-v*w for z,w in zip(a[i],a[r])]
        r += 1
        if r == m:
            break
    return r


def chi(mask, source):
    return -1 if (mask & source).bit_count() % 2 else 1


def nodes(depth):
    return [''.join(s) for k in range(depth) for s in product('01',repeat=k)]


def observer(depth, dim, masks, biases):
    result=[]
    for path_tuple in product('01',repeat=depth):
        row=[]
        for x in range(1<<dim):
            h=''; v=F(1)
            for bit in path_tuple:
                y=1 if bit=='1' else -1
                v*= (1+y*biases[h]*chi(masks[h],x))/2
                h+=bit
            row.append(v)
        result.append(row)
    assert all(sum(row[x] for row in result)==1 for x in range(1<<dim))
    return result


def contrasts(depth, dim, masks, biases):
    ns=nodes(depth)
    rows=[[F(1) for _ in range(1<<dim)]]
    for n in ns:
        row=[]
        for x in range(1<<dim):
            h=''; hit=F(1)
            for bit in n:
                y=1 if bit=='1' else -1
                hit*=(1+y*biases[h]*chi(masks[h],x))/2
                h+=bit
            row.append(hit*biases[n]*chi(masks[n],x))
        rows.append(row)
    return rows


def predicted_depth_two(a,b,c,alpha,beta,gamma):
    if a and alpha:
        return 2 + int(bool(beta) and b not in (0,a)) + int(bool(gamma) and c not in (0,a))
    # Root has source-independent output. An unreachable branch contributes nothing.
    left_reachable=bool(a) or alpha != 1
    right_reachable=bool(a) or alpha != -1
    informative=set()
    if left_reachable and beta and b: informative.add(b)
    if right_reachable and gamma and c: informative.add(c)
    return 1+len(informative)


def main():
    vals=(F(-1), F(0), F(1,2), F(1))
    depth2=0
    counts={}
    for a,b,c in product(range(8),repeat=3):
        for alpha,beta,gamma in product(vals,repeat=3):
            masks={'':a,'0':b,'1':c}
            bias={'':alpha,'0':beta,'1':gamma}
            got=rank(observer(2,3,masks,bias))
            contrast=rank(contrasts(2,3,masks,bias))
            expect=predicted_depth_two(a,b,c,alpha,beta,gamma)
            assert got==contrast==expect, (a,b,c,alpha,beta,gamma,got,contrast,expect)
            counts[str(got)]=counts.get(str(got),0)+1
            depth2+=1
    # Test arbitrary dependent masks with Walsh contrast matrix theorem at depth three.
    depth3=0
    for t in range(250):
        ns=nodes(3)
        masks={n:((t*17+i*13+i*i*7)//(i+1)) % 8 for i,n in enumerate(ns)}
        bias={n:vals[(t+3*i+i*i) % 4] for i,n in enumerate(ns)}
        got=rank(observer(3,3,masks,bias))
        other=rank(contrasts(3,3,masks,bias))
        assert got == other,(t,got,other)
        depth3+=1
    result={
        'schema':'ENTERPRISE_MATH_R749SMN_REPEAT_MASK_RANK_EXACT_V1',
        'status':'PASS',
        'scientific_input':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'predecessor':'R749SMM@d6d80b056e4bc4f579610c4dd8d0e0adf4d57427',
        'arithmetic':'Python fractions.Fraction, exact row elimination',
        'depth_two':'exhaustive all 8^3 mask triples in GF(2)^3 and 4^3 bias triples',
        'depth_two_profiles':depth2,
        'depth_two_rank_histogram':counts,
        'depth_three_dependent_mask_profiles':depth3,
        'scope':'Finite regression checks; general contrast-span proof independent of finite enumeration'
    }
    with Path(__file__).with_name('R749SMN_REPEATED_PORT_OBSERVER_RESULTS.json').open('w',encoding='utf-8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print('PASS',depth2,'depth-2 profiles +',depth3,'depth-3 profiles',counts)


if __name__=='__main__':main()
