# Stage310-B — certified enlargement of the FULL eight-rate Pareto interval

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen account input: GLOBAL_KNOWLEDGE_V1 main@2e4b934513a481b0bd40ac2754a84dd682e210c2; Enterprise Math main@a199abff4dcaeb8fc5a7f8a40ea23e3ce5dd53c6; Stage309-B predecessor fa9f94e70173cc8881edf54bd887f2cc7a06869f. Original P000 V5, ACTIVE worldview, joint-relation preservation and portable research protocol were read. At 2026-10-30T14:08:58Z the Site configuration reported research_authority_granted=false, write_relay_enabled=false, and current owner query returned CONTROL_QUOTA. This is an external finite positive-rational BRC auxiliary model, not native P000 X6 dynamics.

## Model and precise observers

S is fair. Conditional on S, J matches S with probability 7/8, W matches S with probability 3/4 and Y is Bernoulli(p_S), p_0=1/4, p_1=3/4, independently. The private h=(J,W,Y) has the following ordered source mass pairs (256 Pr(S=0,h),256 Pr(S=1,h)):
000:(63,1), 001:(21,3), 010:(21,3), 011:(7,9),
100:(9,7), 101:(3,21), 110:(3,21), 111:(1,63).

Public G=(W,Y); three future F visits emit conditionally IID Bernoulli(p_S) bits, whereas H emits fresh independent fair bits. A compressed port locks one real t_h in [0,1] for each private h, through all three F visits. Policies are adaptive using only public history. The public worst TV is P(t); the worst terminal (S,J,G,trace)-tagged TV is T(t). The all-F policy achieves both maxima by common presampling and a source-preserving stochastic kernel (Stage307-B.1). MAP rates t_h*=p_0 for a_h>b_h and p_1 otherwise yield P0=11/256 and T*=77/1024.

The full eight-real-rate Pareto envelope is F_P(p)=min {T(t): t in [0,1]^8, P(t)<=p}. No symmetry restriction on competitors is assumed.

## Theorem — global sharp interval extended by 225/52

Write
r=9/400, E=r/52=9/20800,
q(u)=9u/128+3u²/32-u³/8,
g(u)=117u/4096-123u²/1024+23u³/256.
For EVERY real epsilon in [0,E], there is a unique u in [0,r] with q(u)=epsilon, and

    F_P(11/256-epsilon) = 77/1024+g(u).

For epsilon>0 there are exactly TWO minimizing eight-rate tables, each changing precisely one light outer fiber: t_100=1/4+u, all others MAP; or t_011=3/4-u, all others MAP. At epsilon=0 MAP is the unique optimum. The preceding Stage309-B interval was [0,1/10000]; E/(1/10000)=225/52>4. This theorem does not determine the first breakpoint beyond E.

## Proof — four exact steps

1. GLOBAL LOCALIZATION. Let D(x,y) be TV of the three-bit IID Bernoulli product laws. In each private h, the triangle inequality gives
a D(p0,t)+b D(p1,t) >= min(a,b)D(p0,p1)+|a-b|D(t,p_MAP).
The projection on the first bit gives D(t,p_MAP)>=|t-p_MAP|, and min_h |a_h-b_h|=2, so

    T(t)-T* >= sum_h |a_h-b_h|D(t_h,t_h*)/256
             >= max_h |t_h-t_h*|/128.                 (1)

The one-light-fiber candidate has P=P0-q(u), T=T*+g(u), on [0,r]. Algebra gives (13/32)q(u)-g(u)=9u²(9-8u)/512>=0. Also q'>0 on [0,r] and q(r)=833571/512000000>E, so the candidate exists for every epsilon<=E. The feasible cube is compact; every true minimizer has T no larger than the candidate. By (1),

    max_h |t_h-t_h*| <=128(T-T*)<=52 epsilon<=r.      (2)

All eight real parameters are localized; no finite grid is used.

2. RATIONAL SIGN CERTIFICATE. For a specific three-bit word with k ones, set B_k(z)=z^k(1-z)^(3-k). At MAP the compressed-minus-target PUBLIC residual for G=00 is (13,3,-3,-13)/1024, by k=0,1,2,3. Both private rates in this public fiber start at p0; their combined mass is 5/16. Over the exact interval [p0-r,p0+r]=[91/400,109/400], monotonic differentiation gives the exact maxima of |B_k'|:

    L = (286443,39243,51557,35643)/160000.

Here B0'=-3(1-z)^2; B1'=(1-z)(1-3z) decreases; B2'=z(2-3z) increases; B3'=3z² increases. The maximal combined per-word changes (5/16)r L_k are exactly

    (2577987,353187,464013,320787)/204800000.

They are respectively STRICTLY smaller than (13,3,3,13)/1024. Thus all outer public signs remain fixed on (2); G=11 follows by bit-complement symmetry. G=01 and G=10 initially have zero public TV, so any perturbation contributes nonnegative TV. Put A(z)=1-3z²+2z³=B0(z)+3B1(z). Moving an outer rate inward toward its minority source by u>=0 decreases outer public TV by at most m_h[A(p0)-A(p0+u)]; moving outward cannot decrease it. For the light fibers 100,011, m_h=1/16, and that amount is q(u). For the heavy 000,111, m_h=1/4 and it is 4q(u). Hence

    P0-P(t) <= sum of positive inward outer gains.    (3)

3. STRICT COST COMPARISON. The exact source-tagged excess cost of an inward adjustment u in a light outer fiber is g(u). In a heavy outer fiber it is
H(u)=[63((3/4)^3-(3/4-u)^3)+A(1/4+u)-A(1/4)]/256.
On [0,r], q'>0, q''=3/16-3u/4>0, g'>0, g''=-123/512+69u/128<0. Consequently C(v)=g(q^(-1)(v)) is strictly increasing, strictly concave and C(0)=0, with 0<C'(v)<=C'(0)=13/32<1. Let M(v)=H(q^(-1)(v/4)). The inequality H'(u)>(4q)'(u) is equivalent to 189(3/4-u)>390(1/4+u), true throughout [0,r] (check its worst endpoint r). Thus M'(v)>1 and M(v)>v for v>0: heavy public gains are always strictly dearer than light gains.

4. FULL CUBE EXCHANGE AND UNIQUENESS. A minimizer with P<=P0-epsilon has total inward outer gains >=epsilon by (3). Trim positive gains to x1,x2 (light) and x3,x4 (heavy) summing to exactly epsilon. Every x_i<=epsilon<=E<q(r), so all inverse functions are in domain. The tagged joint TV is fiberwise additive, and all outward/middle changes have positive cost by (1). Hence

    T-T* >= C(x1)+C(x2)+M(x3)+M(x4)
          >= C(x1+x2)+x3+x4
          >= C(x1+x2+x3+x4) = C(epsilon).

The second inequality uses strict concavity and C(0)=0; the third uses C'<1. The single-light-fiber witness achieves equality, proving the claimed envelope globally. Equality excludes positive heavy gains, simultaneous light gains, surplus gains, outward changes and middle changes. Exactly the two reflected minimizers remain for epsilon>0; unique MAP for epsilon=0. QED.

## Reproduction, actual scope and next obligation

The actual locally executed standard-library Fraction program checked the strictly positive source-pair table; exact endpoint sign margins, derivative comparisons and polynomial factorization; and separately enumerated all 128 source/private/future-F atoms for witnesses u=1/200 and u=3/500. Both witness epsilon values exceed Stage309-B's limit but lie below E. It returned STAGE310B_EXACT_RATIONAL_EXTENSION_PASS. The finite executable corroborates rational identities; the above analytic proof establishes the continuum/exact global claim. This proof is author work pending independent review, and no P000 X6, triadic native closure, heartbeat time evolution or registered Cell address mapping follows.

BRC interface: REUSE_APPLIED, exact positive-rational weighted and provenance-preserving branch carrier from definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json; public and source-tagged observers and locked future-operation port remain typed and distinct. Next: exact first breakpoint beyond E, or sharper global localization using three-bit product TV and refined per-fiber sign certificates.
