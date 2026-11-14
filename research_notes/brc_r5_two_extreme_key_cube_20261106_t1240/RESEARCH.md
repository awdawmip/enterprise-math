# R5: enlarged all-real seedless-LR four-cube with both extreme declaration keys

Date: 2026-11-06 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Model and theorem

Frozen science inputs: GLOBAL a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e. Reuse the exact strictly-positive delta=1/4 four-stage P/Q likelihood-ratio kernels and scalar lift from EM 57f7d654e5dd002567e0b0d333937e6e38f3b4cb, and the preceding cube theorem from EM 0418a72bbd7238f72eb2d92723e8e9fb9d0e8b71. This is a P/Q-BRC auxiliary observer, not native X6 dynamics.

**Theorem.** Every real W=(e_P,e_Q,T_P,T_Q) in the CLOSED four-cube centered at W*=(1/2,1/2,15/8,15/8), with max-coordinate radius h=1/52, is achieved exactly by a valid seedless LR stopping-and-declaration policy. It is therefore in both actual LR and FULL_HIST images. The previous proven radius 10395/788344 is enlarged by exact factor 197086/135135, approximately 1.458438 (+45.84%).

## Universal explicit inverse strategy

Let a=T_P-15/8, b=T_Q-15/8, c=e_P-1/2, d=e_Q-1/2; all lie in [-h,h]. Write z_a=a/h,z_b=b/h. Let u_0=u, u_1=13u/10. Define (g,u,X0,X1,X2)=f0+z_a*fa+z_b*fb with

f0=(7129/20000,137/500,29/400,79/1000,1039/20000)
fa=(-2011/104000,-3/200,-9/2000,3/500,3649/104000)
fb=(673/52000,1/100,23/1000,-3/250,-843/52000).

At time 1 continue with probability g. At time 2 history i use u_i/g. At the shared time-3 LR key j use X_j/V_j, with V_j=(q3[0,j]*u_0+q3[1,j]*u_1)/2. The inherited time-2 Q probabilities are (1/2,1/2), ratios (3/4,5/4). The time-3 Q rows are (13/20,1/5,3/20) and (1/40,9/20,21/40), with ratios (1/2,1,3/2). The time-4 ratio keys are (1/10,1,19/10); outer j=0,2 Q rows are respectively (509,382,9)/900 and (9,382,509)/900 (independent of i), and the central j=1 Q rows are (47/180,43/90,47/180) and (67/162,14/81,67/162). Each Q row is positive, stochastic and has child-ratio mean equal to its parent ratio; P is the LR weighting.

The central pooled coefficient is J=k*X1 with k=353/942, because k=(alpha*(1/10)+beta*(9/40)*(13/10))/((1/10)+(9/40)*(13/10)), alpha=47/180, beta=67/162. Thus F=(A+B)J-X1*(alpha A+beta B)=0 identically, A=u/10,B=9u_1/40.

For the total stopped Q mass at LR key r, write M_r. In particular
M_-=M_(1/10)=(509X0+9X2)/900+kX1,
M_+=M_(19/10)=(9X0+509X2)/900+kX1.

Set the probability of declaring P at r=1/10 to
t_-=1/2+(10c+19d)/(18M_-),
and at r=19/10 to
t_+=1/2-(10c+d)/(18M_+).
At ALL other stopped-ratio keys set the common declaration probability t_r=1/2. Equal LR values always receive the same declaration probability across histories and stages.

## All-real proof

For the inherited stopping laws,
T_Q=1+g+(u_0+u_1)/2+X0+X1+X2,
T_P=1+g+(3u_0+5u_1)/8+X0/2+X1+3X2/2.
Substitution of f0,fa,fb gives T_Q=15/8+b,T_P=15/8+a EXACTLY.

The required timing and declaration margins are affine in real (z_a,z_b). Checking their four corners suffices for the entire square. The exact minima over all four corners are:

g: 168569/520000; 1-g: 317861/520000;
u_0: 249/1000; g-u_0: 39089/520000; g-u_1: 3/104000;
X0: 9/200; V0-X0: 637/800000;
X1: 61/1000; V1-X1: 293/400000;
X2: 339/520000; V2-X2: 4141/10400000;
M_- - 29h/9: 55649227/73476000000;
M_+ - 11h/9: 53140507/73476000000.

Every margin is strictly positive. In particular g,V_j,M_-,M_+ are positive and 0<=u_i<=g, 0<=X_j<=V_j. The above ratio timing policy is therefore legal for EVERY REAL z_a,z_b in the square.

For |c|,|d|<=h, |10c+19d|<=29h and |10c+d|<=11h. Thus the two mass lower bounds imply |t_--1/2|<=1/2 and |t_+-1/2|<=1/2. All seven shared-key declaration probabilities are in [0,1].

Since sum_r M_r = sum_r r*M_r=1, the half-half baseline has (e_P,e_Q)=(1/2,1/2). With corrections s_-=t_--1/2,s_+=t_+-1/2, the changes satisfy
d=M_- s_-+M_+ s_+,
-c=(1/10) M_- s_-+(19/10) M_+ s_+.
The two displayed inverse formulas solve this 2x2 system identically. Hence the exact errors are e_P=1/2+c,e_Q=1/2+d. Every real point of the closed four-cube is attained. QED.

## Verification and status

Python standard-library Fraction independently checks the exact 13 four-corner minima; all seven stopped-ratio masses sum to 1 with first LR moment 1; the F=0 identity; the source Q-kernel normalization and moments; exact timing; legal declaration probabilities and output equality on the 625 rational points of the 5^4 grid (including 16 four-cube vertices). Exact local output tag: PASS_EXACT_R5_TWO_EXTREME_LABEL_KEYS_FOUR_CUBE_1_OVER_52. The finite grid is a regression check; the affine four-corner proof covers ALL REAL targets.

Current unresolved R5 question: whether the full actual image strictly contains the seedless LR image, notwithstanding equal hulls. Next, pick FULL-feasible rational W outside this cube and outside the balanced-error slice, with time pair in the interior of the known octagon, then globally certify the sign interval of the single quadratic F over its complete seven-dimensional linear fiber K(W). No task CLAIM, formal Result or independent Driver mathematical admission was obtained by the present author-side construction.
