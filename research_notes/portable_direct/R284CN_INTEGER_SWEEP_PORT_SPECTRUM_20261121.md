# R284CN — Exact integer-event sweep and 54th-level Port residual gap

**2026-11-21 · Author proof with exact finite certificate · Independent review: NOT_REVIEWED.**

## Scope, source and frozen input

This theorem concerns the frozen *auxiliary 34-bit Port observer* from R284CL–R284CM. The Port circular coordinate is a partial typed readout, not an X6 primitive spatial axis, full native Cell state, or BRC branch-state substitute.

- Modulus: \(P=17\,179\,869\,143\).
- Frozen coefficient vectors: \(D=(1120832,6,13,1651128)\), \(Z=(0,390139,394465,1497639)\).
- Fixed six-coordinate selector: \((0,1,2,4,5,6)\).
- Population \(X\): all 65,536 distinct residues from the exact frozen 4-by-4 two-valued matrix generator. Frozen binary-encoding SHA-256: **b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4**.
- Fibers: 64 labeled circular integer arcs \(A_j=[a_j,a_j+w_j]\pmod P\), with R284CL endpoints and \(307592214\le w_j\le450181375\).

For \(x\in\{0,\ldots,P-1\}\) and integer \(r\ge0\), define
\[
N_r(x)=\sum_{j=0}^{63}{\bf1}\{\operatorname{dist}_{\rm circle}(x,A_j)\le r\},\quad
g(r)=\min_{x\in X}N_r(x),\quad
U_k=\min\{r\ge0:g(r)\ge k\}.
\]
The quantity \(U_k\) is the exact integer-observation radius needed to guarantee \(k\)-fold coverage of **all actual codewords**, and differs from the all-real-circle covering radius in R284CK.

## Theorem 1: exact integer interval sweep, without pairwise critical sites

For a frozen arc \(A=[a,a+w]\pmod P\) and an integer \(r\ge0\), its radius-\(r\) coverage set on **integer residues** is:

- The entire \(\mathbb Z/P\mathbb Z\), when \(w+2r\ge P-1\).
- Otherwise, precisely the cyclic inclusive interval from \(a-r\) to \(a+w+r\) modulo \(P\).

Split the second case at the residue cut if it wraps. Represent each ordinary inclusive integer interval \([L,R]\subset[0,P-1]\) with a difference event \(+1\) at \(L\) and \(-1\) at \(R+1\). Add 0 and \(P\) as event sentinels and a permanent base count for globally covered arcs. The prefix count is then *exactly* \(N_r(y)\) for every integer \(y\) in the band between successive event coordinates.

Sort the finite population \(X\) once. For each such band, one lower-bound binary search determines whether the band contains any \(x\in X\). The minimum event count among occupied bands is exactly \(g(r)\). This uses at most a constant multiple of 64 arc endpoints, with no point-to-arc distance evaluations in the sweep.

**Proof.** The circle distance from an integer \(y\) to a closed circular arc is at most \(r\) if and only if \(y\) lies within that arc's circular Minkowski expansion by \(r\). For \(w+2r<P-1\), the expansion is a single proper cyclic interval with the displayed inclusive integer endpoints. For \(w+2r\ge P-1\), at most a real gap of length one remains, and no integer residue is omitted. Difference-array events compute exactly the sum of the arc-indicator functions, preserving multiple overlapping labeled fibers. No indicator changes between successive event coordinates. Binary search checks whether that band contains any element of \(X\); taking the minimum of its exact count over the occupied bands proves the claim. \(\square\)

**Corollary: exact 64-level spectrum.** The function \(g(r)\) is nondecreasing. At \(r=(P-1)/2\), \(g(r)=64\), since each integer residue is within that radius of every nonempty arc. Lower-bound integer binary search for each \(k=1,\ldots,64\) therefore returns the exact \(U_k\). The search requires no pairwise arc-distance crossing calculation or R284CM's 4,149 critical coordinates and 6,007 candidate codewords.

With \(m=|X|\) and \(n=64\), the preprocessing is sorting \(m\) codewords; the 64 bisections cost \(O(64\log P\,[n\log n+n\log m])\) event sorting and occupied-band lookups in the unit-cost integer model. This is **not** a statement that codeword generation, sorting, integer arithmetic or RAM allocations are free.

## Theorem 2: an exact two-radius certificate for level 54

An exhaustive **integer-event** sweep yields the complete bad-residue intervals:

| Integer radius \(r\) | All integer residues with \(N_r(y)<54\) | Their coverage |
|---|---|---:|
| 7,642,302,203 | [6,683,583,072, 6,683,583,858] | 53 |
| 7,642,302,204 | [6,683,583,073, 6,683,583,857] | 53 |

The two successive frozen codewords bracketing the real-circle apex 6,683,583,465 are 6,683,583,072 and 6,683,702,379. The latter is beyond both bad intervals. Therefore **no codeword belongs to the bad interval at radius 7,642,302,204**, whereas codeword 6,683,583,072 lies in the bad interval at the immediately preceding integer radius. By monotonicity,
\[
\boxed{U_{54}=7\,642\,302\,204.}
\]
These two intervals and their actual codeword bracket constitute an independent *finite-population threshold certificate*, without evaluating 4,194,304 individual distances during the threshold computation.

The pinned R284CK all-real-circle result gives \(T_{54}=15\,284\,605\,194\) in doubled-radius units, with continuous apex 6,683,583,465 and radius \(T_{54}/2=7\,642\,302\,597\). Consequently,
\[
\boxed{T_{54}-2U_{54}
=15\,284\,605\,194-15\,284\,604\,408=786.}
\]
Thus the previously observed **786 doubled-radius units** are explained by the discrete sampling hole around that continuous peak: its closest left codeword is exactly 393 coordinate units away. The integer membership result above supplies both the upper-bound coverage certificate and the adjacent-radius sharpness witness.

## Exact checker and verification

The new self-contained-algorithm checker imports the previously published frozen R284CL generator, verifies its SHA-256, generates and sorts all 65,536 codewords, computes the complete vector of 64 values by **1,772 distinct memoized integer-radius event sweeps**, and checks \(g(U_k)\ge k\) and, for every positive \(U_k\), \(g(U_k-1)<k\).

The complete 64-value vector matches the independently established R284CM spectrum, including \(U_1=0\), \(U_8=1\,236\,647\,378\), \(U_{32}=4\,633\,230\,194\), \(U_{54}=7\,642\,302\,204\), and \(U_{64}=8\,436\,072\,374\). The optional full validation also runs 65,536 × 64 = **4,194,304** exact distance calculations and asserts all 64 radii match. It passed locally.

In one local CPython run, generating and sorting the frozen codewords took 0.169704 s; the complete event sweep and 64 bisections took 0.148424 s; the separate exhaustive distance baseline (after generation) took 0.900870 s. These are reproducibility observations on one runtime, not independent hardware performance guarantees.

Reproduction from the research_notes/portable_direct folder containing the published frozen R284CL checker:

    python R284CN_integer_sweep_spectrum_checker.py --full --output R284CN_integer_sweep_spectrum_certificate.json

Verification evidence: **R284CN_integer_sweep_spectrum_certificate.json**. Code: **R284CN_integer_sweep_spectrum_checker.py**. The JSON provides the full 64-entry vector, runtime observations, integer bad-band witnesses and input pins.

## Interpretation, provenance and next question

The method retains the multiplicity and identity of all 64 residual-fiber arcs while avoiding pairwise critical-site enumeration. It is an exact auxiliary observer calculation within the user's ACTIVE residual-faithful discrete worldview and P000; no statement about replacing the six native X6 axes, triadic primitive balance, BRC path provenance or physical native equivalence is made.

Historical Port attribution: **EM-DIRECT-20B766** and Activity **RA-617F40704F37299B15489DCA**. Those public historical labels do not authenticate the current turn's private native capability. The scientific files can be published independently; the Activity checkpoint remains a separate authorized Source/CAS operation and the result remains **NOT_REVIEWED**.

Next: produce all-level witnesses directly from event bands, reduce the 1,772 radius queries by a shared parametric sweep, and compare repeated-query costs against the 100-byte and 760-byte precompiled residual-fiber indexes of R284CI/R284CJ.
