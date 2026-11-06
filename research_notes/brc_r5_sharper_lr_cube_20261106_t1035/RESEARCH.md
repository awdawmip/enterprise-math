# R5 — sharper exact four-dimensional seedless-LR behavior cube

Date: 2026-11-06 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Question, frozen scope and result
In the strictly positive rational four-stage P/Q experiment at delta=1/4, fix the observer W=(e_P,e_Q,T_P,T_Q), where e_P=P(declare Q), e_Q=Q(declare P). Every distinct stopped likelihood-ratio value must use one common declaration probability, across all occurrences and times. The frozen mother R5 problem compares the actual four-observer images of FULL_HIST and seedless LR, not merely their convex hulls.

Frozen science: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Predecessor EM@6367cb73500431b896938893f39c0098ceca3eee, research_notes/brc_r5_explicit_lr_four_cube_20261106_t0940/RESEARCH.md, certified an LR cube of radius 1/148.

**Theorem.** Put W*=(1/2,1/2,15/8,15/8) and h=11283/1291520. For *every real* W satisfying |e_P-1/2|,|e_Q-1/2|,|T_P-15/8|,|T_Q-15/8| <= h, W is exactly attained by a legal seedless LR randomized stopping and declaration policy. Thus the entire closed four-cube belongs to both actual observation images. The guaranteed radius is larger than the previous 1/148 by the exact factor 417471/322880 (approximately 1.293). This is a direct constructive theorem, covering irrational W and all cube boundaries.

## Inverse policy
Write a=T_P-15/8, b=T_Q-15/8, c=e_P-1/2, d=e_Q-1/2. The six continued-Q flow variables are:

    g=1/2+3*b-2*a;
    u0=u1=1/4;
    X0=27/640, X1=13/320, X2=27/640+2*(a-b).

Let M_rho denote *total* stopped Q mass at ratio rho, summing all occurrences of each key. In the inherited seven-ratio experiment R={1/10,1/2,3/4,1,5/4,3/2,19/10}, this legal flow gives

    M_{1/10}=3761/96000+(a-b)/50;
    M_1 >= 1-g >= 1/2-5*h > 0.

Take the shared P-declaration probabilities:

    t_{1/10}=1/2+10*(c+d)/(9*M_{1/10});
    t_1=1/2-(10*c+d)/(9*M_1);
    t_rho=1/2 for all other stopped ratio keys.

Use time-1 continuation probabilities u_i/g and time-3 continuation probabilities X_j/V_j, with V_j=(u0*q3[0,j]+u1*q3[1,j])/2 and q3 rows (13/20,1/5,3/20), (1/40,9/20,21/40). The inherited positive P-kernels are reconstructed by likelihood-ratio weighting. All time-1 and time-3 decisions share keys as prescribed; ratio-1 declarations are shared among root, time-3 and terminal occurrences.

## Complete proof
The frozen affine timing laws are

    T_P=1+g+(3*u0+5*u1)/8+X0/2+X1+3*X2/2;
    T_Q=1+g+(u0+u1)/2+X0+X1+X2.

Substitution gives T_P=15/8+a and T_Q=15/8+b. At fixed u0=u1=1/4, the three Q capacities are V=(27/320,13/160,27/320). Thus X0 and X1 are precisely half-capacity. Since |a-b|<=2h, we have |X2-27/640|<=4h. The rational inequality h<27/2560 proves 0<X2<V2. Likewise 1/2-5h<=g<=1/2+5h and h<1/20 imply 1/4<g<1. Hence all continuation probabilities are legal, on the whole closed cube.

For the central time-4 merger, put A=u0/10=1/40, B=9*u1/40=9/160, alpha=47/180, beta=67/162 and J_LR=X1*(alpha*A+beta*B)/(A+B). With u_i,X0,X1 held fixed, J_LR is constant. From the frozen affine terminal key-mass lift the contributions at ratios 1/10,1,19/10 are respectively

    (509*X0+9*X2)/900+J_LR,
    382*(X0+X2)/900+X1-2*J_LR,
    (9*X0+509*X2)/900+J_LR.

Other stopped ratio masses include 1-g at ratio 1, (g-u_i)/2 at ratios 3/4,5/4 and V_j-X_j at ratios 1/2,1,3/2. They are all nonnegative for the legal flow. Direct substitution yields M_{1/10}=m0+(a-b)/50 with m0=3761/96000, while M_1 contains 1-g as a nonnegative summand. The seven masses obey sum M_rho=sum rho*M_rho=1 (normalization and P/Q change of measure).

Start by setting each stopped key's P-declaration probability to 1/2: then e_P=e_Q=1/2. Let s=t_{1/10}-1/2, r=t_1-1/2. Because the P mass at ratio rho is rho*M_rho, perturbing only the two *shared* declaration keys produces

    c=-M_1*r-(1/10)*M_{1/10}*s,
    d= M_1*r+M_{1/10}*s.

Solving the two equations gives exactly the inverse declarations above. For all |a|,|b|,|c|,|d|<=h,

    M_{1/10} >= m0-h/25,
    |s| <= 20h/[9*(m0-h/25)] = 1/2,

where the last equality follows from h=9*m0/(40+9/25)=11283/1291520. Also

    |r| <= 11h/[9*(1/2-5h)] <= 1/2,

since h<9/134. Consequently every declaration probability lies in [0,1]. The displayed exact timing and error equations prove realizability for every real W in the closed cube. QED.

**Sharpness within the stated controller.** At corner (c,d,a,b)=(h,h,-h,h), we have M_{1/10}=m0-h/25 and s=20h/[9*(m0-h/25)]=1/2. Any radius h'>h sufficiently close, keeping this exact same inverse section and choosing the corresponding corner, yields s>1/2 and an invalid P-declaration probability >1, while the flow remains feasible. This establishes the maximum cube radius for the *displayed* section; no global optimum across all LR strategies is claimed.

## Exact validation
VERIFY.py (Python 3 standard library fractions.Fraction) reconstructs all seven stopped masses, P/Q mass totals, positive conditional moments, all 625 rational grid targets {-2,-1,0,1,2}^4/2 within the cube and all 16 corners. It confirms both errors and both time coordinates exactly, the saturated t_{1/10}=1 corner, and controller failure at radius 1/114. Its actual execution produced PASS_EXACT_R5_SHARPER_FOUR_CUBE_RATIO_ONE_TENTH_KEY; see EXACT_OUTPUT.txt. General all-real quantification is by the analytic inequalities above.

## Interpretation and next research
This is a faithful seven-key positive-mass BRC observer certificate. Replacing the prior time-2 ratio-3/4 error-control key by the terminal ratio-1/10 key increases the assured deviation leverage while retaining key sharing. The full-history vs LR actual-image separation/equality mother question remains open. Next seek rational FULL_HIST points strictly outside this certified cube, with stopping times inside the established octagon and e_P+e_Q!=1. Evaluate the full six-flow FULL linear feasibility and the global LR K(W) single-quadratic sign test (not a fixed-flow support difference). A positive one-sign certificate or explicit LR reconstruction is the discriminating outcome.

Normative read: global main@97515dba2ddb993adbe778d9c6df6ed58e7cdb9a; EM main@8aacd7312fd930dcf093c942730cc887c0005367. Relevant current P000, ACTIVE worldview, BRC and math proof policies, portable research and continuation normative context were consulted. The auxiliary finite P/Q experiment is not claimed as native X6 dynamics. Authenticated GitHub identity awdawmip; native session request EMR5-20261106T1035-R11-SESSION and task-inventory request EMR5-20261106T1035-R11-TASKS last returned QUEUED, so this document is portable author-side evidence with no represented formal CLAIM or independent acceptance. No credentials appear here.