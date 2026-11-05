# D25 / SECOND-DIGIT-LIFT — reflected 2304 compensation shell through the **second** p-adic digit

**2026-11-06 · TASK_RESEARCH · exact derivation + 16-prime modular arithmetic · AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED.**

- Frozen task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
- Publication: `TP2-B6F4FC938FF94941C1B7`; immutable scientific source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.
- Logical research lane: `chatgpt-research-onhour-enterprise-math-20260923` (no maintenance identity assumed).
- Consumes, without re-proving, `20261106_onhour_d25_shortened_signed_certificate.md` at `f07ae4f5614bc14c5e252c6bcce75418f6c1240c`. Its exact relation is `W_p-V_p = C_p - V_tail (mod p^3)`; the uniform vanishing of that residual remains open.

## Theorem: low-index p-adic reflection of the *entire compensating tail*

For **every prime p>3**, let
[
h=(p-1)/2,qquad L=lfloor(2p-1)/3floor,qquad
K_0=lfloor2L/3floor,qquad
K=K_0-mathbf1_{{2L-3K_0=1}},quad J=h-K-1.
]
As in the consumed theorem, (Kle h); (J=-1) means an empty sum. Put
[
b_k=rac{(4k)!}{2304^k(k!)^4},qquad
V_{mathrm{tail}}=sum_{k=K+1}^{h}(8k+1)b_k.
]
All divisions below occur in (mathbb Z_{(p)}), with final reduction indicated. For (0le jle J), define the **low-index reflected kernel**
[
q_j=9^jrac{(2j)!^4}{j!^4(4j+1)!}
=9^jrac{(1/2)_j^3}{(3/4)_j(5/4)_j,j!},quad q_0=1,
]
and the log-deformation correction
[
D_j=sum_{i=0}^{j-1}left[-rac4{2i+1}
+2left(rac1{4i+2}+rac1{4i+3}+rac1{4i+4}+rac1{4i+5}ight)ight],qquad D_0=0.
]
Write the standard (integer) Wilson and Fermat quotients
[
mathcal W_p=rac{(p-1)!+1}{p},quad
q_p(48)=rac{48^{p-1}-1}{p},quad
H_{4,p}=rac{(h!)^4-1}{p}.
]
Wilson's theorem guarantees that (H_{4,p}) is an integer. Define
[
eta_pequiv 2mathcal W_p-2+H_{4,p}+q_p(48)pmod p.
]
Then **both digits of the signed tail** have the exact finite certificate
[
oxed{rac{V_{mathrm{tail}}}{p}equiv
S_0+pS_1pmod{p^2}},qquad
S_0=sum_{j=0}^{J}(8j+3)q_j,quad
S_1=sum_{j=0}^{J}q_jigl((8j+3)(D_j-eta_p)-4igr).
]
Here (S_0) **must** be retained modulo (p^2); (S_1) requires modulo (p). In particular (S_1) is the first-order **deformation correction**, not necessarily the usual base-(p) digit of (V_{m tail}/p). All denominators of (q_j,D_j) are p-units in the stated range.

### Proof (factorial reflection + first-order parameter lift)

1. In the original tail, (ple4k<2p) and (k<p), so (v_p(b_k)=1). Set (k=h-j). Since (4k>p), (4j+1=2p-1-4k<p). The short kernel and logarithmic denominators are therefore p-units.
2. At the top (k=h),
[
rac{b_h}{p}=rac{(2p-2)!/p}{48^{p-1}(h!)^4}.
]
In (mathbb Z_{(p)}/p^2), use
[
(p-1)!=-1+pmathcal W_p,quad
(p-2)!=1+p(1-mathcal W_p),quad
prod_{a=1}^{p-2}(1+p/a)equiv1+p,
]
the last identity following from (sum_{a=1}^{p-2}a^{-1}equiv1mod p).
Hence ((2p-2)!/pequiv-1+p(2mathcal W_p-2)). Since (48^{p-1}=1+pq_p(48)) and ((h!)^4=1+pH_{4,p}),
[
oxed{b_h/pequiv-1+peta_ppmod{p^2}}.
]
3. The **exact rational** backward coefficient ratio is
[
rac{b_{h-i-1}/p}{b_{h-i}/p}
=rac{2304(h-i)^4}{prod_{r=0}^3(4h-4i-r)}
=rac{144(p-(2i+1))^4}{prod_{r=2}^5(2p-(4i+r))}.
]
Its expansion at (p=0), justified modulo (p^2) by the unit denominators, is
[
R_i{1+plambda_i},qquad
R_i=rac{18(2i+1)^3}{(i+1)(4i+3)(4i+5)},
quad
lambda_i=-rac4{2i+1}+2sum_{r=2}^{5}rac1{4i+r}.
]
Products give (q_j=prod_{i<j}R_i) and
[
rac{b_{h-j}}pequiv(-1+peta_p)q_j(1+pD_j)pmod{p^2}.
]
4. The original weight has the **signed** reversal
[
8(h-j)+1=4p-(8j+3).
]
Multiply the preceding formula without discarding any sign or carry:
[
(8(h-j)+1)rac{b_{h-j}}p
equiv q_jigl[(8j+3)+p((8j+3)(D_j-eta_p)-4)igr]pmod{p^2}.
]
Summing (0le jle J) proves the theorem. No external special-function theorem or unproved all-prime congruence is used.

## Checked finite witnesses and meaning

The companion checker `d25_reflected_tail_second_digit_check_20261106.js` executes **independent factorial-shell multiplication** for each (b_{h-j}/pmod p^2) and compares it with the reversed-kernel + harmonic-deformation formula. It was executed in the JavaScript computation runtime for the exact 16-prime set
`5,7,11,13,17,19,23,31,37,43,61,67,139,211,373,997`, with 0 failed assertions. Number arithmetic stays below (2^{53}) on this specified range.

| p | J | beta mod p | S0 mod p² | S1 mod p | Vtail/p mod p² | Vtail mod p³ |
|--:|--:|--:|--:|--:|--:|--:|
| 13 | 1 | 6 | 50 | 3 | 89 | 1157 |
| 19 | 0 | 16 | 3 | 5 | 98 | 1862 |
| 67 | 4 | 13 | 1371 | 59 | 835 | 55945 |
| 373 | 21 | 299 | 9767 | 296 | 120175 | 44825275 |

The 13,19,67 values **exactly match** the separately established nonzero signed compensators in the predecessor shortened-certificate report. At 373, the tail value here is a *portable 2304 arithmetic witness*, not the native fixed-H0/B0 experiment.

## Direct next mother-objective test

For the two frozen residue classes, consuming the prior original-source-aligned scalar interface and shortened signed transport, the open equality (C_p=V_{m tail}mod p^3) is now equivalently a requirement that the **p-divided carrier** match the explicitly reflected pair
[
oxed{rac{C_p}{p}equiv S_0+pS_1pmod{p^2}}
quad(pequiv13,19pmod{24}).
]
The division is lawful because the inherited first-digit theorem supplies (pmid C_p) on the target classes. This identity gives a candidate telescoper an exact **two-digit signed boundary specification**: (S_0) and the deformation (S_1), including Wilson quotient, factorial half-unit and Fermat quotient. The desired all-prime cancellation remains **OPEN**; the next mathematical step is to derive the carrier's adjoint/telescoping boundary and compare both displayed digits.

**BRC reuse: COMPOSE_APPLIED.** Carrier labels are ((p,k=h-j,j,mathrm{2304},v_p(b_k)=1,q_j,D_j,eta_p,8k+1)); the permitted operation is reversed-index summation followed by p-local division and reduction modulo p². This preserves the index-port inversion and signed correction (-4), avoiding a false total-only or first-digit quotient.

**Native benchmark and role boundary.** The real same-original-class p=373 H0/B0 divided-power module, ([X]Umod139129), rank, semilinear Frobenius/eta, kappa and independent replication remain `NOT_RUN / PENDING_OWNER` in Issue #1559. This note and checker constitute **AUTHOR-SIDE, UNREVIEWED, NOT_ADMITTED** evidence, not a Source-native CLAIM, run, checkpoint, frozen Result or review. Research Source and scientific pin are not mutated.

**Next exact action:** consume the two-digit reflected boundary (S_0+pS_1) inside a genuinely p-parametric telescoper/adjoint for (C_p/p); independently secure an authorized executor for the original fixed-class p373 benchmark and compare its actual operator only after authentication and rank/basis determination.
