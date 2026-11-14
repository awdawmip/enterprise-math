# R762AG — Triadic burst threshold and exact C3 source-residue dynamics

**Status:** author-side conditional proof and exact independent computation; NOT_REVIEWED / NOT_NATIVE_ADMITTED.

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. **Frozen science:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. **Predecessor:** R762AF, Draft PR #2389 at 7db9d11653d34d264aaec846ae6a91f6972cde86. Previously issued researcher EM-X6-3050F6 is historical contribution provenance, not proof of current execution authority.

## Model and observation

The conditional star consists of three one-token outer ports 0,1,2, initially each holding its own *named source token*, and a central hub of integer capacity b, initially and finally empty. A shortest fully moving macro has exactly six steps: each port is vacated once (I_i, token entering hub) and refilled once (O_i, one hub token returning to port i); no source returns to its original port. The complete chronological log tau records the six I/O *port labels in order* but hides the outgoing source identities. The named final source-to-port permutation is therefore a derangement of three labels, necessarily one of the two 3-cycles p+=(1,2,0) or p-=(2,0,1), where entries are the destinations of sources 0,1,2. Let A_b(tau) count distinct compatible named final maps.

This is a capacity-controlled exchange model. A candidate embedding can attach its three ports to three distinct signed X6 directions, but its central occupancy and movement rules have not been admitted as an actual primitive TRIADIC_CLOSURE_E, V29 PASS/TRANSFER law or V17/V39 update. No Euclidean force-vector balancing is used.

## Theorem AG1: sharp three-source buffering and chronological ambiguity

For all integer b>=1, the complete classification of realizable source-blind six-step logs is:

| Hub capacity | Logs with A=1 | Logs with A=2 | Total source-blind logs | Named physical histories |
|---|---:|---:|---:|---:|
| b=1 | 0 | 0 | 0 | 0 |
| b=2 | 24 | 0 | 24 | 24 |
| b>=3 | 24 | 36 | 60 | 96 |

Precisely the 36 logs with all three I steps before every O step have A_b(tau)=2, and they exist only at capacity at least three. All other realizable logs have A_b(tau)=1. Thus at primitive-sized three-source scale, a capacity-two hub makes complete chronology source-injective; permitting one three-token burst introduces exactly one unrecoverable orientation bit.

**Proof.** Every physical map is a three-cycle. Such a permutation sigma is compatible with a logged word iff (i) all prefixes have occupancy between 0 and b, (ii) each port j was vacated before its O_j, and (iii) for each source i, I_i precedes O_{sigma(i)}. Conversely these inequalities realize a unique physical token choice at each outgoing port, because source i is inside the hub exactly from I_i to O_{sigma(i)} and the number of hub tokens is determined by the log independent of their identities. Hence this is exactly the R762AE matching bijection specialized to three tokens.

If **both** three-cycles fit a word, consider its earliest output O_j. That output may receive either of the two *other* source tokens, which therefore both must have already entered before O_j. Port j itself must also have been vacated before O_j. Thus all three inputs precede the first output. Conversely, when all three ingresses occur before all outputs and b>=3, either three-cycle realizes the same word. The 3! ingress orders and 3! output orders give precisely 36 ambiguous words.

At b=1, the first ingress fills the hub and cannot be followed by a non-home output, because the only vacated port is its own; no second ingress is possible. At b=2, a realizable word must begin I_a,I_b,O_j for distinct a,b and j in {a,b}, then perform I_c for the remaining port before the next O step: otherwise the first two source tokens must fill each other's ports, leaving the last token only its own prohibited destination. Both orders of the final two outputs are legal and force the same three-cycle (the source of the first output is the *other* early ingress). Count: (3*2) early ingress orders, 2 first-output choices, 2 final-output orders, giving 24. All have A=1 by the earliest-output argument. At b>=3 every other realizable log has first output after exactly two ingresses, and hence is in the preceding 24-word family. QED.

## Theorem AG2: exact repeated-macro C3 source history and terminal residue

Suppose k>=0 such three-source macros are executed on the same three ports, with **hub empty and one token per port at each boundary**. At every macro the source-blind full I/O word and the boundary reset are observed; each word is realizable at b>=3. The hidden orientation of a burst is independent of other bursts except through the ordinary composition of source permutations. No additional native force-state constraint is assumed.

Let h be the number of burst-ambiguous words. All nonburst words uniquely determine their orientation p+ or p-. Let c in Z/3Z be the sum of those known orientations, with p+ represented by +1 and p- by -1.

There are exactly **2^h ordered compatible source histories**, and the final source permutation is p+^r, where

r = c + epsilon_1 + ... + epsilon_h modulo 3, each epsilon_j in {+1,-1}.

Writing q=r-c (mod 3), the exact multiplicities of final source residues are

- N_0(h) = (2^h + 2(-1)^h)/3;
- N_1(h) = N_2(h) = (2^h - (-1)^h)/3.

Thus the terminal source map has exactly 1, 2 or 3 possible states when h=0, h=1 or h>=2 respectively. The optimal fixed-length repair for **the entire hidden macro orientation history** is h bits; for **the terminal source permutation alone** it is 0, 1 or 2 bits respectively.

**Proof.** A burst has precisely two independent choices and a nonburst has one, yielding 2^h source histories. The two three-cycles generate the cyclic group C3, with p-=p+^{-1}, so their composition has precisely the stated residue. For h ambiguous choices let a_h count residue zero and b_h count each of residues one and two; b_0=0 and a_0=1. Appending ±1 yields a_{h+1}=2b_h and b_{h+1}=a_h+b_h. Hence a_h+2b_h=2^h and a_h-b_h=(-1)^h, giving the closed formulas. The support is 1,2,3 as stated. Fixed-length binary injective encodings need ceil(log2 of support size) bits and this is attainable. QED.

## Theorem AG3: positive weighted BRC residue

If ambiguous burst j has **positive or nonnegative rational branch weights** u_j for +1 and v_j for -1, the exact positive BRC history mass of terminal class r is the coefficient of x^r in the cyclic group algebra expression

x^c * product_{j=1}^h (u_j*x + v_j*x^2)  modulo (x^3-1).

The recurrence B_{j+1}[r]=u_j B_j[r-1]+v_j B_j[r+1] (indices modulo 3), with B_0=(1,0,0), evaluates the full three-residue positive mass exactly in O(h) arithmetic operations. At constant weights u,v,

B_h[r] = sum_{0<=j<=h: 2j-h congruent r (mod 3)} binom(h,j)u^j v^(h-j).

**Proof:** The group algebra product enumerates each ordered orientation word with its product weight and records its orientation sum mod 3. Multiplication by the next binomial updates adjacent residues, which is the displayed recurrence. The constant-weight sum chooses j positive-orientation events. These are positive branch masses/counts, not signed force amplitudes or cancellation coefficients.

## Independent verification and current frontier

The accompanying standard-library Python program exhausts all **6!=720** distinct I/O words for each b=1,2,3. It independently computes compatible maps by explicit physical labeled-token state transitions and by matching inequalities, checking 2,160 exact agreements plus the 0/24/60 logged-word counts and 36 ambiguous burst words. It also verifies residues h=0..14 with integer recurrences and independent binomial formulas for three integer weight pairs, including unequal weights; see the JSON evidence. The general results follow from the proofs, not finite extrapolation.

**Next discriminating native question:** establish the actual P000-admissible TRIADIC_CLOSURE_E Cell/Link/Port source incidence and whether an admissible triad allows three simultaneous in-flight quanta (or an observationally equivalent burst) without violating native force closure. Test actual ordered V29 internal PASS vs boundary TRANSFER, V17 frame action, V39 transport and repeated-event legality. In this model a capacity-two cap certifies source reconstruction from complete chronology; an admitted three-token burst necessitates the one-bit orientation repair. The exact future-operation quotient must preserve whatever source-sensitive native state is subsequently shown to matter. Six-dimensional P000, the ACTIVE worldview, and frozen science remain unchanged.

**Publication boundary:** author-side conditional mathematics, not a current authenticated CLAIM, Source PROGRESS, formal Result, Driver review or native force admission.
