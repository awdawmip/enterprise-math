# PREFIX-402 — noisy I2/Cu sharp square-root localization, robust six-observation branch separation, and frozen-center false negative

Date: 2026-11-01 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING. Model: **external auxiliary static complex three-amplitude five-Port inverse model**, not P000-native X6 or typed BRC dynamics.

Frozen sources: GLOBAL_KNOWLEDGE_V1 main@c93fe73d7cc7391e8c27c5c51e0552ecfd611b2a (bootstrap, manual, P000, ACTIVE worldview, BRC and math rules); enterprise-math main@ace20a3785eb79ba4f7f4fa7299871fffc07a96e (P000 V5, preservation, Portable Research, PREFIX-401). Author-side reuse of PREFIX-401 is scoped to its exact model and hypotheses; independent mathematical admission remains pending.

## 1. Original matrix and exact observational coordinates

Original rows:
    A=[(4,4,0),(0,-4,4),(-5+3i,0,-3+i),(-2-2i,4+4i,2+2i),(-2,0,5+2i)].
The first three rows A3 have determinant -32+32i. Normalize the phase of W=A3 Y to W=(1,u,v); then Y=A3^{-1}W and B=A A3^{-1} is exactly

    (1,0,0); (0,1,0); (0,0,1);
    (5/2+9i/2, 3/2+7i/2, 4i);
    (11/4+15i/8, 11/4+15i/8, 5/4+9i/4).

All five Port outputs are I_j=|(BW)_j|^2. The coherent observers are Cu=|1+u|^2 and Cv=|1+v|^2. Fix I1=1; set u0=59/63. In v=c+id coordinates define N=75154, T=245c-123d, S=123c+245d. For the **nominal frozen u0 only**, original-row expansion gives

    I3=(T²+S²)/N;
    I4^0=16 I3+(16/63)T+300616/3969
       =16/N*((T+37577/63)²+S²);
    I5^0=53/(8N)*((T+43249/63)²+S²);
    Cv=1+I3+(2/N)(245T+123S).

The exact two reference sources have T=122, S=+368 or -368, respectively,
    v+ = 1+i,   v- = -7687/37577 -(52583/37577)i.
They share (I2,Cu,I3,I4^0,I5^0)=(3481/3969,14884/3969,2,550600/3969,4417309/63504), while Cv(v+)=5, Cv(v-)=97357/37577. Their true Cv difference is d0=90528/37577.

## 2. Theorem A: optimal 1/2-Hölder estimate for noisy I2 and Cu

For any complex u and nonnegative epsilon with
    ||u|²-u0²|<=epsilon,   ||1+u|²-(1+u0)²|<=epsilon,
one has

    |u-u0|² <= (1+2u0)*epsilon = (181/63)*epsilon.               (A)

Proof. Write u=x+iy. Subtraction of the two observations yields
    x=(Cu-I2-1)/2, hence |x-u0|<=epsilon.
The exact identity
    |u-u0|²=I2-u0²-2u0(x-u0)
proves (A). For epsilon=1/100000000 the right side is less than
3/100000000 < (1/5000)²; thus |u-u0|<rho=1/5000.

Sharpness: with u=u0+i h for any positive rational h, both observed differences are exactly h² but |u-u0|=h. Taking rational h->0 rules out every uniform exponent alpha>1/2 with a fixed local constant. This is an observer-fiber singularity, not a claim about physical measurement technology.

## 3. Theorem B: positive measured-Cv separation with six independently uncertain observations

Let u,v be arbitrary complex actual sources with I1=1 and

    |I2-3481/3969| <= 10^-8;     |Cu-14884/3969| <= 10^-8;
    |I3-2| <= 1/10;              |I4-550600/3969| <= 1/10;
    |I5-4417309/63504| <= 1/10.

The measured Cv additionally satisfies |Cv_measured-|1+v|²|<=1.
Then S=123 Re(v)+245 Im(v) is always nonzero. Both signs of S occur in the legal source set (the nominal sources witness them). The entire measured Cv set arising from S>0 is separated from the corresponding set arising from S<0 by at least

    GAP=68790132351/1854680473600 > 0.                         (B)

Proof. From (A), |u-u0|<rho=1/5000. I3<=21/10<9/4 gives |v|<3/2. Using the exact B rows, |a4+b4 u0|<9, |b4|<4, |c4|=4; and |a5+b5 u0|<7, |b5|<4, |c5|<3. Therefore the algebraic inequality ||L+E|²-|L|²|<=2|L||E|+|E|² gives

    |I4-I4^0|<120rho+16rho²<1/40;
    |I5-I5^0|<96rho+16rho²<1/50.

Hence |I4^0-J4|<1/8, and |I5^0-J5|<3/25 (the latter further restricts the true source population). The exact nominal identity for I4^0 implies

    |T-122|<=DT=(63/16)(1/8)+63/10=4347/640.

Since T²+S²=N I3,

    S² >= N*(19/10)-(122+DT)²
       = 51693638631/409600 > 355².

Thus the sign(S) branch cannot merge or vanish. Compare |S| to its nominal 368:

    ||S|-368| <= DS=[N/10+(244+DT)DT]/(355+368)
                =3776031769/296140800.

For a given sign, the true Cv is within

    H=1/10+(2/N)(245 DT+123 DS)
     =690021310849/3709360947200

of that sign's nominal Cv. Independent measured-Cv absolute error <=1 enlarges each band radius to H+1. The nominal band centers are separated by d0=90528/37577, and

    d0-2(H+1)=68790132351/1854680473600>0,

proving (B) for the **entire continuous error box**, without a finite grid argument. The conclusion is reliable branch-label discrimination, not point-source uniqueness within either branch.

## 4. Theorem C: exact false negative if variable-u annuli are frozen at u0

Take rational h=1/10000 and the genuine source W=(1,u0+i h,1+i), Y=A3^{-1}W. Its I2 and Cu are each exactly h²=10^-8 above nominal, I3=2 and Cv=5. The remaining I4/I5 shifts satisfy the stated +/-1/10 bounds (direct original-row calculation). Its true fourth-Port reading is

    I4_actual=110122857795101/793800000000.

If an algorithm incorrectly fixes u=u0 and asks for the same **exact** I3=2 and Cv=5, it forces Re(v)=1, Im(v)=+1 or -1. Neither candidate matches the true I4 reading:

    I4_actual-I4(u0,1+i)=720029/200000000 !=0;
    I4_actual-I4(u0,1-i)=-262384879391/4200000000 !=0.

Therefore the fixed-u0 four-annulus solver from PREFIX-401 would return NO on an exactly realizable seven-observer record. When I2 and Cu are intervals, the u-dependent circle centers must remain variable; freezing them is not a sound complete feasibility procedure. This is an explicit information-loss witness for the stated observer and future YES/NO operation.

## 5. Evidence, BRC boundary, and next

The source population retains each complex (u,v) and its exact global-phase-reconstructed Y, five distinct Port labels, Cu, Cv, sign(S) and individual measurement bounds. The branch sign is not erased by a quotient; theorem B certifies its robust observation, theorem C shows that deleting Im(u) destroys exact realizability. No typed BRC arithmetic or heart-world-native scientific operation was executed.

Actual local execution on 2026-11-01:
- verify_prefix402.py: PASS_PREFIX402_TWO_NOISY_U_OBSERVERS_SHARP_SQRT_AND_BRANCH_SEPARATION; SymPy matrix inversion, symbolic Port identities and exact rational inequalities.
- independent_fraction_check.py: PASS_PREFIX402_INDEPENDENT_PURE_FRACTION_ORIGINAL_PORT_WITNESS_AND_GAP; distinct standard-library rational complex-pair implementation.
- All constants and exact rational output recorded in PREFIX402 execution evidence. These are author-side checks, not independent review or canonical theorem admission.

Current native service v0.6.11 reports research_authority_granted=false / UPSTREAM_CODE_REVIEW_REQUIRED, active control quota 5/5, and control-task owner listing returns CONTROL_QUOTA. Thus no current owner/CLAIM/Result/review is inferred from normal GitHub publication.

NEXT PREFIX-403: with u ranging over the **two** measurement annuli from I2 and Cu, construct an executable, complete, two-way YES/NO realizability algorithm for the parameterized four-annulus v fibers; provide algebraic source witness or independently checkable NO certificate. Analyze singular boundaries, conjugate u branches and sign(S) collisions. P000 X6 and typed BRC dynamics require separate native bridge theorems.
