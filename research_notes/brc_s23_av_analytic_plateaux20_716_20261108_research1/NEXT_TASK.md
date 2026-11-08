# S23/AV exact plateaux 20–716: next research unit

Status: AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE; source link in this directory PROOF.md, VERIFY_PLATEAUX20_716.py, RUN_EVIDENCE.txt. Frozen science is unchanged at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Current verified mathematical frontier

For each i=20..716, the first-entry lower bound and interval-covered endpoint upper bound establish `N(h)=M_i=K_i+V_i-V_(i-1)-1` on `[V_(i-1)+511,V_i+510]`. Last endpoint is `h=272324831`, with `N=1486099146`.

This proof relies on the preceding universally quantified scaled-cell first-entry theorem at `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` and the proven top-510-row lemma at `research_notes/brc_s23_av_analytic_plateaux18_19_20261108_r1/PROOF.md`. Its 697 endpoint checks are exact-rational and finite, fully executed.

## Smallest open unit: repair first cover failure at i=717

The existing v-uniform translated-witness cover first fails at `i=717, v=42217880`, while the previous i<=716 endpoints all pass. This is a *certificate-family* failure, not a proven capacity jump.

Derive a conditional or explicit `j`-localized cover for left threshold points `(v,j)` with `v` in the first uncovered band. Instead of deleting a whole v interval whenever a narrow displacement is geometrically possible, retain its exact 2D incidence constraint: for positive-positive `(dv,dj)`, require `j<=H-v-dv-dj`; for negative-negative require `j>=-dj` and `v>=-dv`. Split that j region from the complement, then search integer-shift witnesses there using the same exact rational interval certificates. Verify all j for this band with interval arithmetic and carry the method to `i>=717`.

Recover one effective witness family with a finite certificate. Distinguish improvement in the chosen cover scheme from a claim about the true minimal N. Maintain the label 1/4 joint-count observer, neutral label-3 padding, exact source pin, and separate mother-model transfer problem.

## Delivery and reproducibility

`python VERIFY_PLATEAUX20_716.py` with assertions enabled produces the exact stdout in `RUN_EVIDENCE.txt` and certificate identifier `4a604c8c6b33a8657646fd026eb58494a9fa69f456ae37774b9d876efcd5f4aa`. The checker uses Python standard library only; it does not enumerate threshold pairs. Any new i=717 certificate should include its own proof of complete integer coverage and actual reproduced output.

The result remains author-side; independent mathematical review, formal Result/CLAIM and Foundation admission were not asserted.
