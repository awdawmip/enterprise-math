# PREFIX-995B — Sharp all-horizon distortion of erasing the terminal X6 port

Date: 2026-11-22 (+08).
Status: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_SPOT_CHECKED / NOT_REVIEWED.
Scientific input remains frozen at enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json.
Immediate theorem/proof: PREFIX-995, research_notes/portable_direct/2026-11-22_r6_prefix995_native_x6_positive_port_cone.md, immutable commit 660533de7ad0ee5e783d371c83b8c69c312a5d37.
Operation scope: actual source-defined Stage46 positive-grade outer boundary in native signed X6, normalized single initial directed incoming port; coherent port orthogonality and named-path ordering as proven in PREFIX-995. This is a constitutive BRC candidate rather than a physical heartbeat law.

## Theorem — exact terminal-port erasure factor and sharp worst case

For any positive-length n and six-component nonnegative displacement k with sum_i k_i=n, define

    N(k) = n! / product_i k_i!,
    E_n(k) = N(k)^2 / 36^n

as the **incorrect endpoint-only square** obtained after summing amplitudes belonging to different final incoming-port basis states before squaring.

PREFIX-995 proved the correct candidate Cell probability on this outer boundary is

    P_n(k) = sum_{j:k_j>0} N_j(k)^2 / 36^n,
    N_j(k) = (n-1)! / ((k_j-1)! product_{i!=j}k_i!).

The exact identities

    N_j(k) = (k_j/n) N(k)
    P_n(k) = E_n(k) * (sum_i k_i^2 / n^2)

hold for every n>=1. Define the observer-erasure distortion multiplier

    D_n(k) := E_n(k)/P_n(k) = n^2 / sum_i k_i^2.

Then 1 <= D_n(k) <= 6 for every n,k, with D=1 exactly when all steps follow one native positive axis. Write n=6q+r, 0<=r<6. The sharp worst-case multiplier at fixed n is

    D_n,max = n^2 / ((6-r)q^2 + r(q+1)^2),

attained exactly at the six-coordinate permutations of k having 6-r coordinates equal q and r coordinates equal q+1. For positive n divisible by 6, the maximum is exactly 6. For 1<=n<=6 the maximum is exactly n.

In particular, a reduction that erases the terminal directed-port label but then treats all endpoint amplitudes as coherent can overstate **this endpoint's** Stage46 candidate Cell probability by the sharp factor 6. The distortion is not an absolute model-error bound for unrelated observables.

*Proof.* Algebraically,
N_j(k)/N(k) = k_j/n for all k_j>0, and N_j=0 when k_j=0. Substitute into the exact port-orthogonal sum of squares. Since sum_i k_i=n and all k_i>=0, sum_i k_i^2 <= n^2, with equality exactly for one nonzero coordinate. Cauchy-Schwarz gives sum_i k_i^2 >= n^2/6. For the **sharp integer** minimum with fixed n, whenever some k_a >= k_b+2, replacing (k_a,k_b) by (k_a-1,k_b+1) reduces the sum of squares by 2(k_a-k_b-1)>0. Repeating forces all coordinates to differ by at most one, yielding 6-r entries q and r entries q+1 and minimum (6-r)q^2+r(q+1)^2. Equality, n<=6, and n divisible by 6 follow immediately. QED.

## Exact witnesses and validation

n=2, k=(1,1,0,0,0,0): correct P=1/648, wrong E=1/324, D=2.
n=3, k=(2,1,0,0,0,0): correct P=5/46656, wrong E=1/5184, D=9/5.
n=6, k=(1,1,1,1,1,1): D=6, establishing sharpness.
n=7, k=(2,1,1,1,1,1): D=49/9.
n=12, k=(2,2,2,2,2,2): D=6.

Independent exact integer enumeration checked the sharp lower sum-of-squares formula for all nondecreasing six-vectors of sum n for each 1<=n<=18, with no failures. This uses ordinary integer combinatorics **as a proof audit** of the existing typed Stage46 BRC observer, not a new BRC scientific update or native-to-physics calibration. The proof is valid for all n without reliance on the finite audit.

## Scope and continuation

This distortion law quantifies one precisely identified information-loss residual: failing to retain *joint endpoint and final directed port* when the actual observer sums orthogonal port probabilities. Keeping this BRC port/Cell joint relation repairs it with no extra spatial axis. The observation does not collapse signed/phase histories under arbitrary future Link/Port interactions.

Next: test whether a native occupancy/field coupling makes the safe positive-cone quotient history dependent, and derive an operation-safe state repair when it does. The mother objective B_fix,odd(32) in {19,20} is still open.
