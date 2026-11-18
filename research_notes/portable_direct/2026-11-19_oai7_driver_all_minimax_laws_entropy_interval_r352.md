# OAI7 r352 — Complete classification and sharp entropy interval of all prime-29 minimax laws

2026-11-19. **Exact finite mathematical theorem, author-side Driver context.** This combines r347's rational primal/dual optimum, r348's affine-orbit rigidity, r350/r351's global loss-profile fibers, and a **new full-rank certificate for the 392 active individual test constraints**. It retains the original OAI7 researcher and does not purport to be a Native independent review.

## Model

On \(G=\mathbb F_{29}\), let \(C\) be any random 5-subset and \(K\) any deterministic 4-subset. Define
\[
b_K(C)=\mathbf1\{|K-C|\le16\},\quad
q(\mu)=\max_{|K|=4}\mathbb E_\mu b_K(C).
\]
The exact unrestricted optimum from r347 is
\[
v=\frac{2024467747}{3324255613}.
\]
Write \(D=474893659\), with \(3324255613=7D\). The unique optimal affine-orbit masses from r348 are \(w_j=a_j/D\) on
\[
S=(1,2,5,6,7,11,23,25,30,37,47,50,114,115),
\]
using the exact r347 0-based affine enumeration. Each selected orbit \(j\) contains \(t_j=28\) translation classes except \(t_6=14\). The positive dual test orbits are
\[
I=(8,10,12,13,14,18,21,22,25,26,27,29,31,32),
\]
containing **392 distinct translated-test classes** in total.

## New theorem: all minimizers, not only the affine-invariant one

**(i) Unique mass on each complete loss-profile fiber.** Every globally minimax law on all \(\binom{29}{5}=118755\) raw five-sets has zero mass outside the 14 affine orbits \(S\). Within those orbits, **the total mass of each of the 350 distinct r350 loss-profile fibers is uniquely determined**. Specifically:

- For every \(j\in S\setminus\{1,2\}\), each of the \(t_j\) distinct translation classes has mass exactly \(a_j/(Dt_j)\).
- For \(j=1,2\), the \(t_j=28\) translation classes form 14 reflected indistinguishable pairs. Each such pair has total mass exactly \(2a_j/(Dt_j)\), and its mass can be split arbitrarily between the two classes.
- Within each occupied translation class, the mass can be split arbitrarily among its 29 raw translated sets.

**Conversely**, all laws with these masses are globally optimal and give **exactly the same probability of failure for every individual deterministic 4-set test K**, not just the same worst-case maximum.

**(ii) Sharp global entropy interval.** With base-two Shannon entropy on the originally sampled unordered raw 5-set \(C\), *every* exact minimax law satisfies
\[
\boxed{7.869745624309653\ldots\le H(C)\le12.799695400978694\ldots\quad\text{bits}.}
\]
Both endpoints are attained and every intermediate entropy value is attainable. The lower endpoint is **the absolute minimum entropy among all unrestricted minimax probability laws**, upgrading the conditional support result in r350.

In exact terms, with \(\alpha=(a_1+a_2)/D=34177518/474893659\),
\[
H_{\min}=
-\sum_{j\in S\setminus\{1,2\}}w_j\log_2(w_j/t_j)
-\sum_{j\in\{1,2\}}w_j\log_2(2w_j/t_j),
\]
\[
\boxed{H_{\max}=H_{\min}+\log_2 29+\alpha.}
\]
The maximum is the fully affine-invariant r347 law; a minimum chooses one shift set per positive loss-profile fiber (350 atoms, one raw translation per atom).

## Proof

1. **Support.** r348's exact positive dual gap and 14-by-14 nonsingular active affine matrix prove that the affine-orbit masses of every optimizer equal \(w_j\), hence are supported on \(S\).

2. **All active individual tests are tight.** Symmetrize any optimizer \(\mu\) over \(\mathrm{AGL}(1,29)\). For each of the 14 dual-positive test orbits, the symmetrized law has failure probability exactly \(v\). This is the average of the individual test failure probabilities over that orbit; each individual probability is at most \(v\). Thus **each of the 392 translated-test-class constraints is an equality** for the original nonsymmetric \(\mu\).

3. **New exact active matrix rank.** Restrict these 392 test rows to the 378 selected translation classes in \(S\). r350/r351 established 28 identical pairs of columns and 322 singleton columns, giving at most 350 independent columns. The new exact certificate below computes **rank 350 over \(\mathbb F_7\)**. Therefore the rank over \(\mathbb Q\) is exactly 350. The 392 tight equations uniquely determine the 350 aggregated profile-fiber masses. The positive r350 350-atom law solves them, so its masses are the unique solution. No assumption of symmetry is used for this last uniqueness.

4. **All optimizers classified.** Any split inside a twin fiber and any translation of an atom leaves each \(b_K\) unchanged. Conversely, rank uniqueness and r348 support force every optimum to arise from those splits and translations. This also fixes the full vector of per-test failure probabilities.

5. **Entropy bounds.** The profile fiber is a deterministic function of the raw set. Its mass law is fixed, so \(H(C)\ge H(\mathrm{profile})=H_{\min}\). A singleton fiber consists of 29 raw translates, while a twin fiber contains 58. Conditional entropy is maximized by uniform conditional distribution within every fiber, giving \(H_{\max}=H_{\min}+\log_2 29+\alpha\). All intermediate values follow by continuously deforming these conditional laws while retaining the fixed fiber masses.

## Exact finite certificate (standard Python 3)

The r347/r348 strict dual gap and active-support facts are reused at their pinned exact statements. This checker independently regenerates all selected sets/tests, verifies the r349 exact primal inequalities by integer arithmetic (all 819 test classes), checks equality on all 392 active tests, and establishes the **new rank-350 claim modulo 7**. The modular field is important: the active matrix has rank only 348 modulo 2, but rank 350 modulo 7.

~~~python
from itertools import combinations
from collections import defaultdict, Counter
from math import log2

P=29
FULL=(1<<P)-1
def rot(m,t):
    t%=P
    return (((m<<t)|(m>>(P-t)))&FULL) if t else m
def norm(m): return min(rot(m,t) for t in range(P))
def mul(m,a): return sum(1<<((a*x)%P) for x in range(P) if (m>>x)&1)
def reps(k):
    return sorted({norm(sum(1<<x for x in ss))
                   for ss in combinations(range(P),k)})
def orbits(base):
    ix={c:i for i,c in enumerate(base)}
    seen=set(); out=[]
    for c in base:
        if c in seen: continue
        ids=sorted({ix[norm(mul(c,a))] for a in range(1,P)})
        oo=[base[i] for i in ids]
        assert not (seen&set(oo))
        seen.update(oo); out.append(oo)
    assert len(seen)==len(base)
    return out
def bad(k,c):
    union=0
    for x in range(P):
        if (c>>x)&1: union|=rot(k,-x)
    return int(union.bit_count()<=16)

C=orbits(reps(5)); K=orbits(reps(4))
assert (len(C),len(K))==(150,33)
S=[1,2,5,6,7,11,23,25,30,37,47,50,114,115]
I=[8,10,12,13,14,18,21,22,25,26,27,29,31,32]
a={1:16479487,2:17698031,5:90390274,6:10843621,
   7:139525152,11:6049484,23:10138260,25:26578050,
   30:14514456,37:22809640,47:3118488,50:39221480,
   114:53586612,115:23940624}
D=474893659
assert sum(a.values())==D and 7*D==3324255613
CS=[c for j in S for c in C[j]]
KS=[k for orb in K for k in orb]
IA=[k for j in I for k in K[j]]
assert (len(CS),len(KS),len(IA))==(378,819,392)

# Integer-denominator (28 D) validation for r349 primal law.
coef=[a[j]*(28//len(C[j])) for j in S for _ in C[j]]
assert all(28%len(C[j])==0 for j in S)
target=4*2024467747
assert all(sum(bad(k,c)*coef[z] for z,c in enumerate(CS))<=target for k in KS)
assert all(sum(bad(k,c)*coef[z] for z,c in enumerate(CS))==target for k in IA)

# Selected column identity classes, now restricted to tight tests.
fib=defaultdict(list)
for z,c in enumerate(CS):
    bits=sum(bad(k,c)<<i for i,k in enumerate(IA))
    fib[bits].append(z)
assert len(fib)==350
assert Counter(map(len,fib.values()))=={1:322,2:28}

# Row reduction over F_7, exact small integer field arithmetic.
prime=7
basis={}
for k in IA:
    row=[bad(k,c) for c in CS]
    while True:
        pivot=next((i for i,x in enumerate(row) if x%prime),None)
        if pivot is None: break
        if pivot not in basis:
            basis[pivot]=row
            break
        b=basis[pivot]
        factor=row[pivot]*pow(b[pivot],-1,prime)%prime
        row=[(x-factor*y)%prime for x,y in zip(row,b)]
assert len(basis)==350

Hmin=-sum((a[j]/D)*log2((a[j]/D)/
       (len(C[j])//(2 if j in (1,2) else 1))) for j in S)
Hmax=Hmin+log2(P)+(a[1]+a[2])/D
assert abs(Hmin-7.869745624309653)<1e-12
assert abs(Hmax-12.799695400978694)<1e-12
print("r352 PASS: 392 active test rows, rank 350 mod 7; "
      "all primal constraints exact; global entropy endpoints verified")
~~~

Observed local execution: all assertions PASS. Finite enumeration, matrix entries, inequality comparisons and Gaussian elimination use exact integers; base-two entropy decimals are display only. The proof of *global* minimax uses the already verified r347/r348 exact rational dual certificate as a dependency, not a numerical LP guess.

## Attribution and scope

Sources: r347 exact minimax commit 12bd331ea2aef70cc844682db432a623b235e726; r348 dual-gap/rigidity f41c2690daba467ecbde99615a1337e67be46ffd; r349 quotient eac1b9044c3b76648b6d352c50ec243650b1bec9; r350 twins 2737a8ea300816066714ef0ff8d72b62c6df2e46; r351 global fiber classification 6a9da64ae349c647744773f92c80753a6f9ffb23.

Original OAI7 contributor EM-EMF6D046-5A2844. Task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19. This is an exact finite external cyclic-shift model result in shared Driver research context. Native independent Result review, Source/Activity semantics, native X6 port/provenance transfer, formal Task completion and parent-objective closure have their separate evidence and authorization requirements.
