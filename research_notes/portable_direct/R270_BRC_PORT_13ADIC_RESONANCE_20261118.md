# R270 — Exact 13-adic resonance obstruction in typed BRC port observers

2026-11-18 | AUTHOR_PROVED / EXACT_RATIONAL_CHECK / NOT_REVIEWED
Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Independent portable research; no formal CLAIM. Frontier: R269@5d54f69348795cb229dd568ed64e89e54c0d9f18. Native tool/theorem: WBRC-T30..T32 in definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md.

## Exact model
Take a stable finite-positive-rational one-port BRC module with no hidden node: W=[w], 0 <= w < 1; the effective port signature is W_eff=[w]. A WBRC-T31 context may add a rational nonnegative port self-loop r, provided w+r<1. The WBRC-T30 visible star is S_r(w)=1/(1-w-r). This is a **real admitted typed BRC operation**, not an assumption that R269's auxiliary scalar recurrences are native BRC ports.

Let Z_(13) be rationals with denominators prime to 13, rho_{13^N} their modular reduction.

## Theorem 1: exact nonresonant reduction
If w,r are 13-integral and delta=1-w-r is a 13-adic unit, then rho_13(S_r(w))=[1-rho_13(w)-rho_13(r)]^{-1}. Proof: reduction is a ring homomorphism preserving inverses of units.

## Theorem 2: stable resonant counterexample
Set w0=1/5, w1=33/100 and r=27/50. Both w_i+r<1 and rho_13(w0)=rho_13(w1)=8. Nevertheless:
1-w0-r=13/50, S_r(w0)=50/13;
1-w1-r=13/100, S_r(w1)=100/13.
The normalized 13-integral star readouts are rho_13(13 S_r(w0))=11 and rho_13(13 S_r(w1))=9. Initial mod-13 mass data fails to determine this permitted future port-context/star observer. Exact W_eff distinguishes these modules.

## Theorem 3: no uniform fixed 13-adic depth for all rational contexts
For each integer N>=1 put P=13^N, M=100P+1 and
w0=1/5, w1=1/5+P/M, r=4/5-2P/M.
All are rational nonnegative and strictly stable since 0<P/M<1/100. M is a 13-unit, so w0=w1 (mod P). Yet
1-w0-r=2P/M, 1-w1-r=P/M;
P S_r(w0)=M/2, P S_r(w1)=M.
Consequently rho_13(P S_r(w0))=7 while rho_13(P S_r(w1))=1, since M≡1 and 2^{-1}≡7 mod13. These exact identities prove the claim for all N, irrespective of finite testing.

## Theorem 4: sharp local repair with known resonance depth
For delta=1-w-r in Z_(13), delta≠0 and known valuation v_13(delta)=t>=0, the observer R_t=rho_13(13^t/delta) is determined by delta mod 13^(t+1):
R_t=(delta/13^t mod13)^{-1}.
Proof: write delta=13^t*u with u a 13-unit; t+1 digits give u mod13. This precision is sharp: Theorem 3 for N=t>=1 gives two stable inputs agreeing modulo 13^t but different R_t; for t=0 the single digit is both sufficient and generally necessary.

## Precisely typed bridge to R269
Let F be R269's 6474-profile auxiliary value-function closure and M the set of these BRC one-port modules. On the declared product carrier (q,w), take H_N(q,w)=(q,rho_{13^N}(w)); fix q equal across the two witnesses. H_N is insufficient for the explicitly permitted future BRC port context plus normalized star readout. This establishes failure of **observer factorization** through H_N; it does not claim failure of q's own transition congruence or a source-generated native map. For all WBRC-T31 port contexts, the exact WBRC-T32 signature W_eff is sufficient. Ports, source labels, branch history, six-axis X6 native dimensions and provenance remain distinct, following P000 and joint-relation retention.

## Reproducibility and next question
Python stdlib Fraction exact checker accompanies this note. Independent local exact arithmetic checked the explicit witness and N=1..8, PASS, 2026-11-18. Local full JSON SHA-256: 24a2518a15aeb1ba5f1ed73089c5df429fc9b44aa1788a090a19cfcecb02a193. All-N statement is a separate symbolic proof. Scientific independent review is NOT_REVIEWED.

Next: derive an adjugate/determinant multi-port precision bound for selected entries of (I-W_eff-C)^{-1} under bounded p-adic determinant valuation, preserving labeled ports. Separately search for an actual source-generated map from R269 profile carriers to typed BRC port signatures and test its observer/fiber conditions.