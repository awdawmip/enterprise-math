# BRC–X6 k31–k33 exact cost-cliff classification — author-side portable

Date: 2026-11-08. Status: **AUTHOR_EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_SOURCE_CHECKPOINTED**. This is a neutral evidence index and scoped proof; it is **not** a Source-native CLAIM, Result or predecessor-completed research checkpoint.

## Frozen scientific input and model
Source: 289-layer certificate `X6_ALL_289_CONDITIONAL_SHELL_CERTIFICATE_20261107.json` SHA-256 `47a1446a8d80d1e29302cef58767230362d74726a17ddea2ea44667557a18525`. Model identity SHA-256 `c523b6e8aecee971da44722bd0ff2cc2cbd1308a2c578f7cab7592c7b8562b53`. Same 288 native-source identities, 83 joint X6 observation classes, q=1/20, **IID** independent gain blocks; gains `R∈{0,140,147,157}` bits with frozen positive integer class weights. Let `S_N=Σ_{i≤N}R_i`, `H(N)=140+N/100`, `Q_N=Pr(S_N>H(N))`. The exact-weight histogram and source identities, not the collapsed success indicator, are the BRC carrier. Baseline author-side k30 certificate SHA-256: `4d294c9067a87435d74085f96278228bd3d7c1af621fb9ab00bc5936a520ae87`.

## Scoped finite theorem
Exhaustive integer signs at all 140 hundred-boundaries in each interval:
- k31, N=420000..433999: **27 negative**, **113 positive**, zero zero.
- k32, N=434000..447999: **27 negative**, **113 positive**, zero zero.
- k33, N=448000..461999: **28 negative**, **112 positive**, zero zero.

For the negative-jump sets `D_k`, **`D31=D30+14000`**, **`D32=D31+14000`**, **`D33=(D32+14000)∪{456000}`**. The complete k31/k32 offsets are `0,700,1400,1700,2100,2400,2800,3100,3400,3500,3800,4100,4200,4500,4800,4900,5200,5500,5600,5900,6200,6300,6600,6900,7000,7300,7600`; k33 adds offset `8000`. At all other N, Q cannot decrease because nonnegative gains accumulate while the effective integer threshold is unchanged between consecutive hundred-boundaries. Thus all 42,000 integer N are covered.

At N=456000, threshold is exactly 4700 bits. The complete equality-gain multisets `(t,a,b,d)` solving `157a+147b+140d=4700, a+b+d=t≤33` are:
`(30,29,1,0),(31,15,15,1),(32,1,29,2),(32,8,12,12),(33,1,9,23)`.
Equality support is *not* itself the negative sign proof. The exact gain-minus-loss jump integer is negative, has 44,619 decimal digits, and signed decimal SHA-256 `497a071343b5cc295958eb362cdd43fe2ddb1fa0aa189c0f2f51d8a32c4f8d86`. A separate 115-precision decimal-tail calculation gives `Q_456000−Q_455999≈−0.0000000084689332579849947549350316` percentage points.

## Integer proof kernel and witness
Put `M=A+B+D+Z` with `Z` zero-gain integer weight; for `N≡0 mod 100`, `h=140+N/100`, `T=floor(h/140)`, and `W_t(s)=[x^s](Ax^157+Bx^147+Dx^140)^t`.
Define `G_t(h)=Σ_{s<h}W_t(s)(A·1[s+157>h]+B·1[s+147>h]+D·1[s+140>h])`.
Then
`Q_N−Q_(N−1) = Z^(N−1−T)/M^N * J_N`,
where
`J_N=Σ_{t=floor(h/157)}^{floor((h−1)/140)} binom(N−1,t)Z^(T−t)G_t(h) − Σ_{t=ceil(h/157)}^{floor(h/140)}binom(N−1,t)Z^(T+1−t)W_t(h)`.
Every factor outside J is positive; exact integer evaluation therefore proves each sign. This is an IID-model finite classification, not a uniform all-k theorem.

Deterministic certificate SHA-256: k31 `469dfb97f592fda7e136e1f7c56bba37d0087ba320d67eada76f7d385f4931b3`; k32 `071bad71d382207b5f6980cc8a5b9e49e3777e975737087b6244a8049b3aff36`; k33 `3e7802858647f0362c70bf788d29cd571eb723e3a847e003a7c1bc1de66c0801`. Each JSON retains 140 exact sign rows, numerator digit lengths and decimal SHA-256s, plus four independent Decimal-tail sign spot checks. Recomputations of k31 and k32 using the consolidated driver were byte-identical; original k33 run passed its exact and decimal checks, while a later consolidated-driver replay timed out, so no extra k33 cold-replay success is claimed.

The **full portable artifact** `X6_K31_K33_PORTABLE_20261108.zip` (428,532 bytes; SHA-256 `4f991ac947fcaa9796ae19c1841a54ba685c06a1aa1d7f345088e9cab9acdb46`) was constructed locally and its ZIP members integrity-checked, with original frozen input, old baseline, source Python, new checker and three JSON certificates. **No byte-for-byte remote ZIP publication is claimed**. A local/source-reference pointer alone is not proof of distant persistence.

## Canonical continuation and unresolved dependencies
Mother objective: work on independently authorized Enterprise Math research, respecting canonical dispatch, owner and observer/source pins. Actual Source session, claim, run, predecessor state and pending original request IDs for this conversation are **UNKNOWN**, not empty. Current `em_status` grants `research_authority_granted=false`; the connector describes `recovery_status` but has no callable recovery tool in this turn. Therefore these files do **not** assert `predecessor.completed_units`, Source owner progress, or Result acceptance. For `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS` require complete current-input artifact readback and `frontier_notes.completed_units=[]` before typed continuation_prepare, only if actual native authority allows it.

Separate original UR V2 four-file restoration remains pending: exact 94,687-byte original with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. In this run local files/ZIP entries and indexed GitHub/Drive searches revealed no verified original bytes; do not redo UR mathematics. Next precise step: use actual subject's native recovery and original receipts when available, reconcile before replay, then consume Source continuation/verify claim. In the source-authorized portable scope, test an independent k33 jump certificate or search for a failure of nesting of negative-offset sets. No scheduler or user-notification setting was modified.
