# PREFIX-592-R2 — Adaptive nonnegative dual BRC channels: exact minimality and sharp per-block negative-support bound

2026-11-08. AUTHOR-SIDE PROOF + EXACT NATIVE TRANSITION CERTIFICATE; UNREVIEWED.
Frozen science: `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessors PREFIX-589/590/591; no modification of the original 96 labelled native ports, 576 actions, six axis rewards or three marked gate branches.

Let `W` consist of 24 independent `J_4-I_4` blocks, `T=W^-1 A W>=0` (PREFIX-588/589 for all nonnegative axis/gate parameters), and `H=3W^-1=W-2I` (PREFIX-591). For an arbitrary native nonnegative integer input `r`, define the signed dual integer vector `v=Hr`.

## Theorem 592.1 — Unique pointwise least nonnegative pair

Set `p_i=max(v_i,0)`, `q_i=max(-v_i,0)`, coordinatewise. Then `p,q>=0`, `v=p-q`, and for every other nonnegative decomposition `v=p'-q'` one has `p' >= p` and `q' >= q` coordinatewise. This follows from `p'_i=v_i+q'_i`: if `v_i>0`, `p'_i>=v_i`; if `v_i<0`, `q'_i>=-v_i`. Thus the canonical split is uniquely entrywise least, in contrast to the *fixed linear* universal split `p_0=Wr, q_0=2r` from PREFIX-590.

Since `v=(Wr)-(2r)` and both universal channels are nonnegative for `r>=0`, entrywise `p<=Wr`, `q<=2r`. Nonnegative dual evolution preserves these inequalities for each independently weighted native step. Therefore **every subsequent adaptive positive stream is coordinatewise bounded by its corresponding universal linear stream**, and its active nonzero labelled-edge summand count under the same sparse-edge reference interpreter cannot exceed the fixed split's count. All original path/gate observables recover exactly from `W(T^n p-T^n q)/3`.

## Theorem 592.2 — Sharp local sign structure and one-positive-stream regime

On each four-port group `G`, let `s=sum_{i in G}r_i`. Then `v_i=s-3r_i`. Thus the adaptive negative stream vanishes exactly when `3r_i<=s` for every `i` in every group; in this regime the nonnegative **single** dual stream is sufficient, without final positive-minus-positive cancellation.

For nonnegative `r`, each group contains at most two negative coordinates of `v`. If three distinct coordinates had `3r_i>s`, their sum would exceed `s`, a contradiction. The bound is sharp, e.g. `r|_G=(1,1,0,0)` gives `v|_G=(-1,-1,2,2)`. A singleton `(1,0,0,0)` yields `(-2,1,1,1)`. Uniform `(1,1,1,1)` yields `(1,1,1,1)` and requires no negative channel.

## Executed exact BRC cost check

Companion `PREFIX592_R2_adaptive_split_core.py` directly reuses PREFIX-591 and unchanged PREFIX-589 source construction. It checks all original/dual vector identities at each of 12 steps under four time-varying integer-weight parameter sets. It propagates original, signed-dual, fixed-positive-pair and adaptive-positive-pair states with exact integers and counts a labelled edge contribution exactly when its carried state coefficient is nonzero. Totals across 12 steps are:

| Input | Native | Dual signed | Fixed dual two-positive | Adaptive dual two-positive |
|--|--:|--:|--:|--:|
| Single native port 0 | 2658 | 2400 | 5412 | 5412 |
| All 96 native ports = 1 | 6912 | 6912 | 13824 | **6912** |
| All four ports in one group | 3000 | 2760 | 5520 | **2760** |
| Seven selected sparse native ports | 5658 | 5268 | 11880 | 11880 |
| Two concentrated ports in one group | 2844 | 2592 | 5508 | **5496** |

All assertions passed. These counts establish an exact workload-specific **sparse operation-term improvement over the fixed two-channel decomposition**, including a factor-of-two reduction for balanced/uniform inputs. They do not assert lower elapsed runtime or universal advantage versus direct native propagation. Full cost assessment still includes source transformation, bit lengths, batch reuse, output recovery and the changed support under dual propagation.

## Next: PREFIX-593

Optimize batch source/observer evaluation by choosing, per group, native direct propagation versus signed/one-positive/adaptive-positive dual propagation. Count both exact arithmetic and scalar bit-length work, including conversions and final recovery. Try a family with repeated observers and nonuniform gate weight, and test whether the full cost—including caching—beats the native baseline. Preserve the original labelled BRC semantics and exact observer scope.

Native Source Researcher-ID/Owner/CLAIM/Result are unconfirmed due `BACKEND_IDENTITY_CHECK_UNAVAILABLE / operation_sent=false`; GitHub branch evidence is author provenance, awaiting independent mathematical review.
