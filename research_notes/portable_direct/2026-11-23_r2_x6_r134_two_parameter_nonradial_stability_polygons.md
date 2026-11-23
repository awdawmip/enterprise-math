# X6 R134 — exact two-parameter non-radial stability polygons in two Port-10 eight-direction chambers

Date: 2026-11-23. Status: **AUTHOR EXACT FINITE CERTIFICATE / LOCAL PYTHON FRACTION REPLAY PASS / NOT INDEPENDENTLY REVIEWED**.

## Frozen mathematical model and scope

This is the **conditional four-positive-weight, six-pair BRC observer on a selected three-coordinate slice**. It is **not** a theorem about native six-axis X6 time evolution or a revision of P000. Use the R121 frozen integer Port-10 input and R122 frozen six-gap exclusion:
- R121: `enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`
- R122: `enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`
- R132: `enterprise-math@e297bc1c4f414223f2be0f569d1783d0e30e9711:research_notes/portable_direct/2026-11-23_r2_x6_r132_sharp_two_centered_relative_boxes.md`
- R133: `enterprise-math@12bb5f161a15fb0fe29ce5f5ed8709a359fa3fc9:research_notes/portable_direct/2026-11-23_r2_x6_r133_all_orthant_first_exit_rays.md`

For nonzero signed integer triples `a=(x,y,z)` modulo **sign alone** (positive multiples remain distinct), set `q(a)=max(sum max(a_i,0),sum max(-a_i,0))`, `h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`, and retain **all six** `g_ij(a)=|h_i-h_j|` and `s_ij=w_i+w_j`. Define `F_w(a)=max_(i<j) g_ij(a)/s_ij`, `eta_10(w)=min_(0<q(a)<=10)F_w(a)`, and `N_10(w)={a mod sign:0<q(a)<=10, 2F_w(a)<3eta_10(w)}`.

The exact 18-row bank B18 from R121 Pareto-covers the 1,935 directions. The exact E20 from R122 contains every possibly strict-near direction, for any positive physical weights.

## Theorem I — complete non-radial (B,D) slice at center (136,8,176,185)

Keep `w=(136,B,176,D)` and restrict to `0<B<=20, 150<=D<=220`. Throughout this full rectangle,
`eta_10(w)=3/(136+B)`, and **no** direction outside the original eight-direction center set can become strict-near. The exact original set is

`N_I={(1,0,0),(1,3,-1),(4,-4,1),(5,-4,1),(5,-1,0),(6,-1,0),(7,-1,0),(9,-5,1)}`.

The necessary **and sufficient** conditions for `N_10(w)=N_I` are simultaneously

```text
B < 20,
3D > B+544,
9D > 20B+1496.
```

The three inequalities define three nonredundant strict facets *inside the declared rectangle*. Their load-bearing witnesses are, respectively, `(1,3,-1)` observed on pair 02, `(1,0,0)` on pair 13 and `(7,-1,0)` on pair 03. At equality the listed original member ceases to be **strictly** near. The closure polygon of this exact stability region has the five `(B,D)` vertices

`(0,544/3),(0,220),(8,184),(20,632/3),(20,220)`.

The `B=0` vertices describe only the closure; physical weights require `B>0`.

## Theorem II — complete non-radial (B,D) slice at center (722,465,240,48)

Keep `w=(722,B,240,D)` and restrict to `350<=B<=600, 1<=D<=200`. Throughout this full rectangle, `eta_10(w)=3/(240+D)`; no direction outside the original eight-direction center set becomes strict-near. That exact set is

`N_{II}={(1,0,0),(3,-4,1),(3,3,-1),(4,-4,1),(6,-1,0),(7,-8,2),(7,-1,0),(9,-5,1)}`.

Necessary and sufficient conditions for `N_10(w)=N_{II}` are

```text
5D < 243,
20D < 9B-2640.
```

The two nonredundant strict facets are witnessed by `(3,3,-1)` on pair 02, and `(7,-8,2)` on pair 12, respectively. The exact closure polygon has `(B,D)` vertices

`(350,1),(350,51/2),(1204/3,243/5),(600,1),(600,243/5)`.

These are **two-parameter** classifications (not samples of radial rays), with all real `B,D` in the stated rectangles and all equality boundaries assigned by the strict `<3/2` rule. They do **not** assert full global four-dimensional chamber classification.

## Proof: 18/20 finite reductions and affine polygon certificate

Let `k=01` in Theorem I and `k=23` in Theorem II. Set `b*=(6,-1,0)` whose `g` has a 3 in each respective anchor pair. At all four rectangle corners the following fixed-index inequalities hold: for **each** `b in B18`, one and the same pair `j(b)` satisfies `g_j(b)s_k>=3s_j` on all four corners; for `b*` all six inequalities `g_j(b*)s_k<=3s_j` hold on all corners. Affinity in the physical weights extends these to the whole rectangle, proving `eta_10=3/s_k`.

For each of the 12 candidates `a in E20\N_center`, one fixed pair `j(a)` satisfies `2g_j(a)s_k>=9s_j` at all four corners, hence throughout the rectangle; these candidates never enter. The other 1,915 directions were already globally excluded by the exact R122 certificate.

For each of the eight center members and each of six pair indices, strict nearness now reduces to the **affine** inequality `L_{a,j}(B,D)=9s_j(B,D)-2g_j(a)s_k(B,D)>0`. The three/five stated strict facets are among these 48 tests, up to a positive constant factor. Their closed intersection with each rectangle gives exactly the listed five vertices. Check all 48 affine inequalities at **every** one of those vertices: each is nonnegative, and any zero face lies inside one of the stated strict facet faces. Thus strict positivity of the stated facets forces strict positivity of all 48 comparisons. Conversely, each stated facet is itself a required comparison, so failure removes at least one center member. This proves the claimed if-and-only-if conditions over the full continuous two-parameter rectangles. No approximation, independence assumption between pair capacities or finite-sampling extrapolation is involved.

For transparent exact reproducibility, `research_notes/portable_direct/x6_r134_two_parameter_stability_verify.py` independently reconstructs the 1,935 signed-triplet representatives, checks B18 domination, regenerates E20, verifies all fixed corner witnesses, exactly intersects the rational halfspaces, checks the 48 inequalities and zero-face containment, and checks each facet's explicit witness. Standard-library `fractions.Fraction` arithmetic is used throughout.

## Actual verification and next question

Author-local replay on 2026-11-23:

```text
CENTER_I PASS population 1935 bank 18 envelope 20 near 8 vertices 5 facet_planes 3 vanishing_comparisons 9
CENTER_II PASS population 1935 bank 18 envelope 20 near 8 vertices 5 facet_planes 2 vanishing_comparisons 3
R134 TWO-PARAMETER EXACT NONRADIAL CHAMBER CERTIFICATE PASS
```

This is an **exact conditional finite proof with a reproducible checker**, pending independent mathematical review and any project Result/Review admission. Native X6/P000 spatial, time, source-firewall and shared task authority remain unchanged.

Next: enlarge the two-dimensional rectangles across anchor-switch boundaries, or classify non-radial facets in full positive **projective** four-weight space, tracking optimizer changes and possible entrant directions without treating the six pair capacities as independent.
