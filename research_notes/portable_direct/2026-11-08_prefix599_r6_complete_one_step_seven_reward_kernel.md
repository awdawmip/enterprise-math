# PREFIX-599-R6 — Complete exact one-step native X6-BRC observation kernels for nine roots

Date: 2026-11-08 Asia/Shanghai. 
Researcher-ID: EM-DIRECT-B900FB / TASK_RESEARCH.
Research-Activity-ID: RA-CC93244CAE5F854895CE2C8E.
Frozen input pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_RANK_CHECKED_ON_NATIVE_FORMULA_TRANSCRIPTION / UNREVIEWED / NOT_ADMITTED.

## Exact model and observer

Use the original native PREFIX-565 X6-BRC phase/bit graph, 48 phases × 2 bits = 96 original ports, 6 equally likely native actions, 9 allowed roots. The native full-reward label comprises all six axis BRC step counts and the gate count, while the readout *also includes the exact original next port*. Compare two output alphabets:

- \`O_7\`: (entire native seven-reward vector, exact next original port), action slot/newbit hidden.
- \`O_7^act\`: (entire seven rewards, exact next original port, original primitive action (slot,newbit)).

For each root \`r\`, let \`L_r\` and \`L_r^act\` be the linear one-step transfer operators from signed rational measures on 96 original input ports to rational measures on these output alphabets. Their rows have integer coefficients equal to native six-action output counts; the physical probabilities divide all rows by 6 and preserve rank/kernel.

Write \`d_p=e_(2p)-e_(2p+1)\` for native start-branch-bit contrast at physical phase \`p∈{0,...,47}\`.

The gate target \`TARGET=4\` has precisely three incoming source phases \`P={3,14,15}\`, all with signed native component \`+1\`. Their target action slots are \`s_3=0,s_14=1,s_15=1\`; every other phase has no target slot.

## Theorem: exact rank, kernel and full scope (each of nine roots individually)

For **every** one of the nine frozen allowed roots,

$$
\boxed{\operatorname{rank}_{\mathbb Q}(L_r)=49,\quad
\dim_{\mathbb Q}\ker L_r=47},
$$

and the full kernel has this **explicit basis**:

$$
\boxed{\ker L_r=
\operatorname{span}_{\mathbb Q}\bigl(
\{d_p:p\notin P\}
\cup\{d_3-d_{14},\,d_{14}-d_{15}\}
\bigr)}. \tag{1}
$$

If primitive action labels are retained, then for **every** frozen root,

$$
\boxed{\operatorname{rank}_{\mathbb Q}(L_r^{act})=50,\quad
\dim_{\mathbb Q}\ker L_r^{act}=46},
$$

with full kernel

$$
\boxed{\ker L_r^{act}=
\operatorname{span}_{\mathbb Q}\bigl(
\{d_p:p\notin P\}
\cup\{d_{14}-d_{15}\}
\bigr)}. \tag{2}
$$

In particular, both kernels are root-independent on this exact nine-root domain, and

$$
\dim(\ker L_r/\ker L_r^{act})=1.
$$

Retaining primitive action labels restores **exactly one additional independent initial-port information direction** for the declared one-step full-seven-reward-plus-terminal-port observer.

### Proof

**Upper bounds and explicit inclusions.** For each of the 45 phases not in P, the gate remains zero for every native action from either source bit; their signed six-axis rewards and destination port are likewise independent of the source bit. Hence each \`d_p\` is killed by both operators. PREFIX-598 proves for the three target predecessor phases that their signed bit-contrast images coincide when actions are forgotten, giving two additional independent killed directions \`d_3-d_14\` and \`d_14-d_15\`. When actions are retained, only the pair of phases with the same target slot 1, \`d_14-d_15\`, remains killed. The listed 47 or 46 vectors are visibly independent by disjoint phase-pair support, so \`rank(L_r)≤96−47=49\` and \`rank(L_r^act)≤96−46=50\`.

**Exact lower bounds.** Independently construct the integer one-step matrix from every one of the 96 native source ports, each of the 6 literal native actions, and each fixed root. Enumerate all distinct exact output labels, producing, at each root, a 96 × 97 matrix for \`O_7\` and a 96 × 194 matrix for \`O_7^act\`. Exact rational sparse Gaussian elimination finds **49** nonzero pivots in the former and **50** in the latter, for all nine roots separately. This is a complete finite equality check on the frozen native formula (no float/tolerance, no extrapolation). The companion executable certificate imports the exact frozen PREFIX-565 \`edge\` and redoes this calculation with \`fractions.Fraction\`; the local check used a source-faithful independently transcribed version of that edge formula. Therefore each bound above is attained. The 47/46 independent known kernel vectors constitute the *full kernels*. QED.

The exact rational calculation does not assert that the same ranks hold for other root domains, other native kernels, or observers forgetting the original next port.

## Minimal complete initial-distribution summaries

All kernel vectors in (1)–(2) have zero total mass, and the total mass functional is already determined by the observed one-step probabilities (sum of emitted outcomes). Therefore, among linear summaries of **normalized** initial port laws, the minimum variable coordinate dimensions for the respective complete one-step outputs are **48** and **49**, rather than the 32 coordinates of the weaker PREFIX-594 triple-reward observer.

Moreover, since the full next original port is part of both outputs, equality of these one-step joint laws propagates by the Markov property to equality of the entire ordered future full-seven-reward (and, respectively, action-aware) histories plus terminal original port at every horizon n≥1, for common deterministic nine-root schedules. The same holds for adaptive root selection based exclusively on the respective observed history and independent shared exogenous randomness, by induction. Consequently these 48/49 variable linear coordinates are also sufficient and necessary for this stronger full-history/terminal-port observation language (n≥1), because the language itself includes the one-step output.

### Observer-provenance interpretation

The 45 phase-local source-bit contrasts away from the gate remain invisible even if every primitive action is exposed. Two more independent contrast combinations become invisible when action labels are hidden; if action labels are retained, only one remains. The difference in kernel dimensions is the exact cost of dropping primitive action provenance for this model and observer.

This is a **relation-preserving** result over a declared future language, not a claim that the actual native X6 world has fewer than six axes or that lost information is irrelevant to a different observer. The original six-axis rewards are all retained.

## Validation status

A locally executed Python standard-library independent transcription of PREFIX-565 source formulas returned ranks 49/50 and nullities 47/46 for every one of nine allowed roots. Rank elimination used \`fractions.Fraction\`, source keys were enumerated exactly, and null relations were checked as integer-count identities. This covers all 18 root/observer pairs. Repository-native \`PREFIX599_R6_native_kernel_rank_certificate.py\` imports the original frozen PREFIX-565 source and provides an independent rerun route; execution of that GitHub-importing version was not performed in this session. Author theorem still requires independent scrutiny.

**Next question (PREFIX-600-R6)**: derive the 48 independent phase-background columns directly from a combinatorial matching or a sparse determinant/minor uniform in the nine allowed roots, rather than relying on 18 exact rational eliminations. Quantify interface costs and compare the 49- versus 50-rank full-seven observers with the 33-linear/34-positive triple-observer carrier, while retaining the exact observer and future-operation scope.
