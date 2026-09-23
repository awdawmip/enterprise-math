# D=-24 UR/JT0 independent prior-art closure audit

Status: `UNPUBLISHED_STAGED_EVIDENCE / NO_CLAIM / NO_OPEN / NO_RESULT / NO_REVIEW`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`
Publication: `TP2-C0E85430A37213F301EB`
Frozen task Source pin: `e7df16b829576fc939d2e3521c18209b5f7815d2`
Research logical conversation: `chatgpt-research-hourly-enterprise-math-20260923`
Researcher session created this run: `EM-DIRECT-A71FA7 / MCP-106daeb9d4df43f1bc477337723ce089`

## 1. Frozen inputs consumed, not reproved

The accepted predecessor Result `RR-82F6383FB6634F72B457` and Driver Review `DR-2EA60F5817976E662FA6` establish the D=-24 CM supersingular zero and its simplicity and reduce the first digit exactly to

`JT0 <=> UR`, where

`UR: G_p (-6 Q_m'(1/2)) = 1 (mod p)`

for every target prime `p = 13 or 19 (mod 24)`, `m=(p-1)/6`. The successor handoff requires an independent audit of the unreviewed Chisholm prior-art branch before any longer reproof. `LIFT/JT2` is explicitly deferred and is not touched here.

## 2. Weighted target

Define

`W_p = sum_{k=0}^{p-1} ((1/2)_k (1/3)_k (2/3)_k/(k!)^3) (6k+1) 2^{-k}`.

The frozen successor handoff records the exact project bridge

`W_p = p (mod p^2) <=> JT0 <=> UR`.

Therefore it suffices at this task scope to prove the weighted congruence uniformly for both target residue classes.

## 3. Exact primary-source normalization: d=3, lambda=1/2, a=6

Source A: Heng Huat Chan and Wen-Chin Liaw, *Cubic modular equations and new Ramanujan-type series for 1/pi*, Pacific Journal of Mathematics 192 (2000), 219-238, DOI 10.2140/pjm.2000.192.219.

Their Theorem 1.1 gives the signature-3 expansion

`1/pi = sum_{r>=0} (a_n+b_n r) ((1/2)_r(1/3)_r(2/3)_r/(r!)^3) H_n^r`.

Their Table 6 gives at `n=2` exactly

`a_2=1/(3 sqrt(3)),  b_2=2/sqrt(3),  H_2=1/2`.

Dividing by `a_2` yields the exact identity

`sum_{r>=0} (6r+1) ((1/2)_r(1/3)_r(2/3)_r/(r!)^3) 2^{-r} = 3 sqrt(3)/pi`.

Thus in the normalized Chisholm family the exact parameters are

`d=3, lambda_3=1/2, a=6`

(and the right-side constant is `delta=3 sqrt(3)`). This is an exact scholarly-source binding, not a finite numerical fit.

## 4. Chisholm theorem and exact curve binding

Source B: Sarah Chisholm, Alyson Deines, Ling Long, Gabriele Nebe, Holly Swisher, *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1 (2013), 9-30, DOI 10.3390/math1010009.

Their Theorem 1 treats `d in {2,3,4,6}` and gives the truncated weighted Ramanujan sum modulo `p^2` as

`sgn * ((1-lambda_d)/p) * p (mod p^2)`,

with `sgn=+1` exactly for ordinary reduction, under the stated CM, real/absolute-value, good-reduction, unramified, and p-adic-unit hypotheses.

For `d=3` their curve is

`E_3(t): y^2 + x y + (t/27)y = x^3`,

with `lambda=4t(1-t)` and `t=(1-sqrt(1-lambda))/2`. For `lambda=1/2`, choose `t=(1-1/sqrt(2))/2`; then `t(1-t)=1/8`. Direct Weierstrass calculation gives

`c4=(9-8t)/9`,
`Delta=t^3(1-t)/3^9`,
`j=27(9-8t)^3/[t^3(1-t)]`.

At the chosen `t`,

`j = 2417472 + 1707264 sqrt(2)`

(and the conjugate choice gives the minus sign), with minimal polynomial

`X^2 - 4834944 X + 14670139392`.

This is the Hilbert class polynomial for discriminant `-24`, hence the exact Chisholm specialization lies on the same D=-24 CM class as the accepted parent interface.

## 5. Every Chisholm arithmetic hypothesis on the target lane

For every target prime `p=13 or 19 (mod 24)`:

1. `p>3`; therefore `a=6` and `lambda=1/2` are p-adic units.
2. `lambda=1/2` is rational, totally real, and has absolute value `<1`.
3. `Q(sqrt(1-lambda))=Q(sqrt(2))` has discriminant 8, so every odd target prime is unramified there.
4. Since `t(1-t)=1/8` and `p>3`, both `t` and `1-t` are local units in the unramified quadratic extension and `Delta=t^3(1-t)/3^9` is a unit. Thus the exact specialized curve has good reduction.
5. The accepted parent D=-24 CM/Deuring interface proves the target reductions are supersingular; hence Chisholm's `sgn=-1`. This theorem-level predecessor fact is consumed rather than reproved.
6. The two target residue classes have `p mod 8` equal to `5` and `3`, respectively. Therefore `(2/p)=-1`, and

`((1-lambda)/p) = ((1/2)/p) = (2/p) = -1`.

The two signs cancel, so Chisholm Theorem 1 gives uniformly

`W_p = p (mod p^2)`

for every target prime `p=13 or 19 (mod 24)`.

## 6. Task conclusion and BRC boundary

Composing only with the frozen exact project bridge gives

`W_p = p (mod p^2) <=> JT0 <=> UR`.

Therefore the present audit supplies an all-target-prime mathematical closure candidate for `UR/JT0`. It does not claim canonical acceptance: this file is staged only because the current ordinary-control continuation path still rejects typed continuation preparation before CLAIM/OPEN.

BRC information is not collapsed beyond what the frozen factorization permits. The original weighted population remains labeled by `k`; hypergeometric/binomial provenance is retained; target residue classes remain separate until the final character evaluation; CM reduction type and local field are explicit observer data. Nothing here replaces signed cancellation by a positive mass summary.

No statement about the deferred second digit `LIFT/JT2` is made.

## 7. Deterministic regression, not proof

Use the exact identity

`((1/2)_k(1/3)_k(2/3)_k/(k!)^3) 2^{-k} = C(2k,k)^2 C(3k,k)/216^k`.

An independent exact modular checker evaluated all 166 target primes `p<5000` (83 in each residue class) and found zero failures of `W_p=p (mod p^2)`. The scan is falsification/regression only; the proof is the source-level normalization plus Chisholm theorem and exact hypothesis/sign binding above.

## 8. Control/recovery boundary

Current canonical continuation exposes `last_progress_ref=DR-2EA60F5817976E662FA6` but `progress_reference_readback=null`. The exact immutable review record has been fully hash-verified under this conversation, SHA-256 `5fad6c66720d15f1a3d87eae16fdc370ee3363b4c97de1fc4a72262fe00c613a`, yet typed `continuation_prepare` was rejected `CHAT_AUTHENTICATED_LAST_PROGRESS_ARTIFACT_REQUIRED`. Support issue Enterprise Math #1501 has been updated with this separate Research-lane reproduction.

No CLAIM, OPEN, Source checkpoint, Result, freeze, or review is asserted. After the reviewed/deployed stable-record-ID resolver changes canonical packet behavior, the next legal action is one fresh continuation -> one typed continuation_prepare -> explicit CLAIM -> explicit OPEN, then checkpoint/readback this audit and its checker, freeze a UR/JT0 Result candidate, and route an independent Driver.
