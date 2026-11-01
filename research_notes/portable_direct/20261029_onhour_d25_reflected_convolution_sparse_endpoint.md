# D25 SECOND-DIGIT-LIFT — exact reflected convolution endpoints and a signed observer obstruction

2026-10-29 Asia/Hong_Kong. Status: AUTHOR-SIDE / PROVED DERIVATION / EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Own logical Research lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance; not other hourly lanes).

## 1. Original kernels and typed observables

For every prime p>=5 and 0<=n<p, take p-local rational coefficients

$$a_n=\frac{(2n)!(3n)!}{(n!)^5 216^n},\quad
b_n=\frac{(4n)!}{(n!)^4 2304^n}.$$

Original frozen evaluation observables are A_p=sum_{n<p}(6n+1)a_n and B_p=sum_{n<p}(8n+1)b_n. This unit studies *distinct*, degree-(p-1) finite-square convolution coefficients, not those evaluation observables:

$$C_A=\sum_{n=0}^{p-1}a_n a_{p-1-n},\quad
C_B=\sum_{n=0}^{p-1}b_n b_{p-1-n}.$$

Retain the original signed weights also on the first convolution factor:

$$W_A=\sum_{n=0}^{p-1}(6n+1)a_n a_{p-1-n},\quad
W_B=\sum_{n=0}^{p-1}(8n+1)b_n b_{p-1-n}.$$

All congruences below are in Z_(p), with denominator units.

## 2. Theorem: entire reflection support collapses to three indices

Put m=(p-1)/2, l_A=floor((p-1)/3), u_A=p-1-l_A, l_B=floor((p-1)/4), u_B=p-1-l_B, and n*=p-1-n. Exact p-adic valuations are

$$v_p(a_n)=\lfloor2n/p\rfloor+\lfloor3n/p\rfloor,\quad
v_p(b_n)=\lfloor4n/p\rfloor.$$

For k=2,3,4, writing kn=qp+r (0<=r<p) proves the integer identity

$$\lfloor kn/p\rfloor+\lfloor k(p-1-n)/p\rfloor
=k-\lceil(r+k)/p\rceil=k-1-\mathbf1_{\{r>p-k\}}.$$

The exceptional residues r=p-k+1,...,p-1 correspond to {m} for k=2, {l_A,u_A} for k=3, and {l_B,m,u_B} for k=4. Hence **exactly**, for every 0<=n<p,

$$v_p(a_n a_{n*})=3-\mathbf1_{\{l_A,m,u_A\}}(n),\quad
v_p(b_n b_{n*})=3-\mathbf1_{\{l_B,m,u_B\}}(n). \tag{1}$$

Thus only three indices of each original stream can survive modulo p^3:

$$C_A\equiv a_m^2+2a_{l_A}a_{u_A},\quad
C_B\equiv b_m^2+2b_{l_B}b_{u_B}\pmod{p^3}. \tag{2}$$

This is uniform over both 13 and 19 mod24 frozen target classes and all other primes p>=5.

## 3. Theorem: four universal factorial-unit residues

For **all** primes p>=5,

$$\boxed{a_m^2\equiv4p^2,\quad
a_{l_A}a_{u_A}\equiv3p^2,\quad
b_m^2\equiv p^2,\quad
b_{l_B}b_{u_B}\equiv p^2\pmod{p^3}.}\tag{3}$$

Proof. Wilson and p-unit factorial reduction give

$$(p-1)!\equiv-1,\quad t!(p-1-t)!\equiv(-1)^{t+1}\pmod p,$$
$$\frac{(kp+s)!}{p^k}\equiv k!(-1)^k s!\pmod p
\quad(k=1,2,\ 0\le s<p). \tag{4}$$

In the latter identity, strip the k explicit factors p,2p,...,kp, and use k complete nonmultiple blocks of product -1 mod p and a remaining s! block.

Midpoint: 2m=p-1, 3m=p+(m-1), 4m=p+(p-2), so (4) yields

$$a_m/p\equiv(m-1)!/(m!)^5\,216^{-m},\quad
b_m/p\equiv-1/(m!)^4\,2304^{-m}\pmod p.$$

Since (m!)^2=(-1)^{m+1}, m=-1/2, 216^{2m}=216^{p-1}=1 and 2304^m=48^{p-1}=1 modulo p, their squares are respectively 4 and 1.

A edge: write p=3q+1 or p=3q+2. Both have l_A=q, u_A=p-1-q. In the first case, (4) reduces the numerator unit of a_q a_{2q}/p^2 to -(2q)!(q-1)!; its denominator is (q!(2q)!)^5. Wilson gives q!(2q)!=(-1)^{q+1}, so the ratio equals -1/q=3 mod p. In the second case, the numerator unit of a_q a_{2q+1}/p^2 is -(2q)!q! and the denominator (q!(2q+1)!)^5; Wilson gives q!(2q+1)!=(-1)^{q+1}, and the ratio is -1/(2q+1)=3 mod p. The base factors cancel because 216^{q+u_A}=216^{p-1}=1 mod p.

B edge: write p=4q+1 or p=4q+3. Put u=p-1-q. The common denominator (q!u!)^4 and base factor 2304^{p-1} both reduce to 1 mod p. If p=4q+1, (4q)!=(p-1)!=-1 and (4u)!/p^2=2!(p-1)!^2(p-3)!=-1 mod p; their product is 1. If p=4q+3, (4q)!=(p-3)!=-1/2 and (4u)!/p^2=2!(p-1)!^3=-2 mod p; their product again is 1. This exhausts the residue classes and proves (3).

Combining (2) and (3),

$$\boxed{C_A\equiv10p^2,\qquad C_B\equiv3p^2\pmod{p^3}.}\tag{5}$$

These constants are ordinary integers and include the p=5,7 residues without exception.

## 4. New signed observer transport and exact obstruction

Reflection symmetry gives, over the rational p-local ring, the **exact** identities

$$W_A=(3p-2)C_A,\qquad W_B=(4p-3)C_B.$$

Therefore

$$\boxed{W_A\equiv-20p^2,\quad W_B\equiv-9p^2,\quad
C_A-2C_B\equiv4p^2,\quad W_A-2W_B\equiv-2p^2
\pmod{p^3}.}\tag{6}$$

For every p>=5 the two bridge residuals 4p^2 and -2p^2 are nonzero modulo p^3. This proves the **all-prime failure of naive degree-(p-1) convolution endpoint identification** C_A=2C_B or W_A=2W_B at this precision. It is NOT a counterexample to the distinct original evaluation-level candidate A_p-2B_p+p*chi_p=0 mod p^4, which still requires its valuation-zero/one cancellation and other original observer ports.

## 5. Exact integer verification, BRC, next smallest work

Source checker: research_notes/portable_direct/d25_onhour_reflected_convolution_guard_20261029.py (Git object verified against the actually run local file). It strips p factors from every original factorial, evaluates all coefficients modulo p^3, independently checks per-pair valuation (1), special port residues (3), full convolution (5), weighted transport (6), for all **237 primes 5<=p<1500**. Direct independent original integer binomial checks for all n at p=5,7,11,13,19,31,373. Result: PASS_EXACT_REFLECTED_CONVOLUTION.

At p=373: p^2=139129, p^3=51895117, C_A=1391290, C_B=417387, W_A=49112537, W_B=50642956, and C_A-2C_B=556516=4p^2, W_A-2W_B=51616859=-2p^2 mod p^3. Finite computation checks the already proved all-prime relations; it does not establish universality by itself.

BRC: COMPOSE_APPLIED; the exact branch carrier is (source A/B, n, reflection n*, p-valuation, factorial unit, original signed weight, observer). Collapsing the observer before the pairing erases the certified 4p^2 and -2p^2 differences. This is auxiliary p-local algebra; no native X6 or physical reading is asserted.

Next research unit: consume the proved original A216/B2304 p^4 valuation-two jets and valuation-three tail, then identify which retained low/high *evaluation-level* ports must compensate the convolution-endpoint defect; seek a finite Clausen/WZ/CM character certificate for original C_p^(01)=-p^2 Q_p-p^3 D_p mod p^4 rather than claiming observer equivalence. Highest-priority native missing benchmark remains #1559: fixed-p373 same-original-class divided-power H0/B0 [X]U mod139129, module rank, actual semilinear Frobenius/eta, signed odd Green/Hesse, kappa, Delta-R and independent acceptance.

Native control on 2026-10-29: Site research_authority_granted=false, executor_binding_configured=false; em_checkpoint_list produced ACCESS_DENIED. No Source Researcher session/CLAIM/open/run/checkpoint, Result, Driver review or borrowed identity is claimed. No unknown native request was reissued. Formal continuation needs exact Source recovery and verified authority. Keep P000, frozen scientific pin and scheduled Research lane unchanged.
