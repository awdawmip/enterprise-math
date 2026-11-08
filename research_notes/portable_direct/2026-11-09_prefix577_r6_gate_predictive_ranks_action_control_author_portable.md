# BRC-X6: exact gate-language predictive ranks under four native control regimes

Date: 2026-11-09. Status: **AUTHOR_PROVED / EXACT_INTEGER_AND_MODULAR_CERTIFIED / UNREVIEWED / NOT_ADMITTED**. Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## All-96-port, all-length theorem

Use the original frozen 96 native ports, 576 transitions, labels `a=(slot,newbit)`, and gate output `K∈{0,1}`. Compare four permitted controller operations: passive 6-way uniform, newbit fixed with uniform slot, slot fixed with uniform newbit, and full label fixed. For each control choice `u` and gate `g`, define the **integer** transition matrix
\[
M_{u,g}[p,q]=\#\{a:\operatorname{control}(a)=u,\ K(p,a)=g,\ \operatorname{next}(p,a)=q\}.
\]
For any controlled gate word `w`, its all-initial-port count column is `v_w=M_w 1`. Probabilities are obtained by known nonzero per-step factors of `1/6,1/3,1/2,1` for the four policies. Define `V=span_Q{v_w : all finite gate-control words}`. This is the linear predictive space for the **family of all 96 separate native starting ports** (not necessarily a fixed initial mixture).

| Policy | Exact minimal `Q`-linear prediction dimension | Gate-language equivalent native-port classes | Strong output-bisimulation blocks |
| --- | ---: | ---: | ---: |
| Passive | **11** | **20** | 24 |
| Newbit controlled, slot random | **11** | **20** | 24 |
| Slot controlled, newbit random | **44** | **51** | 51 |
| Both fully controlled | **44** | **51** | 51 |

The full initial-port gate-language equivalence partitions coincide within passive/newbit-controlled and within slot-controlled/full-controlled. The predictive **column spaces** coincide within each pair as well: the weaker controller's operators are sums of the stronger controller's operators, so inclusion holds, and the proved exact ranks agree. The control of `slot` therefore changes the *exact* prediction dimension from **11 to 44**, whereas additional `newbit` control alone does not increase it. All nine frozen roots share the same gate indicator and native action transitions.

This improves the earlier 2026-11-09 strong-quotient classification: preserving complete all-length gate-language probabilities is strictly weaker than preserving all gate-conditioned transitions into strongly bisimilar hidden-state blocks. Linear prediction is a further exact compression, not a replacement of labeled branch provenance under stronger observation regimes.

## Concrete observer-scope separation

Ports **10 and 16** are distinguished by the passive gate-only **24-class strong bisimulation**, yet have **identical probabilities for every passive gate-output word**. Their one-step gate=0 edge counts into strong blocks differ:

- Port 10: 2 edges each into blocks 2, 12, 18.
- Port 16: 4 edges into block 8 and 2 into block 19.

An exact finite basis of every gate-word value vector has identical entries at native ports 10 and 16. Closure of this basis under all passive gate operators proves the identity for **all path lengths**, not only the tested horizon. The 20 gate-language classes are obtained by all-96-port equality of this basis's exact integer signatures. In the slot/full controlled regimes strong and gate-language equivalence each have 51 classes, while the linear predictive dimension is only 44.

## Proof and exact certificate

A fraction-free exact integer closure starts from the all-ones vector, repeatedly applies **every** integer gate/control operator to discovered rationally independent columns, and checks each operator preserves the final finite span. For each regime an independent nonzero modular rank certificate at both `1000000007` and `998244353` proves the matching rational lower bound; exact closure proves the rational upper bound. Numbers of exact generator checks and maximum generating word lengths, respectively:

- Passive: rank 11, closure 22 checks, maximum depth 10.
- Newbit: rank 11, closure 44 checks, maximum depth 10.
- Slot: rank 44, closure 264 checks, maximum depth 5.
- Full: rank 44, closure 528 checks, maximum depth 5.

The script independently recomputes prior strong partitions and confirms 24/24/51/51 strong classes, 20/20/51/51 all-length gate-language classes, and witness (10,16) where the two differ. A separate finite-field implementation directly recomputes the native 96-port rank 11/11/44/44. All 576 native edge records and the nine-root policy-quotient certificate from the preceding author note are retained.

Certificate: `GATE_PREDICTIVE_LINEAR_RANK_CERTIFICATE.json`, SHA-256 **`b4eb623f3325b64f324a9fac9f56e8e0d28118d15527cdc7577d06c6f055714e`**. Self-contained 10-file portable author ZIP SHA-256 **`324a441447d87579345f0892c6625affc53d68b56bbabc331d0c665f24a8eab3`**. Independent extraction and execution of both exact scripts and the modular implementation reproduced certificate bytes and all nine original manifest checks.

The expanded theorem, scripts, original native CSV, frozen kernel, both certificates and manifest are saved in the current research conversation under `/mnt/data/em_turn231/PREFIX577_R6_GATE_POLICY_AND_PREDICTIVE_RANK_AUTHOR_PORTABLE_20261109.zip`. Published author evidence is separate from native Source checkpoint, Result, independent review and theorem admission.

## Current Source, parent objective and next action

Existing D24/UR Result and Driver Review are accepted historical records. D25 Source continuation original request `h40-r11-d25-continuation-20261108t1512-v1` was still `QUEUED / SOURCE_LOCK_BUSY` on 2026-11-09; no new request or CLAIM was sent. Own recovery_status requires a verified private session capability; Source execution authority was not obtained. D25's original H0/B0, `[X]U mod p^2`, Frobenius direction/eta and native CM run remain the priority when legally routed. The original four-file UR V2 bundle still requires exact length `94687` and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`.

Optional independent next investigation, only if permitted by Source and nonduplicate: minimal predictive ranks for *gate plus selected reward axes* under partial action control, preserving intended observer provenance. This note makes no new claim about arbitrary initial mixtures, physical dynamics, Source task completion or model promotion.
