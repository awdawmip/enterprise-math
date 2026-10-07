# Shared-context adversarial check of incidence regularity

Date: 2026-10-07.
Task: `RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007` / `TP2-E49C20B8D0A6569355F6`.
Researcher context: `EM-DIRECT-FA0C27`; temporary collaborator: `/root/backend_route_audit`.
Disclosure: **NOT_INDEPENDENT; NONBLIND_DISCLOSED**. This is a shared-context proof check, not an independent formal review, scientific admission, or a new research identity/claim.

## Result and exact scope

No mathematical error was found in the stated conditional equivalence, identities (1)–(3), the source-labelled two-edge formula (4), or the displayed five-triple example. The equivalence needs precisely the fixed coherent incidence and uniform incident-edge choice stated in the note. It does not establish native triad legality or an occupancy successor.

Reviewed `INCIDENCE_REGULARITY.md`, SHA256 `0991c6469f69d0e99abb32d29b2a2acc8105aeee7643de299feb1fdd8e91d0e6`, lines 1–67. Exact implementation checks used local frozen `source/packet_router.py` (SHA256 `2e1beb9c510cd8235633e33f41d3e3d93ce20665b9d72847d6a13b1d15cda582`) and `source/README.md`, sections 1–2 (file SHA256 `5cbddab25ab9aa6f21359a1eecfcd6ac42ce6cc84fe29a5c686ac0c3e3a4f101`). The source revision cited by the note is `fe9ce58293ac77b72092512620e8670ca9be2d78`; this check does not perform a new remote provenance fetch.

Before checking, loaded project P000, `HEARTBEAT_WORLD_NATIVE_X6_TIME`, `JOINT_RELATION_OBSERVER_PRESERVATION`, the mandatory residual-fidelity companion, local `WORLDVIEW.md`, `BRC_POLICY.md`, `BRC_ONLY.md`, and this task's `TASKBOOK.md`. The mathematical work below is a symbolic audit of the declared positive-BRC branch laws, not a replacement numerical propagation run. No control-plane state was changed.

## Proof steps checked

1. **Incidence and weights.** Every port has `d(p)>0`, so each denominator is defined. Three distinct axes imply three distinct ports and exclude both `p` and `-p` from one triple. For incoming `p`, each triple containing `p,q` contributes the serial response share `1/(3 d(p))`. This gives (1). Counting each incident triple's three legs gives column sum one; its unique anchored leg gives `K(p,p)=1/3`; the opposite-port entry is zero. These are total-response statements, not conservation of the refined CWM branch count.

2. **Reciprocity and stationarity.** Coherence supplies one common incidence set, hence `n(p,q)=n(q,p)`. Multiplying a column by `d(p)` gives `n(p,q)/3`. Summing over `p` counts each triple through `q` exactly three times, giving `d(q)`. The stationary object in (2) is an unnormalized positive weight vector; no probability or primitive-force interpretation is required.

3. **Uniform-input readout.** An input of `1/12` on every incoming port gives output `r(q)/12`. Thus list statements 1 and 2 are equivalent without any assumption about connectedness.

4. **Component regularity is sufficient.** Every port in a triple incident to `q` lies in the same incidence component as `q`. If its common degree is `d_C`, the sum before the outer factor `1/3` is `d_C * 3/d_C`. The row sum is one. Degrees of other components never enter; requiring one degree globally would be too strong.

5. **Component regularity is necessary.** The row equation is `sum_(h contains q) sum_(p in h) x(p)=3`, for `x(p)=1/d(p)`. Dividing by `3 d(q)` gives (3), whose left side is indeed `x(q)`. There are exactly `3 d(q)` terms with positive equal weights and their weights sum to one. At a maximum of `x` in a finite component, equality of the average forces equality at every co-incident port. Each such port is itself a maximum, so the same argument propagates along every finite connecting chain. No irreducibility beyond the defined component, global connectedness, or limiting argument is missing.

6. **Return-port convention.** The frozen router advances along `q` and stores next incoming as `q ^ 1`, i.e. `-q` (`packet_router.py:203–208`). A primitive two-edge return must then leave the neighboring Cell along `-q`. The relevant neighbor entry is consequently `K_neighbor(-q,-q)`, not `K_neighbor(-q,q)`. The use of the anchored diagonal `1/3` in the note is correct.

7. **Two-edge identity.** Equal injection followed by attenuation `rho=12 lambda` emits `lambda r_a(q)`. For `q` outside the occupied-neighbor set `B`, its return contribution is `lambda^2 r_a(q)`; for `q` in `B`, it is `4 lambda^2 r_a(q)`. Column conservation gives `sum_q r_a(q)=12`; summing these contributions is exactly (4). The fixed X6 adjacency admits no other two-primitive-edge return. The coefficient is the depth-two arrival readout before any additional operation at `a`. The neighbor may use a different conservative anchored kernel; its off-diagonal values do not enter this coefficient.

8. **Quantifiers and endpoints.** For one fixed `B`, subtracting the two formulae gives `3 lambda^2 (sum_B r_a-|B|)`. Since `lambda>0`, the stated iff follows. With one kernel fixed while `B` varies over all subsets, singleton sets force each row to be one. For the adjacent labelled pair, the two individual conditions are exactly `r_A(+1)=1` and `r_B(-1)=1`. At `lambda=0` the iff would fail, but that endpoint is explicitly excluded. The upper bound `lambda<1/12` is needed for the all-depth reuse; the finite two-edge algebra itself does not require that upper bound.

9. **Five-triple witness.** In the positive component the reciprocal-degree sums contributed by `{+1,+2,+3}`, `{+4,+5,+6}`, and `{+1,+4,+5}` are respectively `5/2`, `2`, and `3/2`. Dividing the appropriate incident sums by three gives `(4/3,5/6,5/6,7/6,7/6,2/3)`. Each negative component consists of a single triple and has row sum one. Substitution into (4) gives `16/48^2=1/144` at the first site and `15/48^2=5/768` at the second. This is a syntactic-circuit counterexample to transferring the old formula, not a lawful-native-completion witness.

10. **Covariance and all-depth boundary.** Invariance of a fixed kernel under a transitive signed-port permutation action makes all its row sums equal; column conservation then fixes the common row sum at one. Such invariance is an extra circuit hypothesis. Separately, fixed positive propagation with every column total `rho<1` gives layer total `N rho^ell` and the geometric omitted-mass bound. Row uniformity is unnecessary for that proof. The note correctly excludes automatic transfer to storage, reaction, or changing occupancy.

## Recommended wording safeguards

These are clarifications, not blocking proof defects.

- **Title / definition of isotropy:** say “uniform-injection isotropic emission.” The theorem preserves the equal twelve-channel input; it does not assert an isotropic output for every input. A pure-port input has diagonal share `1/3`, already different from `1/12`.
- **All orientations:** explicitly keep the same kernel in the same labelled port frame while varying the pair direction, and require both source-labelled coefficients individually. If only the sum of the pair's two coefficients is observed, the condition for direction `q` is merely `r(q)+r(-q)=2`; that is a different, weaker observer condition. Rotating or refitting the kernel together with each tested preparation is also a different quantifier.
- **“Any anchored equal-three-leg kernel”:** append “conservative, at the same attenuation, with no intervening gate/storage operation.” Those hypotheses are inherited from the frozen circuit, but stating them adjacent to (4) prevents accidental transfer to a lossy or history-dependent material law.
- **Stationarity scope:** (2) concerns the local incoming-to-outgoing port kernel before spatial travel and incoming-port reversal. It does not assert a stationary material configuration or a global field stationary state.
- **Multiplicity boundary:** excluding repeated hyperedges is safe. It is a conservative scope restriction, not a proved obstruction to analogous multiplicity-weighted statements. Such an extension is not needed for this task.

## Evidence limits

This collaborator did not inspect or execute `incidence_check.py`, validate its operation counts, or independently replay `incidence_check.json`; those runtime claims remain outside this check. The displayed finite values above were checked symbolically from the stated branch-weight formula, and are not presented as a separate BRC execution. Joint packet labels remain required for future joint valves; the unary row-sum audit supplies no new license to discard them. No native incidence, indivisible-action realization, material motion, full heartbeat, or parent-objective completion is certified here.

## Final wording revision checked — 2026-10-07

Re-read the final `INCIDENCE_REGULARITY.md`, SHA256 `2a6e31b0c3fb4ea4777237d4dbf3a0da2b2e0905104b1edbc72027e109e966f1`, only to check the requested wording revisions. The initial reviewed SHA and recommendations above are retained as history.

The revised title uses “equal-channel emission,” with the theorem's first condition explicitly specifying equal input. The all-orientations statement fixes one coherent H at both materials and requires each source-labelled coefficient separately; its aggregate alternative correctly states `r(q)+r(-q)=2`. The two-edge paragraph now explicitly requires the same attenuation, conservative anchored equal-three-leg scattering, and no intervening gate or storage delay. The stationarity paragraph explicitly limits (2) to the local port kernel before spatial travel and incoming-port reversal. These revisions correctly address the requested scope safeguards and introduce no mathematical defect found in this limited recheck.

Status remains **NOT_INDEPENDENT; NONBLIND_DISCLOSED**. This addendum does not extend the original proof-check scope or validate the runtime evidence.
