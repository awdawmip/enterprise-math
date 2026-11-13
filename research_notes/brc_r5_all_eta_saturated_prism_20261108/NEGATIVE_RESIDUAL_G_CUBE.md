# R5 follow-up: an unsaturated negative-residual four-real-parameter G-face prism

Date 2026-11-08. Author-side mathematical status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This complements `RESEARCH.md` on the same PR; frozen global scientific pin `a01383f825ef9d43b4b754254303298c64041568`, EM scientific pin `86149263e38c22292c9def1e0f69092efa1be77e` unchanged.

## Theorem (all real)

For all `0<=eta<=1/30`, `0<=kappa,p,q,h<=1` and `0<=s<=g<=1`, define

```
x=(g,s,s*eta,
   s*(13/40+eta/80)*p,
   s*(9*eta*kappa/40),
   s*(3/40+21*eta/80)*q,
   0).
```

Then there exists a lawful seedless LR flow `y` on the **single linear face `G={b'=0,v'=z'}`** and a calibrated nonnegative `7×7` Blackwell kernel `Q` such that, for **every** seven-node declaration vector `d∈[0,1]^7`, the target's row-conditional declaration preserves the four observables `(eP,eQ,TP,TQ)` exactly. The same result holds for the source-to-target interpolation `(1-h)x+h*y` with `Q_h=(1-h)Q+h*diag(M(y))`. `y,Q` may depend on the flow parameters but not on declaration `d`.

The normalized source (`g=a=1,s=1`) has history residual `R=9bz-4a(v-z)=-9*eta*kappa/10`. It is **strictly negative whenever eta>0 and kappa>0**. This is an unsaturated family `0<kappa<1` beyond the saturated-v theorem, not an instance of the prior universal nonnegative-residual theorem. The quantifier domain also includes zero and boundary values.

## Eight exact anchors and universal construction

The file `NEGATIVE_CUBE_CERTIFICATES_B64.txt` is losslessly base64(zlib(JSON)), with **eight exact rational G-face target flows and sparse calibrated Q matrices** at

```
eta=1/30, theta=z=0,
kappa∈{0,1}, p∈{0,1}, q∈{0,1}.
```

They satisfy exact lawfulness, face G, seven target row equations, seven source Q-mass columns, seven likelihood-weighted P-mass columns, P and Q normalizations and both stop-time equations, using likelihoods `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. All entries are nonnegative rational numbers.

At the other eta endpoint `eta=0`, each `x_0=(1,1,0,13p/40,0,3q/40,0)` is itself seedless **on G**, with the diagonal transport `diag(M(x_0))`. Fix arbitrary real `eta∈[0,1/30]`, `kappa,p,q∈[0,1]` and set `lambda=30 eta`. Form the 16-fold nonnegative multilinear mixture over `a,b,c,d∈{0,1}`, with weight

```
(lambda if a else 1-lambda)
 * (kappa if b else 1-kappa)
 * (p if c else 1-p)
 * (q if d else 1-q).
```

For `a=1`, select the corresponding exact G anchor at `eta=1/30,kappa=b,p=c,q=d`. For `a=0`, use the G identity at `eta=0,kappa=b,p=c,q=d`. The weights are nonnegative and sum to one. Source reconstruction holds because the normalized coordinates `u=(13/40+eta/80)p`, `w=(3/40+21eta/80)q`, `v=9eta*kappa/40` are **multi-affine** in independent `eta,kappa,p,q`. All target vertices lie in G, a linear seedless face. The labeled seven Q-masses, likelihood-weighted mass columns and both stopping times are affine in the flow, hence the mixed target remains lawful, seedless, and calibrated, and the mixed Q remains nonnegative.

For general `0<=s<=g<=1`, mix that normalized calibrated triple with the G identity triples at `E1=(1,0,0,0,0,0,0)` and `E0=(0,0,0,0,0,0,0)`, with respective weights `s,g-s,1-g`. The stipulated `h` interpolation is another same-face mixture with a target identity kernel. This establishes the stated all-real theorem, including irrational and boundary parameters. The declaration map is stochastic because each target row is a convex normalized combination of source declarations.

## Verification, provenance and remaining work

The eight corner matrices were found by numerical LP to choose support, then the exact rational linear equations were solved and every matrix identity checked. Independent local standard-library Fraction postvalidation checked all 8 corner transports, **500 exact four-parameter test points**, plus a nontrivial `s,g,h` interpolation case. Actual local output is in `NEGATIVE_CUBE_EXACT_OUTPUT.txt`. This finite sample tests the implementation, not the all-real proof (the proof is the above multi-affine identity). The compact certificate payload is readable using `json.loads(zlib.decompress(base64.b64decode(text)).decode())`; the `VERIFY_NEGATIVE.py` source on this branch reproduces all exact certificate checks and a parametric validation grid using only Python standard library.

The result is an exact theorem **of the frozen finite seven-likelihood P/Q-BRC observer model**; preserving its four listed observables for all seven terminal declarations does not assert additional physical-native X6 dynamics. Native task Owner/CLAIM remains unconfirmed due backend `STATUS_DATABASE_UNAVAILABLE`. The author-side proof is not independently reviewed/admitted.

The full v-unsaturated frontier now reduces to, inter alia, positive z and eta beyond 1/30 for negative history residual. With normalized `z=theta/10` and `v-z=9eta*kappa/40`, the exact residual is `R=(9eta/10)(theta-kappa)`. Previous universal nonnegative-residual result already handles `kappa<=theta`. Therefore **focus on `theta<kappa<1`**, particularly eta=1/20 and small positive theta, then seek exact G/F calibrated corners or a new seedless face. Do not redo the already solved nonnegative-residual part.
