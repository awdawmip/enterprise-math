# D25/LIFT — sharp finite-precision repair for the source-labeled two-group Frobenius observer

2026-10-25 | TASK_RESEARCH portable author-side proof | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT** | shared-context, nonblind. This note is a neutral mathematical consequence of an inherited exact source identity; it neither assumes nor acquires the present Source Task owner role.

**Parent:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source:** `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged). Inherited exact factorization: `research_notes/portable_direct/20261025_offphase_d25_even_harmonic_p8_seam.md` and `20261025_offphase_d25_source_factor_jet_all_precision.md` on Enterprise Math main. Neither the original WZ identity, its factorial components, nor any earlier numerical seam digit is recredited here.

## Observation interface and carrier

Let `p=6m+1>=13` be prime. Write `Z_p` for the p-adic integers. The previously established original-source grouping is

```text
Q_p(p) = T^2 (R^2 A + L),      H = A + L,
T = prod_{j=1}^{p-1}(1+p/j) = binom(2p-1,p-1),
R = (1-p)^2/(1-2p),
A = A_p(p) = old-edge p-integral amplitude,
L = L_p(p) = sum of the four labeled genuine-tail amplitudes.
```

All factors are p-integral. This note considers the **two-group** carrier `(A,L)`, not an illicit identification of its four individual genuine tails. To audit a quotient rigorously, first extend the same fixed source-derived *linear observer* to arbitrary test amplitudes `(a,l) in Z_p^2`, without asserting those counterfactual pairs themselves arise from original factorial sums:

```text
h(a,l)=a+l;     q(a,l)=T^2 (R^2 a+l).
```

Set `tau=T^2` and `alpha=tau*(R^2-1)`. Then exactly

```text
q = tau*h + alpha*a.
```

## Theorem — exact sharp repair budget at every precision

The coefficient of the discarded old-edge coordinate has **exact p-valuation two**, uniformly in the indicated prime class:

```text
alpha = p^2 * T^2 * (p^2-4p+2)/(1-2p)^2,       v_p(alpha)=2.      (1)
```

For every integer `D>=1`, put `e=max(D-2,0)`. For *any two* amplitudes `(a,l),(a',l') in Z_p^2` with `h(a,l)=h(a',l') (mod p^D)`, the following are equivalent:

```text
q(a,l) = q(a',l') (mod p^D)
    if and only if
a = a' (mod p^e).                                            (2)
```

Consequently the exactly sufficient restoration interface for the scalar target `q mod p^D` is

```text
(h mod p^D, a mod p^e)   ->   q mod p^D,                     (3)
q = tau*h + alpha*a  (mod p^D).
```

This repair is **sharp on the unrestricted two-group p-adic carrier**: when `D>=3`, a fixed `h mod p^D` has precisely `p^(D-2)` distinct possible values of `q mod p^D`, realized by varying `a mod p^(D-2)` and taking `l=h-a`. Any exact encoding that retains `h` and distinguishes every possible future `q mod p^D` therefore needs at least `p^(D-2)` states (equivalently, `D-2` base-p digits) of additional information. At `D<=2`, no additional digit is needed. This lower bound concerns the specified freely variable two-group source carrier and single observation `q`; it is **not** a minimality claim about the much smaller actual factorial family or about preservation of all downstream port-sensitive operations.

### Proof

Algebraically,

```text
R^2-1 = ((1-p)^4-(1-2p)^2)/(1-2p)^2
      = p^2*(p^2-4p+2)/(1-2p)^2.
```

Both `T` and `1-2p` are p-units, and `p^2-4p+2 = 2 (mod p)` is a p-unit for every permitted odd p. This proves (1). For the two test pairs, the exact linear identity gives

```text
Delta q = tau * Delta h + alpha * Delta a.
```

If `Delta h` is divisible by `p^D`, the first term vanishes modulo `p^D`. Since `v_p(alpha)=2`, the second vanishes precisely when `p^e` divides `Delta a` (with the condition vacuous for `D<=2`). This proves (2), hence (3). Fixing any `h` and letting `a` run over residues modulo `p^e` while `l=h-a` proves both surjectivity onto the `p^e` distinct values and the exact lower bound. QED.

## Relation to inherited third-digit and eighth-digit results

The two pairs `(a,l)=(0,0)` and `(1,-1)` have identical `h=0` but distinct `q` modulo `p^3`; their exact difference is `alpha = 2p^2 (mod p^3)`. Thus the first precision at which the discarded two-group coordinate can affect this scalar observation is **p-cubed**, and this boundary is forced by the exact source factors, not inferred from finite examples.

For the *actual original factorial family*, `A_p(p) = 2m*C(p)*K_U(p)` with `C(0)=-2` and `K_U(0)=1`, hence `A_p(p)=-4m=2/3 (mod p)`. Also `T=1 (mod p^3)`: the exact even-harmonic product `T=prod_{j=1}^{p-1}(1-p^2/j^2)` and `sum_{j=1}^{p-1}1/j^2=0 (mod p)` suffice. Substitution recovers, without recrediting it, the established third-digit correction:

```text
Q_p(p)-H_p(p) = (4/3)*p^2 (mod p^3).
```

At eighth-digit precision `D=8`, theorem (3) identifies `A mod p^6` as the **exact** old-group repair budget for the two-group scalar observer, consistent with but not a rerun of the already-published degree-five old-edge jet. It explains why higher-order source-scalar computations must carry that coordinate; it does not compute a new WZ numerical digit.

**Exact reproducible spot certificates:** from `T=binom(2p-1,p-1)` and (1), one obtains `alpha = 2p^2+4p^3 (mod p^4)`; thus `alpha mod p^4` equals `9126` for `p=13`, `28158` for `p=19`, `121086` for `p=31`, and `205350` for `p=37`. These are illustrative exact integer residues, not the proof of the universal statement. All divisions in (1) are by p-units.

## Typed observer / BRC boundary and continuation

**BRC applicability:** `COMPOSE_APPLIED` to the labeled old-group/genuine-tail-group p-adic module and its exact observation map. The discarded information is classified as a two-group p-adic repair residue, *not* as positive branch mass, cancellation of unequal signed source ports, a native Enterprise-coordinate state, or an established CM/DP transfer. The theorem proves sufficiency only for the declared `q mod p^D` observation; four individual genuine-tail labels must still be retained for operations that inspect them separately.

**New contribution:** equations (1)–(3), the sharp all-D fiber/equivalence classification and optimal restoration cardinality, together with the exact connection to the inherited p^3 correction. **Inherited, not completed here:** original five-port identity, p^8 seam, Source claim/checkpoint, native same-prime original-class H0/B0/CM/DP representatives, `[X]U mod p^2` and semilinear correspondence. The mother's D25/LIFT target remains OPEN. No existing owner's CLAIM/run or reviewer identity is adopted.

**UR V2 provenance debt:** the authentic four-file 94,687-byte bundle with SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remains unverified, not reconstructed by this note. Native writer/provenance, exact Source continuation, checkpoint and independent review remain pending. The current Site-scoped `static_machine_readonly` gateway grants no native research execution mutation. Next authorized Source action is receipt/recovery/continuation verification for this actual session, not a fabricated predecessor CLAIM; next core mathematical requirement remains an authentic same-prime, same-original-class CM/DP representative and the mapped second-digit certificate.
