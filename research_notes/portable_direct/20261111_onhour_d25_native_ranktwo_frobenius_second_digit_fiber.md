# D25 / JT2 — Rank-two unramified Frobenius second-digit lift fiber (fixed-basis diagnostic)

2026-11-11 Asia/Hong_Kong. Classification: AUTHOR_SIDE / EXACT_ALGEBRAIC_LEMMA / FINITE_EXECUTED_CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source: awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. This note is from the declared Research-onhour logical lane chatgpt-research-onhour-enterprise-math-20260923, not a Source session/CLAIM/RESULT, and uses no maintenance Researcher/Driver identity.

## 1. Selected exact unsolved native issue

Issue #1559 requires the same-original-class fixed H0/B0 divided-power representative [X]U modulo 139129 at p=373, actual module rank and semilinear Frobenius direction, normalization eta, full signed odd Green/Hesse and kappa, original Delta-R and independently executable evidence. At the 2026-11-11 03:00+08 read, the Issue remained OPEN without an assigned executor. The actual native benchmark is NOT_RUN. Prior author-side p373 norm 122102 is a conditional ordinary Hesse comparator, not [X]U.

The new narrowly scoped question is whether a verified raw rank-two geometric q-Frobenius identity, even with a full mod-p matrix, determines the required p² matrix digits in a fixed native basis. The following exact fiber answers this question and gives a concrete independent native-acceptance discriminator. It complements the previously recorded rank-one normalizer fiber (Issue #1559, comment 6408805147); it does not retest or recredit that result.

## 2. Exact algebraic classification

For p odd with (2/p)=-1 (in particular p=13 or 19 mod 24), define the unramified ring

  R_2 = (Z/p² Z)[T]/(T²-2),   sigma(a+bT) = a-bT,

and let sigma act entrywise on matrices. Work in one specified, fixed, two-column basis. Take the model raw p-Frobenius base lift

  F_* = [[0, 1], [p, 0]],     F_* sigma(F_*) = p I.

Let F be ANY 2x2 matrix over R_2 whose mod-p entries equal F_* modulo p. Write F=F_*+p X with X entries in R_1=F_(p²). The following is an if-and-only-if classification:

  F sigma(F) = p I (mod p²)

  iff

  F = [[-p sigma(d), 1+p b], [p, p d]] (mod p²)

  for unique b,d in R_1.

Thus the same mod-p operator, the same exact q-Frobenius square and the same specified basis labels admit precisely p^4 distinct two-digit matrices. Distinct means distinct matrices in this FIXED basis; no claim that the operators represent distinct gauge/isomorphism classes is made.

Proof: Put N=F_* mod p=[[0,1],[0,0]], and X=[[a,b],[c,d]] over R_1. Expand the exact two-digit relation:

  F sigma(F) = p I + p [N sigma(X) + X N] (mod p²).

The bracket is [[sigma(c), sigma(d)+a],[0,c]]. It vanishes iff c=0 and a=-sigma(d); b,d are free. Uniqueness follows from the unique mod-p matrix X, and |R_1|=p², giving p^4 possibilities. Conversely substitution gives p I modulo p². This is the complete proof.

Corollary (conditional native discriminator): if an authenticated fixed H0/B0-to-original-E3 comparison actually identifies a rank-two *raw* integral semilinear F with the unmodified original q-Frobenius sign F sigma(F)=+p I and the above mod-p normal form, then a q-Frobenius square and mod-p coefficient alone cannot recover the two-digit upper/right or diagonal signed source ports. The actual [X]U/eta/operator normalization must be measured and source-pinned, not inferred from a scalar norm or F². An arbitrary native F might use a different basis, twist, covariant convention or normalization; establish the actual typed comparison before using this test.

The ring sigma(T)=-T is a coefficient-field automorphism, not the pointwise map T -> T^p modulo p². The full signed source observer remains separate from this matrix diagnostic.

## 3. Executed exact verification

The companion standard-library checker d25_native_ranktwo_sigma_lift_fiber_20261111.py executes matrix multiplication in R_2, Frobenius conjugation and complete enumeration of all p^4=625 model matrices at p=5 (where 2 remains nonsquare). Every one satisfies F sigma(F)=p I modulo p², shares N modulo p, and is distinct. At p=373 it compares two different models:

  F_0 = [[0,1],[373,0]],
  F_1 = [[138756+373 T, 1+373 T],[373,373+373 T]],  mod 139129.

Both have q-Frobenius square +373 I modulo 139129. The negative sign control [[0,1],[-373,0]] fails the +373 I check. The p373 matrices are explicit MODEL WITNESSES, not observed native operators. Exact checker output:

  p5_distinct_fixed_basis_lifts = 625
  p373_modulus = 139129
  same_q_frobenius = True
  native_h0b0_run = False

## 4. BRC observer audit and true next action

BRC resolution: COMPOSE_APPLIED, reusing source-index / Frobenius/valuation precision typing and the previous p² normalizer distinction. Population is fixed-basis sigma-semilinear matrices over R_2. Operation is F -> F sigma(F). The p² digits (b,d) are preserved repair coordinates; the quotient to (F mod p,F sigma(F)) loses a fiber of size p^4. This is an exact finite-ring fiber result with fixed declared future operations, not an arithmetic positivity or native-X6 physical interpretation.

Source state: Issue #1559 original-class H0/B0 still NOT_RUN / PENDING_OWNER. Its authorized owner/CodeX mathematical implementer must obtain the original fixed divided-power representative (not ordinary Hesse), compute [X]U mod 139129, identify module rank/basis/semilinear direction/eta and full signed Green/Hesse kappa, record executable raw data and independent replica. Where—and ONLY where—the actual comparison establishes the stated rank-two raw +p normalization, the above model is a sanity/identifiability check. The native objective's original input, acceptance and frozen scientific pin remain unchanged.

Exact continuation: consume previously read Research-onhour request onhour11-20261111-0204-exact-cont = SUCCEEDED; no queued action to duplicate. Current direct gateway recovery_status once returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED, with no authenticated same-lane winning CLAIM or open run. Do not register, claim, open or dispatch under maintenance conversation; preserve original requests, predecessor frontier and contribution history. This author artifact is not a native checkpoint or a Result. Next permitted control action is authenticated own-session recovery and exact continuation; until then, preserve the support ticket and current pending owner without claiming execution.

Scientific next action remains actual fixed p373 native [X]U and its provenance. Any accepted external coefficient/fiber comparison requires fresh native data, signed observer and independent reproduction.
