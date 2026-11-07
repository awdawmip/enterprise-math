# BRC-X6 k34-k35 finite IID gain-cost cliff classification (portable author-side)

Date: 2026-11-08 Asia/Hong_Kong. Research role: TASK_RESEARCH (author-side; native registration pending). Status: **AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINTED**. Original author-side calculations, not native predecessor progress or a claimed Source task/result.

## Frozen model and finite exact result
Scientific input: `X6_ALL_289_CONDITIONAL_SHELL_CERTIFICATE_20261107.json`, SHA-256 `47a1446a8d80d1e29302cef58767230362d74726a17ddea2ea44667557a18525`. Frozen model SHA-256 `c523b6e8aecee971da44722bd0ff2cc2cbd1308a2c578f7cab7592c7b8562b53`. Same 288 native-source identities and 83 X6 joint observation classes, q=1/20, integer-weight four-gain IID model `R in {0,140,147,157}` bits. `Q_N=P(sum(R_i)>140+N/100)`, strict threshold.

For `D_k={N in [14000(k-1),14000k-1]:Q_N<Q_(N-1)}`, exact integer enumeration of **all 280 hundred-cost boundaries** proves:
- k34, N=462000..475999: **28 negative, 112 positive, 0 zero**; `D34=D33+14000`, no new or removed offset.
- k35, N=476000..489999: **29 negative, 111 positive, 0 zero**; `D35=(D34+14000) union {484300}`, no removed offset. New relative offset = 8300.
- At any other N in these intervals, Q is nondecreasing because gains are nonnegative and the effective integer threshold is unchanged. Thus all 28,000 integer points are covered.

At the new N=484300, cost h=4983 bits. Exactly four admissible gain-multiplicity tuples (t,a,b,d) solve `157a+147b+140d=4983`, `a+b+d=t<=35`: `(33,16,13,4)`, `(34,9,10,15)`, `(34,2,27,5)`, `(35,2,7,26)`. Equality support alone is not a negative sign proof: the exact complete gain-minus-loss integer J_N is strictly negative, with **47,244 decimal digits**, signed decimal SHA-256 `403fea89adf487f02a7f79dcc34ca4e5c75f1785b128eff867034536b7f8255e`. Independent 115-precision Decimal tails yield `Q_484300-Q_484299 ≈ -0.0000000048336740886983236639433408` **percentage points**.

## Exact integer proof interface and verification
Let `W_t(s)=[x^s](Ax^157+Bx^147+Dx^140)^t`, `G_t(h)=sum_{s<h} W_t(s)*(A*[s+157>h]+B*[s+147>h]+D*[s+140>h])`, `T=floor(h/140)`, `Z=M-A-B-D>0`. Then
`Q_N-Q_(N-1)=Z^(N-1-T)/M^N * J_N`, with
`J_N=sum_{t=floor(h/157)}^{floor((h-1)/140)} C(N-1,t)*Z^(T-t)*G_t(h) - sum_{t=ceil(h/157)}^{floor(h/140)} C(N-1,t)*Z^(T+1-t)*W_t(h)`.
Every factor outside J is positive. Arbitrary-precision integer evaluations classify all 280 boundaries; an exact rational toy DP tests the jump identity, and 4 independent high-precision tail calculations test each k. Input hash checked directly.

Local exact-certificate SHA-256: k34 `a89c256c03b5adc72328d54ac81cff7991452434733e64be64e9c4537d62dffa`; k35 `97c8911d358c54428ae11daf09824fb680dfa49d1b91dad791e733fedcd8e24d`. The k34 cold-directory replay was byte-identical. The attempted k35 cold replay timed out; do not mark that additional check PASS. k36 attempt also timed out without a certificate.

Complete ZIP `X6_K34_K35_PORTABLE_20261108.zip`: **420,087 bytes**, SHA-256 `a389dbd6b5e19f6456f2ccc7f866844b475e2395a296337fc91f9c32d43f7bf0. The ZIP includes the frozen input, preceding k33 certificate, exact Python sources, k34/k35 140-row signed-integer certificates, proof and continuation metadata; ZIP member readback succeeded locally. **No remote ZIP publication is claimed**. Primary previous author summary: `research_notes/portable_direct/20261108_hourly40_x6_k31_k33_author_portable_summary.md` at commit `3a745e28a8603635152a3ec3c7fc2fafd830c46c`.

## Honest recovery boundaries and next actions
Native gateway status read returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; Sites diagnostic `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. Actual Source owner/session/claim/run/original request receipts UNKNOWN; no native mutation, CLAIM, freeze, release or Source checkpoint performed. This GitHub file is neutral author evidence only.

UR V2 prior math is complete: historical true original is **94,687 bytes**, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Bounded local 38-file/87-member scan and targeted GitHub/Drive search did not recover verified bytes. Next: locate original, verify size/SHA, repair only legitimate writer/provenance/checkpoint without redoing UR proof. After restored backend authority, reconcile this conversation's actual original requests and read exact Source continuation/claim; on `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, read all initial artifacts and set `frontier_notes.completed_units=[]`, never substitute author-side evidence as predecessor-completed research.

Independent exact verification **completed in this run**: a separate direct multinomial tuple enumerator (without polynomial convolution or prefix sums) checked all 635 positive threshold-crossing tuples and 4 equality-loss tuples at N=484300. Its signed integer has **47,244 digits**, SHA-256 `403fea89adf487f02a7f79dcc34ca4e5c75f1785b128eff867034536b7f8255e`, exactly matching the first integer engine. The new local ZIP includes this standalone verifier. Next authorized independent science: derive a structural criterion for failure/persistence of negative-offset nesting or verify a different unresolved boundary, without repeating the now doubly verified new point. No repetition of k<=33 or already-proved UR mathematics. Current status: **REGISTER_PENDING / SYNC_DEBT / UNREVIEWED / NOT_ADMITTED**.
