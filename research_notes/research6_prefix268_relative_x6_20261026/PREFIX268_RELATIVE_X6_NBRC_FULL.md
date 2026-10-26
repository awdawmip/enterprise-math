# PREFIX-268 — Native signed X6 relative quotient: first three-step alias, exact growth, and future-safe N-BRC observer

Date: 2026-10-26. Status: AUTHOR_SIDE_EXACT_DERIVATION / TWO_INDEPENDENT_FINITE_CHECKS_PASS / UNREVIEWED / NOT_ADMITTED. This is a self-contained research paper, proof, execution witness, and next-step handoff; **not** a native Task, CLAIM, Result, Driver review, physical heartbeat, or admitted TRIADIC_CLOSURE_E theorem.

## Immutable input and method
Account/global: awdawmip/chatgpt-global-knowledge main@b1c6f9e87fc51617f9b75e37235682850b279b20; 00_BOOTSTRAP, OPERATING_MANUAL, Enterprise Math project/TASK router, matching P000_STARTUP and canonical P000 (blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), ACTIVE 我眼中的世界, math/BRC/code rules.
Project Source frozen for scientific input: awdawmip/enterprise-math main@2c8e32bebf20b3134d51a709f78fce96fbf992a0. Exact relevant sources: docs/PORTABLE_RESEARCH_PROTOCOL.md; AGENTS.md; definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json; definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json; definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json; definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md §§3,6,8–10; definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json; src/enterprise_math/brc_weighted.py; predecessor research_notes/research6_prefix267_signed_path_20261026/PREFIX267_SIGNED_X6_PATH_FORMAL.md.

P000 spatial substrate is a full native six-axis discrete Cell torsor X6=AFFINE_TORSOR(Z^6), not a native plane. There are 12 signed native primitive directions, not 12 spatial dimensions. Time is separately typed and added only when modeling dynamics. We choose one reference Cell only for a raw displacement chart; no privileged ontological origin is introduced, and raw signed Z^6 is not the final registered nonnegative Cell address. Native PERP_E 120-degree relation is left intact. Physics, actual phase, Cell/Port coupling and the full heartbeat update Phi remain unspecified; this study is an exact source-typed **Path-Formal N-BRC positive multiplicity** problem, not a new native time evolution.

Let e_i be the unit vector for signed native direction +E_i. The path alphabet A={+E_i,-E_i: 1<=i<=6}; a path w has n ordered labeled steps and full endpoint z(w)=sum_j delta(a_j), preserving signed labels/provenance even when a readout forgets them. Define D=(1,1,1,1,1,1) and relative observer r(z)=can6(z)=z-min_i(z_i)D, representing G6_REL=Z^6/ZD. Thus r(x)=r(y) iff y-x=kD for some k in Z. We never identify equality of r with equality of full Cell identity.

## Theorem A: Source-backed exact descent for genuine primitive spatial actions
The twelve **pure spatial coordinate adjacency actions actually declared in Source** T_i^sigma(z)=z+sigma e_i (sigma=+/-1) and all axis-label permutations P in S6 descend:
 barT_i^sigma(r)=can6(r+sigma e_i), barP(r)=can6(Pr).
They obey r o T_i^sigma = barT_i^sigma o r and r o P = barP o r. Proof: x and y differ by kD iff their translations still differ by kD, and P D=D. Any finite composition of these declared operations therefore descends for the declared relative-coordinate observer. The witness r(0)=r(D) despite 0!=D proves this observer loses full Cell identity. Nothing here proves descent of the unprovided complete physical Phi, phase updates, material/Port states or a future observer accessing hidden coordinates.

## Theorem B: Exactly 20 first collisions at path length 3
Write E_n={z(w): |w|=n}. Relative r is injective on E_0, E_1 and E_2. At n=3 it has exactly C(6,3)=20 non-singleton fibers, each consisting of precisely two distinct full endpoints.

For every 3-subset S of {1,...,6}, define H_S=sum_{i in S}e_i; write S^c for its complementary three indices. Then r(H_S)=r(-H_{S^c})=H_S. Each endpoint is attained by precisely 3!=6 ordered shortest paths, so positive count/total/dominant CWM for each endpoint is (6,6,1), whereas recoalescing their separate path populations to the same *relative* output gives (12,12,1) under the existing positive BRC (+,+,max) law, not sign/phase cancellation.

Proof of completeness: r(x)=r(y) for x!=y implies y-x=kD with nonzero integer k. The triangle inequality gives 6|k|=||kD||_1<=||x||_1+||y||_1<=2n; so n>=3. At n=3 equality forces |k|=1 and each endpoint length exactly three. After swapping, take y=x+D. Coordinatewise triangle equality forces x_i in {-1,0}; ||x||_1=3 forces exactly three -1 entries. Consequently x=-H_{S^c}, y=H_S with |S|=3. These 20 fibers are disjoint, and any third lift would differ by at least 2D and require n>=6. The word "three" here counts primitive path steps and a combinatorial triple; it is **not** an admissible P000 physical stable three-force incident or TRIADIC_CLOSURE_E proof.

## Theorem C: Exact rational generating function for the complete six-axis relative endpoint image
Let R6(n)=|r(E_n)| and let d([z])=min_{k in Z}||z+kD||_1 be the shortest primitive path distance of a relative class. Sorting its six coordinates gives x_1<=...<=x_6 with adjacent gaps g_j=x_{j+1}-x_j>=0. Exact median minimization yields
 d([z]) = g_1 + 2g_2 + 3g_3 + 2g_4 + g_5.
Because adding kD changes coordinate sum by 6k (even), the parity of ||z||_1 is class-invariant. A class has a signed length-n path iff d<=n and d=n mod 2, because unused even steps can be inverse pairs. Thus R6(n)=sum_{d<=n,d congruent n mod 2} a6(d), where a6(d) is the exact relative sphere count.

For each ordered composition b_1+...+b_t=6 into positive integers, let B_j=sum_{i<=j}b_i and w_j=min(B_j,6-B_j). The full relative sphere series is the 32-term **integer/positive-rational path-composition exact identity**
 A6(x)=sum_{d>=0}a6(d)x^d
 = sum_{ordered compositions b of 6} [6!/(product b_i!)] product_{j=1}^{t-1} x^{w_j}/(1-x^{w_j})
 = (1+7x+22x^2+22x^3+7x^4+x^5)/(1-x)^5.
Here the multinomial counts which labeled axes occupy each equal-coordinate block; each strictly positive inter-block coordinate gap has geometric exact integer multiplicity. The independent 32-composition polynomial certificate below verifies the finite identity exactly, and the composition derivation proves it for every coefficient.

Since R6(n) counts all distance spheres of the same parity up through n, its series is A6(x)/(1-x^2), giving the **all-n exact theorem**
 sum_{n>=0}R6(n)x^n
 = (1+6x+16x^2+6x^3+x^4)/(1-x)^6.
Equivalently, with binom(t,5)=0 for t<5,
 R6(n) = binom(n+5,5)+6binom(n+4,5)+16binom(n+3,5)+6binom(n+2,5)+binom(n+1,5).

Finite **proof certificate**, not a floating fit: enumerate every subset B of the five consecutive gap breakpoints, with weights (1,2,3,2,1), and b_i their induced block lengths, m(B)=6!/(product b_i!). Clearing the common denominators in the ordered-block formula gives
 sum_{B subset {1,...,5}} m(B) x^(sum_{i in B}w_i) product_{i notin B}(1-x^(w_i))
 = 1+10x+47x^2+119x^3+183x^4+183x^5+119x^6+47x^7+10x^8+x^9
 = (1+7x+22x^2+22x^3+7x^4+x^5)(1+x)^2(1+x+x^2).
This equality is checkable by 32 exact finite integer-polynomial multiplications and proves the reduction to the claimed rational expression.

## Theorem D: Exact least relative future observer for h formal last-step deletions
Define D_last(w) as the formal operation removing the last source label (NOT an actual physical heartbeat inverse), and
 O_h^rel(w)=(r(z(w)), r(z(D_last w)),...,r(z(D_last^h w))) for 0<=h<=n.
Then O_h^rel(u)=O_h^rel(v) iff r(z(u))=r(z(v)) **and** the last h signed source labels match in their actual order.

Proof: in quotient group Z^6/ZD, successive observed differences equal the class of each deleted signed unit vector. The twelve classes pi(+/-e_i) are pairwise distinct: if sigma e_i-tau e_j=kD, one of the at least four untouched coordinates forces k=0, then the labels are equal. Thus all h labels can be recovered successively; conversely the endpoint class and ordered suffix reconstruct every prior relative observation. Every reachable prefix relative class independently combines with every length-h suffix, so the exact number of future-safe classes is
 Q6_rel(n,h) = 12^h R6(n-h).
This quotient is *minimal only for this declared relative observation and formal deletion language*. Hidden Cell/Port/phase, path-joint and physical time information is **not** certified erasure-safe.

Examples: n=3, full endpoints=304, relative classes R6(3)=284, hence exactly 20 two-element endpoint aliases. n=10, full endpoints=85,305, R6(10)=40,821. n=12, full endpoints=227,305, R6(12)=93,743; Q6_rel(12,2)=144*40,821=5,878,224. The predecessor full-endpoint future observer gave 12,283,920 classes at n=12,h=2; these are different typed observers. Relative sphere sequence a6(0..12)=[1,12,72,272,762,1752,3512,6372,10722,17012,25752,37512,52922].

## Reproducible compact exact checker (Python 3, standard library only)
The separate full author-side validation artifacts use independent dynamic programming (n<=12) and a 32-composition exact polynomial checker plus exhaustive all words n<=4, all deletion horizons. Both independent executions returned PASS. The following compact checker reproduces the principal two independent identities and endpoint numbers:

~~~python
from collections import Counter, defaultdict
from itertools import combinations
from math import comb, factorial
from functools import reduce
S = [(i,v) for i in range(6) for v in (-1,1)]
def r(z):
    a=min(z)
    return tuple(v-a for v in z)
def f(n):
    c=[1,6,16,6,1]
    return sum(c[j]*comb(n+5-j,5) for j in range(5) if n+5-j>=5)
states=Counter({(0,)*6:1})
for n in range(13):
    observed=len({r(z) for z in states})
    assert observed==f(n),(n,observed,f(n))
    assert sum(states.values())==12**n
    if n==3:
        fibers=defaultdict(set)
        for z in states:fibers[r(z)].add(z)
        assert sum(len(v)>1 for v in fibers.values())==20
        assert all(len(v)<=2 for v in fibers.values())
    if n==10:assert (len(states),observed)==(85305,40821)
    if n==12:assert (len(states),observed)==(227305,93743)
    nxt=Counter()
    if n<12:
        for z,c in states.items():
            for i,s in S:
                t=list(z);t[i]+=s;nxt[tuple(t)]+=c
        states=nxt
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,y in enumerate(b):c[i]+=y
    return c
w=[1,2,3,2,1]
p=[0]
for mask in range(32):
    br=[0]+[i+1 for i in range(5) if (mask>>i)&1]+[6]
    b=[br[j+1]-br[j] for j in range(len(br)-1)]
    m=factorial(6)
    for s in b:m//=factorial(s)
    power=sum(w[i] for i in range(5) if (mask>>i)&1)
    term=[m]
    for i in range(5):
        if not ((mask>>i)&1):
            factor=[1]+[0]*(w[i]-1)+[-1]
            term=mul(term,factor)
    p=add(p,[0]*power+term)
target=mul([1,7,22,22,7,1],mul([1,2,1],[1,1,1]))
assert p==target==[1,10,47,119,183,183,119,47,10,1]
assert len({r(tuple(int(i in Q) for i in range(6))) for Q in combinations(range(6),3)})==20
assert 12**2*f(10)==5878224
print("PREFIX268_COMPACT_INDEPENDENT_INTEGER_CERTIFICATE_PASS")
~~~

Coverage for author-side executions: endpoint dynamic programming for n=0..12, not enumeration of the 12^12 individual path words. Independent integer gap-polynomial identity for all 32 block compositions; exact exhaustive correspondence for all 20 triangular endpoint pairs and all signed path words n<=4, every h<=n, with separate scripts. Numeric checks are exact integers, not a proof of the native physical model. Formulae for all n are justified by the proofs above; finite execution is supplementary validation. No classical pi, trigonometric physical propagator, ordinary matrix exponential or physical phase evolution was evaluated. Existing source methods resolved as REUSE_APPLIED (X6 torsor §3/6/8/10; positive BRC recoalescence); installed Source Python executable was not run as that package was unavailable in the local verifier environment.

## Actual authority / source status
GitHub connector identity: awdawmip; repository permission: admin. Native Sites identity owner-bound but static read-only; allowed em:access/source:read/control:read; research_authority_granted=false. Native em_control_tasks returned CONTROL_QUOTA; attempted em_session_start returned STATIC_READONLY_SCOPE_DENIED and operation_sent=false. Canonical active Task Owner/CLAIM cannot be resolved from this native channel. This note is an independent author-side scientific checkpoint on GitHub, not a native owner takeover, activity claim, publication/Result, independent review, or Foundation promotion. No source/private credentials or hidden session keys are present.

## Smallest exact successor PREFIX-269
First identify an actually admitted Source-typed non-spatial native update Phi on a complete state (Cell identity, Port, phase/sign, field/loop/source, boundary, and explicitly typed time where needed), and declare allowed observers and future operations. Test fiber constancy of the relative map: q(x)=q(y) implies q(Phi x)=q(Phi y). Either prove a proper descent theorem under the precise port-access restrictions or supply an exact pair of fully typed same-relative-output states with different observed successors. Source positive recurrent port-collapse semantics may be REUSE_APPLIED only under its hidden-state-access lease; do not use positive mass as amplitude. If the native Phi contract is not present, preserve this exact capability gap rather than promoting a proposed toy law. A separate authorized driver may review this author-side result, with actual contribution/identity isolation preserved.
