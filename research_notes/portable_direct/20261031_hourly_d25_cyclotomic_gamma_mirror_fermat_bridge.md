# D25/LIFT — cyclotomic Green-terminal / original-216 mirror Fermat bridge

2026-10-31 | AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Research lane \`chatgpt-research-hourly-enterprise-math-20260923\`; not CONTROL_PLANE_MAINTENANCE. Task publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, P000 ACTIVE unchanged. Not a native authorized CLAIM, Result, H0/B0 experiment or D25 full proof.

## Exact reused inputs (not new authorship)

For prime p=6l+1 >=7 let a_n = binom(2n,n)^2 binom(3n,n)/216^n, and Q_p(a)=(a^(p-1)-1)/p. The already established Saalschütz Green terminal formula (EM commit \`cd0d692a5510dddcc42991b056ed032933e0b164\`, report \`20261031_hourly_d25_saalschutz_terminal_gamma_all_jets.md\`) is

\[
\Gamma_l=\frac{(-1)^l}{18\binom{p-1}{l}\binom{p-1}{2l}},
\quad 18\Gamma_l\equiv1+p(H_l+H_{2l})\pmod{p^2}.
\tag{1}
\]

The independently established original factorial mirror endpoint (EM commit \`59e6e9bae32020d361a4ff3dcf6d8cf0dc08bb62\`, report \`20261031_hourly_d25_fermat_endpoint_carry.md\`) is

\[
M_p:=-a_{p-1}/p^3\equiv1+p(13/2-Q_p(216))\pmod{p^2}.
\tag{2}
\]

The present contribution links those two distinct source ports; it does not reprove/re-attribute them.

## Theorem A: sixth-root harmonic linkage

For every prime p=6l+1 >=7, in F_p,

\[
\boxed{H_{3l}\equiv-2Q_p(2),\quad
H_{2l}\equiv-\tfrac32Q_p(3),\quad
H_l\equiv H_{2l}+H_{3l}.}
\tag{3}
\]

Consequently, since Q_p(216)=3Q_p(2)+3Q_p(3) modulo p,

\[
\boxed{H_l+H_{2l}\equiv -2Q_p(2)-3Q_p(3)
\equiv Q_p(2)-Q_p(216)\pmod p.}
\tag{4}
\]

**Elementary cyclotomic proof.** For 1<=k<p,
\[
\binom pk/p\equiv(-1)^{k-1}/k\pmod p.
\]
Summing these terms and using 2^p-2=2pQ_p(2) and H_{p-1}=0 (mod p) proves H_{3l}=-2Q_p(2).

Take omega a primitive cube root, omega^2+omega+1=0, in Z[omega]. Put u=(1-omega)^{p-1}=(-3 omega)^{3l}=(-3)^{3l}. Since omega^p=omega, Frobenius gives u=1 (mod p); u^2=3^{p-1}=1+pQ_p(3), so (u-1)/p=Q_p(3)/2 (mod p). Expanding (1-omega)^p-(1-omega^p) yields
\[
(1-\omega)(u-1)/p\equiv-\sum_{k=1}^{p-1}\omega^k/k\pmod p.
\]
Let T_r=sum_{1<=k<p,k≡r mod3}1/k. The map k->p-k gives T_1=-T_0,T_2=0, so the sum equals (1-omega)T_0. The factor 1-omega is invertible modulo p (norm 3), yielding T_0=-Q_p(3)/2. As T_0=H_{2l}/3, the second identity in (3) follows.

Let zeta be a primitive sixth root, zeta^2-zeta+1=0, so 1-zeta=zeta^{-1}. Since p≡1 mod6, (1-zeta)^p=1-zeta^p exactly. Binomial expansion gives sum_{k=1}^{p-1}zeta^k/k=0 in F_p[zeta]. Write S_r=sum_{1<=k<p,k≡r mod6}1/k. Reflection gives S_1=-S_0,S_5=-S_2,S_4=-S_3. The root identity reduces the sum to
\[
0=\zeta^2(-S_0+2S_2+S_3).
\]
But
\[
S_0=H_l/6,\quad S_3=(H_{2l}-H_l/2)/3,\quad
S_2=H_{3l}/2-S_0+S_3.
\]
Substituting gives H_l=H_{2l}+H_{3l} (mod p), proving (3)-(4). All denominators are p-units. This proof is independent of finite scan data.

## Theorem B: Green / mirror endpoint first-digit matching

Compose (1),(2) with (4):
\[
\boxed{18\Gamma_l\equiv1+p(Q_p(2)-Q_p(216))\pmod{p^2},}
\tag{5}
\]
\[
\boxed{\frac{18\Gamma_l-M_p}{p}\equiv Q_p(2)-13/2\pmod p,}
\tag{6}
\]
\[
\boxed{\frac{18\Gamma_l}{M_p}\equiv2^{p-1}(1-13p/2)\pmod{p^2}.}
\tag{7}
\]
Since M_p≡1 modp, division is legitimate. The *common original-216 Fermat quotient* cancels from the difference of the two first digits; the independent base-2 carry survives. The endpoints coincide mod p^2 precisely when 2Q_p(2)=13 (mod p), an exceptional locus, **not** a universal equality. This does not authorize replacing the fixed denominator 216.

## Exact executed check

Actual executed standard-library checker \`d25_green_mirror_fermat_bridge_check_20261031.py\` tested all 330 primes p=6l+1<=5000: all three harmonic congruences, Q216 multiplicativity, direct binomial Green gamma, separately reconstructed p-stripped factorial mirror endpoint, difference (6), and ratio (7). Seven anchors p=7,13,19,37,67,283,373 additionally used direct full integer binomial coefficients, independently of the p-stripped formula. All PASS; no exceptional-locus prime in that finite tested set (no global absence claim).

| p | l | Qp(2) | Qp(3) | Qp(216) | 18Gamma mod p^2 | M_p mod p^2 | difference/p mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
|7|1|2|6|3|43|1|6|
|13|2|3|8|7|118|79|3|
|19|3|3|18|6|305|191|6|
|67|11|10|15|8|135|2145|37|
|283|47|58|242|51|1982|27452|193|
|373|62|204|301|23|67514|63411|11|

For p=373, 67514-63411=373*11 exactly for the least nonnegative modular representatives: the two source ports are *not* mod-p^2 interchangeable.

**BRC actual composition:** signed p-adic port carrier preserves (p, original a_n/216, indices, valuation p^3, Green Gamma, mirror M_p, Q216, Q2, observer mod p^2); theorem (6) proves which common first-digit coordinate cancels in the declared difference and which residual persists. This is external p-adic mathematics, not transfer into native P000/X6.

**Unresolved science:** the original D25 target A_p≡p (mod p^3), p mod24 in {13,19}, and its coupled four-port Green/first-jet/integer-carry/signed-R identity remain OPEN. Next discriminating step: use the base-2 residual in a single finite WZ/adjoint/CM ansatz connecting the Green-terminal and original tail sources to the low/mid signed levels, without treating Gamma=M_p or E_p=R_p. Preserve nonzero signed R for p=19,67,373, exact Green log-residue repair and fixed 216. No native run, Source checkpoint, review, freeze or formal acceptance.

Control: on this run Gateway 0.6.11 status was research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. No callable recovery_status or new authorized CLAIM/OPEN; existing control support #1558, no maintenance identity or scheduler changes.
