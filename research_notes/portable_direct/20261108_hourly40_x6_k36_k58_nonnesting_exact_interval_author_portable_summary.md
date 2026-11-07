# X6 k36–k58: 3220 exact rational-interval cost-jump signs; negative-offset nesting counterexample
Date: 2026-11-08 Asia/Hong_Kong. Research role: TASK_RESEARCH **author-side portable**, `UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINTED / REGISTER_PENDING / SYNC_DEBT`. This note is **not** a canonical Source Task CLAIM, predecessor progress, Result, review, native experiment, or registration.

## Scientific pin, typed observer and result
Reuse the original frozen `X6_ALL_289_CONDITIONAL_SHELL_CERTIFICATE_20261107.json`, SHA-256 `47a1446a8d80d1e29302cef58767230362d74726a17ddea2ea44667557a18525`, model SHA-256 `c523b6e8aecee971da44722bd0ff2cc2cbd1308a2c578f7cab7592c7b8562b53`. The source retains 288 native identities and 83 X6 joint observational classes. The declared mathematical observer is the exact iid positive-gain law on `R∈{0,140,147,157}` bit with positive integer weights `Z,D,B,A`, total `M=Z+D+B+A`. The aggregation concerns this specific additive-cost observer only, with source identities/provenance retained separately. `Q_N=Pr(sum_{i=1}^N R_i>140+N/100)`. Define `O_k={N−14000(k−1): 14000(k−1)≤N<14000k and Q_N<Q_(N−1)}`.

**Exact finite theorem:** For all integer N from **490000 to 811999** (k=36 through 58), all **3220** hundred-boundary jumps have rigorous, strict exact-rational-interval signs (40 and 55 decimal integer scales agree): **882 decreasing, 2338 increasing, zero undetermined/zero**. All other **318780** integer steps are nondecreasing by nonnegative gains and unchanged integer cost threshold. This covers **322000** N values. K35's previous 140 huge-integer signs were independently reproduced by the new integer-interval evaluator before the extension; original k35 exact certificate SHA-256 `97c8911d358c54428ae11daf09824fb680dfa49d1b91dad791e733fedcd8e24d`.

The number of negative offsets for k=36,…,58 is
`30,30,31,31,32,34,34,35,36,36,38,38,39,39,42,43,43,43,44,45,46,47,46`.

**Counterexample to indefinite nesting:** `O_57⊄O_58`: exactly offset **6500** disappears in k58, `O_58=O_57 \ {6500}`. At `N=790500` (k57), cost 8045 bit, `Q_790500−Q_790499<0`; at `N=804500` (k58), cost 8185 bit, `Q_804500−Q_804499>0`. The offset first appeared in k50; there are no removals from k35 to k57. Thus this is the **first removal in the verified k35→58 sequence**, not a claim about every k<35. Supplementary high-precision magnitude readouts (percentage points): approximately `−1.04078748531345236×10^−13` at 790500 and `+1.72488465965869861×10^−14` at 804500; the sign proof is purely exact integer arithmetic.

## Exact bound theorem
Write `p0=Z/M, pD=D/M, pB=B/M, pA=A/M`, `W_t(s)=[x^s](pA*x^157+pB*x^147+pD*x^140)^t`, and `G_t(h)=sum_{s<h}W_t(s)*sum_{g in {140,147,157},s+g>h}p_g`. At `N=100m` set `h=140+m`, `k=floor(h/140)`. The **nonnegative-coefficient homogeneous** degree-(k+1) polynomials are
`GAIN=sum_{t=floor(h/157)}^{floor((h-1)/140)} binom(N-1,t)*p0^(k-t)*G_t(h)`,
`LOSS=sum_{t=ceil(h/157)}^{floor(h/140)} binom(N-1,t)*p0^(k+1-t)*W_t(h)`.
The exact event decomposition (threshold crossing, versus equality excluded when final gain=0) yields
`Q_N−Q_(N−1)=p0^(N-1-k)*(GAIN−LOSS)`.
For each p_i, scale b=10^d and take integer `l_i=floor(b*p_i)`, `u_i=ceil(b*p_i)`, with endpoints verified by exact cross-multiplication. Positivity of every gain/loss polynomial term gives the exact **integer** inequality
`GAIN(l)−LOSS(u) ≤ b^(k+1)*(GAIN(p)−LOSS(p)) ≤ GAIN(u)−LOSS(l)`.
All 3220 pairs of integer bounds have matching strict signs at d=40 and d=55; no float or approximate-tail sign comparisons are used in the proof. At non-hundred steps the integer profitability threshold is unchanged and `S_N≥S_(N−1)` pathwise.

An independent verifier directly enumerates labelled multinomial triples without polynomial-convolution or sorted-prefix routines at the two critical boundaries: k57 uses **1620 gain tuples and 10 equality-loss tuples**; k58 uses **1675 and 11**. It reproduces the exact lower and upper integer bound SHA-256 values of the convolution algorithm at both d=40 and d=55. The complete portable package was cold-reexecuted in an independent extraction directory with **all three JSON certificates byte-identical**.

## Complete artifact manifest (local author-side; hashes)
- `X6_K36_K58_COMPLETE_INTERVAL_SIGN_CERT_20261108.json`, SHA256 `8b3caee6cea842baf6efcd6b64de14baafab30eda81b238c256b0d7a7ae2e425` (3220 signed-boundary records and per-bound hashes).
- `X6_K36_RATIONAL_INTERVAL_EXACT_SIGN_CERT_20261108.json`, SHA256 `95a5d7931bde0b90a9961e46ccae6b915d99ad9fb0256d33a110f050d81af049` (k36).
- `X6_K57_K58_OFFSET6500_DIRECT_MULTINOMIAL_CHECK_20261108.json`, SHA256 `717f41bd65c480bd2e1dc305a2eae84f4880936c730f53b4bff2fb51d53f196b`.
- Scripts: `x6_gain_cliff_interval_k36.py`, `x6_k36_k58_interval_batch_certificate.py`, `x6_k57_k58_direct_multinomial_interval_check.py` (all packaged with frozen JSON source and k35 parent).
- Full author ZIP `X6_K36_K58_NONNESTING_INTERVAL_PORTABLE_20261108.zip`, **737442 bytes**, SHA256 `fb497a45155cef1dad6bacbb7bba804a6f1f7fd9cac47f3dffed55328a8f2e11`. It is attached to the current conversation, **not claimed uploaded to the canonical Source or GitHub**.
- Full proof/handoff text `X6_K36_K58_NONNESTING_EXACT_INTERVAL_THEOREM_AND_HANDOFF_20261108.md`, SHA256 `088398557b32f36b8c3b5d9db318d016c296023b6ae38a931ec3191b22c14feb`.

## Source authority, UR original and next recovery action
As of 2026-11-08, native `em_status` and `em_checkpoint_list` failed with `BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; Site diagnostic `CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false, backend_connected=false`. The relay's `write_relay_enabled=true` is not authority. Exact current native subject/session/CLAIM/run/continuation_seed are **unknown**. No native mutation, claim, Source result or HANDOFF was attempted; author mathematical work does **not** go into predecessor `completed_units`.

Historical **UR V2** proof is already complete; recovery remains exact original 4-file bundle of **94687 bytes** SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. This turn's 58-local-file/90-ZIP-member search found no same-size object; GitHub exact-hash code search and Library scoped retrieval found citations, not the original bytes. Do not re-prove UR maths or present rebuilt files as the historical original. Upon real authorized Source backend restoration: read actual subject's recovery_status and existing original request receipts/reconcile; verify exact continuation and winning own claim; if seed state is `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, read every seed input and use `frontier_notes.completed_units=[]`; only then use lawful typed continuation, open, writer/provenance/checkpoint readback. Control maintenance's concrete acceptance is native status/recovery/claim/open/checkpoint success, not documentation or relay configuration. No accepted support owner was identified.

Next mathematical discriminant: characterize the weight inequality causing offset 6500 to re-enter/leave negativity and test whether an exact analytic sufficient condition can replace interval enumeration for that class; further k values are open. This author evidence is distinct from Research1 J1/J2 drafts and from native predecessor research.
