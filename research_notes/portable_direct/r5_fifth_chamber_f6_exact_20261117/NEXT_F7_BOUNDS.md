# R5 fifth noise chamber: f=7 initial exact bounds

Using the frozen 256-state integer scalar observer with scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`, 101 physical budgets 214..314, and noise `L<=2η<U` with `L=25845652773852463277015040000` and `U=58182461585441404127941754880`:

```math
7385 <= C*_7(eta) <= 7392.
```

**New exact lower:** Restrict possible true states to the genuine five masks `(18,24,82,34,17)` but retain all 101 physical query budgets. The executed exact Python Bellman minimax at `τ=L` returned:

```json
{"f":7,"cost":7385,"state_count":32379,"actions":[216,223,296,214,215,221,222]}
```

The five-state model is an easier restriction, so this yields the full256 lower bound for every `τ>=L`. The universal descending-query construction previously stored for this chamber yields upper `735+951f`; at `f=7` this is `7392`, applicable throughout the chamber.

The exact f=7 full256 minimax is **OPEN**. The special formula `735+950f`, verified for `f<=6`, predicts cost `7385`; neither its f=7 attainability nor a stronger universal statement is asserted. Next decisive computation: construct/verify a full256 adaptive policy of budget 7385 at `τ=U-1` using the 5-action or 8-action physical budget family, or establish a counterexample to that cap.

Status: `AUTHOR_COMPUTED / EXACT_FINITE_CHECKED (LOWER ONLY) / NOT_REVIEWED`. No P000/worldview change, no Task/CLAIM/Result/Review admission.
