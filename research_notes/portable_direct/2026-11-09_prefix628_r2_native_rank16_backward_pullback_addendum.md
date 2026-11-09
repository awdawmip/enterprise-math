# PREFIX-628 R2 addendum — rank-16 native inverse suffix pullback

Date: 2026-11-09 Asia/Shanghai. Source: original frozen native X6-BRC 48 STAR phases, 96 ports and 576 tagged positive actions at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Status: author-side exact algebraic certificate and original Fraction tests; independent mathematical Driver review pending. Companion to `2026-11-09_prefix628_r2_sharp_full_suffix_tagged_memory.md`.

## Theorem: original current port state has a one-gate exact predecessor inverse on the reachable 16-space

Use exactly the native matrix A(g) from PREFIX-625. Set A0=A(0), E=A(1)-A0, T=A0*A0, V=E*A0, and the fixed zero-based index sets

    R=[0,2,4,6,8,10,12,14,32,34,36,38,48,50,52,54]
    C=[0,4,8,12,16,18,20,22,24,28,42,46,56,60,64,68]

Define K=T[R,C], G(g)=T[:,C]+g V[:,C], N0=K^{-1}(A0 G(0))[R,:], N1=K^{-1}(A0 V[:,C])[R,:], N(g)=N0+g N1. The verified original native symbolic identities are

- det K = -65536 and G(g)[R,:]=K for every g.
- A(c)G(b)=G(c)N(b), verified coefficient by coefficient in the 96x16 matrix polynomial.
- N1 has only entry N1[2,7]=1/2; det N(g)=16384(g+3), hence N(g) is invertible for every native gate g≥0.
- det N0=49152 and tr(N1 N0^{-1})=1/3.

For any k≥2 and a reachable original native history r_k=A(g_k)...A(g_1)E(λd), the PREFIX-625 two-step factorization gives r_k=G(g_k)u_k for a unique 16-vector u_k. The next native step is

    r_(k+1) = A(g_(k+1))G(g_k)u_k = G(g_(k+1))N(g_k)u_k.

Extracting the fixed 16 coordinates R yields (r_(k+1))_R=K N(g_k)u_k. Therefore, when g_k is known, the exact previous *full* 96-port state follows from the **next** full state by

    r_k = G(g_k) N(g_k)^{-1} K^{-1} (r_(k+1))_R.

There is no dependence on the unknown next gate g_(k+1) in this inverse. This identity is a left inverse on the exact native reachable-state fiber with the previous gate supplied, not a generic inverse of 96x96 A(g).

The inverse is rank-one rational:

    U=N0^{-1},
    N(g)^{-1} = U - [g/(1+g/3)] U N1 U,

because N1 is rank one and tr(N1 U)=1/3. The denominator 1+g/3 is positive for all g≥0, including zero-gate boundaries. This gives a reusable exact 16-coordinate predecessor decoder.

## Improved all-labelled L-step suffix algorithm

For the complete suffix-memory problem of the main PREFIX-628 R2 theorem, first decode the last gate and the terminal four mod-4 shifted products from r_n as before. Retain g_t,...,g_(n-1) in L online scalar registers when t=n−L≥5. At t=4 only g5,...,g_(n−1) (L−1 registers) are retained; recover g4 by dividing the uniquely indexed `Π_0(n)` product by known later same-residue factors and subtracting 3.

Then repeatedly apply the new inverse for k=n−1,n−2,...,t to reconstruct the exact original r_t, using only the gates g_k already known. Multiply the actual original typed edge weights to emit each source/action-labelled length-L path. The recursion makes **O(L)** predecessor steps; each step uses fixed 16-dimensional linear algebra and one fixed 96x16 matrix product, so the scalar arithmetic for precursor reconstruction is O(L*(16²+96*16)), independent of total age n. Full explicit labelled tensor output still has length exponential in L, and exact rational bit lengths remain part of bit complexity.

The inverse is valid because every intermediate r_k with k≥2 lies in the original 16-dimensional G(g_k) reachable subspace. All suffix queries in the main theorem have t≥4.

## Exact original-BRC evidence

The standalone `PREFIX628_R2_16state_pullback_checker.py` uses the separately published original 576-edge enum `PREFIX628_R2_full_suffix_checker.py`. It reconstructs A0/E from the original typed edges, computes 16x16 K/N, and symbolically checks all four 96x16 coefficient identities for A(c)G(b). It checks the polynomial determinant, rank-one pattern and trace, and verifies the rank-one inverse against direct exact inverses for gates 0, 1, 2 and 7/3.

For (n,L)=(6,1),(6,2),(7,3),(9,3),(12,3),(18,5), the checker ran actual native Fraction histories, pulled back **17** consecutive predecessor steps in total and compared **all 96 exact port coordinates at every step** against directly evolved native states. All assertions passed. This finite execution checks the implementation; the algebraic identities prove the inverse for any length and all nonnegative gates.

Dependency: PREFIX-625 original finite-horizon BRC factorization and verified 16x16 minor; companion PREFIX-628 R2 sharp memory theorem. Frozen science and P000 unchanged.

## Next

Independently audit the exact endpoint six-parameter factorization and whether complete suffix-labelled path observations separate the full positive fiber; then benchmark replay and 16-state pullback at large n and fixed L with numerator/denominator bit-length accounting. No Native Result, CLAIM or Driver mathematical acceptance has been asserted.
