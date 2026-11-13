# R5 — Full four-parameter Blackwell wedge in the complementary b≥a sector

Date: 2026-11-08, Asia/Shanghai. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific pins carried forward unchanged: Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Previous R5 author research: PR #1798 (all lawful b≤a), PR #1799 (a middle-ratio prism). The result below concerns precisely the frozen seven-node P/Q-BRC statistical observer, rather than native X6 dynamics.

## Model and theorem

Likelihood ratios: `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. For `f=(g,a,b,u,v,w,z)`, define Q-terminal masses

```
M0=509u/900+47z/180+67(v-z)/162+w/100
M1=13a/40+b/80-u
M2=(g-a)/2
M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
M4=(g-b)/2
M5=3a/40+21b/80-w
M6=u/100+47z/180+67(v-z)/162+509w/900
TP=1+g+3a/8+5b/8+u/2+v+3w/2
TQ=1+g+(a+b)/2+u+v+w
```

Lawful flows obey `0≤a,b≤g≤1`, `0≤u≤13a/40+b/80`, `0≤w≤3a/40+21b/80`, `0≤z≤a/10`, `0≤v-z≤9b/40`. Seedless criterion: `9bz=4a(v-z)`.

**Theorem (all-real complementary F-face wedge).** For all real

```
0≤s≤g≤1; 1/5≤xi≤1; 0≤theta,kappa,p,q,h≤1,
a=xi*s, b=s,
x=(g,a,b,(13a/40+b/80)*p,a*theta/10+9b*kappa/40,
   (3a/40+21b/80)*q,a*theta/10)
```

there exist a lawful seedless target flow `y` on the single affine face `F={z'=a'/10, v'-z'=9b'/40}` and nonnegative declaration-independent 7×7 matrix `Q` satisfying for every i,j:

```
Σ_j Q[i,j]=M_i(y); Σ_i Q[i,j]=M_j(x);
Σ_i r_i Q[i,j]=r_j M_j(x); TP(y)=TP(x); TQ(y)=TQ(x).
```

For `x_h=(1-h)x+h*y` put `Q_h=(1-h)Q+h diag(M(y))`. Every terminal declaration `d∈[0,1]^7` transfers to `d'_i=Σ_j Q_h[i,j]d_j/M_i(y)` when the row has positive mass, otherwise choose 0. Both errors and both stopping times match exactly. It includes irrational parameters, boundaries, and s=0.

**Region:** all lawful source flows with `b/5≤a≤b`, any physical u,w,z,v and any g≥b, hence includes both residual signs `R=9bz-4a(v-z)=(9ab/10)(theta-kappa)`. Together with PR #1798's author-side b≤a result, the current author-proved union covers `a≥b/5` for b>0, pending independent review.

## Proof by 32 exact rational certificates

`CERTIFICATES.json.zlib.b64` is a losslessly zlib-compressed, base64-encoded UTF-8 JSON archive: 32 records at normalized (g,b)=(1,1), `a∈{1/5,1}`, `(theta,kappa,p,q)∈{0,1}^4`. Each record contains all seven rational target coordinates and every positive entry `(target_i,source_j,Q_ij)`; omitted matrix entries are exactly 0. The standard-library `VERIFY.py` decodes and checks all rational mass, weighted-mass, legality, F-face and stopping-time equalities.

1. For each endpoint a∈{1/5,1}, the normalized source is multi-affine in theta,kappa,p,q. Mix its 16 calibrated triples with weights `Π_v (v if bit_v=1 else 1-v)`. Each target stays on F, because F is affine; Q calibration, legality, and stops are linear. This reconstructs the exact arbitrary real four-parameter source.
2. For `xi∈[1/5,1]`, combine endpoint triples with weights `1-λ,λ`, `λ=(xi-1/5)/(4/5)`. The new normalized source has a=xi,b=1, and its target is still F seedless.
3. Define E1=(1,0,0,0,0,0,0), E0=(0,0,0,0,0,0,0), each with diagonal identity Blackwell matrix. Mix the normalized triple, E1 and E0 with coefficients `s,g-s,1-g`. The resulting source is exactly displayed x. All coefficients are nonnegative, including boundary cases.
4. Finally mix (x,y,Q) with the diagonal identity triple at y using (1-h,h). The displayed Q_h is calibrated; row normalization is stochastic on positive rows and defines d'.

The nonnegative interpolation proves the all-real claim from the 32 exact finite rational witnesses; no conclusion is extrapolated from finite random tests. Locally executed `VERIFY.py` checked all 32 and 257 exact rational interpolation instances (256 seeded plus one full-interior test):

```
EXACT_32_F_FACE_CORNER_CERTIFICATES_PASS
EXACT_257_ALL_REAL_INTERPOLATION_REGRESSION_PASS
PASS_R5_COMPLEMENT_B_GT_A_FULL_F_FACE_PHYSICAL_WEDGE
```

Author-side certificate search used floating LP *only to propose support*, then exact rational linear reconstruction. The published checker uses standard-library Fraction and exact stored rational entries and is independent of the LP runtime. Full stored certificate recovery: `base64 -d CERTIFICATES.json.zlib.b64 | zlib-decompress` (portable Python command: `python -c "import base64,zlib,pathlib; p=pathlib.Path('CERTIFICATES.json.zlib.b64'); pathlib.Path('CERTIFICATES.json').write_bytes(zlib.decompress(base64.b64decode(p.read_text())))"`).

## Next question and authority

Investigate `0≤a<b/5` (b>5a), especially the corner (g,b)=(1,1), theta=kappa=p=0,q=1, where F-face candidates become constrained; a=0 itself is seedless, suggesting a new seedless-face switch. A face-specific obstruction is not a universal impossibility claim.

Current Site connection reports `research_authority_granted=false`; backend status read failed with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false`. GitHub identity `awdawmip` had repository `admin` permission. Native owner/CLAIM and independent mathematical admission remain unconfirmed. This branch is a portable author-side scientific handoff.
