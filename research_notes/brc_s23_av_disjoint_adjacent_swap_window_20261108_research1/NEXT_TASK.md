# S23/AV continuation after adjacent-swap window theorem

Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Latest author-side result: `PROOF.md`, `VERIFY.py`, `RUN_EVIDENCE.txt` in this directory; PR #1777. Shared task CLAIM, Result/Review and independent mathematical acceptance are not asserted by this handoff.

## Result to reuse

For every `4,910,648 <= H <= 7,365,716`, the *entire* true ordering of the S23/AV threshold triangle `S_H` is obtained from the old integer-key lex order `(2074774v-380295j,-v)` by swapping adjacent pairs `(x,x+(760669,4149979))` for `x>=0`, `|x|_1 <= H-4,910,648`. The pairs are disjoint and number `(s+1)(s+2)/2`; exact rank/select uses only a constant-time membership correction. `H=7,365,717` admits a second class `u+3w`.

This is an exact *ordering* result, not a statement about constant minimal observer capacity `N(H)`.

## Smallest open steps

1. **Capacity route (priority):** independently reuse the source seven-plateau capacity certificate through `H=2,455,578`. Compute the exact prefix occupancy of all newly split gaps when the new `u+w` threshold is introduced at `H=2,455,579`, using the prior threshold rank/select and floor-sum occupancy oracle. A completed certificate must check all changed gaps and distinguish a surviving old capacity bound from an actual capacity increase.
2. **Ordering route:** at `H=7,365,717`, add the `u+3w` comparisons, derive their exact insertion pattern into key fibers, and prove a new finite symbolic correction regime without enumerating `O(H^2)` thresholds. Test overlaps of correction pairs before claiming another disjoint-swap representation.
3. **Reviewer route:** independently check the algebraic sign classification for all `A,B`, the fiber-adjacency argument, the exact 45-term logarithm bounds, and executable source vs run transcript. Keep theorem review independent from author publication.
4. Preserve auxiliary observation (1,4) joint counts and label-3 padding. Treat lawful mother-model encoder/decoder and minimax delta_4 separately.

## Native control and publication

GitHub authenticated account is awdawmip and project branch has author-side research artifacts. The native `em_session_start` and `em_control_tasks` requests `em-research1-20261108T155505-s23-swap` and `em-research1-20261108T155505-tasks` returned `QUEUED` during this run; the session was not reported completed and no active Owner/CLAIM was confirmed. Do not treat a queued session as an active research lease or reproduce any session credential. Reconcile by original request ID rather than repeating a non-idempotent start. All math files are public non-sensitive evidence; credentials are deliberately omitted.
