# C313: High-order mod-7 root factors in the 125-path, 79-branch auxiliary model

**Evidence class:** Author-level exact theorem and finite-family verification. This is a factorized positive-rational *auxiliary scalar* result, not a native GF(2)-BRC/X6 theorem, a Source Result, an independent Driver review, or a Foundation admission.

Frozen canonical reads (one snapshot throughout this research run):
- Global GLOBAL_KNOWLEDGE_V1 main: `40ae4bf39f84a1ad1b122a824019ef562a5e4bc1`, including bootstraps, P000, active worldview and math/BRC policy.
- Enterprise Math main: `e27e64dfe4803804ff84c9ca75d83da4cc38459b`, including the portable research protocol and source control rules.
- Previous immutable C311 certificate: `d6f60a8ebf6a9b9fac7f50e6a881ad1eba211ab2`.
- Existing C312 author branch: `research/c312-zero-extra-content-106-20261026-research2@f7c4e4daa6ecb8eb77b1d2c8d0d33cf5d096f433`.
- C293 frozen 125-path input SHA256: `03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89`.

## Exact mathematical theorem

Let p be prime, and let R(t) = sum_j a_j prod_l f_{jl}(t)^{e_{jl}} be a finite sum of labelled Z[t] terms (e_{jl} >= 0). Reduce modulo p. Delete a term only if its scalar or any factor becomes the zero polynomial in F_p[t]. For a surviving term, set

m_{j,u} = sum_l e_{jl} ord_{t=u}( f_{jl} mod p),  u in F_p,

and let m = min over all surviving pairs (j,u) of m_{j,u}. Then in F_p[t],

```
                 (t^p - t)^m | R(t) mod p.
```

Consequently, all Hasse derivatives D^[k] R(u) vanish modulo p for all u in F_p and 0 <= k < m. In particular R(n) = 0 (mod p) for every integer n. If R mod p is not the zero polynomial, the *exact* largest exponent nu of (t^p-t) dividing it equals min_u ord_{t=u}(R mod p).

**Proof:** For every surviving term, valuation at each linear factor (t-u) is additive across its polynomial factors. Each term therefore contains (t-u)^m for every residue u. These distinct linear factors are coprime, so their product to the power m, namely (t^p-t)^m, divides each term and their sum. Taylor expansion by Hasse derivatives around u gives the jet conclusion; exact nu follows by unique factorization and exact synthetic division. No numerical approximation, evaluation-only inference, or branchwise cancellation assumption occurs. Branchwise m is not necessarily sharp for the sum: for example the terms t and (-t+t^2) over F_7 each have order 1 at zero, while their sum t^2 has order 2.

## New exact finite-family result

For each frozen path i = 0,...,124, use the 79 separately labelled C300/C305 factorized auxiliary numerator terms J_ij and C309/C311 structural gcd lower divisor L_i:

```
R_i = sum_{j=0}^{78} (J_ij / L_i) = C_i P_i / L_i .
```

The equality to C_i P_i rests on the *existing author-level C300/C305 upstream identity* and is **not independently proved here**. The first equality is the actual source factor circuit evaluated in this audit.

Two exact algorithms were executed on all 125 paths: (1) term-factor root orders via repeated synthetic division in F_7, retaining branch IDs to get m_i; (2) full F_7 coefficient convolution of the 79 terms followed by seven exact root-order divisions to get nu_i, checking the resulting polynomial is nonzero.

```
For all 125 frozen paths:
 R_i mod 7 != 0 as a polynomial;
 (t^7-t)^14 divides R_i mod 7;
 14 <= m_i <= nu_i <= 37.
```

Across 125*79 = 9875 labelled branch terms, 3161 remain nonzero mod 7 and 6714 vanish. All 125 computations passed. Exactly **7** paths had a stricter power after actual interbranch cancellation:

| path i (0-based) | branchwise m_i | full-polynomial nu_i |
|---:|---:|---:|
| 3 | 36 | 37 |
| 5 | 27 | 28 |
| 30 | 27 | 28 |
| 49 | 36 | 37 |
| 83 | 36 | 37 |
| 99 | 24 | 25 |
| 113 | 24 | 25 |

The other 118 paths have nu_i=m_i. Special path 28 has reduced denominator degree 265, full R mod7 degree 240, seven residue multiplicities [32,32,24,39,37,23,35], and nu_28=m_28=23. All paths have an *evaluation kernel of depth >=14* in the mod-7 Hasse-jet observer, even though the full polynomial is nonzero. This strictly strengthens the earlier first-order mod-7 zero-function observation from C312 and covers the C311 exceptional 19 paths as well.

The complete replay bundle (separate downloadable conversation artifact) contains both executed Python scripts, 125 full vector certificates for both methods, stdout logs, the frozen C311 upstream archive and SHA256 manifest. A compact auditable vector of all m_i and nu_i is saved alongside this note in the present research branch.

## Boundaries and next

This is exact polynomial mathematics in the stated auxiliary model, NOT physical model evidence and NOT a proved faithful compression of native phase, signed weight, branch provenance, ports, six-dimensional Cell state or future operations. Original labelled terms are preserved until the explicitly typed scalar polynomial diagnostic. P000/worldview are unchanged.

**Still open C314:** reconstruct all 79 *original* C195/H168 rational branches independently of C300/C305 `prepare`, then compare the full exact numerator identity on all 125 frozen paths, with special attention to path 28 and 19 exceptional content-cancellation paths. Separately isolate the labelled contributions causing seven +1 root-order increases.

**Authority observation:** authenticated GitHub identity `awdawmip` has source repository push/admin capability, but native `em_control_tasks` returned `CONTROL_QUOTA` and native `em_session_start` returned `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Therefore active Owner remains UNKNOWN, and native session, CLAIM, Researcher Activity registration, formal Result and Driver admission are **NOT CLAIMED**. Publication on this author branch is persistence only.
