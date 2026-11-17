# R244 — Uniform rational error certificate for the two-leading-mode source observer

Date: 2026-11-17 (Asia/Shanghai). Evidence: AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / NOT_REVIEWED.
Native typed BRC EffectHistogram: NOT_EXECUTED. Formal Task CLAIM/Result/Review: NONE.

## Provenance, frozen science and model

This independent portable scientific unit continues the existing exact work:
- R243: awdawmip/enterprise-math@ef38804fff510da663a49202e4cac8060f2082c8:research_notes/portable_direct/R243_OPTIMAL_PARAMETER_UNIFORM_FIRST_HORIZONS_20261117.md (uniform single-mode horizons 752/1128, three spectral tiers and exact constants).
- R242: awdawmip/enterprise-math@6427030e552a22824a5fc5a9608826890650039b:research_notes/portable_direct/R242_EXACT_RATIONAL_ANCHOR_FIRST_HORIZONS_20261117.md.
- Frozen scientific input (unchanged): awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Fix the real parameter 39/100<s<41/100 and the seven-source strictly positive stationary reversible sticky-reset chain with alpha(s), b(s), pi(s), rho(s) defined in the exact R243 statement. For each proper nonneutral mask U subsetneq {1,...,6}, D_U={0} union U and K_D is the detailed-balance symmetric positive-definite killed transition. The positive scalar source-support principal-ideal observable has spectral form

Phi_n = sum_U W_|U| rho_D^T P_D^(n-1) 1 = sum_j c_j lambda_j^(n-1), n>=2,

with c_j>=0 and 0<lambda_j<1. This is a *derived scalar observer*, not a quotient of P000 native X6 signed directions, ports, source provenance or cross moments.

Call mask 59 (missing nonneutral source 3) the dominant block, with leading eigenvalue r and positive amplitude A. Call mask 55 (missing source 4) the second block, with leading eigenvalue beta and positive amplitude B. For k=n-1, define the two-Perron-mode approximation

X_n = A r^k + B beta^k,
R_n^[2] = Phi_n - X_n,
E_n^[2] = R_n^[2]/X_n.

The constant baseline W_6 of the original ideal-size expectation is unchanged: the two-mode formula approximates its nonconstant tail Phi_n.

## Theorem (strict positive two-mode residual and uniform certificate)

For every real s in (39/100,41/100) and every integer n>=2,

0 < E_n^[2](s) < H_n := (1681/8400) ( (977/1000)/(990628/1000000) )^(n-1)
                    + (4304034541601/625660815360) ( (973/1000)/(990628/1000000) )^(n-1).

Consequently E_n^[2](s)<1/100 for all n>=372 and E_n^[2](s)<1/1000 for all n>=505. The two integers are the *first thresholds certified by this particular explicit H_n bound*, not asserted as the model's sharp first-crossing horizons. R243's exact optimal uniform **single**-mode horizons were 752 and 1128.

### Proof

R243's finite-rational spectral tier certificate supplies the following facts on the *entire real parameter interval*:
1. r(s)>r_0=990628/1000000; the one-Perron amplitude is A(s)>0.
2. The full killed block G with mask 51 (missing both sources 3 and 4) has spectral radius below Gamma=977/1000. Its total positive spectral mass M_G satisfies M_G/A < c_G=1681/8400.
3. After removing the *full* G block and the leading Perron modes Ar^k and B beta^k of masks 59 and 55, every retained eigenvalue is below Delta=973/1000. In particular the subleading eigenvalues of 59 and 55 are below 4/5<Delta.
4. The sum T of all positive spectral weights of Phi_n satisfies T/A<c_0=8424836672439/1042768025600.

Each spectral mass is nonnegative. The G block has at least its positive Perron coefficient, so the residual is strictly positive. The other mass after removing G, A and B is T-M_G-A-B>=0. Hence

0<R_n^[2] <= M_G Gamma^k +(T-M_G-A-B) Delta^k.

Since X_n>=Ar^k, put q_G=Gamma/r_0 and q_D=Delta/r_0 (both in (0,1), q_D<q_G). Dividing by Ar^k and enlarging bases gives

E_n^[2] <= (M_G/A)(q_G^k-q_D^k)
             +(T/A-1-B/A)q_D^k
         < c_G q_G^k +(c_0-1-c_G)q_D^k = H_n.

The strict final inequality follows from positive B and R243's strict mass bounds. The rational coefficient has the exact identity

c_0 - 1 - c_G = 4304034541601/625660815360 >0.

Thus H_n decreases strictly in n. The accompanying pure-stdlib Python 3 Fraction checker computes the exact rational margins 1/100-H_372>0 and 1/1000-H_505>0, and additionally H_371>=1/100, H_504>=1/1000, with no float decision. Monotone decay of H_n establishes every later n. QED.

## Verification and interpretation

Run: python3 R244_two_mode_uniform_tail_check.py > R244_verification.json

The program is an **exact finite verification of the new rational H_n comparison**. All-real mathematical coverage relies additionally on the stated R243 spectral-tier inequalities and positive-spectrum decomposition; they were not re-executed from Markov matrices in this R244 script. The verifier's decimal fields are diagnostic only, with PASS driven by Fraction/integer inequalities. Positive-margin integer SHA256 hashes and bit-lengths are retained in the JSON.

This is an independently derived, second-Perron-mode *theoretical* observer with certified absolute error relative to X_n. Extracting A(s), B(s), r(s), beta(s) at a specified input still has exact algebraic/precision cost. No algorithmic speedup over 230-order recurrence or 256-state propagation is asserted without end-to-end bit-cost accounting.

## Next work

- Construct certified algebraic enclosures for beta(s), B(s) and derive sharper two-mode bounds retaining each block's actual residual mass.
- Determine the true (rather than H_n-certified) parameter-uniform two-mode first horizons, possibly by rational subdivision and an analytic monotonicity argument.
- Compare preprocessing, root isolation, amplitude evaluation, rational bit growth and output recovery against 230-order recurrence and 256-state exact propagation.
- Build a read-only native BRC EffectHistogram interface while retaining signed direction, port/source/provenance, exact rational weight, branch multiplicity and cross moments. This scalar analysis does not replace those types.

Review: NOT_REVIEWED. Project mathematical admission: NOT_CLAIMED.
