# R284CP — 127-sweep certificate and unique second witnesses for the frozen Port spectrum

2026-11-21 · **EXACT_FINITE_CERTIFIED / NOT_REVIEWED** · Auxiliary 34-bit Port observer, unchanged frozen R284CL/R284CN/R284CO input.

## Main theorem: sparse exact certification from two deficit radii per level

Let \(X\subset\mathbb Z/P\mathbb Z\) be a finite nonempty set of integer sites, and let \(A_0,\dots,A_{m-1}\) be labeled closed circular arcs. Let \(d_k(x)\) be the \(k\)-th smallest of the \(m\) integer distances from \(x\) to these arcs, with multiplicity. Define

\[
N_r(x)=\#\{i:\operatorname{dist}_{circle}(x,A_i)\le r\},\qquad
F_k(r)=\#\{x\in X:N_r(x)<k\}.
\]

The exact identity \(F_k(r)=\#\{x\in X:d_k(x)>r\}\) holds for all integer \(r\ge0\).

**Two-radius witness certificate.** Suppose that for each rank \(k\ge2\) a candidate unique maximizer \(w_k\in X\) and proposed maximum \(U_k\) and runner-up \(V_k\), with \(0<V_k<U_k\), are provided. If

- \(d_k(w_k)=U_k\),
- \(F_k(V_k)=1\), and its only deficient site is \(w_k\);
- \(F_k(V_k-1)=2\),

then \(w_k\) is the unique maximum achiever, \(U_k=\max_{x\in X}d_k(x)\), and the second largest value is exactly \(V_k\) with a **unique** runner-up site. If additionally \(F_1(0)=0\), then \(U_1=0\) for all sites. Consequently, given the candidate table, the entire spectrum and unique top-two witnesses are certified using precisely \(2(m-1)+1\) exact population-coverage sweeps plus direct evaluation of the \(2(m-1)\) nominated sites' \(m\) arc distances.

**Proof.** The equality defining \(F_k\) is the definition of the kth order statistic: fewer than \(k\) distances are at most \(r\) if and only if \(d_k(x)>r\). The first deficit condition says that every other site has \(d_k(x)\le V_k\), while the nominated site has \(d_k(w_k)=U_k>V_k\), proving it is the unique maximizer. The second condition adds exactly one other deficient site as the integer radius decreases from \(V_k\) to \(V_k-1\); this site's kth distance must be \(V_k\). Every remaining site's kth distance is less than \(V_k\). The rank-one assertion follows from \(F_1(0)=0\). \(\square\)

### Exact circular event implementation

For an arc of integer width \(w\), its radius-\(r\) integer coverage is the full circle when \(w+2r\ge P-1\), otherwise the cyclic closed interval \([a-r,a+w+r]\pmod P\). Split wraps at zero. Emit \(+1\) events at inclusive left endpoints and \(-1\) events at right endpoint plus one, adding base counts for saturated arcs. Between sorted events, membership and coverage count are constant. Binary-search a sorted population \(X\) to count all deficient sites in each event band. This calculates \(F_k(r)\) and identifies up to two sites exactly, without evaluating all \(m|X|\) point–arc distances. It is the R284CN integer sweep upgraded from a minimum-coverage observer to an exact **deficit-count and deficit-identity observer**.

## Exact frozen computation

For \(P=17\,179\,869\,143\), the original 65,536 distinct codewords, 64 labeled arcs and R284CO candidates, the executable checker confirms:

| Quantity | Exact result |
|---|---:|
| Codewords / labeled arcs | 65,536 / 64 |
| Integer event sweeps | **127** |
| Direct point–arc distances evaluated for proposed top-two witnesses | **8,064** |
| Exhaustive all-population point–arc distance evaluations during this verifier | **0** |
| All 63 ranks \(k=2,\dots,64\): \(F_k(V_k)\) | **1** |
| All 63 ranks: \(F_k(V_k-1)\) | **2** |
| Pairwise-distinct unique maximizing residues | **63** |
| Pairwise-distinct unique runner-up residues | **63** |
| Shared residues between winner and runner-up sets | **2** |

The only two shared residues are \(3\,332\,614\,289\) and \(3\,332\,614\,473\), exchanged between ranks 6 and 19. All rank-1 codewords have distance zero to at least one fiber arc. The computed margins remain \(U_k-V_k\ge64\), with equality only for ranks 15 and 16, and the rank-54 margin remains 78.

The computer checks include frozen SHA-256, correspondence of candidate indices to generated residues, exact nominated top and runner-up order statistics, deficit counts and identities, and all 63 unique indices. The result also verifies the complete 64-level spectrum already published in R284CO and independently obtained via R284CN.

## Method, cost, scope

The 127-sweep checker **verifies a supplied candidate witness certificate**. Discovering that certificate from scratch by R284CO's exhaustive enumeration remains a separate computational cost. For sorted population size \(n\), number of arcs \(m\) and \(m-1\) candidate levels, each deficit scan costs \(O(m\log m+m\log n)\) in a unit-cost integer model; generating and sorting \(X\) costs remain. The verifier is a certified finite-population algorithm, not an authenticated mathematical review or evidence of native X6 physical transfer.

Evidence:
- R284CO_spectral_witness_certificate.json: proposed extrema, witness indices, residues and margins, frozen pins.
- R284CP_127_sweep_witness_verifier.py: runnable, standard-library, imports the R284CO frozen determinant generator from the same directory.
- R284CP_127_sweep_witness_certificate.json: exact counts, the 63 unique runner-up residues, intersection set and runtime observations.

## Next

Use the rank-specific two-deficit-site certificate to search for an inverse construction of witnesses from event geometry, avoiding R284CO's discovery enumeration. Investigate whether the rank 6/19 winner–runner swap is a general symmetry, and whether the 63 runners have a compressed representation under the pinned matrix readout. Keep mathematical admission separate from these finite proofs.