# R81 — Arbitrary-degree graded tomography for X6 ordered BRC observations (AUTHOR-SIDE DRAFT)

Date: 2026-10-16. Status: LOCALLY_VERIFIED / UNREVIEWED / NOT_ADMITTED. This is an independent research note, NOT a formal Task Result, Researcher activity record, ownership CLAIM or Driver acceptance.

Frozen global: awdawmip/chatgpt-global-knowledge@d433f2cbd7e5b458833de3be8db56a8a9b1430d9 (GLOBAL_KNOWLEDGE_V1). Frozen Enterprise Math source: awdawmip/enterprise-math@b7cfee92fd89b145cdfdbc40a31df334271ef0f1. P000 ACTIVE_LOCKED, six native spatial axes; independent time. Builds on R79/R80 author-side ordered observer; upstream results are not treated as admitted.

## Objects

For a signed native X6 path w=(epsilon_j e_{i_j}), define the auxiliary ordered integer observer S_M(w)=PRODUCT_j(1+epsilon_j X_{i_j}) in Z<X1,...,X6>/(Xi^2, degree>M). Write T_k(w) for its homogeneous degree-k component. This is an explicitly typed observer over ordered, positive-rational BRC paths; signed polynomial coefficients are NOT signed/negative BRC branch masses. T_k(uv)=SUM_{j=0}^k T_j(u) T_{k-j}(v).

For distinct a,b choose the genuine four-step closed path c_ab=(+a,+b,-a,-b), and C_ab=XaXb-XbXa. Direct multiplication gives S(c_ab)=1+C_ab-XaXbXa+XbXaXb+XaXbXaXb.

## Theorem 1 — one calibrated probe, all degrees

For every integer d>=1 (with M>=d+2),

T_(d+2)(w c_ab) - T_(d+2)(w)
 - T_(d-1)(w)(-XaXbXa+XbXaXb)
 - T_(d-2)(w)XaXbXaXb = T_d(w) C_ab.

Right multiplication by C_ab is injective on every homogeneous degree d component. To recover coefficient [u]T_d for a legal word u, read coefficient [uab] of the right-hand side when last(u)!=a; otherwise read -[uba]. No other prefix or opposite suffix contributes and the selected boundary is not killed by Xi^2. Therefore ONE probe together with current degree-(d+2) baseline and degree-(d-1),(d-2) slices reconstructs every degree-d coefficient.

## Theorem 2 — FOUR baseline-free probes, all degrees

For (sa,sb) in {+1,-1}^2 set c_ab^(sa,sb)=(sa*a,sb*b,-sa*a,-sb*b). Exact expansion:
S(c_ab^(sa,sb))=1+sa*sb*C_ab - sb*XaXbXa + sa*XbXaXb + XaXbXaXb.

Four-character orthogonality yields:

SUM_(sa,sb) sa*sb*T_(d+2)(w c_ab^(sa,sb)) = 4*T_d(w)*C_ab.

This does NOT require T_(d+2)(w) or ANY lower-degree baseline. Every output coefficient is divisible by 4 and the same explicit suffix left-inverse reconstructs T_d in integers. These four probes are a sufficient upper bound only, with NO minimality claim. When the observer supplies the full truncation through M, these same four post-probe observations recover every T_d for 1<=d<=M-2.

CYCL legality: for a nonempty cyclically freely reduced closed w, choose a,b distinct from the supports of its first and last steps. Six native axes always leave at least four choices. All four sign variants remain CYCL after concatenation and preserve net displacement 0. For strictly positive exact native direction masses q_i^+/q_i^-, every variant has identical positive weight m(w) q_a^+ q_a^- q_b^+ q_b^-. The signed character combination acts ONLY on observer values.

## Nonzero exact witnesses

10-step native CYCL word w=(+1,+2,+3,-2,-3,-1,+3,+2,-3,-2) has [123]T3=1, [1231]T4=-1 and [12321]T5=1. With (a,b)=(4,5), the four signed post-probe sums at output coefficients 12345 / 123145 / 1232145 are exactly +4 / -4 / +4. This tests genuinely nonzero quartic and quintic slices, not just R80's specially zeroed ones.

## Actual finite verification / evidence limits

Independent Python integer certificate: 22 distinct genuine CYCL zero-displacement words (8 signed 10-step variants, 12 closed 12-step six-axis signed words, the R80 40-step collision pair); 28 path/probe pairs verified at d=1..5 (140 identities), and 3 further path/probe pairs verified through d=8 (24 identities); 31 actual pair instances total. Tested full sparse polynomials and explicit integer suffix left inverse, not merely selected outputs; 4650 coefficients additionally checked by independent ordered-subsequence DP. Frozen native BRC kernel Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176 executed for exact short return counts 1,12,396 and positive rational branch masses. Self-contained evidence ZIP: EM_X6_R81_UNIFORM_GRADED_TOMOGRAPHY_20261016.zip, SHA256 d52ed3b367f98564fec3750478547bb68b20c182a27d944d027b6b71640d1366 (local attachment, not claimed to exist in repository). Local outputs: R81_VERIFY_PASS; R81_MANIFEST_PASS; R81_COLDSTART_PASS. General all-degree theorem follows from the written polynomial proof; finite computation does NOT enumerate arbitrary words or prove a real physical sensor.

## Native control state and exact continuation

Own service session_start returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Canonical live task/owner inventory returned CONTROL_QUOTA. Therefore current active owner not established; no winning CLAIM, research activity, formal Source Result or independent Driver review was obtained. This file is an author-side preserved draft only; never count this branch as official Researcher activity or admission.

Next: in the full-postprobe T_(d+2) and no-baseline protocol, determine whether TWO or THREE four-step probes suffice, with a true collision if proving necessity. Distinguish adaptive axes and source-word reproducibility. With permitted Source session and winning ownership, publish exact proof and executable evidence by native research protocol, preserve original contribution identity and obtain independent review.
