# OAI7 r354 — Determinantal kernel lowers exact-minimax uniform-margin entropy

2026-11-19. Exact finite author-side mathematical theorem and reproducible integer certificate. Builds on r347–r353; it is shared Driver research context, not independent Native Result review.

## Statement and scope

Let G=F_29, C a random 5-set and K a deterministic 4-set. The failure event is b_K(C)=1{|K-C|≤16}, and the unrestricted minimax value is

\[
q^*=\frac{2024467747}{3324255613}.
\]

Impose the additional requirement that an ordered realization H=(H_1,...,H_5) of C has **each individual coordinate exactly uniform on F_29**. r352 established that all exact-minimax laws have the same 350 complete-loss-profile atom masses, with minimum unordered-set entropy

\[
H_* =7.869745624309653\ldots\text{ bits}.
\]

The r353 translation-equivariant realization achieves the exact minimax loss with uniform position marginals at entropy \(H_*+\log_2 29=12.727726619437224\ldots\) bits.

**New theorem.** There exists another exact-minimax ordered realization with each of the five position marginals exactly uniform, no extra sorting seed, and joint entropy

\[
\boxed{H(H)=12.7267140345976\ldots\text{ bits}.}
\]

The improvement over r353 is exactly

\[
\boxed{\Delta=\frac{q}{29}\left[
 5\frac12\log_2\frac12+
10\frac34\log_2\frac34+
10\frac54\log_2\frac54+
 5\frac32\log_2\frac32
\right]
=0.00101258483962437\ldots\text{ bits},}
\]
where \(q=\frac{139525152}{28\cdot474893659}=\frac{34881288}{3324255613}\).

This is a strict, constructive improvement in the **uniform ordered marginal** constrained problem. It does not require changing the mass of any r352 complete loss-profile fiber or any fixed-test failure probability.

For a rationally checkable strictly positive lower certificate, Pinsker's inequality gives

\[
\boxed{\Delta \ge
\frac{453456744}{2795698970533\ln2}
>0.00023400223\text{ bits}.}
\]

Thus, under the exact uniform-marginal condition, even the r353 independent-uniform-translation entropy is not optimal.

## Six precisely identified profile atoms

From r347's canonical affine-orbit enumeration (0-based index 7), choose its first six translation-class representatives, in deterministic ordered form:

\[
\begin{array}{c|l}
x&C_x\\\hline
0&(0,1,2,5,6)\\
1&(0,1,4,5,6)\\
2&(0,1,6,7,12)\\
3&(0,2,4,10,12)\\
4&(0,2,8,10,12)\\
5&(0,5,6,11,12).
\end{array}
\]

The r352 unique optimal loss-profile mass on each is \(q\), and orbit 7 has no twin identifications. The r353 construction chooses a profile with its forced mass and then adds an independently uniform translation T to its ordered base tuple. Replace only the six indicated conditional translation laws; leave the remaining 344 profile atoms unchanged.

## Signed minors in the cyclic group algebra

Work in \(R=\mathbb Z[z]/(z^{29}-1)\). For i=0,...,4 and x=0,...,5 form the 5-by-6 matrix

\[
M_{i,x}(z)=z^{c_{x,i}}.
\]

Define \(v_x(z)=(-1)^x\det M_{\widehat{x}}(z)\), where \(\widehat{x}\) deletes column x. The usual alternating-maximal-minors identity proves

\[
\sum_{x=0}^5 z^{c_{x,i}}v_x(z)=0\quad(i=0,\ldots,4)
\]

in R. Moreover, evaluating at z=1 turns every matrix entry into 1, so all 5-by-5 minors vanish and \(v_x(1)=0\). Write \(v_x(z)=\sum_{t=0}^{28}v_x(t)z^t\); the exact integers satisfy

\[
\sum_t v_x(t)=0,\qquad
\sum_x v_x(s-c_{x,i})=0
\quad\text{for each position i and residue s}.
\]

The complete six rows have 30 nonzero coefficients, maximum absolute coefficient \(M_0=2\). Two rows vanish, but four are nonzero (a nontrivial balancing kernel).

Change each of the six joint output probabilities from r353's uniform \(q/29\) to

\[
\boxed{p_x(t)=\frac q{29}\left(1+\frac{v_x(t)}4\right).}
\]

All probabilities are strictly positive because \(|v_x(t)|\le2\). The row-sum identity keeps each profile mass q, and the five column identities keep **each position exactly uniform**, including its full 29-symbol distribution. Since fixed-test losses depend only on the profile, every individual test failure probability is preserved. The map from \((x,t)\) to the ordered H is injective (six different translation classes, and translations within each class are distinct), so its entropy is the entropy of these joint probabilities.

The multiset of all 174 perturbation coefficients \(v_x(t)\) has counts

\[
\#\{v=0\}=144,\qquad
\#\{v=\pm1\}=10\text{ each},\qquad
\#\{v=\pm2\}=5\text{ each}.
\]

The entropy difference is therefore exactly the displayed \(\Delta\). The Pinsker lower bound follows by conditioning on x and summing \(q\,D(P_x\Vert U_{29})\ge q\|P_x-U_{29}\|_1^2/(2\ln2)\). The six L1 coefficient sums are (12,12,0,8,8,0); substituting these into the rational expression yields the stated positive bound.

## Complete exact Python 3 certificate

The following standard-library script regenerates the integer coefficient vectors from signed determinants, verifies their nonvanishing, verifies exact mass preservation and all 145 positional balance equations, checks membership of the six profile atoms in the correct r347 affine orbit, and computes the displayed entropy only after those integer checks.

~~~python
from itertools import permutations, combinations
from collections import Counter
from fractions import Fraction
from math import log, log2

p=29
shapes=[
    (0,1,2,5,6),
    (0,1,4,5,6),
    (0,1,6,7,12),
    (0,2,4,10,12),
    (0,2,8,10,12),
    (0,5,6,11,12)
]
def sign(pi):
    return (-1)**sum(pi[i]>pi[j] for i in range(5) for j in range(i+1,5))

V=[]
for x in range(6):
    remaining=[j for j in range(6) if j!=x]
    row=[0]*p
    for pi in permutations(range(5)):
        k=sum(shapes[remaining[pi[i]]][i] for i in range(5))%p
        row[k]+=(-1)**x * sign(pi)
    V.append(row)

assert [sum(abs(c) for c in row) for row in V]==[12,12,0,8,8,0]
assert Counter(e for row in V for e in row)=={0:144,1:10,-1:10,2:5,-2:5}
assert all(sum(row)==0 for row in V)
assert all(sum(V[x][(s-shapes[x][i])%p] for x in range(6))==0
           for i in range(5) for s in range(p))
M=max(abs(e) for row in V for e in row)
assert M==2

# Verify the fixed r347 orbit-7 enumeration without importing external data.
full=(1<<p)-1
def rot(m,t):
    t%=p
    return (((m<<t)|(m>>(p-t)))&full) if t else m
def norm(m): return min(rot(m,t) for t in range(p))
def mul(m,a):
    return sum(1<<((a*x)%p) for x in range(p) if m>>x&1)
representatives=sorted({norm(sum(1<<x for x in ss))
                        for ss in combinations(range(p),5)})
index={m:i for i,m in enumerate(representatives)}
seen=set(); orbits=[]
for m in representatives:
    if m in seen:continue
    ix=sorted({index[norm(mul(m,a))] for a in range(1,p)})
    orb=[representatives[i] for i in ix]
    seen.update(orb);orbits.append(orb)
assert len(orbits)==150 and len(orbits[7])==28
assert [sum(1<<x for x in ss) for ss in shapes]==orbits[7][:6]

q=Fraction(139525152,28*474893659)
assert q==Fraction(34881288,3324255613)
assert all(q*(1+Fraction(v,4))>0 for row in V for v in row)
L1=[sum(abs(t) for t in row) for row in V]
pinsker_coefficient=q*Fraction(sum(s*s for s in L1),2*(4*p)**2)
assert pinsker_coefficient==Fraction(453456744,2795698970533)
counts=Counter(e for row in V for e in row)
gain=float(q)/p*sum(counts[e]*(1+e/4)*log2(1+e/4)
                    for e in (-2,-1,1,2))
Hstar=7.869745624309653
Hnew=Hstar+log2(p)-gain
assert 0.0010125848<gain<0.0010125849
assert 12.7267140<Hnew<12.7267141
assert float(pinsker_coefficient)/log(2)>0.00023400223
print("r354 PASS: exact six-row kernel, all 5 uniform margins,"
      " profile masses unchanged, gain",gain,"H",Hnew)
~~~

**Observed:** the independent local Python 3 verifier completed with all assertions PASS. All 5×29 column identities, six row identities, coefficients, orbit selection, positivity, and Pinsker rational coefficient are integer/fraction exact. Entropy decimals are illustrative; the closed logarithmic formula is exact.

## Preserved scientific provenance and next question

The finite minimax certificate derives from r347 GitHub commit 12bd331ea2aef70cc844682db432a623b235e726; r350 from 2737a8ea300816066714ef0ff8d72b62c6df2e46; r351 from 6a9da64ae349c647744773f92c80753a6f9ffb23; r352 from c660dc487bbb5f96789a3b2876ed82c32245eecf; and r353 from 39b1a628bede82ecb87683e615321334432549b7. Original OAI7 researcher EM-EMF6D046-5A2844, Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19 remain credited. This is an author-side, shared-context exact finite coverage result. It does not claim Native independent review, Source/Activity acceptance, original X6 carrier/provenance transfer, Task completion or mother-objective closure. The next mathematical problem is the global minimum of joint entropy with all five ordered position marginals exactly uniform, potentially using nonperturbative coupled transport across many atoms.
