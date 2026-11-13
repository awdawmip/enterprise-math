# R5 — Low-ratio positive-z Blackwell prism and face-switch theorem

Research date: 2026-11-08 (Asia/Shanghai). Author-side proof and exact arithmetic; independent review and Source admission pending. Frozen scientific inputs: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. This note extends [the exact R5 low-ratio G-face predecessor](https://github.com/awdawmip/enterprise-math/blob/12f6d57982ca29f360e8f074275d8a23c2c57b5d/research_notes/brc_r5_sharp_lower_ratio_full_rectangle_20261108/LOW_RATIO_BZERO_FACE.md).

## Exact model

Lawful flows are f=(g,a,b,u,v,w,z) with 0<=a,b<=g<=1; 0<=u<=13a/40+b/80; 0<=w<=3a/40+21b/80; 0<=z<=a/10; 0<=v-z<=9b/40. The likelihood nodes are r=(1/10,1/2,3/4,1,5/4,3/2,19/10). The seven Q masses are:

- M0=509u/900+47z/180+67(v-z)/162+w/100
- M1=13a/40+b/80-u
- M2=(g-a)/2
- M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
- M4=(g-b)/2
- M5=3a/40+21b/80-w
- M6=u/100+47z/180+67(v-z)/162+509w/900.

T_P=1+g+3a/8+5b/8+u/2+v+3w/2; T_Q=1+g+(a+b)/2+u+v+w. Seedless condition: R=9bz-4a(v-z)=0. Two linear seedless faces are G={b=0,v=z}, F={z=a/10,v-z=9b/40}.

A nonnegative 7x7 matrix Q (row=target node, column=source node) is a calibrated Blackwell certificate for source x and seedless target y when sum_j Q[i,j]=M_i(y), sum_i Q[i,j]=M_j(x), sum_i r_i Q[i,j]=r_j M_j(x) for all i,j, and T_P/T_Q match. For every terminal declaration d in [0,1]^7 set d'_i=sum_j(Q[i,j]d_j)/M_i(y) for positive mass, otherwise zero. These equations prove both errors and both stopping times match simultaneously.

## Theorem 1: low-ratio positive-z full physical p/q prism

For every real 0<=s<=g<=1, 0<=eta<=1/40, 0<=p,q,h<=1, 0<=theta<=29/112, define

u=s(13/40+eta/80)p, w=s(3/40+21eta/80)q, z=s theta/10,
x=(g,s,eta s,u,s(9eta/40+theta/10),w,z).

There is a lawful seedless G-face target y and calibrated nonnegative Q, independent of d, preserving the four observations of x_h=(1-h)x+h y for every real d. This includes all the physical p/q rectangle and positive z up to 29s/1120.

**Exact certificate:** `THETA_SHARP_CORNERS.json` contains four *new* exact rational 7x7 Blackwell matrices at eta=1/40,theta=29/112,g=a=1 and (p,q)=(0,0),(1,0),(0,1),(1,1). They have respectively 12,11,12,8 nonzero edges (43 in total). All G targets are legal and all 7 row, 7 Q column, 7 likelihood-weighted P column, two stopping-time identities hold. Example at (p,q)=(0,1):

x=(1,1,1/40,0,353/11200,261/3200,29/1120);
y=(1,519/560,0,0,519/5600,1557/22400,519/5600).

**All-real proof:** For eta=1/40, the predecessor at immutable `12f6d57982ca29f360e8f074275d8a23c2c57b5d` supplies the four exact G-face corner transports at theta=0. Interpolate those with the four new theta=29/112 corner triples (x,y,Q) using nonnegative weight beta=112theta/29. For eta=0 at every theta, the physical source is itself seedless in G, so the diagonal M(x) matrix transfers x to itself. Interpolate eta with alpha=40eta; then p/q with nonnegative weights (1-p)(1-q),p(1-q),(1-p)q,pq. The source dependence is affine in eta at fixed p/q and affine in theta; hence this produces exactly x with both physical capacities, while each target remains in G. Introduce E0=(0,...,0), E1=(1,0,...,0), both on G, with weights (1-g),(g-s),s, to obtain arbitrary g,s. Finally interpolate x with target y using h and Q with diag(M(y)). All operations preserve legal convex inequalities, Blackwell calibration and both stop times. Since G is a linear seedless face, y remains seedless. This proves the theorem for **all real parameters**, not merely tested rationals.

## Sharp G-face boundary

For every lawful y=(g,a,0,u,z,w,z) in G, direct substitution proves the exact nonnegative identity

14+47T_Q(y)-54T_P(y)=7(1-g)+20u+34(3a/40-w)+7(a/10-z)>=0.

At eta=1/40,p=0,q=1,g=a=1, source x(theta) satisfies

14+47T_Q(x)-54T_P(x)=(29-112theta)/160.

Consequently every G-face target preserving stop times for this source requires theta<=29/112. At theta=29/112 the new (0,1) exact calibrated matrix attains equality. Thus **29/112 is a sharp G-face ceiling for this corner**, fully attained within the theorem above. It is explicitly a statement about face G.

## Theorem 2: switch to F and cover the maximal-w corner for every theta

For **all real** 0<=s<=g<=1, 0<=eta<=1/40, 0<=theta,h<=1, set p=0,q=1 in the source above. There exists a lawful seedless target on the distinct linear face F with a calibrated nonnegative Blackwell matrix preserving all four observations for every terminal declaration.

`F_FACE_Q1_CERTIFICATES.json` contains **two additional exact 7x7 rational certificates** for theta=0, at eta=0 and eta=1/40 (9 edges apiece). At theta=1 the source is already in F, and diagonal transport works. Interpolate in eta between the two theta=0 target triples, then in theta with the theta=1 identity triple. Apply the same (1-g,g-s,s) and h combinations. All targets stay on F; all row/Q/P/time conditions are affine. This proves the stated all-real theorem across the full theta interval [0,1].

The second theorem shows concretely that the G-specific ceiling can be crossed through an alternative seedless representation. Its full-theta guarantee concerns the specified p=0,q=1 physical corner, whereas Theorem 1 covers the entire physical p/q rectangle up to theta=29/112.

## Verification, input provenance, pending questions

Both JSON certificate files give the complete six new rational nonnegative 7x7 transports (61 nonzero edges). The local Python `fractions.Fraction` verification of all six certificates, all relevant legality, exact calibration, both stop times and the sharp dual identity passed; an additional 243 exact p/q/g/s/h G-endpoint checks and 243 eta/theta/g/s/h F-face checks passed. The all-real proof is the explicit algebraic interpolation. The frozen theta=0 G-face predecessor is reused at its actual immutable commit. The carrier retains seven exact branch masses, likelihood-weighted masses and terminal declaration transformations; the observer consists of two errors and two stop-time scalars. No unverified native P000/X6 realization is asserted.

Next: extend the positive-theta full physical p/q rectangle beyond 29/112 by matching G/F or other lawful seedless targets for p=1,q=0 and the remaining corners; independently examine eta in (1/40,46/705).

Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. On this run the native em_status and em_control_tasks endpoints returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, STATUS_DATABASE_UNAVAILABLE, operation_sent=false. Therefore the active task owner, native Researcher-ID, CLAIM and mathematical admission were not verified; author-side GitHub evidence was published within the actual verified account's repository write permission.
