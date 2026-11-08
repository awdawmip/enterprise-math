# R5: All-real unsaturated Blackwell lift for the complete lawful half-cone 0 ≤ b ≤ a

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.
Immediate predecessor: R5 Draft PR #1796 at 5594be0335d1c410c5d178754248c5d299354a3c, already covering the saturated all-eta prism. The present theorem allows arbitrary v-z and z, covering both residual signs, and is not a new P000 or native-X6 theorem.

## Theorem

In the pinned four-stage seven-likelihood-node P/Q-BRC *statistical* model, let a FULL_HIST flow be x=(g,a,b,u,v,w,z), with the lawful constraints:

    0≤g≤1; 0≤a≤g; 0≤b≤g;
    0≤u≤13a/40+b/80; 0≤w≤3a/40+21b/80;
    0≤z≤a/10; z≤v≤z+9b/40.

The Q branch masses M_i(x), indexed i=0,...,6, are:

    M0=509u/900+47z/180+67(v-z)/162+w/100;
    M1=13a/40+b/80-u; M2=(g-a)/2;
    M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81;
    M4=(g-b)/2; M5=3a/40+21b/80-w;
    M6=u/100+47z/180+67(v-z)/162+509w/900.

The P likelihoods are r=(1/10,1/2,3/4,1,5/4,3/2,19/10), and the observers:

    TP=1+g+3a/8+5b/8+u/2+v+3w/2;
    TQ=1+g+(a+b)/2+u+v+w.

The seedless-LR locus obeys 9*b*z=4*a*(v-z). Both branch measures normalize to 1.

**Proposition, fully quantified.** For **every lawful real x with 0≤b≤a≤g≤1**, there exist a lawful seedless-LR y and nonnegative 7×7 Q[target i, source j] such that

    sum_j Q[i,j]=M_i(y);
    sum_i Q[i,j]=M_j(x);
    sum_i r_i Q[i,j]=r_j M_j(x);
    TP(y)=TP(x), TQ(y)=TQ(x).

Both y and Q are independent of the seven-component declaration d. Therefore for every d in [0,1]^7, d'_i=(sum_j Q[i,j]*d_j)/M_i(y) on positive rows (zero on zero rows) belongs to [0,1]^7 and exactly matches both P and Q error probabilities and TP/TQ. Further, for all h in [0,1], x_h=(1-h)x+h*y is calibrated to y using Q_h=(1-h)Q+h*diag(M(y)). This is a theorem for all real, including irrational and boundary, parameters.

## Exhaustive parametrization of the lower half-cone

When a=s>0 let eta=b/a, theta=10z/a, kappa=40(v-z)/(9b) (use kappa=0 at b=0), p=u/(13a/40+b/80), q=w/(3a/40+21b/80). All eta,theta,kappa,p,q lie in [0,1]. Then every source x with b≤a can be written

    x=(g,s,eta*s,s*(13/40+eta/80)*p,
       s*(9*eta*kappa/40+theta/10),
       s*(3/40+21*eta/80)*q,s*theta/10)

for 0≤s≤g≤1. The a=0 boundary forces b=u=w=v=z=0 and corresponds to s=0. The structural history residual is exactly R=9*eta*s²*(theta-kappa)/10; both signs occur in this theorem.

## Exact calibrated vertices and closed-form interpolation proof

Define two *linear* seedless faces:

    G: b=0, v=z;
    F: z=a/10, v-z=9b/40.

Each face is convex; the legality, mass and Blackwell calibration constraints and both stopping times are affine in (source x,target y,Q). Hence nonnegative convex interpolation **within one chosen face** preserves all required equations. Cross-face mixing is not used.

The exact evidence contains 42 rational vertex triples (x,y,Q), with 360 nonzero rational kernel entries. The authoritative portable file is CERTIFICATES.json, available after extracting the attached compressed evidence bundle; VERIFY.py checks each edge and exact equality. Identity triples at eta=0 already on G (theta=0) or F (theta=1) are the only omitted trivial vertices.

Let G triangle vertices in (p,q) be (0,0),(1,0),(1,1/2), and F quadrilateral vertices be (0,0),(0,1),(1,1),(1,1/2). Together they cover the entire p,q square: for q≤p/2, G weights (1-p,p-2q,2q); for q≥p/2, use t=(q-p/2)/(1-p/2) and F weights ((1-t)(1-p),t(1-p),t*p,(1-t)*p). Each weight is nonnegative and sums to one.

**Regime I, 0≤eta≤1/10.** Set lambda=10eta and T=1-10eta.

* For 0≤theta≤T, choose G when q≤p/2, otherwise F. At the lower theta=0 boundary: eta=0 has G identity or four F quadrilateral exact vertices; eta=1/10 has three G triangle vertices or four F square vertices, for both kappa endpoints. At the upper boundary theta=T: its eta=0 endpoint is theta=1 and the source itself lies on **both** G and F (use same-face identity), while its eta=1/10 endpoint is theta=0 and uses the same G or F vertices. Interpolate each boundary in eta with (1-lambda,lambda), kappa with (1-kappa,kappa), and p,q within its chosen polygon. Interpolate the theta boundaries with (1-theta/T,theta/T), with the T=0 boundary interpreted at theta=0. All mixtures stay on the same face.

* For T≤theta≤1, use only F and its full p,q square vertices. At theta=T interpolate between (eta,theta)=(0,1) F identity and (1/10,0) F vertices; at theta=1 interpolate between (0,1) identity and (1/10,1) F vertices. First interpolate eta/kappa/p/q, then theta with ((1-theta)/(1-T),(theta-T)/(1-T)) when T<1; at eta=0 only theta=1 belongs to this upper region. All are exact calibrated F triples.

**Regime II, 1/10≤eta≤1.** The F face has complete rational corner certificates for each eta in {1/10,1}, theta,kappa in {0,1}, and p,q in {0,1}; 32 F vertex triples (some already used in Regime I). At fixed other inputs, x is affine separately in eta,theta,kappa,p,q. The nonnegative tensor-product interpolation of these F vertices matches the intended x **exactly**, gives legal F target and nonnegative calibrated kernel for every real parameter.

**Scaling.** Let E1=(1,0,0,0,0,0,0), E0=(0,0,0,0,0,0,0), both seedless on G and F. Mix any normalized (g=a=1) triple and diagonal identity triples E1/E0 with weights (s,g-s,1-g). This reproduces the full arbitrary 0≤s≤g≤1 source while preserving its chosen face and calibration. Then the Q_h construction in the theorem statement gives the all-real source-to-target interpolation.

The two regimes exhaust the normalized eta domain, the face/polygon decomposition exhausts p/q, and all weights are nonnegative. The exact vertex checks plus this algebra prove the universal result; sampled numerical grids alone do not imply it.

## Reproducible checks and provenance

SciPy HiGHS was used only to discover feasible support patterns; SymPy rational active-set reconstruction produced exact rational coefficients. An independent Python standard-library Fraction checker verified all 42 source-target pairs, all 49 kernel entries per certificate (including zero entries), P-weighted columns, Q columns, rows, both normalizations, lawfulness, seedless residual and TP/TQ. Actual local execution:

    EXACT_ANCHORS_PASS 42 Q_EDGES 360
    EXACT_NORMALIZED_PARAMETER_GRID_PASS 2160
    EXACT_SCALED_INTERPOLATED_GRID_PASS 4860
    PASS_R5_UNSATURATED_ALL_REAL_B_LE_A_COMPLETE_FIVE_PARAMETER_PRISM_42_RATIONAL_CERTS

These totals are not extrapolated to the reals; the exact affine interpolation above establishes that domain. Source paper, full 42 exact sparse matrices, standalone Python checker, actual local output and next-step notes are in the companion artifact R5_FULL_EVIDENCE.tar.xz (Python stdlib: tarfile.open('R5_FULL_EVIDENCE.tar.xz').extractall(...)). This branch is author-side provenance pending independent review; no native Source CLAIM/Result/Review or full native six-axis physical implication is asserted. Protected P000 and worldview remain unchanged.

**Remaining R5 mother question:** analyze the complementary lawful sector b>a (including a=0<b). The current theorem does not cover it. A discriminating exact test is outlined in NEXT_UNIT.md.
