# PREFIX-872 — First-port fiber capacity and exact collisions for the 32-source, 19-bit boundary

Date: 2026-11-17. Continuation: PREFIX-871 (Theorem A), PREFIX-870 (p=32 open).
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Research object and scope

This is the auxiliary named-binary-source BRC observer, not an asserted native X6/Cell/Link/Port evolution. A state is a named binary vector encoded without loss as an integer \(u\in[0,N)\), \(N=2^p\). A legal ordered transition \((u,v)\) either has \(v=u\), or toggles exactly one named bit: \(v=u\oplus2^i\), \(0\le i<p\). The fixed two-port observation is
\[
\Phi_{q_1,q_2}(u,v)=(u\bmod q_1,\ v\bmod q_2)
\]
for odd moduli \(q_1,q_2\). "Lossless" means injective on all legal ordered transitions, so old/new source state, changed name and direction are recoverable. We keep the full transition and its source identity; no compression of a joint observer is assumed safe without an injectivity proof.

## Theorem A — Conditional first-fiber capacity (all p and odd moduli)

Let \(g=\gcd(q_1,q_2)\). For a first-observation residue \(r\in\{0,\ldots,q_1-1\}\) and an increment residue \(a\in\mathbb{Z}/g\mathbb{Z}\), define
\[
T_{r,a}
=\#\{(u,v):0\le u,v<N,\ v=u\text{ or }v=u\oplus2^i,\ 
u\equiv r\pmod{q_1},\ v-u\equiv a\pmod g\}.
\]
Every lossless two-port observer necessarily obeys
\[
\boxed{\quad T_{r,a}\le \frac{q_2}{g}\quad
\text{for every }r\bmod q_1,\ a\bmod g.\quad}\tag{872.1}
\]

Proof. Fix \(r,a\). For each transition counted by \(T_{r,a}\), the first observed residue is \(r\) and the second residue \(s\) must satisfy \(s\equiv r+a\pmod g\). Exactly \(q_2/g\) residues \(s\in[0,q_2)\) have this class. If \(T_{r,a}>q_2/g\), two distinct legal transitions share the complete observation \((r,s)\). This contradicts injectivity. QED.

This condition is strictly more informative than the aggregate residue-class capacity of PREFIX-871. Indeed summing \(T_{r,a}\) over \(r\) yields
\[
\sum_r T_{r,a}
=N\left(\mathbf 1_{a=0}+\frac{n_a}{2}\right),
\]
where \(n_a\) counts signed named powers \(\pm2^i\equiv a\pmod g\). Summing (872.1) over \(r\) recovers precisely the prior inequality \(q_1q_2/g\ge N(\mathbf1_{a=0}+n_a/2)\). The converse need not hold: an aggregate capacity budget does not guarantee enough room inside each first-port observation fiber.

For a fixed \(r\), the quantity \(T_{r,a}\) can be computed exactly by iterating \(u=r+kq_1<N\), accounting for \(v=u\), and then accounting for \(v=u\oplus2^i\) for every named source bit \(i\). This is a finite calculation for the auxiliary observer, not a native heartbeat numerical evolution.

## The p=32, B=19 extremal cofactor family

Here \(N=2^{32}=4,294,967,296\), \(Q=2^{19}-1=524,287\). PREFIX-871's aggregate test (A2) left the following 23 possible gcds under that necessary condition alone:
\[
G=\{1,3,5,7,9,11,13,15,19,21,23,25,27,29,35,37,39,47,49,53,55,59,61\}.
\]
For each \(g\in G\), let \(A_g\) be the largest positive odd integer at most \(Q/g\) and take the two maximum-product distinct odd cofactor orientations:
\[
(q_1,q_2)=(gA_g,g(A_g-2))\quad\text{or}\quad
(g(A_g-2),gA_g).
\]
Both are within 19 bits and have gcd exactly \(g\). They are candidate modulus pairs, not automatically valid lossless observers.

### Exact finding 1: conditional capacity excludes five high-first pairs

For the first orientation \(q_1=gA_g\), \(q_2=g(A_g-2)\), the exact \(r=0\) first-port counts violate (872.1) for precisely the following five \(g\) among the 23:
\[
\boxed{\{15,21,27,35,39\}.}
\]
For example, \(g=15\) yields \(q_1=524265\), \(q_2=524235\). The first-port zero fiber contains 37,042 legal transitions in the signed-increment class \(a=11\), whereas that class has only \(q_2/g=34,949\) possible second-port residues. Thus the pair cannot encode all transitions, irrespective of decoder implementation. The reverse (lower-first) orientation does not violate the \(r=0\) class-capacity test for any of the 23 gcds; this is not a claim of its injectivity.

### Exact finding 2: all 46 extremal ordered pairs have explicit collisions

The direct collision search enumerates complete named legal transitions starting from old states \(u=kq_1\) for \(0\le k<3000\), recording the exact second residue \(v\bmod q_2\). For each of the 46 ordered pairs, it finds two distinct legal transitions with equal observations, and checks both legality and equality of both residues. The largest first-witness index is \(k=2366\).

An illustrative collision for \(g=1\), \((q_1,q_2)=(524287,524285)\) is
\[
(0,2)\ne(524287,524287),\qquad
\Phi(0,2)=\Phi(524287,524287)=(0,2).
\]
The first transition toggles source bit index 1; the second is a no-change event. Hence the failure concerns full transition recovery, not merely a mistaken sign or capacity estimate.

The machine-readable certificate records both old/new ordered pairs for all 46 counterexamples, as well as each \(T_{0,a}\) maximum, its \(q_2/g\) capacity and the orientation.

## Verification, mathematical strength, and provenance

- Executable exact-integer checker: PREFIX872_R6_FIRST_FIBER_CHECK.py. It fully enumerates \(r=0\) first fibers for all 46 selected pairs, with 32 named flips plus no-change for every old state.
- Result certificate: PREFIX872_R6_FIRST_FIBER_RESULTS.json, 46 ordered pairs and witnesses, verification EXACT_INTEGER_ASSERTIONS_PASSED.
- Python arbitrary-precision integer arithmetic checks XOR, modular classes, counts and inequalities. An independently written JavaScript exact-integer implementation reproduced the same 46 pairs, five capacity failures, and maximum witness index 2366 while assembling the published result.
- Theorem A's proof is independent of finite checks. Counterexamples certify failure of these 46 explicit pairs only. They do not exclude all 19-bit pairs with the 23 gcds and do not resolve the global \(B_{\mathrm{fix,odd}}(32)\in\{19,20\}\) boundary.
- This auxiliary mathematical result does not claim native X6/Cell/Link/Port event fidelity or BRC physical-residual attribution. P000 and ACTIVE worldview remain unchanged.

## Durable frontier and next discriminating questions

1. Extend conditional tests from \(r=0\) to an efficiently computable family of \(r\)-fibers. Determine whether stronger inequalities can exclude whole gcd families under the 19-bit cap rather than only extremal modulus choices.
2. For surviving modulus pairs, derive a parametric CRT/bit-pattern collision criterion to test individual signed-source events without enumerating all \(2^{32}\) old states. Seek either a 19-bit lossless construction or a complete no-go.
3. Apply the same fiber theorem to the coprime \(g=1\), \(p=62\), 34-bit unresolved case, preserving necessary capacity, explicit collisions and full global exclusions as different claims.

This is independent auxiliary BRC observer research; no RS-X6-NATIVE-TIME-DYNAMICS CLAIM is asserted.
