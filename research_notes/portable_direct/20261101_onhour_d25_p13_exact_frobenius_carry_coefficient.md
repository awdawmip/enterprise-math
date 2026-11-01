# D25 / SECOND-DIGIT-LIFT — exact two-port divided-Frobenius coefficient transfer (p13 first jet)

2026-11-01 09:00 Asia/Hong_Kong · author-side mathematical continuation · **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**. This is not a Source CLAIM/open/Result/review or a native H0/B0 experiment.

Mother: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains frozen. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance lane. Reuse the earlier author-proved two-shift congruence from `20261101_onhour_d25_jacobi_two_shift_p13.md` without recrediting the prior Jacobi/CM results.

## New exact coefficient theorem (both original shift ports preserved)

Let p>7 be any prime p≡5 (mod 8), let
[
a=(5p-1)/8,quad b=(7p-3)/8,quad lambda=1/9,qquad 0<a<b<p.
]
Write ([t^r]) for coefficient extraction, and set the **single finite source polynomial**
[
mathcal P_p(t)=(1+t)^a(t+lambda)^b,qquad J_p=[t^b]mathcal P_p(t).
]
Let (K_n(x)=sum_{k=0}^ninom nkinom xklambda^k) for nonnegative integral x. Direct binomial multiplication, with no congruence and no external theorem, gives
[
egin{aligned}
J_p&=K_a(b)=K_b(a),\
K_b(a+p)&=[t^b]mathcal P_p(t)(1+t)^p,\
K_a(b+p)&=[t^{b+p}]mathcal P_p(t)(t+lambda)^p.
end{aligned}	ag{1}
]
The second shifted term is genuinely at degree b+p; changing it to degree b would lose the original K_a(b+p) source.

Define **exact integer/p-local divided Frobenius differences**
[
E_1(t)=rac{(1+t)^p-1-t^p}{p},qquad
E_lambda(t)=rac{(t+lambda)^p-t^p-lambda^p}{p}.
]
These lie in (mathbb Z_{(p)}[t]) because each interior binomial coefficient (inom pk), 1≤k<p, is divisible by p. No artificial division in the finite field occurs. Set two *separately labeled* coefficients
[
C_1=[t^b]mathcal P_p E_1,qquad
C_lambda=[t^{b+p}]mathcal P_p E_lambda.
]
Because b<p and deg (mathcal P_p=a+b<b+p), equations (1) yield the **exact rational equalities**
[
oxed{K_b(a+p)=J_p+p C_1,qquad K_a(b+p)=J_p+p C_lambda.}	ag{2}
]
This is an exact Frobenius-carry transport for the two independent parameters, stronger in precision than the prior mod-p² Taylor representation. It introduces no new axiom, new p-adic factor, or unproved CM assertion.

Consume only the previously established two-shift relation
[
8G_{eta,p}equiv 20J_p-5K_b(a+p)-7K_a(b+p)pmod{p^2},
quad
G_{eta,p}=sum_{k=0}^{p-1}rac{(1/8)_k(3/8)_k}{9^k(k!)^2}.
]
Substituting (2) gives the **new, source-explicit finite polynomial port**
[
oxed{8G_{eta,p}equiv8J_p-p(5C_1+7C_lambda)pmod{p^2}.}	ag{3}
]
Equivalently the two-shift expression is one bounded coefficient:
[
oxed{
8G_{eta,p}equiv[t^{b+p}]mathcal P_p(t)
igl(20t^p-5t^p(1+t)^p-7(t+lambda)^pigr)pmod{p^2}.}	ag{4}
]
Only equation (4)'s *terminal scalar* can be combined; the labels (J, C1, Cλ), parameter direction, p-local coefficient ring and original Gauss observer must be kept for future derivatives and signed boundary composition.

Reduction modulo p turns the divided Frobenius carriers into two distinct finite logarithm polynomials:
[
E_1(t)equivsum_{k=1}^{p-1}(-1)^{k-1}rac{t^k}{k},qquad
E_lambda(t)equivlambdasum_{k=1}^{p-1}(-1)^{k-1}rac{(t/lambda)^k}{k}
pmod p.
]
This is **not** GH98/GH99's different reflected-Green finite-log trace and does not presume its vanishing or reviewer acceptance. The coefficient identities (1)-(4), rather than that other trace, are the newly derived interface.

## Genuine remaining p13 first-jet obligation

For p≡13 (mod 24), consume the earlier *mod-p only* CM selector (J_pequiv G_{eta,p}equiv0pmod p). Therefore (3) proves the exact equivalence
[
oxed{G_{eta,p}equiv0pmod{p^2}
iff 8(J_p/p)equiv5C_1+7C_lambdapmod p.}	ag{5}
]
All divisions by p are performed in (mathbb Z_{(p)}) before reduction. **The all-prime vanishing on either side is still OPEN.** Formula (5) is a finite Frobenius-carry cancellation target with a single (mathcal P_p), not a proof of that cancellation, original 216 LIFT, or the stronger p⁴ affine conjecture. A direct next approach is to prove (5) by a CM-induced coefficient symmetry of (mathcal P_p) that transports *both* Frobenius defect ports; do not invoke a norm-only scalar shortcut.

## Independent exact executable evidence (2026-11-01)

Python 3 standard library script: `research_notes/portable_direct/d25_p13_frobenius_coefficient_port_20261101.py`; actual executed local Git blob and remotely read program blob **04c859cec358b33eb55de0c91c505172b3565096**. It separately constructs original Gauss coefficients by Pochhammer recurrence, Jacobi shifts by integer binomial sums, ([t^r]mathcal P_p) by binomial convolution, and *divided integer* binomial Frobenius carries. Its exact checks passed on all 23 primes p≤500, p≡5 mod8, for (3), plus full independent coefficient/carry checks at 13, 29, 37, 61, 109, 373.

Selected exact source readouts mod p², with carry ports mod p:

| p | J | K_b(a+p) | K_a(b+p) | C1 | Cλ | Gβ mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 104 | 91 | 39 | 12 | 8 | 0 |
| 29 | 403 | 780 | 26 | 13 | 16 | 287 |
| 37 | 555 | 740 | 666 | 5 | 3 | 0 |
| 373 | 27975 | 30586 | 77957 | 7 | 134 | 0 |

At p=13, (J/p=8) and (5C_1+7C_lambda=116equiv12=8cdot8pmod {13}). At p=373, (J/p=75) and (5cdot7+7cdot134=973equiv227=8cdot75pmod {373}). At p=29 (a different mod-24 class) (Gequiv26pmod {29}): dividing J by p is *not* permitted in this negative control. No p13 all-prime claim follows from these finite checks.

## BRC and recovery / exact unfinished work

BRC resolution **COMPOSE_APPLIED**: integer binomial coefficients, two separately typed Frobenius source ports, original coefficient order, (p)-integral divisions and terminal mod-p² observer are retained. The scalar coefficient formula (4) is licensed only for that observer; original signed 216/2304 Clausen tails and the (p^3) digit are not silently erased. These ordinary commutative-field Frobenius carries are **not** the native semilinear H0/B0 Frobenius nor Heartbeat X6/three-dimensional-slice dynamics.

Mother still (Delta_p-R_p=0mod p), equivalent to original (A_pequiv pmod p^3) for p≡13,19 mod24, not yet uniformly proved. Do NOT redo D24 UR, earlier Clausen cutoff, p19 Hensel digits, prior Jacobi two-shift (T), or earlier high-port reflection. **Next smallest unfinished mathematics:** prove or refute the *new coefficient-carry cancellation (5)* for all p13 via a genuine CM/finite field polynomial symmetry, then recombine the **original** 216 signed R port; no surrogate implies the native fixed benchmark is complete.

The separate same-original-class native p=373 benchmark [X]U mod139129, module rank, true semilinear Frobenius direction/basis eta, odd signed Hesse/Green, same-definition κ and independent replication remain **NOT_EXECUTED / PENDING_OWNER**, under existing support issue #1559. Required executor: authorized canonical Source Task/native H0/B0 operator implementer; acceptance needs raw reproducible original object and independent validation; no executor identified or claimed in this lane.

Gateway 0.6.11 in this run: Source Research write authority and executor binding not granted, own checkpoint read ACCESS_DENIED, historical `research-onhour-20261031-0205-dispatch-r15` lookup scoped CONTROL_REQUEST_NOT_FOUND. The original request has **not** been replayed; this is not proof of a new CLAIM or Source checkpoint. Session/claim/open/run none verified. Three earlier staging sources remain separate. Last source-native session/claim ownership uncertain, no replacement minted. This document is **AUTHOR-SIDE ONLY; NOT A NATIVE TASK/RESULT/REVIEW; UNREVIEWED/NOT_ADMITTED; REGISTER_PENDING/SYNC_DEBT**. P000, ACTIVE worldview, frozen scientific Source, existing scheduling and notifications were not changed.
