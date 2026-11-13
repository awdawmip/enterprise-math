# R5 — Sharp affine-face threshold and full lower-ratio Blackwell capacity rectangle

Date: 2026-11-08 Asia/Shanghai. Scope: author-side P/Q-BRC four-stage, seven-likelihood-node model; frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Status: author-proved with exact rational checks; native Owner/CLAIM and independent review unconfirmed.

## Exact model

Write `f=(g,a,b,u,v,w,z)`. Lawful flows satisfy `0<=a,b<=g<=1`, `0<=u<=13a/40+b/80`, `0<=w<=3a/40+21b/80`, `0<=z<=a/10`, `0<=v-z<=9b/40`. The seven likelihood nodes are `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Seven Q terminal masses:

```text
M0=509u/900+47z/180+67(v-z)/162+w/100
M1=13a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4=(g-b)/2
M5=3a/40+21b/80-w
M6=u/100+47z/180+67(v-z)/162+509w/900
```

`T_P=1+g+3a/8+5b/8+u/2+v+3w/2`; `T_Q=1+g+(a+b)/2+u+v+w`. Seedless relation: `R(f)=9bz-4a(v-z)=0`.

## New all-real theorem

For all real `0<=s<=g<=1`, `46/705<=eta<=1`, `0<=p,q,theta,h<=1`, define

```text
u=s*(13/40+eta/80)*p
w=s*(3/40+21eta/80)*q
z=s*theta/10
x=(g,s,eta*s,u,9eta*s/40+z,w,z).
```

There exists a lawful seedless LR flow `y`, independent of the terminal declaration vector, and a nonnegative calibrated 7x7 Q-mass transport matrix `Q` so that every real randomized declaration `d in [0,1]^7` on the FULL_HIST flow `x_h=(1-h)x+h*y` can be transferred to a seedless declaration with identical four observations `(e_P,e_Q,T_P,T_Q)`. Boundary and irrational parameters are included. `R(x)=9eta*s^2*(theta-1)/10`.

For `46/705<=eta<=1/2`, the proof and eight exact rational corner certificates are here. For `1/2<=eta<=1`, use the immutable predecessor full-capacity ratio bridge `RATIO_BRIDGE.md` and exact `BASE_CERTIFICATES.py` at `c5f0dd7d2c1bd170166d00fb54d53c9180a166b7`. The two theorems meet at `eta=1/2`.

## Eight rational corner certificates and continuous construction

`ETA_SHARP_CORNERS.json` records four exact sources, seedless targets and sparse Q matrices at `eta0=46/705` for `(p,q)=(0,0),(1,0),(0,1),(1,1)`. `ETA_HALF_CORNERS.json` preserves all four previously verified `eta=1/2` certificates copied from the pinned predecessor. New matrices contain respectively 12, 11, 9 and 9 nonzero entries. Each matrix has Q rows indexed by target node and columns indexed by FULL_HIST source node. For every corner:

```text
Q[i,j]>=0
sum_j Q[i,j] = M_i(y)
sum_i Q[i,j] = M_j(x)
sum_i r_i Q[i,j] = r_j M_j(x)
T_P(x)=T_P(y); T_Q(x)=T_Q(y); R(y)=0; x,y lawful.
```

Every target in both anchor sets satisfies a **single affine seedless face** `F={z=a/10, v-z=9b/40}`. Let `alpha=(eta-46/705)/(1/2-46/705)` and interpolate matching eta-endpoint transport triples by weights `1-alpha,alpha`. For real p,q combine the four p/q corners by bilinear weights `(1-p)(1-q),p(1-q),(1-p)q,pq`. These nonnegative weights preserve calibration, legality, and the face F. Physical capacities are affine in eta, so source is exactly `c=(1,1,eta,(13/40+eta/80)p,9eta/40,(3/40+21eta/80)q,0)`.

Let `c+` be c with v,z both increased by `1/10`; it is in F. Let `E0=(0,0,0,0,0,0,0)` and `E1=(1,0,0,0,0,0,0)`, also in F. With weights `(1-g),(g-s),s(1-theta),s theta` combine the sources `E0,E1,c,c+`, choosing the previously constructed seedless target for c and diagonal identity transports for the other three. This yields the stated x and its seedless y. Finally form `x_h=(1-h)x+h*y` and `Q_h=(1-h)Q+h diag(M(y))`. All 7 row, 7 Q-column, 7 likelihood-weighted P-column and both stopping-time identities are affine and survive.

For any declaration `d_j in [0,1]`, define `d'_i=(sum_j Q_h[i,j]d_j)/M_i(y)` when positive mass, 0 otherwise. Then `0<=d'_i<=1`, and Q and P expectation identities give exact equality of both error probabilities, simultaneously with stopping times. The argument is symbolic for all real parameters, not finite-grid extrapolation.

## Sharp F-specific threshold: exact dual obstruction

For the saturated-v off-diagonal source `x_eta=(1,1,eta,13/40+eta/80,9eta/40,0,0)` (`p=1,q=0`), define `L(f)=-(616/141)*(T_P(f)-1)+(524/141)*(T_Q(f)-1)`. On every **lawful F-target** y, direct substitution gives

```text
L(y)=-(92/141)*(g-a)-b-(400/141)*w
     -(72/47)*(13a/40+b/80-u) <= 0.
```

On the source `L(x_eta)=46/705-eta`. A stopping-time-preserving F-target therefore requires `eta>=46/705`. The 10-corner certificate at eta=46/705 attains equality with seedless target

`y=(686/705,686/705,0,4459/14100,343/3525,0,343/3525)`.

Thus the fixed face F has the **exact sharp** lower threshold `46/705` for this source corner (within eta∈[0,1/2]), while all four corners have feasible Blackwell matrices at the endpoint. This is a face-specific theorem; lower eta may admit other seedless targets or faces (eta=0 source is itself seedless). The prior floating infeasibility signal for eta=1/4 off-diagonal corners in F is corrected by the exact feasible certificates now recorded.

## Execution, provenance and next question

`VERIFY.py` executes exact Python `fractions.Fraction` validation of eight full 7x7 Q matrices, legality, both measures' normalization, 7+7+7 calibration relations per matrix, two times and seedlessness; 2187 rational combinations of `(g,s,eta,p,q,theta,h)` with three declarations each; and rational instances of the sharp dual identity. Actual output: `EXACT_OUTPUT.txt`. The all-real theorem follows from the displayed nonnegative interpolation and mass identities; the finite regression checks its implementation.

Predecessor: https://github.com/awdawmip/enterprise-math/blob/c5f0dd7d2c1bd170166d00fb54d53c9180a166b7/research_notes/brc_r5_saturated_v_six_parameter_20261108/LOW_RATIO_WEDGE.md. Scientific inputs remain pinned; this four-observer stochastic model does not replace P000/HeartBeat-World X6. The output concerns precisely four declared observations and randomized terminal decisions, with no claim about other future operations. Author-side evidence only: no native Researcher-ID/Owner/CLAIM or independent review established.
