# R5 — Exact 28-facet FULL_HIST projection: stopping times and label-sum residual

Date: 2026-11-06 Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Input, model and mother objective

Frozen scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Immediate predecessor: Git commit ca6ddcacbd02942bcbeee86c50e2bd33a5d3c26a, R5 sharp asymmetric time-gap bound. Current behavioral rules read separately from frozen science. This finite positive P/Q decision tree is a typed auxiliary BRC observer, not an X6 native-space model.

FULL_HIST permits arbitrary history-dependent real randomized stopping and declarations. Observations: e_Q=Q(declare P), e_P=P(declare Q), T_Q=E_Q[tau], T_P=E_P[tau]. Define D=e_P+e_Q-1. The following theorem describes the entire projection (T_Q,T_P,D) of the real FULL_HIST four-observer image, preserving the distinction between projection and full four-coordinate image.

## Theorem — complete all-real three-coordinate polytope

A real triple (tq,tp,d) is FULL_HIST achievable if and only if it satisfies the eight timing rows a*tq+b*tp <= h:

| a | b | h |
|---:|---:|---:|
| -323 | 282 | -41 |
| -188 | 216 | 139 |
| -160 | 160 | 41 |
| -1 | 2 | 4 |
| 3 | -2 | 4 |
| 80 | -80 | 23 |
| 123 | -146 | -23 |
| 274 | -236 | 179 |

and the ten support rows a*tq+b*tp+c*abs(d) <= h:

| a | b | c | h |
|---:|---:|---:|---:|
| -444824 | 376149 | 184500 | -68675 |
| -27912 | 17792 | 136000 | 3887 |
| -12234 | 7979 | 29500 | -4255 |
| -2912 | -3128 | 53000 | -5455 |
| -360 | 0 | 40000 | 9843 |
| -26 | 1 | 200 | -25 |
| -13 | -112 | 1000 | -125 |
| 1063 | -2288 | 9000 | -1225 |
| 3984 | -8904 | 52000 | -2007 |
| 15671 | -21076 | 23000 | -5405 |

All 28 underlying linear halfspaces are genuine facets (each symmetric row means two sign choices). The 3D rational polytope has exactly 23 vertices; its timing projection is an eight-vertex octagon. For every timing pair (tq,tp) in this octagon, the *exact* residual interval is [-M,M] with

$$M(tq,tp)=\min_{\text{ten support rows }(a,b,c,h)}\frac{h-a\,tq-b\,tp}{c}.$$

The formula holds for all real randomized FULL_HIST strategies and all admissible timing pairs.

## Analytic proof and exact finite H/V certificate

The frozen time-3 conditional Q rows are q_0=(13/20,1/5,3/20), q_1=(1/40,9/20,21/40). Let 0<=g<=1 denote time-1 Q continuation; 0<=u_i<=g denote branchwise time-2 continuation parameters; and 0<=x_ij<=u_i*q_ij/2 denote time-3 history continuation Q mass. Define X_j=x_0j+x_1j and J=(47/180)x_01+(67/162)x_11. Exact expectation and total variation support formulas are

$$T_Q=1+g+(u_0+u_1)/2+X_0+X_1+X_2,$$
$$T_P=1+g+(3u_0+5u_1)/8+X_0/2+X_1+3X_2/2,$$
$$S=g/8+3u_0/80+u_1/160+9(X_0+X_2)/1000+9J/10.$$

For a given stopping policy, D=sum_h(1-r_h)Q(h)t_h where r_h=P(h)/Q(h), 0<=t_h<=1 and sum_h(1-r_h)Q(h)=0. Thus D ranges exactly over [-S,S]. The two endpoints use likelihood-ratio threshold declarations, and intermediate D values follow by random mixing.

Any randomized finite-tree stopping policy is a convex combination of deterministic local stop/continue policies: sample all local Bernoulli decisions before walking the tree, then take the resulting deterministic policy. Enumerating the 1+2+6 local binary decisions produces 512 deterministic encodings. Exact rational evaluation yields 82 different triples (T_Q,T_P,S), hence 163 different threshold triples (T_Q,T_P,+/-S). Therefore the entire FULL_HIST three-coordinate image equals their convex hull, even when arbitrary real probabilities are allowed.

VERIFY.py proves equality to the displayed H-polyhedron entirely in rational arithmetic: (i) every signed-threshold point satisfies all 28 halfspaces; (ii) every row has at least three affinely independent tight points, so each row defines a 2D facet; (iii) intersections of every three independent facet planes, with exact feasibility filtering, give 23 distinct vertices and each belongs to the original signed-threshold point set; (iv) the eight timing rows have eight exact pair-intersection vertices in the stopping-time image, and their normals positively span both directions of both timing axes. Consequently the timing polygon is bounded, and a symmetric pair of support halfspaces bounds d over it. A bounded polyhedron is the convex hull of its vertices. This gives both inclusions and establishes the theorem without floating-point geometry.

## Strict refinement at an interior time

At T_Q=T_P=5/2 the ten support rows give the exact sharp bound

$$|e_P+e_Q-1|\leq 1929/10600.$$

The active facet is -2912*T_Q-3128*T_P+53000*|D| <= -5455. Attainment: combine with weights 33/53 and 20/53 the two legal stopping policies (T_Q,T_P,S)=(2,2,1/8) and (133/40,133/40,69/250). The first has g=1,u_0=u_1=0 and all x_ij=0. The second has g=u_0=u_1=1, x_01=1/10,x_11=9/40 and the other x_ij=0. Threshold declarations attain D=S for both, yielding exactly the bound; complementary declarations attain the negative bound.

The predecessor's asymmetric gap bound at this same timing allowed |D|<=3/16, larger by 117/21200. Thus the four-observable rational candidate (e_P,e_Q,T_P,T_Q)=(19/32,19/32,5/2,5/2) obeys that earlier necessary bound and has a feasible time pair but violates the new exact facet. This is a FULL_HIST infeasibility certificate, not a FULL_HIST/LR separation example.

## Executed reproducibility and next question

The Python 3 standard-library Fraction script VERIFY.py was executed locally. EXACT_OUTPUT.txt records actual stdout. The script checks seven stopped likelihood-ratio masses, total Q mass, P moment, time/support formulas, all 28 facets, all 3276 hyperplane triples, all 28 time-line pairs, boundedness, sharpness and the witness mixture. Exact arithmetic establishes the finite part; the finite-tree mixing argument establishes the all-real statement.

For the R5 mother objective, use this exact three-coordinate projection as a fast necessary-and-sufficient filter for (T_Q,T_P,D). Choose an interior rational triple with unequal times, select a feasible split (e_P,e_Q), verify full four-coordinate FULL_HIST feasibility and test seedless LR by the complete semialgebraic feasible family K(W) and the exact residual F=(A+B)J-X1(alpha*A+beta*B). Either an all-real strict-sign certificate or a seedless LR constructive witness is a discriminating next result. Preserve the frozen pins; Source publication here is author-side portable evidence, pending live-owner verification, formal CLAIM and independent admission.
