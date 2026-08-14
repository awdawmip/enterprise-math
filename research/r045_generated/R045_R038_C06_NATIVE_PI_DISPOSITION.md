# R045 — R038-C06 native-pi disposition

Status: `THEOREM_LEVEL_N0_SCOPE_RESOLVED / NOT_CANONICAL`

Researcher-ID: `EM-R045-812A`  
Task: `RS-R045-HISTORICAL-NATIVE-SEMANTICS-RETYPE-R038-N0-REPAIR`  
Task source: `d164ffea25203ff61d6901cf91be5583c93bcb9e`  
Active gate: `ENTERPRISE_MATH_NATIVE_SEMANTICS_ADMISSIBILITY_V2 @ a70c56e5c43772903a74d258ab237825c6045a8c`

## 1. Historical defect

R038 correctly exhibited several incompatible `pi_eff` readouts. What does **not** follow is the metric-free N0 theorem:

`NO_UNIQUE_NATIVE_PI_WITHOUT_READOUT_SEMANTICS`.

Different N2/N3 readouts refute uniqueness **inside that declared readout family**; they do not quantify over, and therefore cannot exclude, every possible N0-definable object.

## 2. Type a candidate before asking whether it exists

A usable native-pi candidate class would need at least a triple `(S,F,R_pi)`:

1. `S`: a declared scalar/object codomain;
2. `F`: an N0-only construction into `S`, with complete transitive dependency closure, independence from non-N0 choices, relabeling/isomorphism invariance or canonical equivariance, and uniqueness/reconstruction at the same promoted semantic strength;
3. `R_pi`: a declared role predicate/structure saying what makes the output a **pi** candidate rather than merely an arbitrary invariant scalar/object.

The bare R038 N0 signature declares none of these scalar/role interfaces.

Therefore the candidate class itself is not currently a well-formed N0 type.

## 3. Exact dispositions

### EXISTENCE

`NOT_WELL_TYPED_BARE_N0`.

This is stronger than “we did not find one” but weaker than nonexistence: the quantifier domain of native-pi candidates has not been declared.

### UNIQUENESS

`NOT_WELL_TYPED_BARE_N0`.

Uniqueness cannot be asserted or denied before the candidate class is formed.

### ROLE

`ADDITIONAL_ROLE_LANGUAGE_REQUIRED`.

Classical roles such as circumference/diameter, area/radius, equal-volume calibration, Gaussian normalization, zeta special value, or Fourier normalization are not present in metric-free relational N0 merely because they are standard mathematics.

### NONEXISTENCE

`NOT_PROVED`.

To prove nonexistence one would have to exhaust a precisely declared candidate class. R038's multiple post-hoc readouts do not do that, and “none found” does not do that.

## 4. What survives unchanged

The historical readout theorem survives:

> In the explicit R038 family of graph-radius, broken-bond, embedding-volume/hull, inradius, RMS and equal-volume Euclidean calibrations, the resulting `pi_eff` values are not unique.

Typing:

- those scalarizations/quotients are `N2`;
- continuum/Euclidean calibrations are `N3` where applicable;
- no metric-free N0 nonexistence consequence follows.

## 5. Strongest legal N0 conclusion

`NATIVE_PI_NOT_WELL_TYPED_AT_N0`.

If a future task first declares an N0-compatible candidate codomain, construction language and pi-role, then existence/uniqueness/nonexistence becomes:

`OPEN_AFTER_EXACT_SCOPE`.

This repair does not redefine classical pi and does not use root, distance, equidistance, radius, embedding or other N1/N2 objects to attack N0.
