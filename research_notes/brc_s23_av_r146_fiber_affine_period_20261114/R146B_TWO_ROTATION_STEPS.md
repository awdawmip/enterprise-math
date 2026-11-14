# R146B — Two rational rotations govern every single-coefficient fiber change

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scope: external tied-phase scalar S23 mechanical words. Status: author-side exact proof; independent review NOT_REVIEWED.
Dependency: R146 exact fiber count in sibling `PROOF.md`, and only its explicit definitions.

Fix `m>=1`, a finite Sturmian word `w`, an integer `K>=2`, and `L=K-1`. Use R146's reduced endpoints `alpha=a/b<beta=c/d`, phase intercept endpoint values `u_alpha` and `ell_beta`, and
[
 A_L=Lalpha-u_alpha,qquad B_L=Leta-ell_eta.
]
The phase-index multiplicity is `C_w(K)=ceil(B_L)-floor(A_L)-1`.

## R146B.1 — Exact signed jump law

Define the two explicit `0/1` integer sequences
[
 I_A(L)=egin{cases}1,&alpha>0	ext{ and }{A_L}ge1-alpha,\0,&	ext{otherwise},end{cases}
]
[
 I_B(L)=egin{cases}1,&eta>0	ext{ and }igl({B_L}=0 	ext{or} {B_L}>1-etaigr),\0,&	ext{otherwise}.end{cases}
]
Both use exact rational comparisons; equality at `1-beta` belongs to the *zero* case of `I_B` unless `{B_L}=0`.

Then, for every admissible `w,m,K`:
[
 oxed{C_w(K+1)-C_w(K)=I_B(L)-I_A(L)in{-1,0,1}.}	ag{7}
]

**Proof.** R146 gives
[
Delta C=igl(lceil B_L+etaceil-lceil B_Lceiligr)-
         igl(lfloor A_L+alphafloor-lfloor A_Lfloorigr).
]
Since `0<=alpha<beta<=1`, the latter parenthesized increment is exactly `I_A` and the former exactly `I_B`, by the definitions of floor and ceiling at rational endpoints. QED.

**Presence/disappearance consequences.** If `C_w(K)>=2`, the word necessarily remains present at `K+1`. Disappearance in one coefficient step occurs **exactly** when `C_w(K)=1`, `I_A(L)=1`, `I_B(L)=0`. Recovery from absence in one step occurs **exactly** when `C_w(K)=0`, `I_A(L)=0`, `I_B(L)=1`. These are exact necessary and sufficient criteria, not heuristic event interpretations.

## R146B.2 — Per-period crossing conservation

Let `P=lcm(b,d)` and `Q=P(beta-alpha)` as in R146. Then for every base `L>=1`,
[
oxed{sum_{j=0}^{P-1}I_A(L+j)=Palpha,qquad
       sum_{j=0}^{P-1}I_B(L+j)=Peta.}	ag{8}
]
These are nonnegative integers; their difference is `Q>=1`. Both equalities follow by telescoping the corresponding integer floor/ceiling sequences across `P` steps, since `P alpha` and `P beta` are integers. Thus a whole period has an exact *net gain* of `Q` phase-index blocks even if individual steps lose one.

## R146B.3 — Finite last-absence reduction

Because `C_w(L+P+1)=C_w(L+1)+Q>=1` for every `L>=1`, every absent coefficient `K=L+1>=2` has `1<=L<=P`. Therefore the exact permanent coefficient for a fixed word can alternatively be written
[
 oxed{T_w=2+maxigl({0}cup{1le Lle P:C_w(L+1)=0}igr).}	ag{9}
]
This finite-period expression is a complementary certificate to R143's more efficient denominator-`b` residue algorithm; it directly displays why all later coefficient cycles remain present.

## Exact finite verification

Companion `check_r146b.py` imports `check_r146.py`, enumerates all finite Sturmian words for `m=1..11`, and compares both sides of (7) using exact `Fraction` at `L=1,2,3,10,31,100,10^70+321`. It checks every (8) over all `P` phases for each word. Observed: 636 word records, 4,452 single-step comparisons, 636 complete-period checks, 338 one-step disappearances and 484 recoveries in the selected finite sample; net step counts `(-1,0,+1)=(572,2844,1036)`. Signature: `R146B_TWO_ROTATION_STEP_PASS`. These finite checks corroborate the universal floor/ceiling proofs.

Next line: combine (7) with R139B's last disappearance to isolate which non-extremal word supports can possess a lone integer phase block at the conjectured threshold `E(m)`. This may yield a direct all-length covering proof or a precise arithmetic counterexample without scanning event atoms.
