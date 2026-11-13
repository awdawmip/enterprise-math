# S23/AV: six exact capacity plateaus and the first five jump locations

Date: 2026-11-08 (Asia/Shanghai). Status: author-side analytic proof with exact-rational implementation checks; independent mathematical review pending.

Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Parent: PR #1777, earlier H=30001 certificate and scaled-gap unimodular first-entry theorem.
Model: auxiliary two-point iid likelihood-sign observer for labels (1,3,4). P0=(1/2,1/4,1/4), P1=(5/7,1/4,1/28). BRC keeps the joint counts of labels 1 and 4; label 3 is padding.

## Definitions and exact theorem

Put r=ln(7)/ln(10/7). For integers h,n>=0 let
T_h={t(v,j)=r v-j : v,j>=0, v+j<=h};
S_n={E(k,l)=k-r l : k,l>=0, k+l<=n}.
The minimum sufficient length N(h) is the smallest n for which EVERY open component of R\T_h meets S_n.

All integer horizons in these six intervals have the following **exact** capacities:

| h, inclusive | N(h) | jump above preceding plateau |
| --- | ---: | ---: |
| 510..380805 | 2455069 | base |
| 380806..761179 | 4530352 | 2075283 |
| 761180..1141474 | 6605047 | 2074695 |
| 1141475..1521848 | 8680331 | 2075284 |
| 1521849..1902143 | 10755026 | 2074695 |
| 1902144..2282517 | 12830310 | 2075284 |

In particular, the **first** strict jump beyond h=510 occurs at exactly h=380806. The proof is a symbolic, constructive all-cell coverage theorem and uses no enumeration of the ~quadratically-many thresholds.

## Unimodular lattice and six certificate points

Let u=(79,431), w=(D,P)=(380295,2074774), epsilon=79r-431, eta=P-Dr. The determinant 79P-431D=1. Exact rational logarithm bounds (see verifier) give 0<eta<epsilon<2eta and r is irrational by unique prime factorization; alpha=eta/epsilon is irrational by the unimodular relation.

For b=1,...,6 define a_b=floor(b alpha), v_b=D b+79 a_b, k_b=P b+431 a_b, delta_b=k_b-r v_b=b eta-a_b epsilon, and m_b=v_b+k_b. Thus 0<delta_b<epsilon. Exact data:

| b | a_b | v_b | k_b | m_b |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 0 | 380295 | 2074774 | 2455069 |
| 2 | 1 | 760669 | 4149979 | 4910648 |
| 3 | 1 | 1140964 | 6224753 | 7365717 |
| 4 | 2 | 1521338 | 8299958 | 9821296 |
| 5 | 2 | 1901633 | 10374732 | 12276365 |
| 6 | 3 | 2282007 | 12449937 | 14731944 |

Take v_0=-1, n_1=m_1 and n_b=m_b-(v_(b-1)+1) for b>=2. Their plateau starts are h_1=510 and h_b=v_(b-1)+511 (b>=2); ends H_b=v_b+510. The starts and ends meet without gaps.

## Lemma 1: global threshold separation for h<m_1

For 510<=h<m_1=2455069, all distinct thresholds t_L<t_R in T_h have t_R-t_L>=epsilon, with equality at (0,0),(79,431).

Proof. A positive difference is r a-b, with (a,b)=(v_R-v_L,j_R-j_L), |a|+|b|<=h whenever both signs agree. Opposite-sign or zero-component cases have positive difference at least min(1,r)>epsilon, or are negative. For a,b>=0 write (a,b)=A u+B w in the integral basis. Then
a+b=510 A+m_1 B, r a-b=A epsilon-B eta.
If B>=1 the length bound forces A<0, yielding negative difference. If B=0, positivity implies A>=1 and difference>=epsilon. If B<=-1, nonnegative a=79A+D B forces A>=1, so difference=A epsilon+|B| eta>epsilon.

For a,b<=0 decompose (-a,-b)=A u+B w instead. If B<=0, coordinate nonnegativity forces A>=1 and the original difference is negative. If B>=1, the length bound forces A<=-1, and the original positive difference is |A|epsilon+B eta>epsilon. QED.

## Lemma 2: narrow-gap classification near the right edge

Let H_*=v_6+510=2282517, so H_*<m_1-6*510=2452009. For h<=H_*, any positive threshold difference STRICTLY SMALLER than 7 epsilon can only be a difference A u=(79A,431A), with 1<=A<=6. Consequently, if its right endpoint has j_R<=430, its gap is >=7epsilon.

Proof. Opposite-sign differences are either negative or have size>=min(1,r)>7epsilon. For a,b>=0 in Lemma 1, B>=1 is impossible for a positive difference. B=0 yields A epsilon. With B<=-1, nonnegative a forces A>=ceil(D/79)>7 and the difference exceeds 7epsilon.

For a,b<=0 decompose (-a,-b)=A u+B w. Positive differences require B>=1,A<=-1. If such a difference were <7epsilon, |A|<=6, implying
(-a)+(-b)=m_1 B-510|A| >=m_1-3060>H_*,
impossible in the triangle. Therefore all gaps <7epsilon have b=431A>0, and j_R>=431. QED.

## Lemma 3: constructive upper cover on each entire plateau

Fix b in 1..6 and h_b<=h<=H_b=v_b+510. We prove N(h)<=n_b.

Consider a bounded threshold cell (t_L,t_R), with left endpoint (v_L,j_L).

Case I: v_L<=v_b. Choose smallest i<=b with v_L<=v_i and j_L<=k_i (exists because k_b>H_b). Prefix counts k=k_i-j_L, ell=v_i-v_L are nonnegative, and E(k,ell)=t_L+delta_i. By Lemma 1 its score lies strictly within the cell. Its length m_i-(v_L+j_L) is <=n_i<=n_b: for i=1 this is immediate; for i>=2, minimality of i implies v_L>=v_(i-1)+1 OR j_L>=k_(i-1)+1>v_(i-1)+1, so length<=m_i-(v_(i-1)+1)=n_i.

Case II: v_L>v_b. Since h<=v_b+510, j_L<=509. Let (v_R,j_R) be the right endpoint. Set q=max(1,ceil((v_R-v_b)/79)), so 1<=q<=7. Define
k=k_b+431q-j_R, ell=v_b+79q-v_R.
Both are nonnegative and the score is
E(k,ell)=t_R+delta_b-q epsilon <t_R.
For q=1, Lemma 1 gives gap>=epsilon>epsilon-delta_b. For q>=2, v_R>v_b+79 and j_R<=h-v_R<=430; Lemma 2 gives gap>=7epsilon>q epsilon-delta_b. Thus E lies above t_L in either case.

For the length, k+ell=m_b+510q-(v_R+j_R).
If q>=2, v_R>=v_b+80>=v_(b-1)+1+510q because v_b-v_(b-1)>=D and q<=7. Hence k+ell<=n_b.
If q=1, we claim v_R+j_R>=v_(b-1)+511. Otherwise v_R<=v_(b-1)+510 gives t_R<=r(v_(b-1)+510), whereas v_L>=v_b+1 and j_L<=509 give t_L>=r(v_b+1)-509. The difference r(D-509)>509 contradicts t_R>t_L. Therefore k+ell<=m_b+510-(v_(b-1)+511)=n_b. The convention v_0=-1 covers b=1.

Exterior cells: E(0,n_b)=-r n_b<-h because n_b>h. E(n_b,0)=n_b>r h follows from
n_b-r(v_b+510)=delta_b+(v_b-v_(b-1)-1)-510r>0,
using r<6 and successive v gaps >=D (and v_0=-1). The extreme thresholds are -h and r h. All cells have length<=n_b witnesses. QED.

## Lemma 4: exact lower bound at each interval's first horizon

The thresholds (0,0) and (79,431) are adjacent in T_510. Indeed their exact integer-order keys P v-D j are 0 and 1. The key preserves strict order for H=510 by coprimality, 510<D, and 510 eta<1. No integer key lies between.

For t>=0, (r t,r t+epsilon) is adjacent in T_(510+t). An intermediate t(v,j) would require v>=t and after subtracting r t would give a T_510 threshold inside (0,epsilon), contradiction.

Prefix E(k,ell) enters the shifted gap precisely if v=ell+t>=t and 0<k-r v<epsilon. Write (v,k)=A u+B w. Then 0<B eta-A epsilon<epsilon. If B<=0, v>=0 forces A>=0, contradicting the inequality. Hence B>=1, and the UNIQUE admissible integer A is floor(B alpha). Both v_B,k_B increase strictly with B, so the shortest entering length is
L(t)=k_(B(t))+v_(B(t))-t
where B(t)=min{B>=1:v_B>=t}. Therefore N(510+t)>=L(t).

At t=0 this gives N(510)>=m_1=n_1. For b=2,...,6 set t=v_(b-1)+1. Then B(t)=b, giving N(h_b)>=m_b-(v_(b-1)+1)=n_b at h_b=v_(b-1)+511. Since T_h are nested, N(h) is nondecreasing. Combined with Lemma 3, this proves every exact plateau and every first-jump location. QED.

## Verification, BRC scope, next open question

VERIFY_FIRST_JUMP.py is a Python standard-library Fraction verifier with 45-term rational atanh enclosures and strict remainder bounds for log(2), log(8/7), log(5/4); it checks the 26-decimal rational r enclosure, six mechanical-sequence floors, all plateau coordinates and jump sizes, right-edge feasibility and the exact numerical hypotheses of the proof. RUN_EVIDENCE.txt is its actual execution output. This code checks the arithmetic hypotheses; the analytic lemmas prove the quantified all-cell coverage.

BRC use is the retained (label-1,label-4) joint count with label-3 padding under finite future likelihood-sign testing. The auxiliary observer result remains distinct from a six-source/ten-label mother-model or native X6 realization. This mathematical output is an author-side proof candidate, not Source-native Result/Review or theorem promotion.

Next: from h=2282518 seek the next exact jump. Lemma 1's bound changes once h reaches m_1=2455069 because the vector w itself enters the allowable differences. Develop a new edge-gap classification that admits this direction, or a conditional finite-window upper certificate. In parallel preserve delta_4 minimax and lawful mother-model observation bridge as distinct open routes. Bit complexity of generalized oracles requires full preprocessing/precision accounting.
