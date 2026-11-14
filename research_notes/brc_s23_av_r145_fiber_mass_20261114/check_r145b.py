"""Exact exhaustive certificate for the conjectural nonextremal-width minimum.

All order-m Farey slope cells are traversed. At each cell the m+1 distinct
intercept words are generated as rational midpoint samples. This is a complete
word enumeration because mechanical-word combinatorics is constant on each cell.
"""
from fractions import Fraction as F
from math import gcd
import json


def language(m):
    farey = sorted({F(a, b) for b in range(1, m+1) for a in range(b+1) if gcd(a, b) == 1})
    result = set()
    for a, b in zip(farey, farey[1:]):
        theta = (a+b)/2
        breaks = sorted({(-j*theta) % 1 for j in range(m+1)}) + [F(1)]
        for x, y in zip(breaks, breaks[1:]):
            if x == y:
                continue
            rho = (x+y)/2
            word = tuple(int((j+1)*theta+rho)-int(j*theta+rho) for j in range(m))
            result.add(word)
    return result


def projection_width(word, L):
    m=len(word)
    s=[0]
    for b in word:
        s.append(s[-1]+b)
    alpha,beta=F(0),F(1)
    for h in range(1,m+1):
        for i in range(m-h+1):
            d=s[i+h]-s[i]
            alpha=max(alpha,F(d-1,h));beta=min(beta,F(d+1,h))
    assert alpha<beta
    ua=min(F(s[j]+1)-j*alpha for j in range(m+1))
    lb=max(F(s[j])-j*beta for j in range(m+1))
    return L*(beta-alpha)+ua-lb


def main():
    rows=[]
    for m in range(5,31):
        words=language(m)
        expected_count=1+sum((m+1-q)*sum(gcd(a,q)==1 for a in range(1,q+1)) for q in range(1,m+1))
        assert len(words)==expected_count,(m,len(words),expected_count)
        E=(m-2)*((m-1)//2)+1
        L=E-1
        shifted=(1,)+(0,)*(m-3)+(1,0)
        complement=tuple(1-v for v in shifted)
        extreme=(1,)+(0,)*(m-2)+(1,)
        complement_ext=tuple(1-v for v in extreme)
        assert len(shifted)==m
        expected=F(m-1,m-3) if m%2 else F(1)+F(m,(m-1)*(m-3))
        if m>=6:
            assert projection_width(shifted,L)==expected
            assert projection_width(complement,L)==expected
        else:
            expected=F(4,3)
        remaining=[]
        for w in words:
            if w not in (extreme,complement_ext):
                remaining.append((projection_width(w,L),w))
        min_width=min(v for v,w in remaining)
        minimizers=[''.join(map(str,w)) for v,w in remaining if v==min_width]
        assert min_width==expected,(m,min_width,expected)
        assert len(minimizers)==(4 if m==7 else 2),(m,minimizers)
        assert all(v>1 for v,w in remaining)
        rows.append({'m':m,'language_size':len(words),'nonextremal_words':len(remaining), 'min_width':str(min_width),'formula':str(expected),'minimizers':sorted(minimizers)})
    result={'marker':'R145B_SHIFTED_EXTREMAL_FINITE_PASS','coverage':'all m=5..30, all Sturmian words from Farey cells','rows':rows}
    with open('verification_r145b.json','w') as f:json.dump(result,f,indent=2,ensure_ascii=False)
    print(result['marker'],len(rows),'lengths',sum(x['nonextremal_words'] for x in rows),'nonextremal comparisons',flush=True)

if __name__=='__main__':main()
