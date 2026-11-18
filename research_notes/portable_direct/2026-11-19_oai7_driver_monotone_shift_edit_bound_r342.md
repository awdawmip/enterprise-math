# OAI7 r342 — Sharp one-sided edit Lipschitz inequality for threshold lists

Date: 2026-11-19. Status: new author-side exact finite-combinatorial lemma, sharpening the quantitative bound in r341 (and its r336 antecedent). This is neither an independent Native Result review nor a frozen Result, Task closure, Activity/Source admission, or native Heartbeat-X6/Link/Port transport. The original OAI7 researcher EM-EMF6D046-5A2844 and the contributors of r307 and r329–r341 retain their respective provenance. The present Driver context has seen and helped produce the earlier author-side results, and asserts no clean review independence.

## 1. Exact monotone edit inequality

Let G be a finite abelian group (written additively), K a u-element subset of G, A,B finite subsets of G, and h any integer. Define
```
N_A(x;K) = #{a in A : x+a in K},
V_A(K;h) = #{x in G : N_A(x;K) <= h}.
```
For all such A,B,K,h,
```
V_A(K;h) - u |B\A| <= V_B(K;h)
                        <= V_A(K;h) + u |A\B|.             (342.1)
```
In particular, if |A|=|B| and r=|A\B|=|B\A|, then
```
|V_B(K;h)-V_A(K;h)| <= u r.                                (342.2)
```
This improves the previously recorded symmetric 2ur bound to ur. Neither shift independence nor a prime modulus is needed. The coefficient u in (342.1)–(342.2) is optimal, even for h=0 and a single swap.

**Proof.** Adding one shift b to a set S only increases N_S(x;K), so V cannot increase. A previously bad start x (N_S(x;K)<=h) can become good (N_(S union {b})(x;K)>h) only if x+b lies in K. There are precisely u such starts, hence
```
V_S(K;h)-u <= V_(S union {b})(K;h) <= V_S(K;h).
```
Conversely deleting one shift can increase V by at most u and can never decrease V. For A,B, first add B\A to A, then delete A\B to obtain B: the addition decreases V by at most u|B\A| and the subsequent deletion never decreases it, giving the left inequality. In the reverse order, first delete A\B from A and then add B\A; the deletion raises V by at most u|A\B| and subsequent addition never raises it, giving the right inequality. If |A|=|B|, the two unilateral bounds combine into (342.2). QED.

The same proof works for nonempty translated test sets of equal size in any finite group with a right-translation action; no new Project axioms are introduced.

## 2. Quantitative correction and strengthening of r341

In the original prime-field setting, let
```
p prime, 1<=u,n<p, n+u-1<p,
W={0,1,...,n-1}, K={0,1,...,u-1},
B_0=p-(n+u-1), threshold T=p^(3/4), h>=0.
```
Since K-W consists of n+u-1 consecutive residues without wrap collisions, all x outside K-W have N_W(x;K)=0<=h; therefore V_W(K;h)>=B_0. For any n-set C, set r=|C\W|=|W\C|. Equation (342.1) yields the improved bound
```
V_C(K;h) >= B_0-u r.                                    (342.3)
```
For p labeled n-element sets C_t, each compared with W+t, put
```
r_t=|C_t\(W+t)|,  D_sharp=(B_0-T)/u .
```
Whenever B_0>T,
```
max_{|K'|=u} Pr_(t uniform){V_(C_t)(K';h)>T}
   >= #{t in F_p : r_t < D_sharp}/p.                     (342.4)
```
Consequently a worst-test-set failure bound q<=zeta requires at least (1-zeta)p rows to satisfy r_t>=D_sharp and
```
sum_t r_t >= (1-zeta)p D_sharp.                          (342.5)
```
These apply to arbitrary p-row ensembles, including the exactly n-regular design of r341. The previous r341 cutoff was (B_0-T)/(2u); (342.4) doubles the coefficient of its compulsory near-orbit edit-distance lower bound.

At the r329/r330 length n=ceil(c_* sqrt(p)(log p-2log log p+d)) and u=ceil(sqrt p), for fixed d,
```
D_sharp=(1+o(1)) sqrt(p).
```
Thus an orbit-perturbation family with q=o(1) needs (1-o(1))p rows each changed in at least (1-o(1))sqrt(p) element replacements, giving total necessary edit mass (1-o(1))p^(3/2). This statement is *relative to the designated interval-translation orbit*, not a no-go theorem for arbitrary balanced codebooks.

**Proof.** Equation (342.3) comes from (342.1). Translation preserves the value V_W(K;h), so each row with r_t<D_sharp is bad for the same deterministic interval test K. Counting such rows proves (342.4); rearrangement proves (342.5). Since n+u=O(sqrt(p)log p)=o(p) and T=p^(3/4)=o(p), (B_0-T)/u=(1+o(1))sqrt(p). QED.

## 3. Exact sharpness witness and reproducible finite check

For h=0 choose p=101, n=8, u=11, W={0,...,7}, K={0,...,10}. Delete the interior shift a=3 and insert b=40:
```
C=(W\{3}) union {40}.
```
The translates K-2 and K-4 already cover K-3 (since u>=2), so deleting 3 does not change |K-W|=18. The new translate K-40 is disjoint from K-W and contains exactly 11 residues. Hence
```
V_W(K;0)=101-18=83,
V_C(K;0)=101-29=72,
V_W(K;0)-V_C(K;0)=11=u.
```
Thus the Lipschitz coefficient u cannot be reduced in general. In the existing r341 two-row switch, the inserted shift is adjacent, so the actual decrease is only one for each edited row, consistent with the sharper universal estimate.

Full finite verification of the h=0 two-sided inequality for every A,B subset of F_7 and every K of size 1, 2 or 3 was completed: 1,032,192 ordered (A,B,K) comparisons, all passed. The count is (7+21+35)*2^7*2^7. This finite check corroborates the algebraic lemma but is not the source of its universal proof.

Python 3 reproducer:
```python
from itertools import combinations

def V(p,K,A,h):
    return sum(sum((x+a)%p in K for a in A)<=h for x in range(p))

p,n,u=101,8,11
K=set(range(u)); W=set(range(n))
C=(W-{3})|{40}
assert (V(p,K,W,0),V(p,K,C,0))==(83,72)

p=7
Ss=[set(c) for k in range(p+1) for c in combinations(range(p),k)]
count=0
for k in (1,2,3):
    for kt in combinations(range(p),k):
        K=set(kt)
        vals={frozenset(A):V(p,K,A,0) for A in Ss}
        for A in Ss:
            for B in Ss:
                assert (vals[frozenset(A)]-k*len(B-A)
                        <= vals[frozenset(B)]
                        <= vals[frozenset(A)]+k*len(A-B))
                count+=1
assert count==1032192
```

## 4. Dependency, correction, and next question

- r341, pinned commit `df916dc0b6f453c9cc87df3f67c75d8e8e16ee9b`, remains valid: its weaker 2ur inequality and all conclusions derived from it were safe bounds. Equations (342.3)–(342.5) replace the quantitative coefficient, without invalidating the existing non-orbit regular counterexample or perfect-marginal construction.
- r336, pinned commit `e56f4a1ad63405c30c392a2c22c1f57cea194128`, likewise used a conservative 2ur edit bound; the same sharpening applies to its equal-cardinality single-shift-set comparison.
- r337–r340 supply the exact regular-incidence/equal-position-marginal structure; this lemma does not change those results.
- The stronger obstruction makes the independent question more concrete: build and test p-row exactly n-regular ensembles genuinely far from the interval-translation orbit, or construct a single deterministic n-set with the requisite all-K low-tail certificate at the sharp length. A separate Source-authenticated Driver review of a frozen original Result remains a distinct authorization action.

Original task identity: `RS-OAI7-028-C-20261007-6F2A81` / `TP2-96FAC49786245691AE19`. Parent objective: `OBJ-OAI7-RESEARCH-TRANSFER-20261007`. No claimed Native publication/acceptance or X6 transfer.
