# EC49FUV — Complete n=30 binary minimax phase atlas: all sixteen mixing windows and all gaps

**Research date:** 2026-11-20 (Asia/Shanghai). **Status:** AUTHOR_PROVED / EXACT_FRACTION_AND_BERNSTEIN_CERTIFIED / PARENT_DEPENDENT / NOT_REVIEWED.

## Frozen science and boundary

Scientific source remains **BRC16943@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**. This note continues the immutable author-proved EC49FUU@ec1aaa789666eda27b15d2540472dafef0187da2 and combines independent author proofs EC49FUO@8df5788adcd977cc809a0e27da180833317e3dfa (uniform count-threshold class), EC49FUQ@96ad7a2c22c274446e74906c48bc6e3234a39436 (endpoint reduction), EC49FUR@0ac1ef58d84517835260e4aefbe6d2c2b3a293c9 (TV dual), EC49FUS@48b9c12889797201e104621dc27a653bc91dc5ef (j=9,10 windows), EC49FUT@328f9f87f928a3080c8df645693bacef2217cae3 (j=11,...,16 windows), and EC49FUU (x>=b16 upper tail). These parents are not independently reviewed.

The scientific object is a **lossy binary clipped-price observer**, not a lossless representation of native X6/Heartbeat World paths, branching, port labels, joint state, signed BRC amplitudes, or native three-dimensional slice. P000, native X6, current ACTIVE worldview and the original frozen source firewall are preserved. The `theta=0` endpoint is a compactification limit of the original nuisance parameter.

## Model and exact notation

Fix n=30, theta in [0,E], width x in [0,1], and

- E = 31597745/1653649, beta = 3/637;
- u(theta) = 21829245984 / (45529434409 - 456083905 theta);
- T(theta,x) = (1-x)(1-beta x+beta x theta);
- p(theta,x) = 1-T(theta,x), q(theta,x) = 1-u(theta)T(theta,x).

Under equal-prior hypotheses K|P is Bin(30,p) and K|Q is Bin(30,q), with common nuisance theta. Define for k=0,...,30

```text
Delta_t(k;x) = C(30,k)[q_t^k(1-q_t)^(30-k) - p_t^k(1-p_t)^(30-k)]
D_t^{>=j}(x) = sum_{k=j}^{30} Delta_t(k;x)
G_j(x) = D_E^{>=j}(x) - D_0^{>=j}(x)
H_j(x) = G_{j+1}(x)
d_j(x) = Delta_E(j;x) - Delta_0(j;x).
```

By the cited FUO/FUQ/FUR parent reductions, the full-bit composite minimax advantage is the finite two-endpoint dual:

```text
A_30(x) = 1 - 2 V_30(x)
        = min_{0<=lambda<=1} sum_{k=0}^{30}
          max(0, (1-lambda)Delta_0(k;x) + lambda Delta_E(k;x)).
```

## Main theorem: global n=30 classification

For each j=1,...,16 there are strictly ordered **unique algebraic transition widths** a_j and b_j in (0,1), defined by G_j(a_j)=0 and Delta_E(j;b_j)=0, and

```text
0 < a1 < b1 < a2 < b2 < ... < a16 < b16 < 1.
```

**All sixteen intervals (a_j,b_j) are compulsory two-endpoint mixing phases.** There is no additional compulsory mixing phase elsewhere on the entire domain x in [0,1].

On each j-window let

```text
lambda_j(x) = -Delta_0(j;x)/d_j(x);
gamma_j(x)  = -G_{j+1}(x)/d_j(x).
```

For x in (a_j,b_j), 1/3 < lambda_j(x) < 1 and 0 < gamma_j(x) < 1, and the endpoint prior weight lambda_j is **uniquely** minimax. The minimax decision is left at K<j, right at K>j and randomized right with probability gamma_j at K=j. Its advantage is

```text
A_30(x) = (1-lambda_j)D_0^{>=j+1}(x)
        + lambda_j D_E^{>=j+1}(x).
```

Outside those mixing windows and for every x<1, the unique minimax endpoint-prior weight is lambda_E=1. The E-Bayes optimal threshold is K>=1 on [0,a1); K>=j+1 on each pure bridge (b_j,a_{j+1}); and above b16 is the deterministic E-Bayes threshold established in EC49FUU, switching as count roots c17,...,c29 are crossed.

At x=a_j, all least-favorable endpoint prior weights are [lambda_j(a_j),1]; the deterministic K>=j rule is minimax. At x=b_j, the least-favorable prior is uniquely pure E, with a minimax decision allowing right probability gamma in [0,gamma_j(b_j)] at K=j and right at all K>j. The boundaries between parent j=9,...,16 and the new j=1,...,8 share these same exact formulas. E-Bayes threshold changes at c17,...,c29 admit arbitrary boundary-count randomization with pure-E least-favorable prior as in EC49FUU.

At x=0: V_30(0)=u_E^30/2. At x=1 the two Bernoulli laws coincide, V_30(1)=1/2 and the least-favorable prior is not unique.

## New eight windows (j=1,...,8): strictly isolated rational roots

For each row a_j and b_j lie **strictly** between the displayed integers divided by 10^12. Each such bracket is checked by exact substitution and signs (no floating root oracle).

| j | certified interval I_j | entry a_j lower | entry a_j upper | exit b_j lower | exit b_j upper |
|---:|---|---:|---:|---:|---:|
| 1 | [0.00000005, 0.0000002] | 57344 | 57345 | 116382 | 116383 |
| 2 | [0.00020, 0.00031] | 210890907 | 210890908 | 295647554 | 295647555 |
| 3 | [0.0032, 0.0042] | 3272963990 | 3272963991 | 4052279778 | 4052279779 |
| 4 | [0.0129, 0.0153] | 13040063802 | 13040063803 | 15172923983 | 15172923984 |
| 5 | [0.0302, 0.0342] | 30318029224 | 30318029225 | 33991824019 | 33991824020 |
| 6 | [0.0538, 0.0593] | 53973751741 | 53973751742 | 59034877419 | 59034877420 |
| 7 | [0.0824, 0.0890] | 82545953450 | 82545953451 | 88690324086 | 88690324087 |
| 8 | [0.1146, 0.1219] | 114799449865 | 114799449866 | 121675180194 | 121675180195 |

Entries and exits for j=9,...,16 are *unchanged* from the pinned EC49FUS/FUT notes (and their independently executed exact certificates); b16=c16 from EC49FUU.

## Proof of the eight new windows

The companion standalone Python verifier uses **512 rational closed slabs** for each j=1,...,8. On each complete I_j the following eight strict inequalities are certified by outward exact Fraction interval evaluation:

```text
Delta_E(j-1) < 0;  Delta_0(j-1) < 0;
Delta_0(j)   < 0;  Delta_E(j+1) > 0;
[2 Delta_0(j)+Delta_E(j)]/3 < 0;
[2 Delta_0(j+1)+Delta_E(j+1)]/3 > 0;
G'_j > 0;  G'_{j+1} > 0.
```

Exact evaluations at the rational endpoints further give G_j(I_j.left)<0<G_j(I_j.right), Delta_E(j;I_j.left)>0>Delta_E(j;I_j.right), and G_{j+1}(I_j.right)<0.

The last inequality and G'_{j+1}>0 imply H_j<0 throughout I_j. The strict G'_j>0 and opposite endpoint signs give a **unique** a_j. The sign of Delta_E(j) is the sign of

```text
u_E^((30-j)/j) (1-u_E T_E) - (1-T_E).
```

Since T_E decreases strictly in x, this expression crosses zero at most once; its certified opposite endpoint signs give a **unique** b_j. The exact isolating brackets show a_j<b_j.

Before b_j the count-j mass of E is positive and count-(j-1) negative, hence E's Bayes rule is K>=j; after b_j it is K>=j+1. For x<b_j, Delta_0(j)<0<Delta_E(j); the strict mixture-at-1/3 sign guarantees lambda_j>1/3. Count j+1 is positive at lambda_j because its mixture at lambda=1/3 is already strictly positive and Delta_E(j+1)>0; counts below j are negative at both endpoints. The previously proved uniform mixed-binomial likelihood-ratio ordering excludes other count sign crossings.

At the unique count-j kink in the convex TV dual, the left slope is H_j<0 and the right slope is G_j. G_j strictly crosses zero at a_j. Therefore the minimizer is pure E below a_j, [lambda_j,1] exactly at a_j, unique lambda_j in (a_j,b_j), and pure E at/above b_j. Equating the endpoint advantages of the randomized test yields gamma_j=-H_j/d_j with 0<gamma_j<1 in the mixed region. At entry gamma_j=1; at exit the stated interval of tied test probabilities follows from Delta_E(j)=0 and the strict endpoint advantage gap.

This proves each entire I_j including its real-valued interior, not just a sampled list of widths.

## Proof that *all* fifteen intermediate gaps are pure E

The previously published window neighborhoods are I_9=[0.1498,0.158], I_10=[0.186,0.196], I_11=[0.224,0.235], I_12=[0.264,0.273], I_13=[0.305,0.314], I_14=[0.346,0.354], I_15=[0.388,0.394], I_16=[0.431,0.435]. All adjacent neighborhoods I_j and I_{j+1} are separated by disjoint rational bridges.

On every bridge [I_j.right,I_{j+1}.left] for j=1,...,15 the code constructs the *exact degree-59 rational polynomial* G'_{j+1}(x). It converts the polynomial into Bernstein form on this entire bridge and checks **all 60 coefficients are strictly positive**. It also checks G_{j+1}(I_{j+1}.left)<0 and the E signed mass endpoint signs. Hence G_{j+1}(x)<0 throughout each bridge and pure E with threshold K>=j+1 is strictly minimax there. This includes the seven gaps left open between previously proven j=9,...,16 neighborhoods, and the new j=1,...,8 inter-neighborhood gaps.

On the initial interval [0,I_1.left], the same 60-coefficient Bernstein argument proves G'_1>0 and the right endpoint G_1<0. Thus K>=1 with pure E is optimal there, even though Delta_0(1) is positive at the exact zero-width endpoint. For x in [b16,1) invoke the already certified global pure-E upper tail EC49FUU. The union of the new eight window intervals, the eight pinned j=9,...,16 window intervals, all fifteen bridges, the initial interval, and the previously proven upper tail is [0,1]. This establishes the full atlas.

## Reproducibility, scope, and remaining science

Run **the accompanying standard-library checker**, without external packages:

```sh
python3 research_notes/portable_direct/EC49FUV_N30_FULL_ATLAS_VERIFY.py
```

The actual local Python run on 2026-11-20 returned:

```text
ALL PASS: 33728 exact rational interval/Bernstein sign inequalities, 16 root brackets, 8 new full windows, 15 pure-E bridges plus initial, 18 exact dual crosschecks.
```

The 33,728 tally comprises eight windows times eight inequalities times 512 slabs (32,768), plus sixteen intervals times 60 strictly positive degree-59 Bernstein coefficients (960). Additional exact root endpoint and E-Bayes sign checks, and eighteen rational-width direct TV dual candidate comparisons, were executed separately. Bernstein conversion uses the identity expressing t^k as a nonnegative combination of degree-d Bernstein basis functions; positive coefficients imply strict polynomial positivity on the complete interval.

This is a **full parameter-width classification for n=30 within the frozen lossy binary observer**. It inherits FUO/FUQ/FUR's general composite-game reductions and FUS/FUT/FUU's j>=9 windows/upper tail. Independent mathematical review of those parent reductions and this new certificate is **NOT_REVIEWED**; the finite exact verifier checks all newly claimed rational inequalities, not the analytic parent proofs.

A useful next research unit is to develop the **arbitrary-n mixing-window count and root-order law**, using this complete n=30 atlas alongside n=15. A separate BRC/X6 observer-fiber analysis should quantify when labeled price source, joint residual, path or port information distinguishes histories collapsed by the binary count.

Historical contribution provenance: EM-DIRECT-8454C6 / MCP-44cfc4e6f2094f96861854ebefc77e84 and Activity RA-ED136F89271FD89288F3E58D are prior source metadata, **not** authenticated current execution capabilities. This independent portable scientific publication asserts no formal CLAIM, RUN, Result, Review, or P000 update. New Activity association remains a separate current-identity/CAS operation.
