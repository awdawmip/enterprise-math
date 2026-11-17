# R5 K3 — Exposed clock face rules out all nonuniform proportional-clock family members in four observers

Date: 2026-11-03 Asia/Shanghai. Claim: PROVED (author proof); verification: EXACT_FRACTION_CHECKED; status: UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Source and scope
Immediate predecessor: `0e92beadc96c1389e7516ef1391c04abf536f46e`, `research_notes/brc_r5_k3_clock_plane_hull_family_20261103_t2142/RESEARCH.md`: equality of all signed two-clock convex supports in a nonuniform family. Earlier uniform-clock common-label classification: `c7caa7554474a18e3e5a71398e0293317624c10c`. Frozen scientific pins (unchanged): Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative context was read independently. P000 and ACTIVE Heartbeat/X6 worldview are unchanged.

Four positive BRC source carrier maxima `c=(1/8,1/6,1/16,3/32)`, sources C,I,BJ,IJ. FULL uses `0<=x,y<=1`, `0<=i<=1-x`, sourcewise controls `z_s,t_s,u_s in [0,1]`. Seedless LR uses `i=(1-x)y`, common `z,t,u`. Set `w=(1/4,(1-x)/4,y/8,i/8)`, `alpha=(1/2,2/3,1/2,3/4)`, `M_s=w_s alpha_s z_s`, `S_s=(2/3)M_s t_s`, `U_s=S_s u_s`, `d=y/16+3i/32`. The strict common terminal-label finite P/Q experiment has readouts

    eP=107/128-21x/128+d/4-(sum S)/2+sum_s p_s S_s/8
    eQ=13/64+3x/64-d/2+(sum S)/8+sum_s q_s S_s/32
    TP=3+sum M+(3/2)sum S+sum_s r_s U_s
    TQ=3+(sum M)/2+(3/8)sum S+sum_s v_s U_s/4.

All p_s,q_s,r_s,v_s in (0,1). The statement concerns this specified finite probability experiment, not an additional native X6 realization.

## Theorem (continuous eleven-parameter sharp exclusion)

Fix real `0<L<R<1`, `0<k<=1` and independent `p,q in (0,1)^4`. Put

    r=(R,R,L,L),  v=k*r.

Then, although FULL and LR have identical convex hulls after projection to `(TP,TQ)` (the predecessor's all-signed clock theorem), their FULL and LR **four-observer** convex hulls are strictly unequal for every choice of `p,q`:

    conv O(FULL) != conv O(LR).

In fact a specific FULL observation W lies outside `conv O(LR)` and possesses a mixed signed rational hyperplane separator whenever the parameters are rational.

Combining this result with the prior all-real uniform-clock ten-parameter classification gives the **complete characterization in the closed ordering family** `0<L<=R<1, 0<k<=1, p,q in (0,1)^4`:

    conv O(FULL) = conv O(LR)
      iff R=L and p_C=p_I=p_BJ=p_IJ and q_C=q_I=q_BJ=q_IJ.

Under these equality conditions the actual real-behavior images themselves are equal. Thus no member of this entire proportional-clock ordered family realizes the mother target (equal 4D convex hulls but unequal 4D real images).

## Proof of strict four-dimensional separation for R>L

For any signed clock normal `n0=(0,0,m,-1)`, the carrier-normalized source stages are

    V0=0, V1=m-1/2, V2=2m-3/4,
    V3(t)=2m-3/4+t(4m-k)/6,  t in {R,L}.

The unique zero of `V3(t)` is

    mu(t)=(9+2kt)/(8(3+t)).

Direct algebra gives

    mu(t)-k/4=(9-6k)/(8(3+t))>0,
    3/8-mu(t)=t(3-2k)/(8(3+t))>0,
    mu'(t)=(6k-9)/(8(3+t)^2)<0.

Since R>L, choose any `mu(R)<m<mu(L)`, for example their midpoint. Then `k/4<m<3/8`, so `V1,V2<0`, whereas `A:=V3(R)>0` and `B:=V3(L)<0`.

At this signed clock normal, sourcewise FULL optimality requires stage 3 for C,I and stage 0 for BJ,IJ, with carrier weights C,I at their maxima. The FULL upstream corner `(x,y,i)=(0,1,1)` and stages `(3,3,0,0)` attain clock support `3(m-1)+(7/24)A`. LR attains exactly the same clock support by upstream `(0,0,0)` and common stage 3, since that produces carriers `(1/8,1/6,0,0)`. This is the BRC provenance-preserving mask: dropping BJ/IJ sources by upstream suppression changes the answer baseline.

**Uniqueness of the LR exposed face.** LR's four deterministic upstream corners are `(0,0,0),(0,1,1),(1,0,0),(1,1,0)`. Stage 0 yields carrier score 0; stages 1 and 2 have negative source-independent score. At stage 3 the four carrier scores are, respectively,

    (7/24)A,
    (7/24)A+(5/32)B,
    (1/8)A,
    (1/8)A+(1/16)B.

Since A>0 and B<0, only the first is maximal. Thus exactly one of the 16 deterministic LR four-observer vertices lies in the exposed clock face. Multi-affine decomposition (proved in the predecessor for all real controls) ensures every real LR observation in that face is the SAME point H. No unexamined stochastic LR mixtures can enlarge this exposed face.

Let `W=O_FULL((0,1,1),(3,3,0,0))`, and `H=O_LR((0,0,0),stage3)`. Both have identical `TP,TQ` and identical source C/I contributions `M_s,S_s,U_s`, while `d(W)=5/32`, `d(H)=0`; both have `x=0`. Therefore for *all* p,q,

    W-H=(5/128,-5/64,0,0).

In particular `W!=H`. If W belonged to the LR convex hull, maximizing the clock normal would force every LR vertex of a convex representation to lie in the unique LR exposed face, whose only observer is H. That would imply W=H, contradiction. Hence W is outside the LR convex hull.

A constructive mixed separator follows. Write `g=min_{Z in LR vertices, Z!=H} [n0.H-n0.Z]>0` and `D=max_{Z in LR vertices}|eP(Z)-eP(H)|`. For `eps=g/(2(1+D))>0`, the signed normal `n_eps=(eps,0,m,-1)` keeps H as the unique LR support maximizer because each other vertex loses at least `g-eps D>0`. At W,

    n_eps.W - h_LR(n_eps) = eps*(5/128)>0.

For rational p,q,R,L,k, all construction data and eps are rational, giving an explicit rational Farkas/support certificate. The proof works for every real parameter in the stated domain, including boundary `k=1`. The separate `R=L` case is governed by the cited uniform-clock classification.

## Concrete exact rational witness

Take `R=4/5, L=1/5, k=1/2, p=q=(1/2,1/2,1/2,1/2)`. Then `mu(R)=49/152`, `mu(L)=23/64` and `m=1/3` lies strictly between them. The two observers are

    W=(455/576,39/256,673/180,4663/1440)
    H=(865/1152,59/256,673/180,4663/1440).

For the **fixed explicit rational separator** `n=(1/16,0,1/3,-1)`, exhaustive exact deterministic support calculation yields

    hFULL(n)=-53707/27648
    hLR(n)=-107549/55296
    hFULL(n)-hLR(n)=5/2048
    n.W=hFULL(n), n.H=hLR(n).

Consequently `dist_infinity(W,conv O(LR))>= (5/2048)/(67/48)=15/8576`. This example uses source-uniform p,q, showing that tuning the terminal answer channels to uniformity does not resolve the nonuniform proportional-clock four-observer obstruction.

## Verification scope and present status

`VERIFY.py` (standard-library Fraction, no floats) was locally executed and produced 53 exact assertions. For three rational parameter configurations it generates the complete 1,536 FULL and 16 LR deterministic four-observer points, checks the exposed-clock support and unique LR maximizing vertex, the universal baseline difference, a constructive mixed separator and its exact positive gap. For the fixed instance it independently checks the explicit supports, W, H and `15/8576` bound. This finite calculation crosschecks the rational examples; the algebraic/multi-affine proof above establishes the continuous-real conclusion.

BRC resolution: `REUSE_APPLIED` (four positive source masses and provenance-preserving upstream mask; no averaging prior to face comparison). External historical novelty and independent Driver acceptance have not been assessed. Native Site read scope is configured static/read-only, and current owner list returned CONTROL_QUOTA; do not interpret this GitHub author artifact as formal Result, CLAIM or independent review. Original mother objective remains open. The next useful route is outside this eliminated clock-equality family.
