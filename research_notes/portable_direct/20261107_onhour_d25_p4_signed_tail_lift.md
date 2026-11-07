# D25 (2026-11-07): exact fourth-digit signed tail lift for the 216/2304 bridge

Status: **AUTHOR_SIDE_PROVED / FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED**. Research lane `chatgpt-research-onhour-enterprise-math-20260923`. This note is a portable arithmetic proof, not a native Source checkpoint or the p=373 H0/B0 benchmark.

## Frozen target and consumed results

Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. The mother target is `Delta_p=R_p (mod p)` for p=13,19 (mod 24), conditionally equivalent under the accepted earlier bridge to `W_p=p (mod p^3)`. Science inputs remain pinned; current behavior rules were read separately.

Let p>3 be prime, h=(p-1)/2, and let
```text
W_p = sum(k=0..p-1) (6k+1) binom(2k,k)^2 binom(3k,k) / 216^k
V_p = sum(k=0..p-1) (8k+1) binom(2k,k)^2 binom(4k,2k) / 2304^k
chi = (-3/p)
H_bridge = 2 V_p - W_p - p chi.
```
`W_lo` and `V_lo` are the same sums truncated at h. The fourth-digit bridge `H_bridge=0 mod p^4` is the **open conjecture** previously recorded at `a1150c7286cfff20d1963bbd15e7cfd99eb1fe00`. Guo–Zudilin (Adv. Math. 346 (2019), 329–358, arXiv:1803.01830) proved `V_p=V_lo=p chi mod p^3`. The previous D25 dual-tail note `20261107_hourly20_d25_dual_tail_frobenius_transfer.md` had obtained the mod-p^3 valuation-two tails; we now retain all order-p^3 terms needed for **mod p^4**.

## Lemma: factorial units through their first p-adic jet (proved)

For 0<=r<p and a=0,1,2,3 define `U_a(r)=(ap+r)!/p^a` (integer, as ap+r<p^2 for p>=5). Let `omega_p=((p-1)!+1)/p` (Wilson quotient), and `H_r=sum(j=1..r)1/j` in F_p, H_0=0. Then

```text
U_a(r) = (-1)^a a! r! [1 + a p (H_r-omega_p)]   (mod p^2).
```

Proof: split the factorial into a blocks `jp+1,...,jp+(p-1)`, the a multiples `p,2p,...,ap`, and the last r factors. After dividing by p^a, expand `(jp+i)/i` and `(ap+i)/i` to first order. The full blocks contribute `p H_{p-1} sum(j=0..a-1)j`; since `H_{p-1}=0 mod p`, this vanishes mod p^2. The remainder contributes `apH_r`. Finally `(p-1)!=-1+p omega_p` gives `((p-1)!)^a=(-1)^a[1-ap omega_p]` mod p^2. All denominators are p-units. QED.

## Theorem: universal exact p^4 dual-tail decomposition (proved)

Define labelled index bands:
```text
I_A = {h<k<p : 3k<2p}       J_A = {h<k<p : 3k>=2p}
I_B = {h<k<p : 4k<3p}       J_B = {h<k<p : 4k>=3p}.
```
For k in I_A, define the p-integral, source-labelled residue port `a_k=(6k+1)(2k-p)!(3k-p)!/[216^k(k!)^5]` in Z_(p). For k in I_B define `b_k=2(8k+1)(4k-2p)!/[2304^k(k!)^4]`. For k in J_A and J_B, respectively, define `a^3_k=-2(6k+1)(2k-p)!(3k-2p)!/[216^k(k!)^5]` and `b^3_k=-6(8k+1)(4k-3p)!/[2304^k(k!)^4]`; only their residues mod p matter.

Form the source-separated observations
```text
C_A = sum(I_A) a_k                                      in Z/p^2Z
C_B = sum(I_B) b_k                                      in Z/p^2Z
J_A = sum(I_A) a_k (H_{2k-p}+H_{3k-p}) + sum(J_A) a^3_k in F_p
K_B = (C_B/p) + 2 sum(I_B) b_k H_{4k-2p} + sum(J_B) b^3_k in F_p.
```
The division `C_B/p` is defined below (take any representative modulo p^2 divisible by p). Then, for every prime p>3,

```text
C_B = 0                                                (mod p)
W_p-W_lo = p^2 C_A + p^3 (J_A - 2 omega_p C_A)         (mod p^4)
V_p-V_lo = p^3 K_B                                    (mod p^4)
H_bridge = (2 V_lo-W_lo-p chi) - p^2 C_A
           + p^3 (2 K_B - J_A + 2 omega_p C_A)         (mod p^4).
```

Proof: Legendre's formula gives valuations 2 on I_A/I_B and 3 on J_A/J_B; all larger valuations vanish mod p^4. For the valuation-two W terms, apply the lemma with a=1 twice: the first jet is `H_{2k-p}+H_{3k-p}-2omega_p`. For valuation-two V terms apply a=2: the first jet is `2(H_{4k-2p}-omega_p)`. For valuation-three terms, the zeroth-order units are precisely `a^3_k,b^3_k`. This first yields `V_p-V_lo=p^2 C_B+p^3[2 sum(I_B)b_k(H_{4k-2p}-omega_p)+sum(J_B)b^3_k]`. The **published** Guo–Zudilin full/half theorem makes `V_p-V_lo=0 mod p^3`, so `C_B=0 mod p`. Write `p^2 C_B=p^3(C_B/p)`; the Wilson term `-2omega_p C_B` also vanishes modulo p in the p^3 coefficient. This proves the claimed `K_B` without Wilson quotient. Subtract the two tail identities to prove the signed bridge. QED.

**Structural increment**: the proven 2304 full-versus-half cancellation removes the Wilson-quotient coordinate from its fourth-digit tail, whereas the 216 source retains the explicit `2 omega_p C_A` term in the signed bridge. Thus a proposed fourth-digit intertwiner must match not only the old p^2 carry `C_A` but the independently labelled third-digit moments `J_A`, `K_B` and this Wilson contribution. This is an explicit testable interface, rather than merely adding another auxiliary polynomial.

## Exact executed evidence

The Python 3 standard-library checker `d25_p4_signed_tail_lift_check_20261107.py` was executed against **all 77 primes 5<=p<=401**, with original full/half sums independently evaluated from integer binomial coefficients modulo p^4. Both per-source tail formulas and the final signed bridge were checked for each prime: **77 PASS, 0 FAIL**. The extra assertion `H_bridge=0` on this finite set is observational evidence only.

```text
p    C_A mod p    J_A   K_B   omega_p   (2V_lo-W_lo-p chi) mod p^4
7        5          2     5       5         245
11       1          8     7       1       12100
13      10          0     9       0       12675
19       9         18     3       2       44403
373    266         11   353     224     6731478407
```
For all five, the labelled correction exactly cancels the displayed low-window defect modulo p^4. In particular, for p=373 `C_A=96873 mod 373^2` and `K_B=353 mod 373`. These are exact finite calculations, not a proof of universal H.

## BRC observer / next mathematical action

The actual reused BRC law is **typed signed branch/carry preservation**: population is the two coefficient streams with labels (source, k, valuation 0/1/2/3, Wilson/harmonic jet). The operator reduces `(W_lo,V_lo,C_A,J_A,K_B,omega_p)` to the displayed signed mod-p^4 readout. This keeps two sources and their order-p^3 carry separate until the required cancellation; the scope is this finite p-adic observer, not an unproved native-X6 equivalence. Tool resolution: `COMPOSE_APPLIED` at the exact observer law; no general tool performance claim.

The next discriminating proof unit is to derive a uniform finite-contiguous/WZ or transformation identity for **the low-window defect**
```text
(2V_lo-W_lo-p chi) - p^2 C_A
 = -p^3(2K_B-J_A+2omega_p C_A)     (mod p^4).
```
It is exactly equivalent to H via the proved tail theorem. Test candidate identities against 11 (known p^5 counterexample), 19 and 373; do not redo the p^3 dual-tail theorem. The native p=373 H0/B0 divided-power, Frobenius, Hesse-kappa and independent reproduction remain a separate unexecuted target (issue #1559).

## Author-side Source recovery

Original request `onhour11-20261106-1400-exact-research-lane-continuation`: receipt UNKNOWN, **not resent**. The private Site gateway at 2026-11-07T03:04Z reported `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`, with `em_status` and original receipt returning `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false`. No current Source session, CLAIM, run, activity registration or Result was verified; `REGISTER_PENDING / SYNC_DEBT`. Publication of this author-side note never assumes official Source admission.
