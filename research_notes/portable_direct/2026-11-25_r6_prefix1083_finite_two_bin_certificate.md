# PREFIX-1083 — Phase-free finite integer certificates for two-bin negative residual observation

2026-11-25. AUTHOR_CONDITIONAL_ALGEBRAIC_PROOF / FINITE_EXACT_COMPUTATION / NOT_REVIEWED.
Independent R6 continuation, own session metadata verified by recovery_status for MCP-f6d93209fc8e4c5bb2c3b44f69a47174, researcher EM-DIRECT-780BBE, Activity RA-0ABD84561C86E53067DB0322. Owner inventory r6-20261125-1749-owner-read was RUNNING at last observation before this note; no CLAIM or shared Task mutation. Own metadata does not grant Task authority.

Frozen P000 V5: f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Same Stage46 X6 chart O, incoming -e1, reversal -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full paired Cell, signed phase, port identity and ordered multiplicity are retained in the inherited CT observer.
Parents:
- e5f4fc3df56133a943b1fd5d1b9784771066b1ea:research_notes/portable_direct/2026-11-25_r6_prefix1082_exact_ct_integer_sign_triangle.md
- f4bc55889416ec8d3561a99c89002fafa4f7121a:research_notes/portable_direct/2026-11-25_r6_prefix1081_critical_two_bin_phase.md
- aab4dd2e200a0f2da10c32b8406164042da8f4c9:research_notes/portable_direct/2026-11-25_r6_prefix1080_negative_mass_lattice_prefactor.md

## 1. Exact finite mass certificate without continuous zero rounding

Use parent integer observer T(M,Q)=4*36^(8+M+Q)*D_M(Q), T(M,Q+1)=36*T(M,Q)-T(M+1,Q). Given m>=0, r>=1, M=m+r, D_m(k)>0, a finite window k..E whose last observed negative index is K<=E, write s=K-k>=1. Assume T(M,K-j)<0 for 0<=j<=s; only this finite terminal window is considered, and T(M,Q)>=0 for K<Q<=E. Then the negative masses grouped by terminal offset Q=K-j have the exact common-denominator representation
    w_j = binom(s-j+r-1,r-1)*(-T(M,K-j))*36^j,
    C = 36^(r+s)*T(m,k)>0,
    N_window = sum(w_j)/C.
The factor is the exact number of ordered r-tuples of nonnegative offsets summing to s-j. The equality follows directly from the inherited telescoping joint observer J_r=D_M(Q)/D_m(k). It neither replaces the native carrier nor asserts anything about Q>E. Given s=0 only one bin exists. If intermediate bins are not all negative, replace -T by max(0,-T); the following slope theorem instead requires positive consecutive bins.
The normalized finite negative mass has probabilities w_j/sum(w). Two-bin truncation and renormalization has exact total variation error
    e2 = sum_(j>=2) w_j / sum_(j>=0) w_j.
It is an exact rational certificate, independent of the continuous root phase. The closest two-bin probability approximation in total variation has precisely this distance (every omitted mass must be paid). This only compresses the grouped negative-mass observation, not the native state or general future operations.

For a positive integer numerator W=sum(w), the bit-length difference L=bit_length(C)-bit_length(W) approximates -log2(N_window) with absolute error <1. This uses integer size without evaluating a small floating point mass. The distance of the full normalized signed joint law from the probability simplex is 2*N_full; N_window alone gives a lower bound for that distance, not an upper bound. Its bits give an upper bound, to within the stated rounding, on the full-law separation exponent when the joint law has total mass one.

## 2. New finite derivative-free slope certificate

Define G_j=-D_M(K-j)/Beta(M+1,K-j+1)>0. The Beta kernel identity implies
    G_j = g_j/(4*36^(8+M+K)),
    g_j=(-T(M,K-j))*36^j*(M+K-j+1)*binom(M+K-j,M).
All g_j are positive integers. Let 0<L<=g_(j+1)-g_j<=U for every 0<=j<s and R=U/L. Let W(u)=binom(u+r-1,r-1)*Beta(M+1,k+u+1). The exact adjacent ratio for u>=1 is
    W(u-1)/W(u)= u/(u+r-1)*(M+k+u+1)/(k+u).
For k>0 define Q=s/(s+r-1)*(M+k+1)/k. Then W(u-1)/W(u)<=Q throughout 1<=u<=s, since the first factor increases in u and the second decreases. If Q<1, the omitted mass divided by the retained mass is at most
    H=max(Q/(1-Q), R*Q*(2-Q)/(1-Q)^2),
    e2 <= H/(1+H).
Proof: w_j is proportional to W(s-j)*g_j (constant independent of j). For j>=2, W(s-j)<=W(s-1)*Q^(j-1), g_j<=g_0+jU, and retained mass is at least W(s-1)*(g_0+L). Thus the ratio is bounded by [g_0 Q/(1-Q)+U Q(2-Q)/(1-Q)^2]/(g_0+L), using the positive geometric sums. This is at most H; conversion from omitted/retained to omitted/total yields the result. No lower bound on g_0 other than positivity is used. This is a finite, phase-independent counterpart to PREFIX-1081. It does not require differentiability, knowledge of p or d, or a real root. It requires certified slope bounds across the retained window, which may cost more than two direct evaluations; a cheap independent uniform slope certificate is still open. When Q>=1 this geometric estimate is not asserted; exact w_j remains valid.

## 3. Executed finite BRC paired CT calculation

Use PREFIX-1082 exact polynomial and six-axis joint multinomial contraction unchanged (66 terms, 8 symmetry classes, maximum degree 3), Nmax=620. Verified the first eight A_m exactly against parent. Retained integer magnitudes for m=0 and M=5,10,15,20,23. For each M choose K as the last negative index in its computed row (end E=620-M), initial m=0, r=M, and k=K-s for s=1,2,5,10,20. All 25 input denominators positive; all bins k..K negative; all K+1..E positive. 215 binned observations including repeated terminal indices. The 25 exact rational comparisons e2<=6*q/5 passed, with q=s/(s+r-1)*(M+K+1)/K. This is a finite tested inequality, not a uniform theorem. All g_j increments strictly positive in all 25 windows; Q<1 and the phase-independent bound above passed by exact Fraction arithmetic in all cases.

Table of e2 (rounded solely for presentation):
M | K | E | s=1 | s=2 | s=5 | s=10 | s=20
5 | 208 | 615 | 0 | .185226 | .576842 | .819832 | .944294
10 | 314 | 610 | 0 | .053314 | .273882 | .548349 | .795940
15 | 421 | 605 | 0 | .035028 | .199699 | .443159 | .708846
20 | 528 | 600 | 0 | .021364 | .136481 | .339472 | .607765
23 | 592 | 597 | 0 | .012592 | .089624 | .250138 | .505465

For s=1, final-bin shares respectively .517627,.785505,.810360,.853907,.899827; integer mass bit-length differences respectively 31,58,86,115,131. This illustrates very small observable negative mass at higher finite depths. At M=23,s=2, first two bins retain 98.74084%; at s=5, 91.03760%; at s=20 only 49.45350%. For M=5,s=20 the modal bin is j=5, not among the two retained bins; exact omitted share 94.42939%. Thus unconditional two-bin compression is false even on a finite parent-model observation; the critical scale and certificate matter. At M=23,s=2, slope ratio R=1.01547751, Q=.08672316; finite tests are consistent with the critical law, not a proof of asymptotic or global last-negative location. The largest observed e2/q was approximately 1.160917, at M=15,s=20. No classical trig/pi reference or native kernel re-enumeration executed.

## 4. Reproduction and exact evidence

Run the PREFIX-1082 reproduction code through the construction of A, changing Nmax=1200 to Nmax=620. Stop before its switches loop (the old full-triangle digest checks concern a different range). Then run this exact new suffix. It recreates the actual integer weights, finite coverage assertions, and rational certificates; SHA256 is over decimal-string JSON array of each weight vector. Decimal output is presentation, not proof.

```python
from fractions import Fraction
assert A[:8]==[3474227232,83430021744,2013683977632,50005705455360,1283772437946144,33996158582646432,924583802183434368,25711602118824644352]
Ms=[5,10,15,20,23]; rows={m:[] for m in [0]+Ms}; cur=A[:]
for k in range(Nmax+1):
    for m in rows:
        if m<len(cur): rows[m].append(cur[m])
    cur=[36*cur[i]-cur[i+1] for i in range(len(cur)-1)]
for M in Ms:
    row=rows[M]; K=max(i for i,t in enumerate(row) if t<0)
    assert K+1<len(row) and all(t>0 for t in row[K+1:])
    for s in [1,2,5,10,20]:
        k=K-s; r=M
        assert rows[0][k]>0 and all(row[i]<0 for i in range(k,K+1))
        w=[comb(s-j+r-1,r-1)*(-row[K-j])*36**j for j in range(s+1)]
        total=sum(w); err=Fraction(sum(w[2:]),total)
        phase=Fraction(w[0],total); odds=Fraction(w[1],w[0])
        q=Fraction(s*(M+k+s+1),(s+r-1)*(k+s))
        assert err>=0 and phase>0 and err*5<=q*6
        gg=[(-row[K-j])*36**j*(M+K-j+1)*comb(M+K-j,M) for j in range(s+1)]
        dif=[gg[j+1]-gg[j] for j in range(s)]
        assert min(dif)>0
        R=Fraction(max(dif),min(dif)); Q=Fraction(s*(M+k+1),(s+r-1)*k)
        if Q<1:
            bound=max(Q/(1-Q),R*Q*(2-Q)/(1-Q)**2)
            assert err<=bound/(1+bound)
        C=36**(r+s)*rows[0][k]
        digest=hashlib.sha256(json.dumps([str(x) for x in w],separators=(',',':')).encode()).hexdigest()
        print(M,K,s,len(row)-1,float(phase),float(err),float(err/q),
              float(odds),max(range(len(w)),key=w.__getitem__),
              C.bit_length()-total.bit_length(),float(R),float(Q),digest)
```

Selected exact vector SHA256:
M=5,s=20: 868260bec724eb70fe0a92d4b6f9b6a5d3b7f245eb1bbd92a4ee7e97c12363f6
M=10,s=2: e51a2ee88ad5a0df30754e34bad278af4209422ce17255ece8f2228bdbaae1cd
M=15,s=20: 3582674a69fe48054c9ba6e006ae5c0037c39697d44a7f5cc599b91d676f1cf8
M=20,s=1: 8c25bc53cd40b7ba5f44929a34b6fd6318a2bb7fae41ff22eac7f849b3fc22e5
M=23,s=2: 43cfcb3b3524d9dcf7158cb05d96a07fa5a8cd59f0fd482a3f239c31455a38a2
M=23,s=20: 050ee9ff6a406405ca21f2bdc490bf81f973f396c60db3ddfe15078d22018bab

## 5. Next
Find a uniform cheap certificate for the normalized slope range without scanning the entire omitted window, or derive a rigorous spectral p,d enclosure. The finite E above is not a proof of no later negative bins. The full signed law needs its remaining tail certified before claiming a full-law error bound. Preserve the existing mother objective B_fix,odd(32) and frozen inputs. No independent review, formal checker, or measured acceleration was claimed.
