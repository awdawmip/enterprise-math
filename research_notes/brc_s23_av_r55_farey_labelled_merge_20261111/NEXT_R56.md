# R56 — grouped cut transitions and provenance-safe future-observer compression

Source: R55 author-side proof, self-contained `VERIFY_R55_PUBLISHED.py`, 594 exact merge tests and full 78-stage/298-run frozen S23 compilation. Scientific input remains the unchanged pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

**Question 1 (grouped phase updates).** For `m,H` and requested `k`, can Farey-step runs be grouped into a finite arithmetic-progressions/piecewise-affine event structure which updates the *entire labelled* youngest-source vector, instead of materializing all `K` cuts? Give the exact group action, applicable range, and a proof that every `z+r=s` crossing yields the identical history-owner age vector as R52/R53.

**Question 2 (gap-spanning source ranges).** R55's generic circular-merge cost depends on `K=max(m-1,j-1)-min(0,j-H)`. For `|j|≫m+H`, design a two-interval circular merge over only the historical and source index blocks, avoiding the intervening empty integer region. Verify against direct exact rational sorting including negative indices.

**Question 3 (observer lease).** Specify the future operations: stage-risk queries, threshold counts and optional later-source updates. Prove when a compressed state retains exactly the original labelled observer values; find a concrete finite counterexample for any overly coarse compression. Compare honest total bit costs (precision, Farey bracket, grouped events, labels, output) against R49/R51/R53/R55.

Expected acceptance: an actual scoped theorem/counterexample with proof or exact finite test, not task-wide formal claim/promotion. No native X6 dynamics inferred from auxiliary rotation.
