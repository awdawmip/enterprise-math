# PREFIX-918 — Complete disjoint mass of *all* named two-flip collisions under a two-port modular observer

Date: 2026-11-19 (Asia/Shanghai). Lane: 进取数论研究6.
Status: AUTHOR_PROVED / EXACT_INTEGER_COMPUTED / SMALL_STATE_EXHAUSTIVE / INDEPENDENT_CONGRUENCE_FIRST_RECOUNT / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Direct dependencies: PREFIX-915 (fixed signed identity multiplicity), PREFIX-916 (only high-source-first, positive terminal gap), and PREFIX-917 (equal-start classes).
This result is a provenance-preserving auxiliary labeled-XOR two-port theorem; it does not assert native X6 Cell/Link/Port time admission.

## 1. Exact observer and all-pair partition

Fix integer \`p>=2\` and \`N=2^p\`. A named bit-flip trajectory is \`F_x^i=(x,x XOR 2^i)\` with \`0<=x<N, 0<=i<p\`. The observer is \`Phi_(a,b)(u,v)=(u mod a,v mod b)\`, with positive odd \`a,b>1\`.

We count **all unordered pairs of distinct named bit-flip trajectories** with equal observations. They are partitioned uniquely into (I) \`x=y\`, \`i<j\` (common initial state, PREFIX-917) and (II) \`x<y\`, where indices \`i,j\` at these respective states may be in any order, including equality.

For \`A=ka=y-x>0\`, with \`1<=k\` and \`A<N\`, define signs \`eps,eta in {-1,+1}\` by \`x XOR 2^i=x+eps*2^i\` and \`(x+A) XOR 2^j=x+A+eta*2^j\`. Then the terminal gap is \`D=A+eta*2^j-eps*2^i\`, permitted to be positive, zero, or negative.

Let \`K_p(A,i,j,eps,eta)\` count \`0<=x<N-A\` with bits \`bit_i(x)=1[eps=-1]\` and \`bit_j(x+A)=1[eta=-1]\`.

**Theorem 918-A (orientation-complete collision mass).** Define
\`\`\`text
Z_p(b)=(N/2)*sum_{d=1}^{p-1}(p-d)*(1[b | 2^d-1]+1[b | 2^d+1]).
T_p(a,b)=Z_p(b)
  + sum_{1<=k,ka<N} sum_{0<=i,j<p} sum_{eps,eta in {-1,+1}}
      1[b | (ka+eta*2^j-eps*2^i)] * K_p(ka,i,j,eps,eta).
\`\`\`
Then \`T_p(a,b)\` equals exactly the number of distinct unordered labeled two-flip collision pairs at observer \`Phi_(a,b)\`. Every positive term is disjoint from all other parameter fibers, including fibers where \`i=j\` or \`D<=0\`.

**Proof.** Every colliding unordered pair with unequal starts has a unique smaller start \`x\` and larger start \`y=x+A\`. Their identical first-port residues force a unique positive integer \`k=A/a\`. The two source indices \`i,j\` and their signs \`eps,eta\` are determined by the actual named trajectories. Identical second-port residues hold exactly when \`b|D\`. Conversely every \`x\` counted by such a term creates two *distinct* named-flip trajectories with both port residues equal. The recovery of \`(k,i,j,eps,eta,x)\` from the pair proves disjointness, regardless of terminal-gap sign. If the starts coincide, distinctness forces \`i<j\` after ordering; PREFIX-917 counts precisely those pairs as \`Z_p(b)\`, disjoint from all unequal-start fibers. QED.

## 2. Constant-time exact integer kernel for every index order

Define for arbitrary integer \`z\` and \`0<=l<p\` the periodic primitive
\`\`\`text
G_l(z) = floor(z/2^(l+1))*2^l + max(0,(z mod 2^(l+1))-2^l),
\`\`\`
using mathematical floor and nonnegative remainder even when \`z<0\`. Differences \`G_l(w+L)-G_l(w)\` exactly count low-bit-one positions in an arbitrary translated integer interval.

For \`h>l\`, high-bit value \`u in {0,1}\`, shifted low-bit value \`v in {0,1}\`, define \`F_{h,l}^{u,v}(z;delta)\` as the number of \`0<=t<z\` with \`bit_h(t)=u\` and \`bit_l(t+delta)=v\`. Set
\`\`\`text
H=2^h, P=2H, q=floor(z/P), r=z mod P,
w=clamp(r-u*H,0,H), one=G_l(delta+w)-G_l(delta),
F = q*(H/2)+(one if v=1 else w-one).
\`\`\`
This is exact because the high-bit-selected half-period has length \`H\`, which is an integer multiple of \`2^(l+1)\` and hence contains exactly \`H/2\` low-bit-one positions. The remaining initial high-bit segment is counted using \`G_l\`.

With \`L=N-A\`, \`u=1[eps=-1]\`, \`v=1[eta=-1]\`, we have:
\`\`\`text
i>j: K_p(A,i,j,eps,eta)=F_{i,j}^{u,v}(L; A).
i<j: K_p(A,i,j,eps,eta)=F_{j,i}^{v,u}(N; -A)
                         - F_{j,i}^{v,u}(A; -A).
\`\`\`
For \`i=j=t\`, the previous \`j<i\` formula does not apply. Let \`H=2^t\`, \`P=2H\`, and \`r=A mod P\`. For any \`0<=z<=P\`, let
\`\`\`text
B_t^{u,v}(z;r)
 = sum_{m=0}^1 length( [uH,(u+1)H) intersect [0,z)
                      intersect [vH-r+mP,(v+1)H-r+mP) ).
K_p = floor(L/P)*B_t^{u,v}(P;r)+B_t^{u,v}(L mod P;r).
\`\`\`
The two modularly translated half-period intervals enumerate all possible shifted-bit regions within one period. These formulas use O(1) integer arithmetic per eligible identity, without scanning the \`2^p\` starting states.

## 3. Exact full p=32 result for a strict-19-bit observer

For \`p=32, a=321651, b=440665\`, there are \`(2^32-1)//a=13352\` possible positive first-port multiples \`k\`. A complete C++17 enumeration of all \`k,i,j,eps,eta\`, using the kernels above, and an independent Python enumeration that instead solves \`k*a == eps*2^i-eta*2^j (mod b)\` with the modular inverse of \`a\` modulo \`b\`, agree exactly:

| Mutually disjoint class | Labeled unordered collision pairs |
|---|---:|
| \`x<y, i>j, D>0\` — PREFIX-916 slice | 196,960,748,158 |
| \`x<y, i>j, D<=0\` | 7,516,192,768 |
| \`x<y, i<j\`, any \`D\` | 204,476,940,926 |
| \`x<y, i=j\`, any \`D\` | 13,416,271,437 |
| \`x=y, i<j\` — PREFIX-917 slice | 0 |
| **All distinct named two-flip collision pairs** | **422,370,153,289** |

Exactly **557** signed parameter identities yield positive witness mass. The first row recovers PREFIX-916's separately established \`196960748158\` **exactly**, an independent regression for that original narrower theorem. Thus the broader class adds \`225409405131\` actual labeled trajectory pairs at the same observer. These are not additional distinct modulus pairs; the observer was already certified as colliding.

The original global uniform pigeonhole capacity lower bound is zero at this \`(a,b)\` because \`a*b > 33*2^32\`, but named trajectory multiplicity is substantial.

## 4. Validation, code and scope

- \`PREFIX918_R6_COMPLETE_TWO_FLIP_MASS.cpp\`: C++17 exact integer checker, positive first-port multiple traversal, all \`i,j\` including equal, all four XOR signs and all signed terminal gaps. Uses 64-bit integer gaps and unsigned 128-bit mass accumulation.
- \`PREFIX918_R6_COMPLETE_TWO_FLIP_MASS_RESULTS.json\`: full class breakdown and testing counters.
- \`PREFIX918_R6_INDEPENDENT_RESIDUE_CHECK.py\` and its JSON: independent modular-inverse-first enumeration for the p=32 pair, with a separately written integer kernel; matches all five class counts and 557 positive parameter families.
- **38,324** exhaustive direct bit-kernel parameter comparisons: all \`2<=p<=7\`, all valid \`A,i,j\` and all four signs, every allowable starting state. Zero mismatches.
- **85** complete small-observer comparisons: all \`2<=p<=6\`, odd \`3<=a,b<=min(11,2^p-1)\`, direct brute-force all distinct unordered named trajectory pairs versus theorem 918-A. Zero mismatches.
- The p=32 census is algebraic/kernel based; no \`2^32\`-state explicit materialization or formal proof checker is claimed. This is author proof and exact finite computation, not independent mathematical review or source admission.

## 5. Next science / authority

The next useful question is distribution of \`T_p(a,b)\` over the strict 19-bit observer domain, especially minimal positive mass above the uniform capacity threshold. A separate direction is integrating zero-step-versus-flip collisions into a truly complete zero-or-one-flip trajectory count. Preserve source label multiplicity rather than collapsing to Boolean observation support.

All results remain in the auxiliary double-modulus representation. No primitive native 2-D plane, actual X6 triadic event, time update law, mathematical acceptance, shared CLAIM or formal Result is asserted.
