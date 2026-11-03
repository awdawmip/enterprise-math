# Stage397-B — exact future-minimal BRC path memory with directed joint history

Date: 2026-11-03. **Author-side mathematical research**, status UNREVIEWED / NOT_ADMITTED.
Parent: Stage396-B, Research2 PR #1736, commit 81c76f5ef7014115f52eec321cc9d77d501e6826.
Frozen science: Enterprise Math \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`; account science \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`; P000 blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Current behavior was read independently from canonical 2026-11-03 main.

## Domain, observer and operations

\`A={+E_i,-E_i | 1<=i<=6}\`. A state is a finite *ordered* word \`w in A^*\`. Its native endpoint is \`z=sum(w) in Z^6\`. Fix one source label, strictly positive rational endpoint weights \`p_d\`, and separately fixed nonzero rational individual-history factors \`omega_d\`. For any \`w\`, the observer \`O_J(w)\` contains source, length \`m\`, native endpoint via all 20 complete relative three-component X6 projections plus common depth \`h\`, native full-length \`N_m(z)\` and positive-rational \`W_m^p(z)\`, the individual signed product \`Omega(w)=prod omega_{w_i}\`, the turn count \`tau(w)\`, and the **ordered joint edge histogram**
\`J_w(d,e)=#{i in {1,...,m-1}: (w_i,w_{i+1})=(d,e)}\` for all 144 signed pairs.

Actions: APPEND(d) for any of 12 labels; POP_D of an allowed terminal label \`d in D\` up to \`H\` total times; CANCEL of an inverse terminal pair \`(d,-d)\` up to \`C\` total times. Definedness is observable. Every intermediate observation is observable. APPEND has arbitrary finite horizon. \`H,C\` are nonnegative integers. This is path-formal typed history rewriting, with time/order separate from the six spatial axes.

In this model \`tau(w) = sum_{d!=e} J_w(d,e)\`; therefore the separate tau coordinate can be reconstructed from J at every update. This is an exact observer/future-operation redundancy within the stated \`O_J\` carrier.

## Result 397.1: finite algorithm for the coarsest future quotient

For any finite initial \`O_J\`-fiber \`F_o\` and fixed \`D,H,C\`, the relation
\`w~v\` iff all common action words have identical enabledness and their identical defined prefixes have equal intermediate \`O_J\`
is **decidable by a finite pair-state graph**. The exact minimum number of memory symbols is \`q(o)=|F_o / ~|\`, and the minimum fixed-length binary memory is \`ceil(log_2 q(o))\`.

For each pair \`(w,v)\` with equal initial observation, set \`L=H+2C+1\`. Store only the two terminal suffixes of length \`min(m,L)\`, the remaining budgets \`h,c\`, and a Boolean that all preceding readouts were equal. Explore all 12 APPEND actions, enabled POP_D, and enabled CANCEL; immediately mark the pair distinguishable if their enabledness differs or a newly observed readout differs. Otherwise continue with suffix length \`h+2c+1\` after each action. This is a finite graph: both recorded suffixes always have length <=L over a 12-letter alphabet and budgets belong to finite sets. Breadth/depth search with visited states terminates even though the APPEND horizon is unlimited.

**Proof of exactness.** If the prior readouts coincide, source, \`z,m,N,W,tau,J,Omega\` coincide. Every next readout-equality test depends only on the accessible last labels and the operation:
* APPEND(d): \`z'=z+d\`, \`m'=m+1\`, \`Omega'=Omega*omega_d\`; if a preceding label \`b\` exists, \`J'=J+[b,d]\`.
* POP_D of terminal \`b\`: \`z'=z-b\`, \`m'=m-1\`, \`Omega'=Omega/omega_b\`; if penultimate \`a\` exists, \`J'=J-[a,b]\`.
* CANCEL of last \`(b,c)\`, \`c=-b\`: \`z'=z\`, \`m'=m-2\`, \`Omega'=Omega/(omega_b omega_c)\`, \`J'=J-[b,c]-[a,b]\` if predecessor \`a\` exists, else \`J'=J-[b,c]\`.
Here \`[d,e]\` denotes the unit count at that directed edge. \`tau\` follows from J, while N and W are deterministic exact native BRC functions of \`z,m\`. A POP requires at most two accessible letters and reduces \`h+2c+1\` by one. CANCEL requires at most three and reduces it by two. APPEND only requires the terminal letter and can truncate to the unchanged cap. Hence the finite suffix retains every label needed by subsequent one-step equality and enabledness tests. The abstract graph and the full pair transition system have identical possible first observable disagreements (induction on action length). Therefore reachability of a disagreement is equivalent to distinguishability under arbitrary finite futures. The equivalence classes, not the fixed suffix classes, give the exact coarsest quotient. QED.

This is an exact finite **decision procedure**, not a claim of polynomial complexity: the worst-case abstract pair graph grows exponentially with \`H+2C+1\`. Enumerating an infinite \`O_J\`-fiber requires an additional symbolic or regular-language representation; the present algorithm accepts an explicit finite fiber.

## Result 397.2: closed form for H=0, C=1, any source and weights

When \`D\` is irrelevant (\`H=0\`) and at most one CANCEL is allowed, define for a word of length \`m\`:
* \`kappa(w)=w\` if \`m<=2\`;
* for \`m>=3\`, \`kappa(w)\` is the last **three** letters if the final two are inverse, and the last **two** letters otherwise.

For **every** initial \`O_J\`-fiber and for all original words \`w,v\` in that fiber,
\`w~v iff kappa(w)=kappa(v)\`.
Thus \`q(o)\` equals the number of distinct \`kappa\` signatures present in \`F_o\`.

**Sufficiency.** Before its unique CANCEL, a future may append any number of letters. That CANCEL can erase (a) two appended letters, requiring only the original last letter at the surviving boundary; (b) the original last letter and one appended inverse, requiring the original penultimate at the new boundary; or (c) two original letters if they are already inverse, requiring the third-from-last. After cancellation, no additional deletion is allowed; only the new terminal label affects further J and tau updates. The stated \`kappa\` carries exactly the necessary boundary data, while current O_J supplies the cumulative totals. Identical kappa therefore ensures identical future readouts and definedness.

**Necessity.** If final letters differ, a common APPEND of one candidate final label distinguishes tau. If final letters agree but penultimate differ, APPEND of the opposite final label followed by CANCEL exposes the different penultimate; a further APPEND distinguishes tau. If last two agree and are inverse but third letters differ, an immediate CANCEL exposes the two distinct third letters; a subsequent APPEND distinguishes tau. All distinguishing sequences have length at most three. If \`m<=2\`, the same cases apply with absent predecessor handled by the empty state. Thus different signatures imply distinguishability. QED.

This closed form gives a future-safe, smaller-than-uniform suffix repair when the last pair is not inverse.

## Result 397.3: a strict BRC joint-fiber reduction from 3 to 2 states

Consider the four length-six histories consisting entirely of \`+E_1\` except for one \`-E_1\` at position \`r in {2,3,4,5}\`. Write them \`w_r\`. Each has:
* \`z=4E_1\`, \`m=6\`, source fixed; all 20 complete X6 triple readouts and common depth match;
* \`J(+E_1,+E_1)=3\`, \`J(+E_1,-E_1)=1\`, \`J(-E_1,+E_1)=1\`, other J entries 0, so \`tau=2\`;
* \`Omega=omega_{+E_1}^5 omega_{-E_1}\` for **any** nonzero rational letter factors;
* \`N_6(4E_1)=156\` exactly, by the 12-direction all-length BRC kernel, and the same positive weighted mass \`W_6^p(4E_1)\` for any fixed positive p.

These are exactly the four words in this entire O_J-fiber: its J-support forces the alphabet to be just \`{+E_1,-E_1}\`, the positive endpoint and length force five pluses and one minus, and the two directed off-diagonal edges force the minus to be interior.

At H=0,C=1, the fixed Stage396 suffix length is three. It gives three signatures: \`(+,+,+)\` for r=2,3; \`(-,+,+)\` for r=4; \`(+,-,+)\` for r=5. But \`kappa\` gives only **two** classes: r=2,3,4 all have noninverse final \`(+,+)\`; r=5 has inverse final \`(-,+)\` with preceding \`+\`. Consequently \`q(o)=2\`, with only **one bit** of extra future-safe memory, versus three uniform-suffix classes requiring two bits. The current joint histogram alone does not distinguish these four original histories. This is a certified exact strict compression at the full original O_J-fiber level.

The native positive weighted endpoint mass is separate from the signed individual-history factor. For example choose \`p_{+E_1}=2\`, \`p_{-E_1}=3\` and all ten other signed directions weight 1; exact native weighted recurrence gives \`W_6^p(4E_1)=2976\`, agreeing across the four histories.

## Exact execution evidence and next unit

The standalone Javascript checker uses integer and BigInt recurrences (12 signed directions) and exhaustive paired continuation checks over the smaller declared alphabet \`{±E_1,±E_2}\`, initial lengths up to five and future traces up to four steps. It additionally checks all six pair comparisons of the strict four-word fiber to depth five, and exhausts the 64 two-letter-alphabet length-six words to establish its fiber size. Its full stdout and JSON certificate are preserved beside this proof. All-horizon scope follows from the proofs.

BRC reuse: \`REUSE_EXECUTED\` for the frozen native full-length signed X6 BRC count/positive weighted recurrence; \`COMPOSE_APPLIED\` for joint edge histogram and operation-sensitive future quotient. Status: PORTABLE_AUTHOR_PROOF / EXACT_INTEGER_BRC_EXECUTED / FINITE_CROSSCHECK / GITHUB_PERSISTED only after remote readback / UNREVIEWED / NOT_ADMITTED. No native CLAIM, Source Result, Driver review or promotion is asserted.

Next Stage398-B: derive a compact symbolic representation for infinite O_J-fibers, test multiple CANCEL operations \`C>=2\` for exact reduced signatures, and quantify quotient complexity and costs of materializing J versus incremental edge updates. Preserve original source pins and the separated signed/positive BRC carriers.
