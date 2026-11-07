"""R434 exact signed BRC left-edge fifth-order Toeplitz certificate.
No native X6 correspondence, independent Driver review, or project admission.
Python standard library only. The proof supplies the degree <=30 argument.
"""
from fractions import Fraction
from math import comb, gcd
from functools import reduce
from itertools import permutations
from pathlib import Path
import json

def coef(q,r,s):
    return sum(comb(2*s,q-2*j)*comb(r-s,j) for j in range(r-s+1)
               if 0 <= q-2*j <= 2*s)

def original_H(r,s):
    return (comb(r+s,2*s)*(coef(r,r,s)-coef(r-1,r,s))
            if 2 <= s <= r else 0)

def cat(k):
    return comb(2*k,k)//(k+1)

def catalan_H(r,s):
    if not 2 <= s <= r:
        return 0
    k=r//2
    if r%2:
        d=sum(comb(s-1,2*t)*4**t*cat(k-t)
              for t in range((s-1)//2+1))
    else:
        d=sum(comb(s-1,2*t+1)*2*4**t*cat(k-1-t)
              for t in range((s-2)//2+1))
    return comb(r+s,2*s)*d

def det5(A):
    total=0
    for p in permutations(range(5)):
        v=1
        inv=0
        for i in range(5):
            v*=A[i][p[i]]
            inv+=sum(p[i]>p[j] for j in range(i+1,5))
        total+=-v if inv%2 else v
    return total

def raw_minor(r):
    H={s:original_H(r,s) for s in range(2,8)}
    return det5([[H.get(3+i-j,0) for j in range(5)]for i in range(5)])

def seven_terms(H):
    a,b,c,d,e,f=(H.get(s,0) for s in range(2,8))
    return (a**4*f-2*a**3*b*e-2*a**3*c*d+
            3*a*a*b*b*d+3*a*a*b*c*c-4*a*b**3*c+b**5)

def P(k):
    return (1375232*k**9+6684416*k**8-23083312*k**7
            -342536356*k**6-1617117168*k**5-4362096657*k**4
            -7458198896*k**3-8057900273*k**2-5092612394*k
            -1432864592)

def Q(k):
    return (343808*k**8+2196736*k**7+3492724*k**6+
            8377372*k**5+11173205*k**4+14689622*k**3+
            10984269*k**2+6451956*k+124308)

def parity_formula(k,parity):
    if parity:
        return Fraction(-k**5*(k+1)**5*(k+2)*(2*k+1)**5*
                        (2*k+3)**5*P(k),662010148800000)
    return Fraction(-k**5*(k-1)*(k+1)**5*(2*k-1)**5*
                    (2*k+1)**5*(2*k+3)*Q(k),10343908575000)

def shift_coefficients(coeff,shift):
    return [sum(v*comb(t,j)*shift**(t-j)
                for t,v in enumerate(coeff) if t>=j)
            for j in range(len(coeff))]

odd_coeff=[-1432864592,-5092612394,-8057900273,-7458198896,
           -4362096657,-1617117168,-342536356,-23083312,
           6684416,1375232]
even_coeff=[124308,6451956,10984269,14689622,11173205,
            8377372,3492724,2196736,343808]
shift8=shift_coefficients(odd_coeff,8)
assert all(x>0 for x in shift8) and all(x>0 for x in even_coeff)
assert all(P(k)<0 for k in range(2,8)) and P(8)==83290020660000
assert all(sum(c*k**i for i,c in enumerate(even_coeff))==Q(k)
           for k in range(2,35))
assert all(sum(c*k**i for i,c in enumerate(odd_coeff))==P(k)
           for k in range(2,35))

# 31 exact points per parity prove each degree <=30 identity,
# PROVIDED the polynomiality argument in R434_PROOF is used.
points=0
cat_checks=0
for parity in (0,1):
    for k in range(4,35):
        r=2*k+parity
        H={s:original_H(r,s) for s in range(2,8)}
        for s in range(2,8):
            assert H[s]==catalan_H(r,s),(r,s)
            cat_checks+=1
        d=raw_minor(r)
        assert d==seven_terms(H),(r,'Leibniz')
        C=cat(k if parity else k-1)
        assert Fraction(d,C**5)==parity_formula(k,parity),(r,'factorization')
        points+=1

# Boundary values not covered by polynomiality in the declared k>=4 range.
small=[]
for r in range(4,17):
    k=r//2;parity=r%2
    H={s:original_H(r,s) for s in range(2,8)}
    for s in range(2,8):
        assert H[s]==catalan_H(r,s),(r,s)
        cat_checks+=1
    d=raw_minor(r)
    C=cat(k if parity else k-1)
    assert Fraction(d,C**5)==parity_formula(k,parity),r
    small.append({'r':r,'det_decimal':str(d),'sign':(d>0)-(d<0)})

# Actual signed row, not only Catalan shorthand; check positive gcd scaling.
r=17
A=[original_H(r,r-h) for h in range(r-1)]
g=reduce(gcd,A)
A0=[x//g for x in A]
d0=det5([[A0[r-3+j-i] if 0<=r-3+j-i<len(A0) else 0
          for j in range(5)]for i in range(5)])
draw=raw_minor(r)
assert g==38
assert d0==-645900499675468409684083200000
assert draw==-51178034603069684920011159277977600000
assert d0*g**5==draw
assert Fraction(draw,cat(8)**5)==parity_formula(8,1)

evidence={
 'schema':'EM_R434_SIGNED_BRC_EDGE_PF5_EXACT_V1',
 'model':'original_signed_BRC_auxiliary_scalar',
 'theorem':'E_r<0 even r>=4 and odd r>=17; E_r>0 odd 5<=r<=15',
 'polynomial_degree_upper_bound':30,
 'exact_identity_points_per_parity':31,
 'exact_identity_total_points':points,
 'original_signed_vs_catalan_checks':cat_checks,
 'direct_determinant_checks':points+len(small),
 'positive_shift_coefficients_low_to_high':[str(x)for x in shift8],
 'P_small_sign_checks':[{'k':k,'P':str(P(k))}for k in range(2,9)],
 'Q_positive_coefficients_low_to_high':[str(x)for x in even_coeff],
 'r17':{'rows':[0,1,2,3,4],'cols':[14,15,16,17,18],
        'gcd':str(g),'normalized_det':str(d0),'raw_det':str(draw),
        'max_PF_order':'4, conditional on R433 author-side complete PF4'},
 'boundary_r4_through_r16':small,
 'exact_arithmetic':'Python arbitrary-precision int and Fraction; no float',
 'admission':'AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING',
 'native_X6_transfer':'NOT_ESTABLISHED',
}
Path(__file__).with_name('R434_EVIDENCE.json').write_text(
    json.dumps(evidence,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('R434_EXACT_PASS parity_polynomial_points',points,
      'catalan_checks',cat_checks,
      'direct_5x5',points+len(small),
      'r17_raw',draw,
      'odd_shift8_all_positive',all(x>0 for x in shift8))
