# D25 / 2026-11-02 — full-truncation Picard–Fuchs endpoint, all prime-power lengths

**Status:** AUTHOR-DERIVED / EXACT PROOF / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0. This is an author-only neutral research note, **not** a formal Source checkpoint, CLAIM, execution, Result or review. Scientific source pin remains `c47e13e4aba0e006366f989d6334d443f6333ae3`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Research logical lane is `chatgpt-research-onhour-enterprise-math-20260923`, not the maintenance lane. No Source-registered identity is asserted.

## Exact theorem

Fix any prime p>3 and integer r>=1; put N=p^r, theta=z d/dz, and work with the p-integral rational polynomials

[
a_k=rac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}
=rac{inom{2k}{k}^2inom{3k}{k}}{108^k},qquad F_N(z)=sum_{k=0}^{N-1}a_kz^k,
]

[
b_k=rac{(1/4)_k(1/2)_k(3/4)_k}{(k!)^3}
=rac{inom{4k}{2k}inom{2k}{k}^2}{256^k},qquad H_N(z)=sum_{k=0}^{N-1}b_kz^k.
]

Define the operators (mathcal L_A=	heta^3-z(	heta+1/2)(	heta+1/3)(	heta+2/3)), (mathcal L_B=	heta^3-z(	heta+1/4)(	heta+1/2)(	heta+3/4)). Then, **as exact rational polynomial identities**,

[
oxed{mathcal L_A F_N=-N^3 a_Nz^N,qquadmathcal L_B H_N=-N^3b_Nz^N.}
]

Moreover, for **every** p>3 and r>=1, (a_Nequiv1/9pmod p), (b_Nequiv3/32pmod p), both units. Consequently the endpoint source coefficients have **exact** p-adic valuation 3r. Thus both full truncated equations are homogeneous modulo p^(3r), but have nonzero sources modulo p^(3r+1):

[
mathcal L_A F_Nequiv-(p^{3r}/9)z^N,qquad
mathcal L_B H_Nequiv-(3p^{3r}/32)z^Npmod {p^{3r+1}}.
]

At the **two original model arguments**, where (W_p=(1+6	heta)F_p(1/2)), (S_p=(1+8	heta)H_p(1/9)),

[
oxed{(mathcal L_A F_N)(1/2)equiv-p^{3r}/18,quad
       (mathcal L_B H_N)(1/9)equiv-p^{3r}/96pmod{p^{3r+1}}.}
]

The ratio of these **two specifically typed differential defects** is (16/3mod p), *not* a proved isogeny period or native Frobenius transfer factor.

### Proof and checkable integer origin

The term recurrences give (n^3a_n=(n-1/2)(n-2/3)(n-1/3)a_{n-1}) and (n^3b_n=(n-3/4)(n-1/2)(n-1/4)b_{n-1}). The interior coefficients cancel under their displayed operators; at the unique omitted degree z^N, the remaining coefficient is -N^3a_N or -N^3b_N. For N=p^r, Lucas gives (inom{2N}{N}equiv2), (inom{3N}{N}equiv3), (inom{4N}{2N}equiv6mod p). Fermat gives (108^Nequiv108), (256^Nequiv256mod p), hence (a_Nequiv12/108=1/9), (b_Nequiv24/256=3/32mod p). Their preceding coefficients have exact valuation 3r because all three factors N-alpha are p-units. Also ((1/2)^Nequiv1/2), ((1/9)^Nequiv1/9mod p). This proves the two special-point defects.

The computation independently evaluated the four original integer-binomial coefficients `a_(N-1),a_N,b_(N-1),b_N` modulo p^(3r+1), verified their boundary recurrences and the evaluated ODE source. **12/12 exact cases passed:** p=5,7,13,19,37 with r=1,2; p=373,1171 with r=1. For p=373, p^3=51895117, p^4=19356878641: original-point defects are 7524791965=145 p^3 and 12299142729=237 p^3, with ratio 254 (mod 373). For p=1171 the leading digits are 65 and 1110. Finite checks support, but are not the proof.

## Impact, provenance and actual remaining work

The original mother task is still (Delta_p-R_p=0mod p) for p=13,19 (mod24), equivalently (W_pequiv pmod p^3) under the frozen accepted UR and *signed* Clausen source identity. This theorem **does not prove LIFT or W-S**. It establishes a sharp formal-boundary fact: modulo p^3, the **full** unweighted original model differential equations have no truncation source, whereas the previously analyzed **reflected sub-tail** has a nonzero mod-p endpoint source. These are different source objects. At p^4 the full source reappears and must not be erased. Preserve both weighted derivative ports, the signed cutoff Q, the CM twist and the odd Hesse/Green observer.

**Next exact science:** derive or disprove a p-adic horizontal/Gauss–Manin or finite WZ transfer that matches **both weighted observables** at their CM points modulo p^3 and directly yields (W_p-S_p=0mod p^3) or (Delta-R=0mod p). A common j, a scalar ODE residual, or more numerical examples does not suffice. Earlier accepted CM0/SIMPLE/UR, reflected source-port identity, Wilson decompositions, gauge analysis and zero-fiber fourth-digit witnesses are not reopened.

The **original native fixed373** H0/B0 divided-power `[X]U mod 139129`, rank, actual semilinear Frobenius eta, signed odd Green/Hesse, kappa, and independent reproduction are still NOT_EXECUTED/PENDING_OWNER via `awdawmip/enterprise-math#1559`. Do not equate the ordinary Hesse candidate norm 122102 with the native coefficient without original-class rank and normalization evidence.

Control status read this run: Sites gateway 0.6.11 reports `research_authority_granted=false`, `executor_binding_configured=false`, `UPSTREAM_CODE_REVIEW_REQUIRED` and 5/5 active native jobs. Prior request `research-onhour-20261031-0205-dispatch-r15` ended FAILED (recorded in `awdawmip/kimi-query-bridge#6633`); it was not reissued. No active own session, claim, run or Source checkpoint is claimed; this neutral Git note is **evidence persistence only**, subject to independent review and formal intake.
