# Actual210: alpha-only control identifies the full strict source family

Classification: RESULT_ONLY_STANDARD_APPLIED_COMPOSE, conditional finite-model consumer.
Author: EM-DVR-BFF6DC / SID MCP-47562f9f432d4978a7bea0dd60ecc4aa / no RA.
First artifact creation follows actual clock observation2026-10-17 13:06:28 UTC.
Creation status: AUTHOR_HAND_PROVED / LOCAL_UNREVIEWED.
New author Source: PENDING. New independent technical whole: PENDING.
No new Paper, generic Tool, formalTask, Native operation or physical implementation.
Root contributes CONTROL/routing and zero mathematical formulas, repair or votes.

## 1. The precise new scope and the changed control hypothesis

C23 explicitly supplies a full-span sufficient known-control scheme but does
not claim its number of scaled parameters is minimal. Its low-rank orbit
ambiguity is for GENERAL positive K, not automatically for the restricted
source-monomial family. This is a concrete remaining interface in the actual
source, not a new condition-number constant.

Here ONLY the original210 graph is used: the bottom rectangle has a=b=1,
four vertices, four cyclic edges and ONE face. There are13 mixed parameters
q_v,alpha_e,beta_e,z, ALL in(0,1), and32 complete relative old-character states.
The control scales ONLY the four alpha_e by known rho_e in(0,1); every other
parameter is unchanged. Its active columns have rank4 in a5-dimensional
state space. The resulting operator has two positive16-state blocks and
zeros between them: it is NOT entrywise strictly positive.

The new conclusion is global exact identifiability: any two actual strict-domain
parameter vectors and arbitrary common strictly positive backgrounds producing
the same two complete A/B distributions must have equal parameters and backgrounds.
No genericity, small-parameter limit, Jacobian test or numerical recovery is used.
The complete old-character observations and known control values remain assumed.

This is the D=0 returned-control model (one shared unknown Q and no drift).
The earlier strictly-positive-T Perron theorem is NOT invoked outside its domain.
Backgrounds that depend on the control label, D>=1 statements, more than one bottom
face, optimality of four controls, physical calibration, errors and costs are
outside the conclusion of this artifact.

## 2. The same actual source coordinates and alpha-only operator

Label the four edges of the bottom square by e=1,2,3,4 and its vertices by v.
For an edge subset U let partial U be its mod2 vertex boundary.
Write the complete state as y=(t,u) in F2 x F2^4.
The first bit is dual to the unique-face source and the four other bits
are dual to the alpha-edge sources. With chi_U(u)=(-1)^(U dot u), define

  A_U = product_(e in U)(alpha_e beta_e) product_(v in partial U)q_v,
  B_U = z product_(e in U)alpha_e product_(e notin U)beta_e
                     product_(v in partial U)q_v,
  K_lambda(t,u)=sum_(U subset{1,2,3,4})
                         [A_U+(-1)^t B_U] chi_U(u).                   (1)

These are the literal C22 sources(T=empty,U) and(T={face},U).
All A_U and B_U are strictly positive; A_empty=1 and

  k=B_empty=z beta_1 beta_2 beta_3 beta_4 in(0,1).
  tau_e=beta_e^2 in(0,1), tau_U=product_(e in U)tau_e,
  B_U/A_U=k/tau_U.                                                     (2)

In particular the unknown q and alpha cancel in this RATIO, but they have
not been set to zero or discarded from K. Uniform mean K=1 follows from
its constant Fourier coefficient A_empty.

For completeness positivity is the actual finite source-family property,
not a new assumption about arbitrary signed functions: the source columns
are gamma_z=(1,0), gamma_alpha_e=(0,e_e),
gamma_beta_e=(1,e_e), and gamma_q_v=(0,incidence row of v).
Independent bits of bias lambda_i have characteristic coefficients precisely
the monomials in(1); character orthogonality gives K(y)=32 Pr(sum delta_i gamma_i=y).
All bits have both probabilities positive in the strict domain and the
z/alpha columns span F2^5, so K is strictly positive on all32 states.
This finite algebraic identity is not an additional observation or simulation.

Now let delta_e be independent bits with
Pr(delta_e=0)=(1+rho_e)/2, Pr(delta_e=1)=(1-rho_e)/2, and define

  (T f)(t,u)=E_delta f(t,u+delta).                                     (3)

All16 bit assignments have strictly positive mass. Thus T is stochastic,
preserves uniform mean and1, has strictly positive entries inside each
fixed-t block, and has zero entries between t=0 and t=1.
On chi_U its multiplier is product_(e in U)rho_e; applying this to BOTH
layers in(1) proves

  T K_lambda = K_(q, rho alpha, beta, z).                              (4)

The controlled parameter vector is still in the original open cube.
The four scaled parameters here are literal mixed alpha coordinates.
They are not four measurements, four physical knobs or a minimal-cost claim.

## 3. What equality of two complete data pairs actually leaves free

The actual data model is

  P_A(y)=Q(y)K(y)/Z_A,
  P_B(y)=Q(y)(T K)(y)/Z_B,
  Q(y)>0, sum_y Q(y)=1,                                               (5)

with all rows complete positive normalized distributions. Each Z is the
FULL positive normalizing sum. Suppose another original pair K',Q'
gives the SAME two distributions, with its own Z'_A,Z'_B.

Dividing P_B by P_A does not assume normalizers known. It gives

  (T K')(y)/K'(y)=c (T K)(y)/K(y)                                     (6)

for one constant c>0. Define r(y)=(T K)(y)/K(y)>0 and
M=diag(1/r)T. Then MK=K and MK'=c K'.
This M is not globally positive. On each fixed-t block conjugate it by K:
P_ij=M_ij K_j/K_i. Its row sums are1, every within-block entry is strictly
positive, and with v_i=K'_i/K_i it satisfies P v=c v.

At the maximum of v within one block, averaging gives c<=1; at the minimum
it gives c>=1. Therefore c=1. A nonconstant v in that block would make both
inequalities strict, so v is constant on the block. The same argument on
the other block leaves exactly two positive scale factors. Consequently

  K'(t,u)=h(t) K(t,u), h(0)>0,h(1)>0.                                  (7)

This is an orbitwise conclusion, not the invalid use of a global strict
Perron theorem. For unrestricted positive K the ambiguity(7) really remains.

Write h(t)=a(1+x(-1)^t), with a>0 and -1<x<1.
Because BOTH K and K' have uniform mean1, (1)-(2) give
1=a(1+xk). Put d=1+xk>0. Then Fourier coefficients transform as

  A'_U=(A_U+x B_U)/d,
  B'_U=(B_U+x A_U)/d,
  k'=B'_empty=(k+x)/d.                                                (8)

The prime coefficients are strictly positive because K' is assumed to
belong to the SAME original strict source family. In particular k+x>0.
No claim is made that an arbitrary positive h automatically preserves
this source family; testing that is exactly the remaining new obligation.

## 4. Strict source-monomial constraints eliminate the orbit factor

The second actual parameter vector has its own
tau'_e=(beta'_e)^2 in(0,1). Applying the identity(2) to it requires

  (B'_U/A'_U)/k' = 1/tau'_U.

Using (2) and (8), the left side is
F(tau_U), where

  F(s)=[(1+xk)/(k+x)] [(k+xs)/(s+xk)].

Every denominator used here is nonzero: d>0 and k+x>0 were just proved;
A'_U>0 together with A_U>0 also gives tau_U+xk>0.
For two DISTINCT edges e,h set t=tau_e and u=tau_h.
Because tau'_U is the product of its single-edge values, original
source-family membership forces the EXACT multiplicativity

  F(tu)=F(t) F(u).

Clearing the nonzero denominators gives the elementary polynomial identity

  0=(k+x)(k+x tu)(t+xk)(u+xk)
       -(1+xk)(k+xt)(k+xu)(tu+xk)
   =xk(1-x^2)(1-t)(1-u)(tu-k^2).                                     (9)

This factorization is an ordinary hand expansion, not a symbolic-computation
claim. To see the factors explicitly, collect respectively
t^2u^2, tu(t+u), t+u,1,tu. Their coefficients after extracting
xk(1-x^2) are 1,-1,k^2,-k^2,1-k^2.
The remaining bracket is
tu[tu-t-u+1]+k^2[t+u-1-tu]=(1-t)(1-u)(tu-k^2).

All factors in(9) except possibly x are NONZERO in the actual domain:
k>0, |x|<1, 0<t,u<1, and the other two distinct square edges give

  k^2=z^2 product_(j=1)^4 tau_j
      =tu [z^2 product_(j notin{e,h})tau_j] < tu.                      (10)

The strict inequality uses only the original z,beta parameters in(0,1).
One may choose adjacent e,h, so their paired source has exactly the allowed
mod2 vertex boundary; the ratio formula(2) cancels that boundary correctly.
No omitted q factor or unsupported source label is inserted.

It follows that x=0. Then d=1, a=1 by normalization, and (7) yields

  K'=K on the COMPLETE32-state space.                                (11)

The positive source constraint is what recovers the relative scale between
the two disconnected control orbits. No full-rank kernel assumption is hidden.
This is a GLOBAL proof throughout the stated strict domain, including equal
parameter choices, not just a locally full-rank calculation.

## 5. Recovery of all13 parameters and the common background

For clarity, equality of complete K also recovers the original parameters;
this is not a new unproved source-family inverse premise.
Put W_e=A_{e}. For every vertex v choose its two incident edges e=(u,v),h=(v,w)
and put R_v=A_{e,h}. Put H_e=B_{e} and B=B_empty=k.
Directly from(1),

  q_v^2=W_e W_h/R_v,
  beta_e^2=W_e B/H_e,
  alpha_e^2=W_e H_e/[B q_u^2 q_v^2],
  z^2=B^2/product_(e=1)^4 beta_e^2.                                   (12)

For example in W_e W_h/R_v the common q_v is squared in the numerator
and absent from R_v, and the other factors cancel. The next three cancellations
give beta,alpha,z squares exactly. Every coefficient and denominator is
strictly positive. Therefore K'=K makes all original parameter squares equal,
and positivity gives lambda'=lambda without a sign choice.
This is the same exact C22 inverse, here explicitly used on its REAL domain.

Finally P_A and K give the unique normalized common background

  Q(y)=[P_A(y)/K(y)]/sum_z[P_A(z)/K(z)].                                (13)

Thus Q'=Q as well. All data normalizers are then the actual sums determined
by the same K,Q; none was assumed identical at the start.
Combining(5)-(13) proves the stated full global identifiability for every
strict-domain source vector, every positive common Q and all known
rho_e in(0,1). Both configurations have nonzero original parameters.

The proof does not promise an algorithm that finds a candidate from arbitrary
input tables, or assert that arbitrary positive data are realizable.
The prior actual-family member test still requires ALL coefficient equalities
and strict parameter bounds after any target has been recovered.
No source coefficient is claimed to be directly observed without the already
assumed complete data and source-model inference.

## 6. What changes, and which old boundaries remain

The C23 full-span construction controlling alpha and z scales E+F=5 parameters
on this smallest graph and gives a globally positive control operator.
The present4-alpha construction has rank4, leaves two orbits and fails that
GLOBAL positivity hypothesis. Its injectivity on the actual source family
therefore is not a re-use of the old positive-kernel uniqueness theorem.

It also does not contradict C23's orbitwise nonidentifiability for GENERAL
positive targets: that ambiguity was precisely the h(t) in(7).
Equations(8)-(10) prove that its nonconstant members cannot simultaneously
satisfy the strict actual13-parameter monomial constraints here.
One must not present a generic-K orbit factor or an endpoint with a zero
or unit parameter as an actual counterexample to this theorem.

Only an upper bound on the number of scaled coordinates needed for THIS
global identifiability protocol has been established. Four is NOT asserted
minimal; a single differently chosen control, other subsets and larger
rectangles have not been classified. This artifact stops at actual210.
For a larger rectangle the remaining orbit factor can depend on multiple
face bits; the one-variable form(8)-(9) is not silently applied to it.

This D=0 common-background proof is not an automatic drift/stability theorem.
The older returned-good-schedule/strictpositiveT statements retain their
own actual hypotheses. No error/noise amplification, uniform lambda modulus,
parameter boundary inverse, comparison of control costs, calibration or
physical feasibility is inferred. The actual source family stays(0,1)^13,
and the all-positive common-background assumption is not relaxed to
control-dependent or memory-dependent backgrounds.

## 7. Actual input ledger and source distinctions

The initial new caller is my personal full immutable C23 intake:
Source87577d0e11761c50d358aa8c804bb62c3394e6ee,
research_notes/divisor_extrema/20261015_c23_two_level_blind_reference.md,
9623B/SHA256dfa77387eba6b61017e34bce5ff94d401a16cbb667277ca9aad7b78414fe4d14/
GitOID2e5994baa4e4d6ee16b3aa85e1cbd2f6647a9892.
I genuinely read the whole8-section text during the bounded actual-family
citation restoration, with my own immutable UTF8 length/SHA/blob/URL.
Sections2-3 declare the actual family and control; Section5 explicitly warns
that the low-rank generic-K example is not a result for restricted sourceF.
No original experiment, code, numerical table, physical correspondence,
registration or whole old theorem is endorsed by this reading.

The source-monomial/domain definition is personally genuinely full-read C22
remote transcription at
Source15dd9dc4beb060eeb3e76f13fa481486293f1100,
research_notes/divisor_extrema/20261014_c22_seventh_order_parameter_reconstruction.md,
13359B/SHA256c84fe60e7e9822eb3e3a03e71abb4ccba00844da1104865415afe56a372ef9cd/
GitOIDbd6fda0b3cf249dcf769cf17ec318e8894abdc03.
The OTHER original attachment is also13359B but has
SHA256587d1e4ff325fe3b7b42a437a20488264f2b9270ba2499040d48e5686a78911c/
GitOIDbf27478277eca90bec261cd5a24ed7f9bf757d7f.
I have not whole-read that other original attachment and do not call the
remote transcription its identical restored bytes.

The already genuinely closed applied-family interface is my21721 at
Sourcebc18927084a5e10d19e8071afbb2ac0b6b025105,
research_notes/owner_goal_20261017/c26_actual_lambda_family_intake_bff6dc/C26_ACTUAL_C22_SOURCE_FAMILY_MEMBERSHIP_POSITIVE_ENDPOINTS_AND_FIT_NONATTAINMENT_APPLIED_CONSUMER_V1.md,
21721B/SHA25697af517fa8bee0b241f191abf153c4373d80411daafb779369be99a1164dac2c/
GitOID866c0df398c61567ea2711b498a3c2695d9e116e.
Its genuine new technical whole peer22076 is
Sourceb668f2f421c89313a1966cf769c47427c27c5adc,
research_notes/owner_goal_20261017/reviews/c26_actual_lambda_family_independent_9f7a5c/C26_ACTUAL_C22_FAMILY_MEMBER_ENDPOINT_AND_ORIGINAL_FIT_NONATTAINMENT_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md,
22076B/SHA2560e5f080f9388c12078c2744593c766ae8300ab7145ba2fb41604f3f6f5d483f5/
GitOID7d82d45266ff5f368591327ce6896d3b3101b894.

My true author21721 whole/own Source exact1 and peer22076 full ordinary/own
Source exact1 already closed2/43797 with zero correction/repair.
This scope does not recycle that vote: the rank-deficient-control problem
and rigidity identity(9) were not in that earlier whole.
That old fullrank-control nonattainment result remains in its stated domain.
No old source or context is modified.

For every cited file the exact immutable URL is
https://github.com/awdawmip/enterprise-math/blob/{full Source}/{path}.
Their full raw intake/receipts are held in the preceding
c26_actual_lambda_family_intake_bff6dc directory; no repeated old GET,
whole/commit comparison or borrowed Source API was manufactured here.
Old C23/C22 SELF_CHECKED_UNREVIEWED and original registration/session-denial
states, and the original source/program/experimental claims, remain separate
from this newly proved finite conditional consumer.

## 8. Construction, review boundary and stopping point

BFF is sole new constructor of the blockwise-data reduction plus the
strict-family Möbius rigidity proof and its applied consumer.
New internal/private construction is NONZERO.
The original source formula/control definitions retain C22/C23 credit;
the preceding member/endpoint application and9F7's genuine review remain
separately attributed. No existing paper or generic Tool is invented.

Root accepted the source-explicit scope and restated restrictions, but
supplied zero mathematical construction, formula, repair or vote.
A/CF/4A supplied no candidate, proof or repair. After the full prior
21721 ordinary closed, I sent9F7 ONLY the already fixed C23 INPUT
Source/path/bytes/SHA/OID and its old conditional status, as Root requested.
Neither this new proof nor an unfrozen new candidate formula was supplied
to him or any other possible independent reviewer.
Any natural associations on reading that input are not falsely called
zero private thinking; future review must disclose actual warm histories.

All reasoning here is hand finite algebra. The displayed factorization(9)
was obtained and checked by the coefficient collection shown beside it;
no symbolic algebra system, scientific program, numerical probe, enumeration,
native operation, helper, new formalTask/identity/RA/budget or remote Source
mutation ran. Administrative file/UTF8/hash IO and Source reading are not
scientific experiments. LC/hdiv/P11/M7/R101/883 STOP boundaries are unchanged.

The original kill conditions were actual-source/domain matching, a genuine
global all-positive proof instead of a generic-K or endpoint example, and
a valid orbit-factor elimination. Sections2-5 pay each of these within the
exact fixed210 scope. No further variant is claimed or needed for this result.

At first artifact creation the complete actual selfreading and external
oncefreeze of THIS new body are subsequent observations, not filled in
prospectively here. New Source and independent whole remain pending;
publication or an old PASS cannot replace that new independent challenge.
Parent Goal remains OPEN.

Global-Knowledge-Sync: main@67a02007 / GLOBAL_KNOWLEDGE_V1
