# R284BB — A sharp dimension transition for adversarial-noise-resilient single-scalar star-Port observation

Date: 2026-11-19. Lineage: R284AT, R284AX, R284AZ, R284BA. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.

**Scientific scope.** This is the auxiliary, named directed-Port determinant observer inherited from the frozen source line; it is not a native heartbeat dynamic, an X6 geometrical statement, or a physical instrument calibration. All native P000 and residual-fidelity premises are unchanged. Exact integer arithmetic is used for this auxiliary polynomial theorem.

## The observation model

Fix integers n >= 2, H >= 2 and a known adversarial absolute-error bound 0 <= delta < infinity. Unknown C lies in {1,...,H}^{n x n}, every entry strictly positive. Choose integer diagonal controls d_0,...,d_{n-1} and simultaneous directed row-zero star controls z_1,...,z_{n-1}. The noiseless readout is

P_C(d,z) = det(diag(d_0,...,d_{n-1}) - C - sum_{i=1}^{n-1} z_i E_{0i}).

One observation reports y = P_C(d,z) + epsilon with |epsilon| <= delta. All controls are selected nonadaptively; one scalar is returned. The magnitude of controls is unrestricted but their bit length is accounted for below.

## BB1. Nonconstant coefficient completeness (n >= 3)

Let [d_T] P denote the coefficient of the product of d_j over j in T; [z_i d_T] similarly. For any distinct i,j with i,j >= 1,

(1) [d_{[n]\{i}}] P = -C_ii, and this also holds for i=0.

(2) [d_{[n]\{i,j}}] P = C_ii C_jj - C_ij C_ji, for all i != j, including pairs containing 0.

(3) [z_i d_{[n]\{0,i}}] P = -C_i0.

(4) [z_i d_{[n]\{0,i,j}}] P = C_i0 C_jj - C_ij C_j0.

These follow by choosing the indicated diagonal entries in the determinant expansion and restricting the remaining determinant to the named 1-, 2-, or 3-index principal block with the indicated edited entry. Formula (4) includes the case n=3, where the d-product is empty.

For n >= 3, every monomial displayed in (1)-(4) is nonconstant in the combined control variables (d,z). From (1) recover all C_ii. From (2) recover all pair products C_ij C_ji. From (3) recover each C_i0 > 0; hence C_0i is obtained by division of the known pair product. Finally (4) gives

C_ij = (C_i0 C_jj - [z_i d_{[n]\{0,i,j}}] P) / C_j0, for all distinct i,j >= 1.

Strict positivity makes these divisions legal. Thus **the nonconstant coefficients of P_C determine every entry of C, for every n >= 3**. In particular, for distinct matrices C,C', the integer polynomial Q=P_C-P_C' is nonconstant.

For n=2 the pair-minor coefficient is constant, so this last conclusion fails. R284BA gives the explicit pair [[1,1],[1,1]] and [[1,2],[1,1]], whose complete two-Port response polynomials differ by the constant 1, for every diagonal and allowed star control.

## BB2. Arbitrarily large finite adversarial noise is correctable with one scalar if n >= 3

**Theorem.** For each n >= 3, finite H >= 2, and finite delta >= 0, there exists a *single fixed* integer control choice (d,z), common to every candidate, for which all H^(n^2) exact outputs are separated by more than 2 delta. Therefore a single adversarial-noisy read guarantees exact recovery by finite candidate matching. For n=2 and H>=2, a finite observation protocol can guarantee recovery exactly when delta < 1/2 (using the original R284BA result).

**Deterministic construction.** There are m=2n-1 control variables, and P_C is integer and multi-affine in them. Set

L = n! 2^n H^n,
B = max(4L+4, ceil(4 delta)+4).

The absolute value of each coefficient of P_C is at most L, by the Leibniz expansion (at most n! permutations and 2^n binary entry expansions per term). Enumerate the variables in the order d_0,...,d_{n-1},z_1,...,z_{n-1}, and set the j-th variable to B^(2^j), j=0,...,m-1. Each squarefree monomial now occupies a unique base-B exponent. For Q=P_C-P_C', its highest nonzero base exponent e is at least 1, by BB1. The coefficient of that exponent has absolute value >=1 and every lower coefficient has absolute value <=2L. Consequently

|Q(d,z)| >= B^e - 2L (B^e - 1)/(B-1) > B^e/2 >= B/2 > 2 delta.

This is an explicit, fully deterministic, single-reading construction, with exponential-in-n control bit length O(4^n (n log(H+1) + n log n + log(1+delta))).

**Probabilistic low-bit construction.** Put N=H^(n^2), J=binom(N,2), K=4nJ, and let X have m independent uniform integer coordinates from {0,...,K}. For each distinct C,C' write Q=P_C-P_C'; let r be its positive maximal total degree, and Q_r its nonzero homogeneous leading part. Since r<=n, the elementary polynomial-zero bound (Schwartz-Zippel over this finite integer grid) gives Pr[Q_r(X)=0] <= n/(K+1). A union bound over J pairs yields

Pr[Q_r(X) != 0 for every pair] >= 1 - n J/(K+1) > 3/4.

Let A=2^(2n) L K^n, and fix the integer scaling factor

t = max(2A+2, ceil(4 delta)+2).

Each coefficient q_s(X) in Q(tX)=sum_s t^s q_s(X) is an integer of absolute value <=A; by the successful event its leading coefficient q_r(X) is a nonzero integer. Hence

|Q(tX)| >= t^r - A (t^r-1)/(t-1) > t^r/2 >= t/2 > 2 delta.

Thus independently randomized X, then the fixed scaling t, gives a one-scalar observer with simultaneous pairwise separation greater than 2delta with probability >3/4. The setting can also be found by finite exhaustive search and verified against all candidates before use.

For this construction, each individual control has O(n^3 log(H+1) + n log n + log(1+delta)) bits; the scalar output has O(n^4 log(H+1) + n^2 log n + n log(1+delta)) bits. Candidate-table construction, collision checking and decoding may take time exponential in n^2 log H. These are setting/readout **bit bounds**, not a polynomial-time decoder claim.

**Sharp dimension distinction.** Under the declared simultaneous star interface and unbounded finite control range, n=2 has an adversarial-noise threshold delta=1/2, while every n>=3 tolerates any prescribed finite delta with a one-scalar fixed setting. The resource cost changes with delta. The statement does not assert a bounded-dynamic-range instrument has the same property.

## Exact finite verification

The companion Python 3 standard-library checker exhaustively enumerates all 2^9=512 positive 3x3 integer matrices with H=2. It verifies the determinant/coefficient identity at five values of t for each matrix (2560 exact tests). With fixed RNG seed 28417 it obtains X=(7340,6572,5070,7899,352). At t=100 all 512 exact scalar outputs are distinct; the minimum adjacent sorted output gap is exactly 14595, so every bounded adversarial error delta < 7297.5 is correctable by nearest-candidate matching. A demonstration at delta=7000 is therefore covered. Largest control value is 789900. A separate deterministic base-B instance at delta=7000 has B=28004, 512 distinct outputs, minimum gap 784224015, largest control 237 bits and largest output 267 bits. Integer results are reproducible without numerical tolerance.

The finite checks demonstrate the stated finite fixture. The general theorems follow from BB1 and the algebraic separation arguments, not from finite enumeration. Independent mathematical review: NOT_REVIEWED.

## Research continuation

1. Tighten the necessary and sufficient maximum-control amplitude K for n>=3, fixed H and delta; distinguish worst-case, random-choice and explicit constructions.
2. Determine whether polynomial-time reconstruction is possible without enumerating H^(n^2) candidate matrices and whether adaptive, lower-bit multi-read methods improve the Pareto frontier.
3. Preserve named directions, star control constraints, exact noise model, and source lineage when comparing to BRC/Enterprise observers; any native transfer requires an explicit typed embedding and observation-preservation proof.
