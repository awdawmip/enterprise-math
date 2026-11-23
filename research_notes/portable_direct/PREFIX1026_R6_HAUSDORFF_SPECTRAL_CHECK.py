#!/usr/bin/env python3
"""Exact finite Hausdorff differences and signed spectral-distribution identity.

Frozen P000 V5, candidate Stage46 signed BRC, Link {0,e1} bidirectional block,
grade k=1, positive terminal-port contrast from the immutable PREFIX-1016 packet.

Requires Python >=3.10; stdlib only. No floating point. No native BRC run is asserted.
"""
from __future__ import annotations
from math import comb
from fractions import Fraction
import hashlib, json
from pathlib import Path

MAX_M_PLUS_K = 240


def six_label_collision(max_r):
    """Independent multinomial-splitting A_6(r), integer exact."""
    A = [1] * (max_r+1)  # A_1
    for d in range(2, 7):
        A = [sum(comb(n, k)**2 * A[n-k] for k in range(n+1))
             for n in range(max_r+1)]
    return A


def contrast(m, A):
    """Exact three A6-shifts from PREFIX-1016, n=m+4 and m>=1."""
    z = (Fraction(-72*(72*m*m+163*m+80),5*(m+1))*A[m+1]
         +Fraction(2*(144*m**3+1135*m*m+2367*m+1310),5*(m+1)*(m+2))*A[m+2]
         -Fraction(2*(m+8)*(2*m+5),5*(m+2))*A[m+3])
    assert z.denominator == 1
    return z.numerator


def spectral_distribution_monomial(m, A):
    """Action of exact signed spectral distribution on x**m; see the paper."""
    z = Fraction(
        -4*m*(A[m+3]-72*A[m+2]+1296*A[m+1])
        -2*(17*A[m+3]-703*A[m+2]+3276*A[m+1]), 5)
    z += Fraction(12,5) * (
        Fraction(66*A[m+1]-11*A[m+2],m+1)
        +Fraction(6*A[m+2]-A[m+3],m+2))
    assert z.denominator == 1
    return z.numerator


def main():
    limit = MAX_M_PLUS_K
    A = six_label_collision(limit+3)
    assert A[:8] == [1,6,66,996,18306,384156,8848236,218040696]
    values = [contrast(m,A) for m in range(1,limit+1)]
    assert values[:9] == [25620,386028,7124592,149251656,3398043852,
                          81969197100,2063490736128,53703289713528,
                          1436011181064216]

    # Independent signed-distribution moment identity for each m in the window.
    assert all(spectral_distribution_monomial(m,A)==values[m-1]
               for m in range(1,limit+1))

    # Prefix finite-difference triangle: E_(m,0)=Delta_m,
    # E_(m,k+1)=36*E_(m,k)-E_(m+1,k), where
    # E_(m,k)=36^(m+k)*(-1)^k nabla^k [Delta_m/36^m].
    # (nabla denotes unit forward difference and Delta_m is unnormalized.)
    row = values
    sha = hashlib.sha256()
    sample_coords = {(1,0),(1,1),(1,2),(1,10),(1,40),(1,100),(1,200),
                     (2,12),(5,20),(10,100),(40,40),(120,100),(240,0)}
    selected = {}
    positive_counts = {}
    smallest_numerator_per_order = []
    for k in range(limit):
        assert len(row)==limit-k
        assert all(x>0 for x in row), (k,[i+1 for i,x in enumerate(row) if x<=0][:5])
        positive_counts[str(k)]=len(row)
        smallest_numerator_per_order.append(str(min(row)))
        for i,e in enumerate(row):
            m=i+1
            sha.update(f'{m},{k},{e}\n'.encode('ascii'))
            if (m,k) in sample_coords:
                selected[f'{m},{k}']=str(e)
        row=[36*row[i]-row[i+1] for i in range(len(row)-1)]

    assert sum(positive_counts.values()) == limit*(limit+1)//2
    cert={
       'schema':'ENTERPRISE_MATH_R6_PREFIX1026_HAUSDORFF_SPECTRAL_EXACT_CERT_V1',
       'scientific_pin':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json',
       'model':'Stage46 signed BRC W=J12-6I; native X6; blocked Link {0,e1}; grade k=1; coherent Cell-port squares',
       'source':'PREFIX-1016 exact three-shift identity; PREFIX-1025 finite positive contrast Hankel observations',
       'arithmetic':'Python unbounded integer + Fraction only; independent multinomial convolution and signed-distribution moment identity',
       'm_plus_k_limit':limit,
       'm_range':'1..240',
       'k_range_for_each_m':'0..240-m',
       'strictly_positive_integer_witness_count':limit*(limit+1)//2,
       'E_definition':'E_(m,0)=Delta_(m+4), E_(m,k+1)=36E_(m,k)-E_(m+1,k); E_(m,k)=sum_i (-1)^i*binom(k,i)*36^(k-i)*Delta_(m+i+4)',
       'normalized_basis':'Delta_(m+4)/36^m; (-1)^k forward_difference^k equals E_(m,k)/36^(m+k)',
       'all_checked_strictly_positive':True,
       'all_witnesses_sha256':sha.hexdigest(),
       'witness_canonicalization':'ASCII lines m,k,E\\n ordered by ascending k and ascending m (1-based); the SHA covers every integer witness',
       'selected_E':selected,
       'first_nine_contrasts':{str(m+4):str(v) for m,v in enumerate(values[:9],start=1)},
       'spectral_signed_distribution_identity':'nu[f]=(-4 <mu,y^2(y-36)^2 f_prime> -2<mu,y(y-36)(17y-91) f> +12<mu,(6-y) integral_0^y (11+x)f(x) dx>)/5',
       'spectral_monomial_checks':'240/240 exact matches',
       'unresolved':'Whether E_(m,k)>0 for all m>=1,k>=0 and whether the signed spectral distribution is a positive measure; no full all-order moment representation is claimed',
       'review':'NOT_REVIEWED',
    }
    out=Path(__file__).with_name('PREFIX1026_R6_EXACT_CERTIFICATE.json')
    out.write_text(json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: 240 integer contrasts, 240 independent spectral moments, 28,920 positive Hausdorff witnesses')
    print('Witness digest:',sha.hexdigest())
    print('Output:',out.name)

if __name__=='__main__':
    main()
