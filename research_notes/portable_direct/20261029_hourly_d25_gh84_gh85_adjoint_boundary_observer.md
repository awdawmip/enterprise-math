# D25/LIFT GH-84–GH-85 — exact adjoint boundary source and root non-descent

2026-10-29 Asia/Hong_Kong. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN). Historical Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged. Logical research lane: chatgpt-research-hourly-enterprise-math-20260923, not the maintenance or on-hour lane. No native session/claim/run/Source checkpoint, Research-Activity registration or independent review is claimed.

## Original sources, distinct observers

For a prime p=4d+3 >=7, in k=F_p, theta=z*d/dz, retain

S_d(z)=sum_{r=0}^d c_r z^r, c_0=1, c_{r+1}/c_r=(4r+1)^3/[(4r+2)(4r+3)(4r+4)],
T_{p,z}=(8theta+1)S_d;

U_d(z)=sum_{r=0}^d h_r z^r, h_0=1, h_{r+1}/h_r=(4r+3)^3/[(4r+4)(4r+5)(4r+6)],
Hcal_d(z)=(8theta+5)U_d.

All denominators in the stated coefficient ranges are units. T is the actual GH-3 finite truncation. Hcal is GH-16's reflected Laurent double-pole observer, not the elliptic Hasse invariant or the endpoint Laurent constant.

## GH-84 — adjoint pair, exact terminal defect and full bilinear identity

Define
L_- = theta(theta-1/2)(theta-1/4) - z(theta+1/4)^3,
L_+ = theta(theta+1/4)(theta+1/2) - z(theta+3/4)^3.

**Theorem (all primes p=4d+3 >=7; complete polynomial identities).**

(84.1)  L_- S_d = (c_d/8) z^(d+1), while L_+ U_d = 0.

Proof: coefficient recurrences eliminate z^n for 1<=n<=d. At n=d+1 the L_- term equals -(d+1/4)^3 c_d = c_d/8, since d+1/4=-1/2 mod p. The L_+ terminal term is -(d+3/4)^3 h_d=0, since d+3/4=0 mod p. All further coefficients vanish by degree. This explicitly retains the truncation defect rather than treating S_d as a homogeneous solution.

The formal logarithmic adjoint (dz/z, theta^dagger=-theta) satisfies
(84.2)  L_-^dagger = -L_+.

Define the signed bilinear concomitant

B(S,U)=(1-z)[U theta²S-(theta U)(theta S)+(theta² U)S]
       +(z-3)U theta S/4 +(3-5z)(theta U)S/4 +(2-7z)US/16.

**Theorem (new finite dual boundary and support gap).**

(84.3)  theta B(S_d,U_d)=(c_d/8)z^(d+1) U_d(z).

(84.4)  B(S_d,U_d)=1/8+(c_d/8) sum_{j=0}^d [h_j/(d+1+j)] z^(d+1+j).

Proof: put L_-=(1-z)theta³-3(1+z)theta²/4+(2-3z)theta/16-z/64. Repeated algebraic integration by parts gives U L_-S-S L_-^dagger U=theta B(S,U), with the stated explicit B. Equation (84.1) yields (84.3). B(0)=1/8 because S(0)=U(0)=1 and theta-derivatives vanish at zero. All integers d+1+j in [d+1,2d+1=(p-1)/2] are p-units. Coefficientwise integration in the degree <=2d+1 polynomial ring yields (84.4). Thus coefficients of degrees 1 through d in the full signed concomitant **vanish exactly**; the true finite-source defect survives in degrees d+1 through 2d+1. QED.

The bilinear source identity is an additional arithmetic observer, not a substitute for the original T_{p,z} finite sum, GH-15's Laurent endpoints, original W/S, the native H0/B0 experiment or a mod-p² theorem.

## GH-85 — exact special-fiber formula and counterexample to root descent

Let a be any ordinary finite-field parameter (a != 0,1) satisfying Hcal_d(a)=0. Then theta U(a)=-5U(a)/8 and theta²U(a)=(theta Hcal_d(a))/8+25U(a)/64. Direct substitution into the full B gives

(85.1)
B(a)=(1-a)U(a)theta²S(a)
 -(1+3a)U(a)theta S(a)/8
 +(1-a)[theta Hcal_d(a)/8+3U(a)/64]S(a).

At the target a=9, using T=(8theta+1)S,

(85.2)
B(9)=-8U(9)theta²S(9) -(7/16)U(9)T_{p,9}
     +(U(9)/16-theta Hcal_d(9))S(9).

If U(a)=Hcal_d(a)=0 simultaneously, the entire coefficient of theta S and theta²S disappears: B(a)=(1-a)(theta Hcal_d(a))S(a)/8. The signed flux cannot determine T_{p,a} from that root datum. Formula (85.2) is conditional on Hcal_d(9)=0; it is not a proof of T_{p,9}=0.

**Exact non-descent witness.** At p=11,d=2 the original coefficient recurrences yield
S=1+6z+4z²,  T=1+10z+2z²,
U=1+6z+9z²,  Hcal=5+z+2z².
At a=7: Hcal(7)=0, but T_{11,7}=4 (mod 11). At a=9: Hcal(9)=T_{11,9}=0. Therefore Hcal(a)=0 does **not** imply T_{p,a}=0 for arbitrary a, even with the actual original finite truncation and reflected Laurent source. Any proof of the GH-3 special value must use arithmetic specific to a=9 and/or a further source-faithful boundary condition, not only the Hcal root.

## Exact verification and continuation

An executed pure-standard-library integer finite-field checker independently constructs S and U from their separate recurrences; verifies both complete differential equations including the terminal defect; expands B and independently compares every coefficient with (84.4) for **154 primes** 7<=p<2000, p=3 (mod 4). The same checker verified (85.1) at **582 finite-field Hcal-roots** for primes p<500, including 513 cases also satisfying U=0 and 528 controls where T is nonzero. The p=11,a=7 counterexample is also asserted from explicit coefficient vectors. Computation uses no floating point and supplies implementation evidence; mathematical generality rests on the displayed proofs. Author-side checks are not independent review/formal admission.

BRC: COMPOSE_APPLIED with population (p,z,r), ordered c_r/h_r and their distinct source labels, signed first/second jets, reflected root fibers, terminal forcing and B pairing. The integral observer must not erase a second-jet or collapse Hcal, T and Laurent H_r. All calculations here are in an explicitly external auxiliary scalar finite-field chart; they are not Heartbeat World native X6 cells or native transfer. P000 ACTIVE and observer/provenance preservation remain unchanged.

Inherited, not newly credited: GH-3 true finite source; GH-15/16 Laurent and reflected double-pole source (20261028_hourly_d25_gh15_gh16_finite_laurent_counterterm.md, blob fcfad3c663bf917cac691deea4b5585738eb69e5); GH-78 differential operator; GH-83 all-rank Laurent jet (blob fcfd4c576d749e8279bb72776b6769e12735688b). Other on-hour research at enterprise-math@6aed9ded2a54f765249cddaa6cc4c4e71527e9f8 studies a separate p²/CM Hasse rank-line source; not counted as this work.

**Next precise action:** find a source-independent CM/WZ evaluation of B(9) or its finite dual sum together with enough true S(9),theta²S(9) information to solve (85.2) for T_{p,9}; for double-root fibers seek a distinct second adjoint companion or exact finite endpoint certificate. The GH-83 remaining C_d(H_d+8d+1)-H_0+B_0L cancellation, independent GH-74/75 CM audit, GH-20/21, W/S, six Hasse ports, R23/R36 and native p=373 H0/B0 (#1559) remain open. At this run the gateway reported 0.6.11, Source sync control CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false and active quota 5/5; native recovery is tracked by #1558. No old session/claim/staging/request was modified, and no Source checkpoint is asserted.
