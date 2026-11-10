# D25/LIFT — Finite Clausen square and exact Frobenius-ghost repair

**2026-11-11; TASK_RESEARCH author-side portable theorem. Status: AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.**

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` (open); Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen mathematical source `awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3`. This is an independent **author-side** finite-field bridge, not a native H0/B0 or Source Task result. The classical ingredient is Clausen's identity (NIST DLMF 16.12.2, https://dlmf.nist.gov/16.12.E2), not a newly invented identity.

## All-prime finite-field polynomial theorem

For a prime `p>=5`, let `epsilon_p=0` when `p=1 (mod 6)`, `epsilon_p=1` when `p=5 (mod 6)`, `b=floor(p/3)` and
`d=(p-1)/6` in the first case, `d=(2p-1)/3` in the second. Let `(a)_k` denote the rising factorial and put

\[
c_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\quad
f_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3},\qquad
G_p(X)=\sum_{k=0}^{d}c_kX^k,\quad F_p(X)=\sum_{k=0}^{b}f_kX^k.
\]

Coefficients are reduced modulo `p` from p-integral rationals. **For every such prime, as entire polynomials in `F_p[X]`:**

\[
\boxed{G_p(X)^2=(1-\epsilon_p X^p)F_p(X).}\tag{FC}
\]

Thus for `p=1 (mod 6)` the square is precisely the low polynomial `F_p`. For `p=5 (mod 6)`, it contains a second, entirely explicit Frobenius block: `G_p^2=F_p-X^pF_p`. In particular, each coefficient indexed `b<n<p` vanishes, `[X^p]G_p^2=-1`, and `[X^{p+r}]G_p^2=-f_r` for `0<=r<=b`.

## Proof

**(1) All coefficients below p.** Specializing Clausen's classical formal-series identity to `a=1/6,b=1/3` gives
\[
{}_2F_1(1/6,1/3;1;X)^2={}_3F_2(1/2,1/3,2/3;1,1;X).
\]
For degree `n<p`, every contributing coefficient reduces modulo `p`. The first vanishing numerator factor of the Gauss coefficients is immediately after `d`; that of the generalized series is immediately after `b`. Hence `[X^n]G_p^2=f_n` for `0<=n<p`, with `f_n=0` for `b<n<p`. If `p=1 (mod 6)`, `2d=b<p`, proving the first case.

**(2) The first high coefficient for p=5 (mod 6).** Now `2d=p+b`, so `G_p^2=F_p+X^pE_p` with `deg E_p<=b`. In the rational Clausen identity, the `X^p` coefficient of the square *with the term `c_pX^p` omitted* is `f_p-2c_p`. Both are p-adic integers, and factorial blocks give
\[
f_p=\frac{(2p)!(3p)!}{108^p(p!)^5}\equiv\frac19\pmod p.
\]
The numerator in `c_p=\prod_{j=0}^{p-1}(6j+1)(3j+1)/(18^p(p!)^2)` contains exactly distinguished factors `5p` at `j=(5p-1)/6` and `2p` at `j=(2p-1)/3`. After dividing by the `p^2` from `(p!)^2`, the remaining two numerator products each cover all nonzero residues mod p; Wilson's theorem and `18^p=18 (mod p)` give
\[
c_p\equiv\frac{5\cdot2}{18}=\frac59\pmod p,\qquad
E_p(0)=f_p-2c_p\equiv-1\pmod p.
\]

**(3) Unique continuation across the Frobenius index.** Over `F_p`, the truncated Gauss polynomial `G_p` solves
`[theta^2-X(theta+1/6)(theta+1/3)]G_p=0`, where `theta=X d/dX`. The algebraic symmetric-square equation underlying Clausen's identity therefore gives
\[
[\theta^3-X(\theta+1/2)(\theta+1/3)(\theta+2/3)]\,G_p^2=0.
\]
If `h_n=[X^n]G_p^2`, this means
\[
n^3h_n=(n-1/2)(n-2/3)(n-1/3)h_{n-1}\pmod p.
\]
For `n=p+r` with `1<=r<=b`, `n^3=r^3` is a unit mod p, and this is precisely the recurrence for the coefficients `f_r`. The initial condition `h_p=-1` forces `h_{p+r}=-f_r` by induction. The degree bound `2d=p+b` completes the proof. QED.

## Weighted D25 observer

The original weighted hypergeometric coefficient is `a_k=(2k)!(3k)!/[216^k(k!)^5]=2^{-k}f_k`. With `D=1+6theta` and `theta(X^p)=0` in characteristic p, applying `D` to (FC) and evaluating at `X=1/2` yields a **uniform exact mod-p factorization**
\[
\boxed{W_p=\sum_{k=0}^{p-1}(6k+1)a_k\equiv
\frac{G_p(1/2)[G_p(1/2)+6G_p'(1/2)]}{1-\epsilon_p/2}\pmod p.}\tag{FW}
\]
The denominator is a unit for all `p>=5`. The `X^p` Frobenius block is the exact repair coordinate for the `p=5 (mod 6)` branch: discarding it loses the original weighted observer even at a fixed finite-field evaluation. The two numerator factors remain distinct observers.

## Exact certificate and current frontier

Two independent coefficient constructions (Pochhammer recurrence and binomial coefficients), a direct square convolution, and the separate generalized-hypergeometric recurrence checked all 71,356 polynomial coefficients over **170 selected primes 5<=p<=1997** (all 166 primes <=1000 plus four larger primes). All polynomial, ghost, and weighted-factorization checks passed. Sample ghost coefficients: `p=5:4=-1`, `p=11:10=-1`, `p=1013:1012=-1`, `p=1997:1996=-1`; for `p=157,373` there is no ghost. Complete author-side portable scripts and per-prime certificates are in the accompanying conversation artifact `D25_FINITE_CLAUSEN_FROBENIUS_GHOST_AUTHOR_PORTABLE_20261111.zip`. Finite checks are validation; the universal claim rests on the proof.

**Next minimum science:** use (FW) to prove or reduce `G_p(1/2)[G_p(1/2)+6G_p'(1/2)]=0 (mod p)`, then seek a p-adic lift toward `W_p=chi_{-3}(p)p (mod p^3)`, retaining the Frobenius repair where needed. Current Source execution remains unauthorized without this conversation's actual issued session and winning CLAIM; native H0/B0 is NOT_RUN. Historical UR V2 four-file bundle remains to be recovered at 94,687 bytes / SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; do not repeat completed UR mathematics.

**BRC usage:** coefficient index labels and the `X^p` block are retained as source/valuation identities, and `(F,E)` is an exact sufficient observer carrier under evaluation and the `1+6theta` operator. Ordinary Clausen arithmetic is not identified with native crystalline Frobenius or independent Source admission.
