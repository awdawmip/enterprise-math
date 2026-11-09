# PREFIX-627 — Sharp online finite-lag provenance memory in native X6-BRC

Date: 2026-11-09 (Asia/Shanghai). Evidence: AUTHOR-SIDE EXACT MATHEMATICS, independent Driver review pending.
Task: RS-X6-NATIVE-ROTATION-DYNAMICS.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Exact dependency: PREFIX-626 at 07de77571c6dca23f6e4858464d9514f6aaf10db, research_notes/portable_direct/2026-11-09_prefix626_sharp_tagged_history_reads_four_point_probe.md.

## Statement, original observer, domain

Use the original 48 STAR phases, 96 ports, 576 labelled positive BRC actions, and the four-point native probe d=e4+e11+e14+e32. Let λ>0, g_1,...,g_n≥0, and r_n=A(g_n)...A(g_1)E(λd). The observer receives the entire 96-port endpoint r_n plus an online-updated bank of m continuous real scalar registers. Registers are separate from the endpoint. Fix an integer lag L with 1≤L≤n−4 (equivalently n≥L+4).

The requested original fully source/action-labelled length-n path coordinates are J_n[W(n,k)] for k=n−L+1,...,n. The W(n,k) are precisely the PREFIX-626 original native positive paths: a weight-one seed-to-port-9 prefix, original gated edge 9→29 at step k, then the original weight-one 29→80→52→8→29 cycle. The exact original native identity is

  J_n[W(n,k)] = λ g_k, for every k≤n, including g_k=0.

THEOREM: for every fixed L≥1 and every n≥L+4,

  m_online(n,L) = L−1

additional continuous real scalar registers are necessary and sufficient to reconstruct all L requested original labelled path masses from the current full 96-port endpoint. One algorithm supports every permitted horizon without knowing n in advance. Fixed L therefore yields constant additional scalar-register storage for arbitrarily long input streams. At L=n−4 the result specializes to PREFIX-626's sharp n−5 full-history deficit.

## Native constructive online algorithm

From PREFIX-626's exact original endpoint decoder, for n≥2 define v_i=r_n[2i]+r_n[2i+1] except v_4=r_n[8]=r_n[9]. Let δ=r_n[29]−r_n[28] and ℓ=v_3+v_14+v_15−2v_2. On the original reachable four-point probe family ℓ>0 and ℓ−3δ>0, and

  g_n=(ℓ+9δ)/(ℓ−3δ).

For t=n−2 and p=(2,28,38,16), a pure phase row gives

  λ=v_{p[(t+2) mod 4]}/(4·2^t).

Initialize r_0=E(λd) and an empty ring of capacity L−1. Apply the actual native r_j=A(g_j)r_{j−1}. Just before the update for step j≥6, decode g_{j−1} from r_{j−1}, append it to the ring, and evict the oldest entry if the ring exceeds L−1; skip the ring when L=1. No persistent additional last-gate register is needed: the current endpoint itself supplies the last gate.

For every n≥L+4, the ring contains exactly (g_{n−L+1},...,g_{n−1}). Decode (λ,g_n) from r_n, then output λ times these L gate scalars in their original index order. The algorithm requires neither prior knowledge of n nor construction of the complete tagged path tensor. Zero gate factors work without dividing by any gate; shifted factors (g+3) stay positive.

For fixed L, ring operations and the endpoint decoder require O(1) scalar operations per step in addition to maintaining the original native endpoint. The standalone reference enumerates all 576 original typed action entries per full 96-port update. The L requested path masses require L scalar multiplications after decoding, instead of explicitly enumerating L different length-n paths. The bit complexity is the sum of exact rational numerator/denominator lengths; L−1 scalar registers are not L−1 bits.

## Sharp lower bound

On the open input domain λ>0 and all g_k>0, PREFIX-626 establishes that the full 96-port endpoint factors continuously through exactly the six scalar observations

  (λ, Π_0, Π_1, Π_2, Π_3, g_n),
  Π_r=∏_{1≤k≤n, k mod 4=r}(g_k+3).

Fix λ and all gates outside {1,2,3,4} ∪ {n−L+1,...,n−1}, and freely vary the L−1 late gates in a small open neighborhood. Because n−L≥4, the first four indices are disjoint from the requested tail. For each residue r, let i(r)∈{1,2,3,4} be the unique index with i(r) mod 4=r. Replace its early gate by the exact compensated value

  g'_{i(r)}+3=(g_{i(r)}+3)∏_{n−L+1≤k≤n−1, k mod 4=r}((g_k+3)/(g'_k+3)).

Near any strictly positive reference input these four modified early gates remain strictly positive. This constructs an open (L−1)-parameter family with identical (λ,Π_0,...,Π_3,g_n), hence an identical full 96-port endpoint. However, its target path masses λg_k for the first L−1 indices of the tail vary injectively.

If an online scheme with m<L−1 continuous real registers recovered all requested path masses, its final memory restricted to this fixed-endpoint fiber would be a continuous injection from an open subset of R^(L−1) to R^m. Invariance of domain (embed R^m into R^(L−1) if needed) forbids that injection. Thus m≥L−1, matching the construction. L=1 is the zero-register boundary case.

This is a continuous-register/declared-observer theorem. It does not assign constant bit cost to a single unbounded integer or allow discontinuous pathological encodings.

## Exact two-history witness

For n=10, L=3 and λ=3/2, set every gate to 1 in history A. In history B set g_9=4/3 and g_1=9/13, leaving the other eight gates equal to 1. The relevant shifted product is unchanged:
  (9/13+3)(4/3+3)=(48/13)(13/3)=16=4·4.
All other residue products and the last gate agree, so all 96 terminal ports are exactly equal. But the original tagged path coordinate J_10[W(10,9)] changes from 3/2 to 2.

## Actual original-BRC computation

Standalone program: PREFIX627_native_streaming_lag_checker.py. It independently reconstructs the frozen original 48 STAR phases, 96 ports and 576 native source/action labels, then uses Python Fraction arithmetic to perform real native BRC updates and literal labelled-path products. Local run passed 144 complete streaming test cases (nine horizons 6 through 48, eight candidate lags and three rational inputs where admissible), 687 labelled path-coordinate comparisons, and 39 strict-positive same-endpoint/different-tagged-path collision cases. Local separate cross-check against the original PREFIX-626 checker confirmed identical native operators on ten arbitrary rational port states, fifteen endpoints and 180 path definitions. The universal theorem follows from the original native formulas and the algebraic proof, not extrapolation from these finite checks.

Only the specified source-labelled positive BRC path probes W(n,k) are included in the asserted observer. The project-wide signed/phase and full arbitrary path-fiber observer remain separately typed. P000 is unchanged.

## Next research question

For the complete set of ordered labelled paths inside a rolling L-step suffix (not just the one-gate W(n,k) witnesses), determine whether the 96-port endpoint plus L−1 late gates suffices. Try to invert the 16-dimensional stable reachable dynamics from PREFIX-625 over the allowed gate domain, then recover the suffix's original predecessor-port distribution and its action-tensor weights. A native exact witness or a same-observation/different-suffix-path counterexample distinguishes the two outcomes.

Research result status: AUTHOR_SIDE_UNREVIEWED. No formal CLAIM, Native Result, Driver review, Foundation promotion or physical calibration is asserted.
