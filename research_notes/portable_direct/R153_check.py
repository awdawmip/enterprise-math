#!/usr/bin/env python3
"""Exact validation for R153: distinct-denominator injectivity and equal-denominator aliases.

All calculations use Python arbitrary-precision integers and Fraction; no floating point.
"""
from collections import defaultdict
from fractions import Fraction
from math import gcd, lcm
import json


def count(L, a,b,c,d,U,V):
    return -((-(c*L-V))//d) - ((a*L-U)//b) - 1


def increments(a,b,c,d,U,V):
    return tuple(count(L+1,a,b,c,d,U,V)-count(L,a,b,c,d,U,V)
                 for L in range(lcm(b,d)))


def word_cuts(word):
    m=len(word)
    p=[0]
    for bit in word:p.append(p[-1]+bit)
    alpha,beta=Fraction(0),Fraction(1)
    for i in range(m):
        for j in range(i+1,m+1):
            alpha=max(alpha,Fraction(p[j]-p[i]-1,j-i))
            beta=min(beta,Fraction(p[j]-p[i]+1,j-i))
    if alpha>=beta:return None
    a,b=alpha.numerator,alpha.denominator
    c,d=beta.numerator,beta.denominator
    U=min(b*(p[j]+1)-j*a for j in range(m+1))
    V=max(d*p[j]-j*c for j in range(m+1))
    return a,b,c,d,U,V


def endpoint_test(max_denom=12):
    all_pairs=unequal_pairs=equal_pairs=0
    states=unequal_states=0
    equal_alias_examples=[]
    for b in range(2,max_denom+1):
      for d in range(2,max_denom+1):
       for a in range(1,b):
        if gcd(a,b)!=1:continue
        for c in range(1,d):
         if gcd(c,d)!=1 or a*d>=b*c:continue
         all_pairs+=1
         if b!=d:unequal_pairs+=1
         else:equal_pairs+=1
         seen={}
         for U in range(b):
          for V in range(d):
           key=increments(a,b,c,d,U,V)
           if b!=d:
            assert key not in seen,(a,b,c,d,seen.get(key),(U,V))
            unequal_states+=1
           elif key in seen and len(equal_alias_examples)<5:
            equal_alias_examples.append({'endpoints':[a,b,c,d],
                                         'first':list(seen[key]),'second':[U,V],
                                         'D':list(key)})
           seen.setdefault(key,(U,V))
           states+=1
         if b!=d:assert len(seen)==b*d
    return dict(all_reduced_pairs=all_pairs,unequal_denominator_pairs=unequal_pairs,
                equal_denominator_pairs=equal_pairs,total_cut_states=states,
                unequal_cut_states=unequal_states,
                examples=equal_alias_examples)


def resonant_family_check(max_b=50):
    tests=0
    for b in range(3,max_b+1):
      a,c=1,b-1
      seen=defaultdict(list)
      for U in range(b):
       for V in range(b):
        s=increments(a,b,c,b,U,V)
        expected=tuple(1-int(L==(U-1)%b)-int(L==(-V-1)%b)
                       for L in range(b))
        assert s==expected,(b,U,V)
        seen[s].append((U,V))
        tests+=1
      assert len(seen)==b*(b+1)//2,(b,len(seen))
      assert sum(len(t) for t in seen.values())==b*b
    return dict(b_range=[3,max_b],tested_states=tests,
                waveform_count_formula='b(b+1)/2 for every b in this range')


def alternating_check(max_h=50):
    actual_checks=0
    for h in range(2,max_h+1):
        m=2*h;b=2*h-1;a=h-1;c=h
        w0=tuple(j%2 for j in range(m))
        w1=tuple(1-j%2 for j in range(m))
        z0=word_cuts(w0)
        z1=word_cuts(w1)
        assert z0==(a,b,c,b,h,0),(h,z0)
        assert z1==(a,b,c,b,b,h-1),(h,z1)
        assert increments(*z0)==increments(*z1)
        for L in range(1,2*b+2):
            C0=count(L,*z0);C1=count(L,*z1)
            assert C0==C1 and C0>=1,(h,L,C0,C1)
            # Closed form: ceil(hL/b)+ceil((hL-(h-1))/b)-L.
            target=-((-h*L)//b)-((-(h*L-h+1))//b)-L
            assert C0==target==(-((-L)//b)),(h,L,C0,target)
            actual_checks+=1
    return dict(h_range=[2,max_h],paired_words=max_h-1,checked_coefficients=actual_checks)


def full_word_finite_check(max_m=12):
    rows=[]
    for m in range(1,max_m+1):
      words={}
      for x in range(1<<m):
        w=tuple((x>>(m-1-j))&1 for j in range(m))
        z=word_cuts(w)
        if z is not None:words[w]=z
      eq=[w for w,z in words.items() if z[1]==z[3] and z[1]>1]
      expected={tuple(j%2 for j in range(m)),tuple(1-j%2 for j in range(m))} if m>=4 and m%2==0 else set()
      assert set(eq)==expected,(m,eq)
      rows.append(dict(m=m,actual_words=len(words),same_denominator_actual_words=len(eq)))
    return rows


def main():
    output={'result':'R153_DISTINCT_DENOMINATOR_INJECTIVITY_AND_RESONANT_ALIAS_PASS',
            'arithmetic':'exact Python integers and fractions.Fraction',
            'endpoint_test':endpoint_test(12),
            'resonant_family':resonant_family_check(50),
            'actual_alternating':alternating_check(50),
            'finite_word_sweep':full_word_finite_check(12),
            'independence':'author-side exhaustive and symbolic validation only; NOT_REVIEWED'}
    print(json.dumps(output,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
