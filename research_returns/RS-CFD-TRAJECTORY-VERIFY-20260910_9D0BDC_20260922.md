# RS-CFD-TRAJECTORY-VERIFY-20260910 — 9D0BDC continuation return

Researcher-ID: `EM-CFD-VFY-KWISE-9D0BDC`
Claim: `CLM-CFDVFY-9D0BDC-20260922-0613`
Predecessor durable frontier: `0baf64869d8f90b94878794a7d6dd440e3808842` (AA1231)
Status: `CONTINUATION_REQUIRED`

## Scope

Consume AA1231 without replay and quantify exactly how much finite-order cross-cycle dependence control would be sufficient for the frozen `n=23`, `r=16` cycle-count gate. The physical/correctness manifest is not changed. No native-host timing is executed here.

## 1. Sharp one-sided k-wise success-intersection envelope

Let `X_1,...,X_n in {0,1}`, `S=sum X_i`. Assume only that for every coordinate subset `A` with `1 <= |A| <= k`,

`P(X_i=1 for every i in A) <= 2^{-|A|}`.

This is deliberately weaker than full k-wise Bernoulli independence: it constrains only all-success intersections, not mixed success/failure patterns.

For every `j <= min(k,r)`, pointwise

`1{S>=r} <= C(S,j)/C(r,j)`.

Averaging and summing the order-j intersection bounds gives

`E C(S,j) <= C(n,j)/2^j`,

so

`P(S>=r) <= C(n,j)/(2^j C(r,j))`.

Taking the best order gives

`B_k(n,r) = min(1, min_{1<=j<=min(k,r)} C(n,j)/(2^j C(r,j)))`.

The bound is sharp. Put probability `p=B_k(n,r)` on a uniformly random success set of exactly size `r`, and probability `1-p` on the empty success set. For every fixed `j`-subset `A`,

`P(A is all-success) = p C(r,j)/C(n,j) <= 2^{-j}`,

while `P(S>=r)=p`. Thus the upper certificate and primal witness coincide exactly.

For the frozen `n=23,r=16` gate the sequence decreases through orders 1–9 and then stops improving. The sharp values are:

`k=1: 23/32`, `2: 253/480`, `3: 253/640`, `4: 253/832`, `5: 4807/19968`, `6: 1311/6656`, `7: 22287/133120`, `8: 7429/49920`, and for every `k>=9`, `7429/53248 ≈ 0.1395169772`.

The order-9 and order-10 ratios are equal; higher orders are weaker. Therefore **even imposing the one-sided success-intersection bound at every order through all 23 cycles cannot certify size 0.05** for the frozen `16/23` gate. The exact best all-order envelope is `7429/53248 > 1/20`.

This sharpens AA1231: replacing arbitrary dependence merely by finite-order (or even all-order) one-sided positive-intersection controls is still insufficient.

## 2. Stronger contrast: exact full k-wise independence

A natural question is whether ordinary exact k-wise Bernoulli(1/2) independence is enough. Here there is an exact near-complete counterexample.

Under exchangeability, let the count law be

`P(S=s)=C(23,s)/2^23 * (1+(-1)^s)`.

Equivalently, keep only the even-parity part of the `Binomial(23,1/2)` law and double it; conditional on `S=s`, choose the success set uniformly. The signed difference from the binomial law is proportional to `(-1)^s C(23,s)`. Its factorial moments through degree 22 vanish by the 23rd finite-difference identity. Consequently, for every `j<=22`,

`E C(S,j)=C(23,j)/2^j`.

By inclusion-exclusion, every 0/1 pattern on every set of at most 22 coordinates has probability exactly `2^{-m}`. Hence this is a genuine **22-wise independent** Bernoulli(1/2) family.

Yet its frozen-gate tail is

`P(S>=16)=35075/524288 ≈ 0.06690025330 > 0.05`.

The ordinary fully independent 23-cycle tail is

`P(Binomial(23,1/2)>=16)=763/16384 ≈ 0.04656982422 < 0.05`.

For 22-wise constraints the symmetrized moment problem has one free direction: any count law matching binomial factorial moments through order 22 is `binomial + t (-1)^s C(23,s)`, and nonnegativity gives `|t|<=2^{-23}`. The frozen-tail alternating sum is `170544`, so the exact maximum is the endpoint value above. Since this 22-wise witness is also k-wise for every `k<=22`, **no exact full k-wise independence assumption with k<=22 is sufficient to guarantee alpha<=0.05; exact 23-wise independence is the first k-wise level that does so for this threshold.**

This does not say literal statistical independence is the only possible confirmatory calibration. A separately predeclared joint-law condition may be weaker than full independence if it directly proves the relevant null tail <=0.05. It does show that generic partial-independence language, even '22-wise independent', is not enough for this exact `16/23` gate.

## 3. Machine verification

`research_checks/RS_CFD_TRAJECTORY_VERIFY_9D0BDC.py` uses only standard-library exact `Fraction` arithmetic. It checks, for `k=1..23`, every primal subset constraint and the dual pointwise majorant over all `S=0..23`; it verifies the exact plateau `7429/53248`; it checks all factorial moments of the parity witness through order 22; it explicitly verifies all inclusion-exclusion pattern probabilities for subset sizes through 22; and it checks the exact alpha comparisons. Local `py_compile` and execution both pass. Checker SHA-256: `468ce8378008337643f9ca6b296b09dc42ad519bbbc8452801c90f1da0cdcaf4`.

Machine certificate: `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_9D0BDC/kwise_tail_certificate.json`.

## 4. Decision boundary and next action

The frozen 23-cycle physical/correctness manifest remains unchanged. For confirmatory use of its `16/23` count gate, do not treat marginal validity, one-sided k-wise success-intersection controls, or even exact 22-wise Bernoulli independence as enough to justify alpha 0.05. A native run can still be executed exactly as frozen, but confirmatory interpretation must additionally bind either full cycle independence or another predeclared joint dependence model/certificate that directly yields a <=0.05 null tail at the gate. Otherwise the cycle-count evidence remains descriptive/fail-closed.

No spectralDNS/shenfun/MPI/FFTW execution, speedup/slowdown conclusion, generic CFD acceleration claim, continuous-PDE theorem, Working Truth/Foundation promotion, or final acceptance is made in this return.
