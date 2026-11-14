# R5 — Exact signed-error support plane and sharp all-real stopping-time interval

Date: 2026-11-07 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Provenance and scope

Continuation of the frozen four-stage P/Q-BRC observer model, NOT native X6 dynamics. Immediate scientific predecessor: awdawmip/enterprise-math commit 42ae6b7c6e4c08471a9286d959ac18f15d711c9b, research_notes/brc_r5_three_key_sharp_capacity_20261107_t1144/RESEARCH.md. Frozen scientific pins unchanged: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current normative overlay: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context; project P000, ACTIVE worldview, portable research protocol, research_priorities/research_method.json, current Global Knowledge math/output/code rules.

Mother question: equality or strict separation of unrestricted FULL_HIST and seedless LR **complete four-observer images**, W=(eP,eQ,TP,TQ). Earlier capacities concern distinct unsigned objectives. This unit solves the signed direction eQ-(1-eP)=eP+eQ-1 with **all seven LR declaration keys**, and provides a continuum of sharp symmetric stopping times.

## Exact real flow model

Let (g,a,b,u,v,w,z) be arbitrary real numbers with 0<=a,b<=g<=1 and:

- C0=13a/40+b/80; 0<=u<=C0.
- C1=a/10+9b/40; 0<=v<=C1.
- C2=3a/40+21b/80; 0<=w<=C2.
- 0<=z<=a/10; 0<=v-z<=9b/40.

Stopping times TP=1+g+(3a+5b)/8+u/2+v+3w/2; TQ=1+g+(a+b)/2+u+v+w. Seven LR stop keys r=(1/10,1/2,3/4,1,5/4,3/2,19/10); stopped Q masses:

M0=509u/900+47z/180+67(v-z)/162+w/100;
M1=C0-u;
M2=(g-a)/2;
M3=1-g+C1-v+191(u+w)/450+43z/90+14(v-z)/81;
M4=(g-b)/2;
M5=C2-w;
M6=u/100+47z/180+67(v-z)/162+509w/900.

Choose declarations 0<=Ej<=Mj. Observations eQ=sum Ej and 1-eP=sum rj*Ej. Seedless LR is a FULL_HIST subclass with one common central-node continuation; for positive branches its algebraic relation is 9*b*z=4*a*(v-z).

## Theorem A — universal four-observer support plane

For ALL real legal FULL_HIST timing and declaration policies, including every seedless LR policy,

**eP+eQ-1 <= 13269/53000 + (391/6625)(TP-31/10) + (364/6625)(TQ-31/10).**  (A)

Proof: Let S=(9/10)M0+(1/2)M1+(1/4)M2. The only positive signed declaration coefficients 1-rj occur at keys 0,1,2. In fact

S-(eP+eQ-1)
=(9/10)(M0-E0)+(1/2)(M1-E1)+(1/4)(M2-E2)
 +(1/4)E4+(1/2)E5+(9/10)E6 >= 0.       (B)

Direct exact substitution into the frozen mass/time expressions gives this **identity for all seven arbitrary real flow variables**:

13269/53000 + (391/6625)(TP-31/10)
 + (364/6625)(TQ-31/10) - S
 = (117/10600)(1-g)
 + (3999/53000)u
 + (1283/10600)(C1-v)
 + (7127/53000)w
 + (247/1800)(9b/40-v+z).               (C)

All five terms on the right are nonnegative by legality. Combining (B),(C) proves (A) for all real policies. The executed Fraction checker checks the affine identity at the origin and seven basis vectors, an algebraically sufficient identity certificate. Rational sample policies are not used to infer the all-real quantifier.

## Theorem B — sharp for every symmetric stop time in a full interval

For **every real 2<=t<=133/40**, both unrestricted FULL_HIST and unrestricted seedless LR have exactly the same extremum:

**max_{TP=TQ=t} (eP+eQ-1) = 1/8 + (151/1325)(t-2).**  (D)

For the lower bound, define r=40(t-2)/53 in [0,1] and choose

(g,a,b,u,v,w,z)=(1,r,r,0,13r/40,0,r/10).

Then C1=13r/40=v, z=a/10, v-z=9b/40. Both central histories continue fully, so this policy is seedless LR, including degenerate r=0 by the direct zero-capacity interpretation. The third-stage other-node continuation probabilities are zero. Its exact observations are TP=TQ=2+53r/40=t. The seven stopped Q masses are

(M0,...,M6)=(143r/1200,27r/80,(1-r)/2,13r/150,(1-r)/2,27r/80,143r/1200).

They are nonnegative, sum to 1 and have likelihood-ratio first moment 1 for every real r in [0,1]. Declare E0=M0, E1=M1, E2=M2, all remaining Ej=0. Then

eQ=1/2-13r/300; eP=5/8+583r/3000;
eP+eQ-1=1/8+151r/1000=1/8+(151/1325)(t-2).

This attains the global FULL_HIST upper bound (A) at TP=TQ=t and proves (D) over the entire real interval, including irrational times/endpoints. At t=31/10, r=44/53 gives **W=(2359/3000,3689/7950,31/10,31/10)** and **max(eP+eQ-1)=13269/53000**.

**Rigidity.** All five coefficients in (C) are strictly positive. Equality forces g=1,u=w=0,v=C1,z=a/10. Setting TP=TQ then forces a=b=40(t-2)/53, so the equality timing flow is unique. Equality in (B) forces E0=M0,E1=M1,E2=M2 and E4=E5=E6=0. E3 is free within its capacity (its coefficient in the signed functional is zero), so declaration uniqueness is not asserted.

## Common real observer region

For every r in [0,1] and t=2+53r/40, both classes realize the full set

W=(1-x/10-y/2-3s/4, x+y+s,t,t),

where 0<=x<=143r/1200, 0<=y<=27r/80, 0<=s<=(1-r)/2. This is the image of one fixed seedless timing policy under all three independent declaration probabilities, a shared two-error-coordinate zonotope. It is a certified **common subset**, not complete image equality.

## Validation, authority and next research dependency

Companion VERIFY.py was executed with Python Fraction and no floating optimization. It checks affine identity on 8 basis samples, 54 rational equality flows, seven mass normalization and first-moment constraints, all-real seedless construction's exact formulas, the sharp W at 31/10 and 128 additional seven-key declaration samples. EXACT_OUTPUT.txt is the actual stdout. The universal theorem follows from analytic (B),(C), not from finite testing.

The unresolved mother problem remains complete four-observer FULL_HIST vs seedless LR equivalence/separation. Move to perturbed signed directions alpha*eQ+beta*(1-eP), retain the nonlinear common-central relation and globally reoptimize early continuation flows; see NEXT_UNIT.md.

Author-side evidence only. Actual GitHub actor: awdawmip; administrative repository push permission is not native Task ownership. Native Enterprise Math status/tasks returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false. Current Owner, formal CLAIM, independent review and mathematical admission are unconfirmed. No credential or sharing change.
