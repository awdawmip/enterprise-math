#!/usr/bin/env python3
"""Exact exhaustive corroboration of R162 all-length symbolic fiber theorem."""
from collections import defaultdict
from math import gcd
import json

def signature(n, m):
    p = [0]
    for j in range(m):
        p.append(p[-1] + ((n >> (m-1-j)) & 1))
    a,b,c,d = 0,1,1,1
    for i in range(m):
        for j in range(i+1,m+1):
            q, k = p[j]-p[i], j-i
            if (q-1)*b > a*k:
                a,b = q-1,k
            if (q+1)*d < c*k:
                c,d = q+1,k
    if a*d >= c*b:
        return None
    g=gcd(abs(a),b)
    a,b=a//g,b//g
    g=gcd(abs(c),d)
    c,d=c//g,d//g
    U=b+min(b*p[j]-a*j for j in range(m+1))
    V=max(d*p[j]-c*j for j in range(m+1))
    return (a,b,c,d,U,V)

def prefixes(n,m):
    p=[0]
    for j in range(m):
        p.append(p[-1]+((n>>(m-1-j))&1))
    return p

def main():
    summary=[]
    candidate_total=0
    admitted_total=0
    pair_total=0
    terminal_aliases=[]
    for m in range(1,19):
        classes=defaultdict(list)
        for n in range(1<<m):
            key=signature(n,m)
            if key is not None:
                classes[key].append(n)
        count_pair=0
        for key,words in classes.items():
            assert len(words)<=2, (m,key,words)
            if len(words)!=2:
                continue
            count_pair+=1
            a,b,c,d,U,V=key
            p,q=prefixes(words[0],m),prefixes(words[1],m)
            changed=[i for i in range(1,m+1) if p[i]!=q[i]]
            assert len(changed)==1 and abs(p[changed[0]]-q[changed[0]])==1
            D=b*c-a*d
            assert D>0 and (d*U-b*V)%D==0
            index=(d*U-b*V)//D
            assert index==changed[0], (m,key,changed,index)
            if index==m:
                terminal_aliases.append((m,words))
            else:
                w=prefixes(words[0],m)
                v=prefixes(words[1],m)
                assert w[index-1]==v[index-1]
                assert w[index+1]==v[index+1]
        admitted=sum(map(len,classes.values()))
        summary.append({"m":m,"admitted":admitted,
                        "signature_classes":len(classes),
                        "size2":count_pair,"size_ge3":0})
        candidate_total+=(1<<m)
        admitted_total+=admitted
        pair_total+=count_pair
    assert candidate_total==524286
    assert admitted_total==3694
    assert pair_total==304
    assert terminal_aliases==[(1,[0,1])],terminal_aliases
    return {
        "marker":"R162_EXACT_FIBER_TWO_TO_ONE_PASS",
        "algorithm":"integer cross-products and gcd; no floating point",
        "scope":"all binary words, lengths 1 through 18 inclusive",
        "candidate_total":candidate_total,
        "admitted_total":admitted_total,
        "two_word_fiber_total":pair_total,
        "terminal_aliases":[{"m":m,"words":ws} for m,ws in terminal_aliases],
        "by_length":summary
    }

if __name__=="__main__":
    print(json.dumps(main(),sort_keys=True,indent=2))
