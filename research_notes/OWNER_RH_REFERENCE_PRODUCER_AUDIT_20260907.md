# Independent audit of the N8 reference producer

Status: **PASS_WITH_DECLARED_TRUST_BOUNDARY / BOUNDED_PRODUCER_AUDIT**.
Date: 2026-09-07. Role: `ANCHOR_EXPOSED` internal owner helper, not a registered
Researcher-ID, official V2 review, new tool family, or RH proof.

**Conclusion.** No blocking mathematical, enclosure, or assembly defect was found
in the frozen producer below. Its current run003 constructs the declared
eta=9/10 reference and binds the actual producer bytes and explicitly trusted
component cache. Exact inspection confirms that run003 has the same matrix
bounds, eta and labels as run002. The callback-budget test returns UNDETERMINED
without bounds, despite a python-flint exception-conversion limitation.

This is an independent source/contract audit with bounded numerical checks. It
does not infer correctness from the producer's ENCLOSED string, rerun the old
eta=1 certificate, recompute all 256 Cauchy integrals, or certify an inertia.
The separate Fraction verifier has authority only over its supplied interval
matrix; this audit addresses the mathematical meaning of those intervals.

## 1. Frozen bytes and actual provenance

Paths in the table are relative to `D:/em/owner-20260907`.

| Artifact | SHA256 |
|---|---|
| `experiments/owner_rh_reference_20260907/reference_builder.py` | `67a15aaebe4a27b59dd29b1e833da456e85581705eb601eeba712818c37f92ca` |
| `experiments/owner_rh_reference_20260907/reference_bounds_run001.json` | `99dc6f7824c09e1018d2e5cbf1bb91eb8ae2235c7f5a59bd87c71c09e8bb9a2f` |
| `experiments/owner_rh_reference_20260907/reference_bounds_run002.json` | `4f72786fd9ef23a8176cda3bdec3e2412d10d3d69b9cbab055c7fed0faeb6e67` |
| `experiments/owner_rh_reference_20260907/reference_bounds_run003.json` | `385ea5b8806f302b6bf403842a0ae496233f67227841c8e5c320ff82f5e9453a` |
| `experiments/owner_rh_reference_20260907/reference_components_run001.json` | `6769025e9448c1c0c57c4b3653f902f9486c34f2e963eaa4633968afcc91260e` |
| `scripts/rh_log3_n8_arb_certificate.py` | `4e337855d8605125ded80c029022fdc950d1b92cf78ce772480a7b99b9dad49b` |
| `research_notes/OWNER_RH_REFERENCE_REUSE_AUDIT_20260907.md` | `719d2803f75de2e0c3c63afbe4207438b96d25e2ce2f31d7368ebbabbbb7d97d` |
| `research_notes/OWNER_RH_FINITE_CERTIFICATE_INTAKE_20260907.md` | `0bde55d47149d04a9c34d049bc9e9473604d16ac554d1f47e6ef2b467dc42b66` |

The producer hash was checked before and after the local tests. No producer,
inertia-checker, historical evidence, or frozen source was modified by this audit.

run001 saved its diagonal/prime components before its tiny-radius rational-text
export hit Python's integer-string digit limit. Its final payload is
UNDETERMINED, with no bounds; eight completed cross entries are not a matrix
certificate. run002 successfully enclosed the matrix after the export change,
but its JSON predates producer-source and explicit trusted-cache binding.
Consequently this audit does not retroactively claim that run002 captured the
current source hash. The producer's documented reconstructed run002 snapshot is
historical reconstruction, not a contemporaneously recorded execution hash.

run003 independently inspected here records the frozen producer SHA above and
both the actual and explicit trusted cache SHA `6769025e...`. Its eta, dimension,
labels and entire bounds array equal run002 exactly as parsed JSON values.
The cache also matches its declared K256/P10/384-bit parameters, inherited-source
hash, schema and complete labels. Supplying no trusted SHA or an incorrect SHA
is rejected before any integration callback.

An explicitly trusted content hash authenticates an already accepted artifact;
it does not prove arbitrary cached numbers are mathematical enclosures. This
legacy cache does not itself record its creator's producer SHA. Acceptance here
uses the recorded run history, audited component construction, current hash
binding, and bounded recomputation below. This audit did not freshly recompute
all cached entries. A caller must not take a hash supplied by an untrusted cache
and silently promote it to the external trusted-hash argument.

## 2. Target, labels and complete component accounting

The target is exactly

`H = [[81 A/100, B_prime+C], [(B_prime+C)^T, D]]`.

The declared order is O- modes 1..8, O+ modes 1..8, S- modes 1..8, S+ modes
1..8. Supports are respectively `[-log2,0]`, `[0,log2]`, `[-log3,-log2]`,
`[log2,log3]`, with normalized Dirichlet sines and zero extension. Filtering
the inherited S-, O-, O+, S+ list gives the exact old/shell permutation
`[8..23, 0..7, 24..31]`. No support, sign, mode, or parity label is merged.

The fresh component path adds `arch_partial + accelerated_tail + pole_matrix`
on each complete 16-dimensional old/shell group, and then adds its corresponding
prime block. Thus A and D include cross-branch terms within their groups,
the regular archimedean terms, and both pole channels. The pole expression is
`l_plus l_minus^T + l_minus l_plus^T`. Prime shifts use exact Fraction support
selectors and all prime powers `{2,3,4,5,7,8,9}`; q=9 has only endpoint contact
and contributes zero overlap. Restricting the inherited routines to these
groups does not change any retained matrix entry.

The old/shell cross is built separately as `B_prime+C`. It deletes the entire
pole cross and the entire regular arch cross `B_arch-C`. It does not accidentally
reuse the complete Weil cross, delete only a high-degree regular remainder,
or restrict C to touching pairs. Each of the four branch pairs O-/S-, O-/S+,
O+/S-, O+/S+ has 64 entries. Only A is multiplied by eta squared; neither
the cross nor D is multiplied by eta.

Each exact target is real and symmetric. `_mirror_upper` copies one valid
enclosing triangle, including its radii. It does not average midpoints or discard
uncertainty. For B the lower block is explicitly its transpose.

## 3. Arch tail and its parameter gate

The preceding reuse audit supplies the detailed derivation; the actual inherited
functions were re-read for this audit. The normalized basis gives the exact
leading Laplace coefficient I, so omitting the cancelled `c^-1` coefficient
before Hurwitz-zeta summation is valid. The prefix includes h0 I and n=0..K-1;
the accelerated tail covers n>=K with `c_n=2n+1/2`, including algebraic
remainders and every exponentially small nonzero-gap term.

For a product denominator, the shipped remainder uses
`M=abs(alpha)_upper+abs(beta)_upper`, with `rho=(M/c_K)^2`, not a bound based
only on the larger individual frequency. `_check_tail_domain` actually checks
`1-rho>0` for every ordered pair of the full basis. It also rejects non-integer
K/P, booleans, K<80 and P<6. Single-denominator convergence follows from the
product bound. The inherited product remainder factor
`(T+1)/(1-rho)+rho/(1-rho)^2` is the sum of the convolution tail, and all
Hurwitz-zeta powers used after cancellation are greater than one.

The fixed N8 frequencies satisfy `alpha_old<48`, `alpha_shell<80`, using
`pi<4`, `log2>2/3`, `log(3/2)>2/5`. Hence M<160 and K>=80 is a sufficient
mathematical range, while the actual ball gate certifies the implemented upper
endpoints. K256/P10 passes. This is a convergence condition, not a promise of
a sufficiently small final spectral error. Exact touching gaps are retained
algebraically; all other fixed-geometry gaps are positive and support the
exponential geometric tail bound. Every signed remainder is enclosed by a
two-sided ball, not asserted to be PSD.

## 4. Cauchy orientation, analytic callback and tail

The exact support comparisons put S- before either old interval and either old
interval before S+. In particular, passing `(old,S-)` straight to the inherited
one-sided dispatcher would give zero; the current adapter instead calls the
ordered closed form with the correct left interval first.

For ordered supports define
`L_ij(c)=integral_(x<y) phi_i(x) phi_j(y) exp(-c(y-x)) dxdy`. The reference
kernel `-1/(2(y-x))` gives `C_ij=-(1/2) integral_0^infinity L_ij(c) dc`.
At a touching corner the absolute majorant `1/(u+v)` is locally integrable
in two variables. Thus the exchange is justified even for signed sine products.
The source calls `-ordered_distinct_laplace/2` exactly once. Transposing the
finished cross is not a reason to insert another factor two.

The callback expression uses rational operations and exponentials of c with
fixed real ball coefficients. It has no c-dependent branch-cut function.
Ignoring the analytic flag is valid for this meromorphic expression provided
denominator-zero balls return nonfinite values, as they do in the local test.
This matches the official [python-flint acb integration contract](https://python-flint.readthedocs.io/en/latest/acb.html).
The apparent denominator poles can be removable for exact Laplace data; returning
nonfinite on such balls is conservative. Positive-real panels avoid these poles.
Taking the real part of a finite complex enclosure is valid because the exact
integral is real; an imaginary enclosure containing zero is checked as well.

The finite integral uses 16 panels covering [0,20000]. Tolerances are accuracy
goals; a finite wider ball remains an enclosure whose actual radius must be
retained. The closed form has four endpoint exponentials of absolute value at
most one and a denominator at least c^4 for real c>0. Therefore

`|(1/2) integral_(C0)^infinity L_ij(c) dc| <= 2 norm_i norm_j alpha_i alpha_j/(3 C0^3)`.

Using `norm_old norm_shell<4`, `alpha_old<48`, `alpha_shell<80` gives
`10240/C0^3`. At C0=20000 this is exactly `1/781250000`. The producer adds
this as a two-sided radius to every cross entry before combining it with the
prime entry. It includes separated as well as touching pairs. Finite-integration,
arch-tail, arithmetic and export uncertainties remain in the final intervals.
There is no discarded frequency tail and hence no additional beta.

## 5. Directed export and exact matrix inspection

For each finite Arb ball, `lower()` and `upper()` are directed endpoints.
Their exact `man_exp()` data are rounded by integer floor/ceiling to 2^-160.
Arithmetic right shift performs floor even for negative integers; the upper
formula `-((-mantissa)>>n)` performs ceiling. No displayed decimal is parsed.
The official [Arb API](https://python-flint.readthedocs.io/en/latest/arb.html)
provides the endpoint and exact-binary semantics used here.

The claim of extra widening less than 2^-160 refers to the grid-rounding step
relative to those directed endpoints. Directed endpoint extraction and preceding
ball arithmetic also contribute uncertainty, which is captured by the final
interval. Nonfinite export is rejected. At the tested 384-bit precision, exact
checks covered zero, both signs of 1 and 1/3, extremely small ±2^-20000, a
zero-centred tiny-radius ball, and signed nonzero balls with radius 2^-180.
Each final interval contained the directed binary endpoints, with each additional
grid slack less than 2^-160; ±2^-20000 did not collapse to a false exact zero.

Independent Fraction inspection of run002, inherited identically by run003,
checked all 1024 ordered matrix entries for shape, ordered endpoints, exact
symmetry and the dyadic grid. It checked diagonal-block scaling against the
cached intervals and every cross prime-plus-Cauchy diagnostic interval against
the final cross interval. No diagnostic-sum shortfall was found. All 256 distinct
cross index pairs, physical orientations, tail values, 16-panel records and
the total 174828 callback count agreed. The exact maximum row-radius sum is

`2024912878742577611153949018957860044801 / 91343852333181432387730302044767688728495783936`,

approximately `2.2168025838855614e-8`. It was recomputed from the exported
intervals, not accepted from the metadata. This two-sided bound includes all
entry errors; separate tail estimates must not be added again.

## 6. Actual bounded execution and failure boundary

Execution used Python 3.12.14 at
`C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`,
with python-flint 0.9.0 from
`C:/Users/Administrator/AppData/Local/Temp/em-owner-flint-py312` and 384 bits.
Imports disabled bytecode writes.

The following are actual checks, not producer self-reports:

- Exact export, nonfinite rejection, invalid-K rejection, and the actual
  K256/P10 product-domain gate passed.
- A complex ball containing an ordered-Laplace denominator pole returned
  nonfinite rather than a falsely analytic finite result.
- One complete O- k1 / S- k1 Cauchy entry used 1309 callbacks, was finite and
  strictly negative, correctly sorted S- then O-, and included the exact tail.
- Two 2x2 component groups, with indices `{0,8}` in each of A and D, were
  freshly recomputed at K256/P10 using prefix, tail, both pole channels and
  prime terms. All eight directed result intervals were contained in the
  corresponding cached intervals. Two prime cross entries `(0,0)` and `(0,8)`
  were also recomputed and contained. This is a cache-consistency sample;
  mathematical justification comes from the formula audit, not sampling alone.
- The top-level budget test used cutoff=2, entry_eval_limit=1 and the trusted
  cache. It returned UNDETERMINED, zero completed cross entries, 12 callbacks,
  and **no bounds**. Missing and incorrect trusted cache hashes were rejected
  with zero callbacks. These final bounded test batches exited successfully.
- run003 source/cache binding and exact equality of eta, dimension, labels and
  bounds with run002 passed; the frozen producer hash remained unchanged.

One implementation limitation was found and communicated immediately: raising
`Undetermined` inside the python-flint C callback can emerge as a `SystemError`
chain. A first direct-entry test expecting only the original exception therefore
terminated with SystemError. The subsequent top-level test verified the actual
boundary: `except Exception` returns UNDETERMINED and removes bounds. The
saved reason was `SystemError: <cyfunction acb.integral ...> returned a result
with an exception set`. This is not clean exception propagation, and the callback
count can exceed the requested limit while the backend unwinds. It did not yield
a finite accepted partial matrix or a false inertia assertion. The producer was
left frozen; no numerical evidence was overwritten to hide this behavior.

The closed work unit is the audited producer for this finite, labelled N8
reference. Its numerical realization uses external real/complex ball analysis;
the branch/mode carrier is not an added physical X6 axis, and algebraic signed
entries are not relabelled as positive BRC branch masses. Neither this audit nor
ENCLOSED establishes an inertia by itself, a full Weil-cross result, a Galerkin
complement estimate, an infinite-operator statement, or RH.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
