# R5: an exact noncentral four-observer LR repair cube and robust fifth-observer residual

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific inputs unchanged: GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Exact predecessor: EM 5250299b49b4ee89bf199091f2e95da44c90ea71, research_notes/brc_r5_five_observer_mass_repair_20261106_t1937/{RESEARCH.md,PROJECTION_REPAIR.md,VERIFY.py,VERIFY_PROJECTION.py}. This is the fixed strictly positive four-stage delta=1/4 P/Q-BRC likelihood-ratio tree, not native X6 dynamics or a revision of P000.

## Theorem A: all-real closed four-dimensional inverse neighborhood

Let W=(e_P,e_Q,T_P,T_Q), where e_Q=Q(declare P) and e_P=P(declare Q), and fix

W*=(161801/180000,6499/18000,267/80,137/40),

h=93519/349275680=0.000267751250244506....

**For every real W such that ||W-W*||_infinity <= h, an explicit legal seedless LR policy exactly realizes W, including boundary points.** For the *fixed flow and two-label affine inverse section below*, h is the maximal centered L-infinity cube radius. This section-specific optimality is distinct from global LR-image optimality.

Choose Q continuation g=u0=1, u1=37/40, X2=0. The pooled time-3 likelihood-ratio key capacities are

V0=13u0/40+u1/80=1077/3200,
V1=u0/10+9u1/40=493/1600,
V2=3u0/40+21u1/80=1017/3200.

The central terminal coefficients are alpha=47/180, beta=67/162, A=u0/10, B=9u1/40. Seedless LR pooling forces J=k X1 with k=(alpha A+beta B)/(A+B)=359/986.

At the center set X0*=5/32, X1*=49/160, ell_a*=1787/9000 for likelihood ratio a=1/10 and ell_b*=13/80 for b=1/2. For a real target W, put dp=e_P-e_P*, dq=e_Q-e_Q*, dtp=T_P-T_P*, dtq=T_Q-T_Q* and take

    X0 = 5/32 + 2(dtq-dtp)
    X1 = 49/160 + 2dtp-dtq
    X2 = 0
    ell_a = 1787/9000 + (5/2)dp + (5/4)dq
    ell_b = 13/80 - (5/2)dp - dq/4.

At each present LR key j, use the common continuation probability z_j=X_j/V_j, independently of earlier history. Equivalently, frozen Q3 history flows are x_ij=(u_i/2) q3[i,j] z_j. The stopped Q masses at the two declaration keys are

    M_a=(509/900)X0+k X1,   M_b=V0-X0.

Declare P at ratio a with probability p_a=ell_a/M_a and at ratio b with probability p_b=ell_b/M_b; declare Q otherwise. This is a seedless LR policy. Exact observer equations are

    T_Q=1+g+(u0+u1)/2+X0+X1,
    T_P=1+g+(3u0+5u1)/8+X0/2+X1,
    e_Q=ell_a+ell_b,
    e_P=1-(1/10)ell_a-(1/2)ell_b.

Both pairs are invertible linear maps, so substituting the construction returns precisely W.

Legality reduces to eight affine inequalities

    0<=X0<=V0,  0<=X1<=V1,  0<=ell_a<=M_a,  0<=ell_b<=M_b.

The initial g,u0,u1 are legal, the positive frozen Q3/Q4 kernels reconstruct legal stopped masses with normalization and LR first moment one. Each affine slack f(W) with center s and coefficient vector c has minimum s-h*sum(|c_i|) on the entire closed real four-cube. The exact complete list of center slack, L1 coefficient norm, and allowed radius s/L1 is:

| inequality | center slack | coefficient L1 | radius |
|---|---:|---:|---:|
| X0>=0 | 5/32 | 4 | 5/128 |
| V0-X0>=0 | 577/3200 | 4 | 577/12800 |
| X1>=0 | 49/160 | 3 | 49/480 |
| V1-X1>=0 | 3/1600 | 3 | 1/1600 |
| ell_a>=0 | 1787/9000 | 15/4 | 1787/33750 |
| ell_b>=0 | 13/80 | 11/4 | 13/220 |
| M_a-ell_a>=0 | 10391/7888000 | 2182973/443700 | **93519/349275680** |
| M_b-ell_b>=0 | 57/3200 | 27/4 | 19/7200 |

The smallest ratio is precisely h. Hence all eight inequalities hold for every real target in the cube. The limiting affine slack M_a-ell_a has coefficient vector (-5/2,-5/4,2k-1018/900,1018/900-k); at W*+(h,h,h,-h) this slack equals 0 and p_a=1. Any larger centered cube in THIS SAME affine inverse section violates p_a<=1 at the corresponding corner. This proves the section's exact radius optimality without relying on finite samples.

## Theorem B: a continuum of matched four-readouts and separated five-readouts

The exact predecessor FULL_HIST witness has W*, stopped Q masses M_a^F=1787/9000, M_b^F=13/80, M_3/2^F=27/80, and probability-one declarations at a,b. Keep all its history-sensitive continuation flows fixed and decrease the two stopped P declaration masses by arbitrary REAL s,t in [0,h/2] each. Both new probabilities remain legal. The new FULL_HIST four-readout is

    W_F(s,t)=(e_P*+s/10+t/2, e_Q*-s-t, T_P*, T_Q*),

while M_3/2^F(s,t)=27/80 remains constant.

Every such W_F(s,t) lies in the cube of Theorem A, because |delta e_Q|=s+t<=h, |delta e_P|=s/10+t/2<=3h/10, and the time coordinates are unchanged. Thus EACH member of this real two-parameter FULL_HIST family has a matching seedless LR four-readout. That LR construction has the constant stopped-mass coordinate M_3/2^LR=V2-X2=1017/3200, so the hidden fifth-coordinate discrepancy is exactly

    M_3/2^F-M_3/2^LR=63/3200.

The five-observer separation persists uniformly throughout this rectangle. The predecessor's algebraic certificate proves that for ANY seedless LR strategy with the *fixed* (T_P,T_Q,M_3/2)=(267/80,137/40,27/80), one has D=e_P+e_Q-1<=10113/40000, because saturated M_3/2 forces g=u0=u1=1, X2=0 and the pooled central terminal coefficient. For our family,

    D_F(s,t)=5199/20000-(9/10)s-t/2,
    D_F(s,t)-10113/40000 >= 57/8000-7h/10
                            =15144537/2182973000>0.

Consequently, each such four-readout is LR-attainable, yet its enriched five-readout with M_3/2=27/80 is strictly FULL_HIST-only, with a uniform exact rational margin. The four-observer projection therefore erases a genuine family of BRC history-residual distinctions.

## Verification, scope and next action

The accompanying exact standard-library Fraction verifier tests the eight sharp affine-slack radius bounds; all sixteen closed-cube vertices including the binding corner; eighty-one rational parameter pairs from the rectangle; mass conservation, LR first moment, the exact time/error inverse equations and the uniform strict five-coordinate gap. The observed local output is in EXACT_OUTPUT.txt. The theorems for *all real* targets follow from the explicit affine inverse and the L1 slack certificate, not the sampled grid. The independent predecessor checker validated the positive frozen stochastic kernel and history-dependent witness. An expanded local checker additionally rechecked all positive Q3/Q4 kernels and shared-history flow reconstruction.

BRC use: the seven-bin stopped ratio-mass carrier and pooled central J (REUSE_APPLIED), preserving source/historical provenance while comparing the four-observer projection with the extra M_3/2 bin. This is a noncentral robust repair theorem; original R5 global four-observer equality/separation remains open. Current global and EM main normative rules were separately read, frozen science and P000 unchanged.

Next unit: find an interior rational FULL_HIST four-readout W outside this verified LR cube, construct its complete seven-variable K(W), and decide the global real sign of F=(A+B)J-X1(alpha A+beta B). A zero is a seedless LR reconstruction; an exact one-sided certificate separates the original four-readout images. A separate constructive route optimizes u1 and label keys for larger repair neighborhoods. Native owner/CLAIM and independent review remain separate from author-side Git evidence.
