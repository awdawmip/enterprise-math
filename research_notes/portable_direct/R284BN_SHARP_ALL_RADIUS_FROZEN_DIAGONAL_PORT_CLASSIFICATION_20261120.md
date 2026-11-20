# R284BN — Sharp frozen-diagonal classification for every finite circular-noise radius

Date: 2026-11-20 (Asia/Shanghai). Mathematical status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED.

Scientific lineage: R284BM at immutable pin awdawmip/enterprise-math@35206e6ee5129b923ad2677cdeaaac9fda370d11:research_notes/portable_direct/R284BM_FROZEN_DIAGONAL_MODULAR_PORT_EXACT_CLASSIFICATION_20261120.md, itself continuing R284BJ. These statements concern an auxiliary algebraic star-Port observer and leave P000, Heartbeat World X6, shared Task ownership, and prior scientific pins unchanged.

## Exact model and theorem

For the 512 unknown matrices C in {1,2}^{3×3}, define

\[
F_C(d,z)=\det(\operatorname{diag}(d_0,d_1,d_2)-C-z_1E_{01}-z_2E_{02}).
\]

Fix a prescribed *integer* diagonal setting d_j=t, for j=0,1,2. Choose the other two diagonal controls and the two named directed star controls once, uniformly for every C, over a freely chosen prime field F_p. The single observation is the residue F_C mod p, corrupted by an adversarial *real circular error* of radius \(\rho\ge0\) on the circle of circumference p. Successful uniform decoding means all 512 closed circular error balls are disjoint.

**Theorem BN1 (sharp all-radius classification).** Put \(m=\lfloor2\rho\rfloor\), for any finite real \(\rho\ge0\). A prime p and one fixed four-control setting exist that guarantee recovery of every candidate under every allowed error **if and only if**

\[
\boxed{\begin{aligned}
j=0 &: \quad t\notin\{-1,0,1,2,3,4\},\\
j\in\{1,2\} &: \quad t\notin\mathbb Z\cap[-m-3,\ \max\{4,m+1\}].
\end{aligned}}
\]

Thus the root forbidden set is independent of the finite noise radius; each leaf's forbidden interval expands with radius. For integer error \(|e|\le\delta\), take \(m=2\delta\). At \(\delta=3\) this gives exactly R284BM's root values -1 through 4 and leaf values -9 through 7. The smallest nonnegative allowable integer is 5 for the root and \(\max(5,m+2)\) for a leaf. This is an existence classification, not a claim of optimal prime size or efficient parameter search.

## Proof

### 1. Exhaustive, integer-unbounded polynomial criterion

For distinct C,C', let \(Q=F_C-F_{C'}\). Once d_j=t is fixed, the four free controls form a vector \(x\). The polynomial Q is separately affine in every coordinate of x and affine in t. Its sixteen Boolean corner evaluations on \(x\in\{0,1\}^4\) determine every coefficient by Boolean Möbius inversion.

For the kth corner write its difference as \(u_k+t v_k\), with u obtained from d_j=0 and v from the difference d_j=1 minus d_j=0. The specialized polynomial is a constant c precisely if

\[
(u_k-u_0)+t(v_k-v_0)=0\quad(k=1,\ldots,15),\qquad c=u_0+t v_0.
\]

For each of 130,816 unordered pairs, the exact checker solves the equations for *every integer t*: if all relative slopes vanish, it either rejects or records the universal affine constant \(a+bt\). Otherwise one nonzero relative slope determines a single rational t; an integral t is retained only after all fifteen equalities are independently checked. This uses exact integers and fractions, without searching a bounded range of freeze values.

### 2. Full finite classification

The standard-library checker enumerates all 512 candidates and all 130,816 unordered pairs for each index, using 16 Boolean corners at frozen values 0 and 1. Its computed exact summaries (all checked by assertions) are:

| Frozen index | Universally constant pairs | Universal affine forms | Isolated-in-t constant pairs | Isolated integer t |
|---|---:|---:|---:|---|
| root j=0 | 0 | none | 304 | -1,0,1,2,3,4; each constant is 0 |
| leaf j=1 | 256 | 10 | 1,824 | -1,0,1,2,3,4 |
| leaf j=2 | 256 | 10 | 1,824 | -1,0,1,2,3,4 |

For either leaf, the **complete** universal-form list is

\[
\{-3+2t,-2+2t,-1+t,-1+2t,t,2t,1+t,2+t,2+2t,3+t\}.
\]

Five forms are \(t+a\) for each \(a\in\{-1,0,1,2,3\}\). For integer \(m\ge0\), a control-independent difference of absolute value at most m exists among them exactly at

\[
-m-3\le t\le m+1.
\]

All remaining slope-two forms \(a+2t\) have any integer solution of \(|a+2t|\le m\) inside the same interval (their offsets a are between -3 and 2). All isolated constant responses occur only for t=-1,...,4, with at least one *zero* difference at each such t. Thus the leaf obstruction set is exactly

\[
([-m-3,m+1]\cup[-1,4])\cap\mathbb Z
=[-m-3,\max(4,m+1)]\cap\mathbb Z.
\]

At the root no pair has a universal constant difference, and the complete isolated set is precisely the six values -1,...,4, each giving equality. This establishes the necessity classification independently of the magnitude of m once the finite integer-pair classification has been certified.

### 3. Impossibility at every excluded value

At a forbidden integer t, distinct candidate matrices have a control-independent integer difference c with \(|c|\le m=\lfloor2\rho\rfloor\). For every choice of prime and every free-control setting, their circular centers are within distance \(2\rho\), hence their *closed* circular radius-\(\rho\) error balls intersect. A single observation cannot guarantee recovery. The root has c=0 witnesses even at zero noise.

### 4. Existence at every permitted value

Fix an allowed integer t. For each distinct pair and each integer \(c\in[-m,m]\), the polynomial \(Q(t,x)-c\) is nonzero over \(\mathbb Z[x]\) by the classification. Select a prime p larger than the absolute values of all nonzero coefficients of all these finitely many polynomials and satisfying

\[
p>8(2m+1)\binom{512}{2}.
\]

Every difference-minus-c polynomial remains nonzero over \(\mathbb F_p\). Its total degree in x is at most two because the unique degree-three term \(d_0d_1d_2\), which is independent of C, cancels between candidates; every star term is also at most quadratic. Schwartz–Zippel gives failure probability at most \(2/p\) for each equality \(Q(t,x)=c\pmod p\), when all four free controls are independent uniform field elements.

A union bound gives failure probability at most

\[
\frac{2(2m+1)\binom{512}{2}}p<\tfrac14.
\]

A setting exists that avoids all the prohibited circular integer differences. Hence every pairwise circular distance is at least \(m+1>2\rho\); the 512 closed noise balls are disjoint and nearest-center recovery succeeds. This completes BN1.

## Hand-check witnesses and reproducible evidence

For leaf j=1, each of the following pairs has exact polynomial difference \(F_C-F_{C'}=d_1+a\), for any other four controls. Each 9-digit word represents the row-major entries of one candidate matrix.

| a | C | C' |
|---:|---|---|
| -1 | 111121111 | 112121111 |
| 0 | 111111111 | 112111111 |
| 1 | 111111121 | 112111121 |
| 2 | 111221121 | 112221121 |
| 3 | 111211121 | 112211121 |

The additional leaf j=1 zero-difference obstructions for t=2,3,4 have witnesses (C,C') respectively (111111121,111111212), (111121121,111121212), and (111222121,111222212). Exchanging the named two leaves gives j=2 witnesses. The six root zero-difference pairs are included in the JSON checker output and can be inspected without dependence on this narrative.

Reproduce using Python standard library:

    python3 R284BN_noise_radius_diagonal_checker.py > out.json

Compare out.json byte-for-byte with R284BN_noise_radius_exact_verification.json. The executable checks exact counts and the complete list of universal forms, verifies every possible integer frozen t via rational equation solving, and separately compares predicted and computed forbidden sets for m=0,...,30. Additional independent off-Boolean witness tests, including negative free controls, checked 126 determinant identities. The resulting finite classification plus the general algebraic/field argument proves BN1 for all finite radii.

Scope: integer t, positive *binary* 3x3 matrices, named directed star-Port modular observation and real circular error, arbitrary selected prime. The result is not a statement about arbitrary positive rational matrices, infinite noise, native X6 coordinates or direct physical observability. Independent mathematical review remains NOT_REVIEWED.

## Next questions

- Find a conceptual orbit/symmetry proof of the ten universal leaf forms and six isolated root exceptions, replacing exhaustive pair classification.
- Determine sharp all-radius frozen-control bounds for alphabets H>=3 and n>=4, with exact input and output resource accounting.
- Construct small-prime, low-memory, efficiently decodable control settings approaching the circular packing lower bound.

Research Activity history: EM-DIRECT-E6B1DD / RA-DD7D715E42D8874661313886 is preserved as provenance. No CLAIM, Result, Review or native owner authorization is conferred by this source publication.
