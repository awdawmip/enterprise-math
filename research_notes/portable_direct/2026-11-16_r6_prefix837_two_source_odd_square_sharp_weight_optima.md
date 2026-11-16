# PREFIX-837 — Sharp uniform resource lower bound and exact optimal odd-square recollisions for two named positive BRC sources

Date: 2026-11-16.
Status: AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION / EXACT_NAMED_STATE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Antecedents: PREFIX-832 through PREFIX-836, particularly the Q-only full-histogram difference formula and odd-time two-source recollision interface. This is a **typed auxiliary positive named-source BRC model**, not an assertion about native X6 physical time or signed-amplitude cancellation.

## Definition of the exact problem

Fix capacity p=q=2, two initially present distinguishable unmarked sources with positive-integer weights (x,y), marked source initially absent, and a=1,b=2. Q=R+A is the **sum of legal weighted alternative operations**: each unmarked source can be removed with its own weight, the marked source can be removed with weight 2 when present, and the marked source can be added with weight 1 when absent and occupancy is below 2. No merging of named-source identities is done in the underlying branching state.

Let Y(t)=(Y_0(t),Y_1(t),Y_2(t)) denote the unnormalized occupancy histogram after t applications of Q. For every odd integer T>=3, define M_2(T) as the minimum possible largest individual weight of two *distinct* two-source multisets A,B such that Y_A(1) != Y_B(1) but Y_A(T)=Y_B(T).

The condition for positive odd T (derived directly below) is

\[
\Delta e_1+(T-1)\Delta e_2=0,\qquad
e_1(x,y)=x+y,\quad e_2(x,y)=xy.
\tag{837.1}
\]

## Lemma 837.1 — Exact recollision equation and parity

For odd t>=1, the only potentially nonzero occupancy bin is bin 1; the exact two-source difference is

\[
Y_{A,1}(t)-Y_{B,1}(t)
=2^{(t-1)/2}\left(\Delta e_1+(t-1)\Delta e_2\right).
\tag{837.2}
\]

For even t>=2, the bin-0 difference includes
\[
Y_{A,0}(t)-Y_{B,0}(t)
=2(t-1)2^{(t-2)/2}\Delta e_2
\tag{837.3}
\]
and therefore cannot vanish if the pairs obey the nontrivial odd-time recollision equation (837.1).

**Proof.** Expand the named-source Q transition (initially full). At each step, the occupancy parity changes, so only occupancy 1 is possible at odd steps. Collect the full Q transition weights by which original named sources are removed. The full future-difference formula of PREFIX-832 has the only two contributions to occupancy 1: (d,m)=(1,0) with coefficient \(2^{(t-1)/2}\Delta e_1\), and (d,m)=(2,1) with coefficient \(2^{(t-1)/2}(t-1)\Delta e_2\); the latter is zero at t=1. At even steps, occupancy 0 receives the (d,m)=(2,0) term, giving (837.3). Alternately, these identities follow by induction on the explicit three-bin marked-state Q recurrence. If (837.1) holds with distinct A,B then \(\Delta e_2\neq0\), since \(\Delta e_1=\Delta e_2=0\) fixes the monic quadratic with roots A and B, hence A=B. Equation (837.2) has a single positive odd zero at t=T and differs at t=1; (837.3) rules out even-time recollision. QED.

## Theorem 837.2 — Uniform sharp-leading resource law

For **every odd integer T>=3**,

\[
\boxed{\left\lceil T+2\sqrt{T}\right\rceil\le M_2(T)\le 2T+1.}
\tag{837.4}
\]

Consequently M_2(T)=Theta(T) over all odd T; in particular, the least number of sources (two) imposes linear maximal-integer-weight growth. The bound improves the elementary M>=T/2 and is **uniform**, unlike the three-source even-time Pell-subsequence square-root upper bound in PREFIX-836.

**Proof.** Let A=(x,y), B=(u,v) with x<=y, u<=v, all entries between 1 and M. Since the distinct pairs satisfy (837.1) for T>1, orient them so that \(x+y>u+v\) and \(xy<uv\). Put \(k=uv-xy\ge1\). Then

\[
x+y-u-v=k(T-1)>0. \tag{837.5}
\]

These sum and product inequalities force x<u and y>v. Indeed if x>=u, then x+y>u+v implies any decrease y<v is smaller than x-u; since y>=u, \(xy-uv=(x-u)y+u(y-v)>0\), impossible. If y<=v, the positive sum difference forces x>u, already excluded.

**Case k>=2.** We have \(u-x>=1\), \(v>=u>=2\), \(y<=M\), so
\[
k(T-1)=(y-v)-(u-x)\le M-3.
\]
Thus \(M>=k(T-1)+3>=2T+1>=T+2\sqrt T\) for T>=3, because \(T+1-2\sqrt T=(\sqrt T-1)^2>=0\).

**Case k=1.** AM-GM on B gives \(u+v>=2\sqrt{uv}=2\sqrt{xy+1}\). Therefore
\[
T-1\le x+y-2\sqrt{xy+1}.
\]
Because x<u and u<=v<y, we have 1<=x<=y-1. For fixed y>=2, the right-hand side decreases as x increases over [1,y-1], since its x derivative \(1-y/\sqrt{xy+1}<0\) there. For x=1, the expression \(1+y-2\sqrt{y+1}\) increases with y. It follows that
\[
T-1\le M+1-2\sqrt{M+1}.
\]
Set z=\(\sqrt{M+1}\). Then \(T\le(z-1)^2\), hence z>=1+\(\sqrt T\), or \(M>=T+2\sqrt T\). The integer ceiling gives the stated lower bound.

For the upper bound, the already verified explicit positive pair
\[
A=(1,2T+1),\quad B=(2,T+1)
\]
has \(\Delta e_1=T-1\), \(\Delta e_2=-1\), so (837.1) holds and M<=2T+1. QED.

## Theorem 837.3 — Exact optimum and uniqueness at every odd square

For **every odd integer s>=3** and T=s^2,

\[
\boxed{M_2(s^2)=s^2+2s.} \tag{837.6}
\]

Up to swapping the two multisets and permuting weights within each multiset, the **unique** optimal witness is

\[
\boxed{A_s=(1,s^2+2s),\qquad B_s=(s+1,s+1).} \tag{837.7}
\]

Its entire full-occupancy observation history is identical at exactly t=0 and t=s^2, and different at all other nonnegative integer times.

**Proof.** The lower bound (837.4) gives M>=s^2+2s. For the displayed pair, \(e_1(A_s)=s^2+2s+1\), \(e_1(B_s)=2s+2\), so \(\Delta e_1=s^2-1=T-1\). Moreover \(e_2(A_s)=s^2+2s\), \(e_2(B_s)=(s+1)^2=s^2+2s+1\), so \(\Delta e_2=-1\). It attains (837.1) with M=s^2+2s; uniqueness of the collision time follows from Lemma 837.1.

For uniqueness of the *minimum-weight realization*, k>=2 would force M>=2s^2+1>s^2+2s for s>=3. Thus k=1. Equality in the chain
\[
s^2-1\le x+y-2\sqrt{xy+1}\le M+1-2\sqrt{M+1}=s^2-1
\]
forces x=1, y=M (strict monotonicity where x<y) and equality in AM-GM forces u=v=\(\sqrt{M+1}=s+1\). Therefore the displayed pair is the only optimum modulo reordering. QED.

## Corollary 837.4 — Asymptotically optimal leading constant on an infinite odd-time family

On the odd perfect squares,
\[
\lim_{\substack{s\to\infty\\s\ {\rm odd}}}\frac{M_2(s^2)}{s^2}=1,
\quad
M_2(s^2)-s^2=2s.
\]
The universal lower bound proves that the coefficient 1 cannot be improved in a uniform linear lower asymptotic. This result and PREFIX-836 distinguish the resource laws for two-source odd-time and three-source even-time observers; they do not assert one shared operator-independent optimization law.

## Finite exact computation and independent named-state regression

The accompanying Python standard-library checker enumerates all unordered positive pairs x<=y in nondecreasing maximum weight M. Its exact collision key is
\[
F_T(x,y)=x+y+(T-1)xy.
\]
Different pairs with the same key cannot have the same product (otherwise they also have the same sum, hence the same unordered roots). The **first** key collision gives the rigorous finite optimum for that T; all smaller maxima were completely enumerated.

For odd T=3,5,...,51 (25 targets), full enumeration returns:

| T | M_2(T) | T | M_2(T) | T | M_2(T) |
|---:|---:|---:|---:|---:|---:|
| 3 | 7 | 5 | 11 | 7 | 15 |
| 9 | 15 | 11 | 22 | 13 | 24 |
| 15 | 23 | 17 | 32 | 19 | 37 |
| 21 | 31 | 23 | 38 | 25 | 35 |
| 27 | 39 | 29 | 52 | 31 | 53 |
| 33 | 47 | 35 | 47 | 37 | 74 |
| 39 | 55 | 41 | 60 | 43 | 66 |
| 45 | 59 | 47 | 82 | 49 | 63 |
| 51 | 71 | | | | |

The program independently evolves the full legal *named-subset plus marked-bit* weighted Q branching dynamics for each finite-optimal pair through t=T+2, and for the explicit odd squares s=3,5,7,9,11,13 through t=s^2+2. Exact equality times are {0,T} in every case.

Execution with Python 3 standard-library integers yielded \`ALL_EXACT_ASSERTIONS_PASSED\`, 27,189 examined unordered pairs aggregated over 25 separate finite searches and 3,666 full histogram scalar comparisons. These finite computations are implementation/regression evidence; Theorems 837.2 and 837.3 are proved algebraically above and cover all declared integers.

## Preserved next questions

1. Determine M_2(T) for nonsquare odd T at increasing horizons, and construct subfamilies achieving \(M_2(T)=T+O(\sqrt T)\). The universal sharp-leading lower coefficient is now closed; the uniform best *upper* coefficient remains between 1 and 2.
2. Determine whether the p=3 even-time M(T) from PREFIX-835/836 admits a uniform O(sqrt T) upper bound (the existing Pell construction applies to an infinite subsequence).
3. Determine minimal observation coordinates that remain faithful across the isolated single-frame aliases, then examine q>=5,b>0 minimal nonnegative integer Q-only carriers.
4. Independently address native X6 Cell/Link/Port authorization and physical causal time. The present exact Q model gives no native cross-Cell permission.

Researcher provenance: continued independent auxiliary scientific line of PREFIX-836, with no asserted shared RS-X6 CLAIM, formal Result, independent review or Foundation promotion.
