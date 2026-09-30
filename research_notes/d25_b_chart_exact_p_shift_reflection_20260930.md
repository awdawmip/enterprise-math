# D25 portable research: exact p-shift reflection and finite-holonomy form of the C13 defect

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit continues only the portable upper-B-chart lane. It does not claim a native session, CLAIM, run, Result, review, or theorem admission, and it does not reopen the canonical Research1 normal-Dixon / Gauss-Manin lane.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main for this execution phase: 680f483384bed1a541ed674efde3106d746d360f.
- Enterprise Math canonical main for this execution phase: 6b09272ee49b33f98bac9f35a800b877a62a2e19.
- P000 remains ACTIVE_LOCKED; current research position remains RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Immediate durable portable predecessor: d25_b_chart_reverse_reflection_p2_endpoint_theta_20260930.md, blob 59c2e766344f06ef4d438bf34ff544d5382694b0.
- Portable branch head before this write: 7704689cbeaec4cdb85aa8d6c99e57f85e000713.
- Current recovery record remains Issue #2578 for logical conversation EM-DIRECT-C4D02C: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false, source_authority_verified=false. This proof does not change that control state.

## 1. Definitions

Let p=6m+1 and n=2m=(p-1)/3.

For a parameter eps define

t_r(eps)
= 2^r * ((2-eps)/3)_r / ((3-2eps)/6)_r,

and

Q_s(eps)
= - 2^(-s) * ((5+2eps)/6)_s / ((2+eps)/3)_s.

The durable Q carrier is Q_s(0), while t_r(0) is the reversed carrier used in the preceding endpoint-theta note.

## 2. Exact p-shift reflection

For every 0<=s<=n one has the exact rational-function identity

- Q_s(eps)
= t_(n-s)(p+eps) / t_n(p+eps).                 (1)

Proof: put delta=p+eps. Since p=3n+1,

(2-delta)/3 = 1/3 - n - eps/3,
(3-2delta)/6 = 1/6 - n - eps/3.

Therefore

t_(n-s)(delta)/t_n(delta)
= 2^(-s)
  * (1/6-eps/3-s)_s
  / (1/3-eps/3-s)_s.

Using (x-s)_s=(-1)^s(1-x)_s gives

= 2^(-s)
  * ((5+2eps)/6)_s
  / ((2+eps)/3)_s
= -Q_s(eps).

No modular reduction is used. Equation (1) is an exact characteristic-zero identity.

At eps=0 this becomes

- Q_s(0)
= t_(n-s)(p) / t_n(p),                         (2)

which is the all-order version of the previously proved rowwise mod-p^2 reflection.

## 3. The previous p^2 reflection is the first-order shadow

Write

E_r
= sum_(u=0)^(r-1) 1/[3(3u+2)(2u+1)].

Then

d/deps log t_r(eps) at eps=0 = E_r.

The durable endpoint note proves

t_n(0) = 1 + p theta_p  (mod p^2),
theta_p = q_p(2),

and also

E_n = -q_p(3)/2  (mod p).

Taylor-expand (2) at eps=0:

t_r(p)
= t_r(0) [1+pE_r]  (mod p^2),

t_n(p)
= t_n(0) [1+pE_n]  (mod p^2).

Because

theta_p + E_n
= q_p(2)-q_p(3)/2
= -q34/2,

where q34=q_p(3)-2q_p(2), equation (2) yields

- Q_(n-r)(0)
= t_r(0) [1+p(q34/2+E_r)]  (mod p^2).

Thus the earlier p^2 theorem is not an isolated jet formula: it is exactly the first p-adic coefficient of the finite translation eps -> p+eps in (1).

## 4. Exact two-ended family identity

Define the full C13 Q-shell family

U_n(eps)
= sum_(s=0)^(n-1)
  Q_s(eps) / (s+(1+eps)/3),

and the reverse logarithmic family

J_n(delta)
= sum_(r=1)^n
  t_r(delta) / (r-delta/3).

Put r=n-s in U_n. Since

s+(1+eps)/3
= (p+eps)/3-r
= -(r-(p+eps)/3),

equation (1) gives the exact finite identity

U_n(eps)
= J_n(p+eps) / t_n(p+eps).                     (3)

This is a genuine two-ended relation: the Q-shell at parameter eps equals the reverse-prefix family evaluated one finite p-step away.

For the cutoff used by the regularized C13 bulk, exclude the last Q row and define

U_n^-(eps)
= sum_(s=0)^(n-2)
  Q_s(eps) / (s+(1+eps)/3),

J_n^-(delta)
= sum_(r=2)^n
  t_r(delta) / (r-delta/3).

Then exactly

U_n^-(eps)
= J_n^-(p+eps) / t_n(p+eps).                   (4)

## 5. Finite-holonomy form of the divided reflection defect

Let

A_p := J_n^-(0) = J_m - 8/3,

and define

G_n(delta)
:= J_n^-(delta) / t_n(delta).

Equation (4) at eps=0 gives

U_n^-(0)=G_n(p).                                (5)

Also

A_p=t_n(0)G_n(0).                               (6)

Hence the previously staged divided reflection defect

kappa_p
:= [U_n^-(0)-A_p]/p  (mod p)

has the exact two-ended representation

kappa_p
= [G_n(p)-t_n(0)G_n(0)]/p  (mod p).            (7)

Using t_n(0)=1+p theta_p mod p^2, Taylor expansion of the exact finite displacement gives

kappa_p
= [d/ddelta - theta_p] G_n(delta)|_(delta=0)
  (mod p).                                      (8)

So the covariant derivative found in the preceding portable analysis is the first divided digit of a real finite p-translation, not an ad hoc local jet.

Equation (7) does not evaluate kappa_p by endpoint data alone. It identifies the correct nonlocal carrier and proves that no additional provenance beyond the two endpoint evaluations of the same G-family plus t_n(0) is needed for this specific finite-holonomy observer.

## 6. BRC interpretation

Population:
- Q-shell rows s=0..n-2;
- reversed rows r=2..n;
- parameter line delta in {0,p} for the present observer.

Fine state:
- row labels;
- Q/t provenance;
- finite p-shift;
- endpoint multiplier t_n(0).

Observer:
- the divided two-ended defect kappa_p mod p.

Safe quotient proved for this observer:
- the accumulated rowwise connection E_r can be replaced by the exact finite translation (7) if both endpoint evaluations G_n(0), G_n(p) and t_n(0) are retained.

Unsafe quotient:
- replacing G_n(p) by G_n(0), or t_n(0) by 1, before dividing by p; either loses the defect.

Tool/BRC resolution: COMPOSE_APPLIED using the existing residual-faithful BRC carrier, valuation retention, and operation-safe quotient rules. No new top-level method family is claimed.

## 7. Independent verification

Two checks were performed.

1. Exact rational verification for m=1..7 and eps in {0, 1/7, -2/5, 3/11}:
   - every row of (1);
   - the full-sum identity (3).
   Total exact equality checks: 280, zero failures.

2. Dependency-free modular regression for every prime p<10000 with p=1 mod 6:
   - exact p-shift reflection (2) modulo p^2 on every row;
   - its first-order expansion equal to the durable rowwise p^2 formula.
   Result: 611/611 primes, zero failures.

The regression is not the proof. Equations (1)-(4) are exact finite Pochhammer identities.

## 8. Next exact unit

Do not search again for a scalar local primitive of the C13 jet.

The next smallest unit is to combine the exact p-shift family (3) with the existing Q-contiguous law before taking the divided digit. Differentiate the exact contiguous relation in eps, then rewrite every C13 derivative through the finite translation eps -> p+eps. The concrete question is whether the resulting two-ended combination cancels the surviving kappa_p in the full regularized m-transport.

If it does not cancel, retain kappa_p itself as the minimal nonlocal repair coordinate. Do not reopen the cubic/sextic/Kummer state and do not enter the canonical Research1 normal-Dixon lane.
