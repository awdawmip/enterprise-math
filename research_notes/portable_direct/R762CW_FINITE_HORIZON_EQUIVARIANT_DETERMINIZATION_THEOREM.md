# R762CW — Exact deterministic-memory costs of the mixed-sign X6 minority-Port BRC

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, immutable publication TP2-8B7E13C5904A2D6F1142.
Date: 2026-11-17. Predecessor: R762CVb at PR #2623, commit e8fefcad3c297156a4bc64a8c21bd4d79826078f.
Frozen scientific assumptions: P000 V5 at enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Status: complete algebraic proofs and exact author checks; independent review NOT_REVIEWED.

## Observer and exact model

In the signed X6 three-Port *candidate* model of R762CVb there are 20 supports and two mixed sign-count types, hence 40 independent sectors. On each sector the unique minority-sign Port can occupy one of three named axes a,b,c. A transition relocates the minority to either other axis with multiplicity one. Its positive N-BRC matrix is A=J3−I3; its normalized kernel is P=A/2. For every integer t≥0:

\[
(A^t)_{ii}=\frac{2^t+2(-1)^t}{3},\qquad
(A^t)_{ij}=\frac{2^t-(-1)^t}{3}\quad(i\neq j).
\]

The future observer is the *named terminal minority Port*. Hidden flags or path tapes are provenance state, never new spatial axes. We study deterministic presentations with no fresh random/branch input after initialization.

## Theorem A: exactly four equivariant bijective two-sheet one-step lifts

For a support S and sign-count k∈{1,2}, represent a hidden flag as (S,k,a,b) where a is the unique minority-sign Port and b is one distinguished majority-sign Port. Let c be the third axis of S. There are exactly 240 flags in the 120-base-state two-sheet covering. Let the S6 action relabel occupied axes and unused axes, and let global sign reversal replace k by 3−k, keeping a,b.

Subject to preserving support and k, changing the minority Port, S6 equivariance and global sign-reversal covariance, exactly four deterministic flag maps exist:

| Map | (a,b) maps to | Order |
|---|---|---:|
| F_ba | (b,a) | 2 |
| F_bc | (b,c) | 3 |
| F_ca | (c,a) | 3 |
| F_cb | (c,b) | 2 |

Every one is a bijection. For any base a, its two hidden flags yield exactly the two distinct allowed successors b,c on one step, and 2 is the minimal hidden-fiber cardinality for this source-resolved one-step property.

Proof. The occupied-axis S3 acts freely and transitively on six ordered distinct flags (a,b) in each support/sign-count orbit. The stabilizer of a flag permutes only the three unused axes. An S6-equivariant output flag on the same support is therefore determined by the output of one reference flag. Requiring a change of minority restricts the first output coordinate to b or c, with two choices for the second coordinate in either case, giving four maps. Transitivity makes each a bijection. Sign reversal couples k=1 and k=2, yielding exactly four global maps. Direct composition gives the stated orders. A one-element fiber cannot project to two distinct successors. ∎

Each of the four maps reproduces one-step branching after uniformly averaging over the two flags. Its two-step endpoint distribution differs from P²: its return probability is 1 for period-two maps and 0 for period-three maps, whereas P²(i,i)=1/2. One-step deterministic lifts are therefore not complete future BRC state presentations.

## Theorem B: exact h-bit hidden-memory lower bound, attained

Fix h≥0 and an initial named minority position i. Consider any deterministic evolution whose M possible hidden *initial* states over i are equiprobable. If its projected endpoint distributions at all integer times 0≤t≤h equal P^t(i,·), then 2^h divides M, and the sharp minimum is

\[
\boxed{M_{\min}(h)=2^h,\qquad \text{minimal fixed-length initial memory}=h\text{ bits}.}
\]

This bound already follows when only the distribution at t=h must match.

Proof of lower bound. For j≠i and h≥1 the target probability is

\[
P^h(i,j)=\frac{2^h-(-1)^h}{3\cdot 2^h}.
\]

The integer (2^h−(−1)^h)/3 is odd. Hence the reduced denominator is exactly 2^h. Any image of M equiprobable deterministic initial atoms assigns each target an integer multiple of 1/M. Thus 2^h divides M. At h=0 the bound is one atom.

Construction. Initialize one hidden atom for every legal length-h path word (i=a_0,a_1,...,a_h), where consecutive positions differ. Exactly 2^h words exist. At each subsequent typed time step shift the next Port into the visible position; the stored tail and clock position specify the deterministic step through h. Relabeling axes acts componentwise on the tape, proving S6 and sign-reversal covariance. For each t≤h each length-t path has exactly 2^{h−t} extensions. Therefore the projected proportion of tapes ending at j is 2^{h−t}(A^t)_{ij}/2^h=P^t(i,j). ∎

The construction realizes finite-horizon endpoint and path-word statistics with time-layered finite provenance. It is not an autonomous unbounded-time random process.

## Theorem C: no finite autonomous deterministic all-time representation

Let X be any finite hidden state set, F:X→X a deterministic *time-homogeneous* map, π:X→{a,b,c} a named-Port observer and μ_i an arbitrary fixed probability measure on π^{-1}(i), even one with irrational weights or without equivariance. Then

\[
\pi_* F^t_* \mu_i = P^t(i,\cdot)\quad\text{for every }t\ge0
\]

is impossible.

Proof. Every deterministic orbit of a map on a finite set is eventually periodic. Taking the maximum transient and a common multiple of all periods gives N,p>0 with F^{t+p}=F^t for t≥N on the entire set; therefore its projected probability distribution is eventually periodic. But for j≠i, P^t(i,j)=(1−(−1/2)^t)/3 takes pairwise distinct values for distinct nonnegative t, and so is not eventually periodic. Contradiction. ∎

## Verification, epistemic scope, and next test

The standard-library checker enumerates 20 supports, 240 flags, all 720 axis permutations and four allowed lifts: 691,200 exact S6 covariance equations, 960 sign-flip equations, all permutation cycle periods, and the two successor images in every fiber. It separately enumerates 2^h candidate branch words for each h=0,...,12 and compares all 39 endpoint counts to the exact integer formulas. General h and all-time conclusions follow from the proofs.

The result makes the information cost of hiding *repeated positive branching* exact even for the coarse named-terminal-Port observer. It does not assume that the candidate K3 kernel is a licensed physical or native TRIADIC_CLOSURE_E update. The next native-law step is to establish the actual signed Cell/Link/Port legality predicate and V17/V29/V39 transport and then determine whether its future observation carries this branching or requires additional 15-pair area/source residuals (R762CH/CK).

Reproduction: run python3 R762CW_VERIFY.py with Python standard library; compare generated JSON with R762CW_EVIDENCE.json. Project admission and independent review: NOT_REVIEWED.
