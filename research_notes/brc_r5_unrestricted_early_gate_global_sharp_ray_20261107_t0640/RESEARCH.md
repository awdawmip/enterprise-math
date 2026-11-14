# R5 — Unrestricted seedless-LR critical ray: exact global optimum and rigidity

Date: 2026-11-07 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen science: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Current governing source main was separately consulted (Global `eff87ce124122b5ad7e3c58d8f6ffa9999a5d72c`, EM `d7cc063fea267dc5d21df06a1ad371b1d0652024`). P000 / ACTIVE Heartbeat worldview retained. Predecessor: `f847d8b76069999da5e8eb3c0f6124fe05890941`, same sharp bound previously proved only when g=u0=u1.

## Theorem: the unrestricted ray is now solved

In the frozen strictly positive four-stage P/Q likelihood-ratio tree at delta=1/4, consider **all** seedless likelihood-ratio strategies: arbitrary real early continuation 0 <= u0,u1 <= g <= 1, arbitrary stage-3 continuation by the current pooled LR key, and arbitrary randomized declarations at all stopped LR/time keys. The four fixed observers are
W=(eP,eQ,TP,TQ), eP=P(declare Q), eQ=Q(declare P), T=expected stopping time.
Set W*=(161801/180000,6499/18000,267/80,137/40) and W(h)=W*+h(1,1,1,-1).

**Exact unrestricted theorem:** for every real h>=0,
`W(h) is seedless-LR achievable  <=>  0 <= h <= H := 16917/4642820.`
This holds for all real policies, including irrational probabilities and the boundary. Moreover at h=H every realizing policy has g=u0=u1=31911/33163, x1=(13/40)g, E_{1/10}=M_{1/10}, E_{1/2}=M_{1/2}, and zero declarations in every other LR bin. The remaining flows x0,x2 equal the rational endpoint below (up to arbitrary actions at zero-mass keys).

**Scientific change:** the earlier equal-gate optimum is proved sharp for the entire unrestricted early-gate family, despite its nonlinear central history mixture. The original R5 FULL_HIST-versus-seedless-LR *four-dimensional image equality* remains the mother question; this theorem solves its selected one-dimensional LR ray optimization.

## Exact BRC carrier and complete policy parametrization

The time-2 Q masses are 1/2 each at LR 3/4 and 5/4. Time-3 Q conditional rows at LR (1/2,1,3/2) are respectively (13/20,1/5,3/20) and (1/40,9/20,21/40). The time-4 LR support is (1/10,1,19/10); the rows at time-3 LR=1/2, 3/2 are (509,382,9)/900 and (9,382,509)/900, while the two *history-distinct* central LR=1 rows are (47/180,43/90,47/180) and (67/162,14/81,67/162). All are positive martingale kernels.

Write a=u0, b=u1, 0<=a,b<=g<=1. The pooled time-3 Q capacities are
V0=13a/40+b/80, V1=a/10+9b/40=(4a+9b)/40, V2=3a/40+21b/80.
Choose continuing Q masses X=(x0,x1,x2), 0<=xj<=Vj, using common continuation at each stage-3 LR key. For a+b>0 the *retained* central history mixture gives the symmetric time-4 side probability

`s(a,b)=(94a+335b)/(90(4a+9b))`, central probability `1-2s`.
For a=b=0, x1=0 and s is immaterial.

The stopped Q histogram M over r=(1/10,1/2,3/4,1,5/4,3/2,19/10) is exactly
```text
M0 = 509*x0/900 + s*x1 + x2/100
M1 = V0-x0
M2 = (g-a)/2
M3 = 1-g + V1-x1 + 191*(x0+x2)/450 + (1-2*s)*x1
M4 = (g-b)/2
M5 = V2-x2
M6 = x0/100 + s*x1 + 509*x2/900 .
```
These satisfy sum M=1 and sum r*M=1 for every legal flow. Declare P from Q-mass Ej at each stopped bin, 0<=Ej<=Mj. A common declaration fraction Ej/Mj at every occurrence of the same LR (0 if Mj=0) realizes every such aggregate E, so the parametrization is exact for all four observers:
```text
eQ=sum Ej;  eP=1-sum rj*Ej;
TQ=1+g+(a+b)/2 + x0+x1+x2;
TP=1+g+(3a+5b)/8 + x0/2+x1+3x2/2 .
```
The seven-bin histogram retains time-2 stop mass and the central history mixture until the observer map. The fiber theorem uses only these observers; future operations that need individual history are outside the declared quotient.

## Exact global dual identity

For the ray W(h) define four equality left sides (their fixed values shown after '='):
```text
A1 = g+(a+b)/2+x0+x1+x2 + h                       = 97/40
A2 = g+(3a+5b)/8+x0/2+x1+3x2/2 - h                 = 187/80
A3 = sum Ej - h                                     = 6499/18000
A4 = sum rj*Ej + h                                  = 18199/180000 .
```
Define six nonpositive legality slacks
```text
C1=x1-V1; C2=E0-M0; C3=E1-M1;
C4=-E3; C5=-E5; C6=-E6.
```
All six multipliers `mu=(18878,72000,26396,30609,87614,133218)` are positive. The equality multipliers are `lambda=(21126,-13604,-83401,114010)`.

**Identity valid for arbitrary reals g,a,b,X,E,h with a+b>0** (even if they are not feasible):
```text
S := 21126*A1 -13604*A2 -83401*A3 +114010*A4
   +18878*C1 +72000*C2 +26396*C3
   +30609*C4 +87614*C5 +133218*C6

S = 232141*h + R
R = 5005*(g-a)+2517*(g-b) - 30400*(b-a)*x1/(4a+9b)
    +(4213/2)*E2+(118223/2)*E4 .
```
At a=b=0, x1=0 and the quotient term is defined as zero. The exact identity then follows directly by substitution. It is checked independently by the adjacent `VERIFY.py` using a finite polynomial-identity certificate: after clearing `4a+9b`, the discrepancy is affine in the other twelve independent coordinates, with degree <=2 in each of a,b. Its values at 3x3 distinct pairs and the 13-point affine basis vanish exactly, which proves the identity as a polynomial, not by an empirical sample.

To show R>=0 on **every** legal real policy, first suppose b<=a. Every displayed summand of R is nonnegative. For b>a, capacity x1 <= (4a+9b)/40 implies
```text
-30400*(b-a)*x1/(4a+9b) >= -760*(b-a).
```
Also g-a >= b-a. Therefore
```text
R >= 4245*(b-a)+2517*(g-b)+(4213/2)*E2+(118223/2)*E4 >=0.
```
For a=b=0 the same assertion is immediate. On the ray, each Ai is its displayed fixed constant and Ci<=0. Therefore
```text
232141*h <= S <=
21126*(97/40)-13604*(187/80)-83401*(6499/18000)
+114010*(18199/180000) = 16917/20 .
```
Thus `h <= 16917/4642820` for **all** unrestricted seedless-LR strategies. This covers arbitrary early gates and nonlinear central pooling exactly.

## Attainment, all-real interval, and endpoint rigidity

At h=H an exact legal witness is
```text
g=a=b=t=31911/33163
X=(3199433/18571280, 31911/102040, 220131/18571280)
E=(886766809/4178538000,1415873/9285640,0,0,0,0,0).
```
The corresponding M in the seven-bin order is
```text
(886766809/4178538000,1415873/9285640,0,
 416394241/2089269000,0,726381/2321410,
 57150451/464282000).
```
Every 0<=Ej<=Mj and 0<=xj<=Vj holds. Both BRC mass moments equal one, the observers equal W(H), all six Ci vanish, and R=0.

At h=0 use
```text
g=a=b=77/80;
X=(3/16,3/10,1/80);
E=(1297/6000,879/6400,0,563/144000,0,0,349/96000).
```
For any real z in [0,1], interpolate the two displayed (g=a=b,X,E) flow vectors. Along this equal-gate face, s=11/30 is constant, M is affine, all probability/capacity inequalities are preserved, and W becomes W(zH). This establishes attainment for every real h in [0,H].

For rigidity at H, both inequalities in the sharp upper proof must be equalities. R=0 forces g=a=b and E2=E4=0 (the b>a or b<a cases give a strictly positive R). Positivity of every mu forces Ci=0. Substituting these saturation conditions into the four observer equations gives uniquely
```text
t=31911/33163, x0=3199433/18571280,
x1=31911/102040, x2=220131/18571280 .
```
The declarations in occupied bins follow from E0=M0, E1=M1 and E3=E5=E6=0. This supplies a rigidity statement in addition to the sharp bound.

## Exact execution, status, continuation

Actually executed a stdlib `fractions.Fraction` checker, saved as `VERIFY.py` with stdout in `EXACT_OUTPUT.txt`. It checks the 117-basis coefficient identity (validity by degree argument above), both exact primal policies, seven-bin probability/martingale checks, the endpoint complementary slacks, selected convex interpolants, and asymmetric-gate examples. Universal real conclusions follow from the displayed sign split and convexity, not an approximate optimizer.

Next scientific unit: with the LR ray solved, prioritize the original R5 four-dimensional mother problem. Pick a rational interior FULL_HIST four-observer point outside the currently certified LR cube, compute the full seven-variable K(W) and decide real feasibility of the pooling residual F=(A+B)J-X1(alpha*A+beta*B), searching for a strict separating certificate or a new constructive image-equivalence lemma. A second route determines the attainable *four-dimensional* LR region and compares its boundary with FULL_HIST; the ray certificate is a potential exposed supporting witness.

Research provenance: GitHub authenticated actor `awdawmip` has source push permission. Native Enterprise Math gateway `em_status` and `em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `operation_sent=false` this turn. Active R5 Owner and formal CLAIM are unconfirmed, no native Result/Review/admission is asserted. This is independent author-side mathematical evidence, pending review.
