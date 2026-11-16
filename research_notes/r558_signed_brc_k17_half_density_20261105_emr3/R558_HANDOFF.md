# R558 handoff — fixed k=17 signed BRC half-density

**Scientific frontier:** Frozen R462 `18783e01e3646c72b7aab3b16d3f565e83e6446f`; predecessor R557 immutable `72efdc6f4b9e7e0e071687b6908243e80374ec29`. Model is the signed BRC scalar Toeplitz–Hessenberg determinant `D_m(k)=det[H_k(3+i-j)]`; `H_k(t)=binom(2k+1+t,2t)[x^(2k+1)](1-x)(1+x)^(2t)(1+x²)^(2k+1-t)`.

**Completed unit:** For k=17, verified author-side proof that strict positive and negative signs each have natural density 1/2 and only finitely many zero terms. Exact test: all 33 degree-33 roots are isolated by radius 1e-22 rational Rouché disks; unique dominant conjugate pair |λ|>27 and remaining |λ_j|<10. Direct phase exclusion: complete 2063 cyclotomic-order candidates φ(q)≤1056, q≤2230272, each excluded by an exact rational enclosure for θ/π of width<1e-18. First 1025 exact recurrence values: +514 / -511 / zero0; adjacent sign changes307; 12 independent raw determinant checks.

**Artifacts:** `R558_PROOF.zh-CN.md`, `R558_VERIFY.py`, `R558_EVIDENCE.md`. Run `python R558_VERIFY.py` (Python3 and SymPy 1.14). All proof-critical acceptance checks use integer or Fraction arithmetic; `nroots` supplies candidate centers only.

**Project status:** Author-side, mathematical independent review pending; no new formal CLAIM, Result or Driver acceptance inferred from file publication. Research session was registered separately; canonical owner may be unknown pending native inventory. P000, ACTIVE worldview and frozen inputs unchanged.

**Next independent question:** Extend root and direct phase certification to k=18, then seek a uniform k≥5 bound on the maximal-modulus conjugate pair. Distinct issue: devise/verify an explicit observer-preserving mapping from auxiliary signed determinant to native X6/three-dimensional-slice residual semantics before any native claim.

**Do not re-run** R558 exact root/phase verification without changing assumptions, source inputs or checker; use the verified artifact directly and audit changed obligations.
