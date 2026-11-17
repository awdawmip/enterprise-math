# X6 Unit107 — exact named-axis BRC repair and coordinate-subset lower bound

**2026-11-18 · RS-X6-LEGACY-PLANE-RECONCILIATION · TP2-B4A441B23DA3159232C2**

Status: **AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Immutable model and observed source

P000 V5 signed Cell torsor is frozen at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; comparison input at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Exact source interfaces:

- `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` at the P000 pin, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`: `shortest_path_multiplicity(z)` uses the signed six-axis factorial law.
- `research_checks/P000_SIX_AXIS_JOHNSON_TROPICAL_ARITHMETIC_INTEGRATION_CHECK_20260830.py` at the historical pin, blob `62ea223dcbbb118186513737243ead040b77adc0`, lines 10–13 and 82–87: three complementary pairs, parity/mod-3 `rho_J`, sorted product orbit `q_orbit`.
- Unit106's verified Johnson packet `P(z)=(rho_J(z),q_orbit(z),L1(z),L_E²(z),F(z))` with `F(z)=∏|z_i|!` retains current shortest-path count but cannot alone compute every named next count.

This unit supplies an **exact operation-aware repair criterion**, directly using the native BRC law; no original R063/Helly benchmark was rerun.

## Theorem A — exact one-step formula

For `z∈Z^6`, `L=Σ|z_j|`, `B=L!/∏|z_j|!`, and a named primitive signed operation `T_i^ε z=z+εe_i`, `ε∈{-1,+1}`, let `a=|z_i|`. Then

```text
If |z_i+ε|=a+1:  B(T_i^ε z) = B(z) * (L+1)/(a+1).
If |z_i+ε|=a-1:  B(T_i^ε z) = B(z) * a/L.
```

The second case occurs only when `a≥1` and `L≥1`. Each quotient is exactly an integer. Proof: all other factorial denominators are unchanged, while the chosen axis factorial is multiplied by `a+1` or divided by `a`; the total numerator changes from `L!` to `(L±1)!`. The displayed quotients follow by cancellation.

**Operational consequence:** for one specified named signed step, exact `(L,B,z_i,ε)` suffices to calculate the next **scalar** N-BRC shortest-path multiplicity without consulting the other five coordinates. This is an operation-scoped query interface, not a claim about retaining path-word provenance or sequential arbitrary-axis updates.

## Theorem B — no proper *raw-coordinate subset* repairs the whole Johnson packet over Z⁶

Fix any proper subset `S⊊{0,…,5}`. The observation `(P(z),(z_i)_{i∈S})` does not determine all twelve next shortest-path multiplicities `B(T_j^ε z)` on `Z^6`.

**Constructive proof.** Choose a missing axis `j∉S` and a distinct axis `k` that is not its complementary-pair partner. Such a `k` exists for each of the six axes. Put

```text
x = e_k + 3 e_j,    y = e_k - 3 e_j.
```

All coordinates other than `j` agree. All three complementary products are zero, hence `q_orbit(x)=q_orbit(y)=(0,0,0)`; complementary-difference parity agrees because `3≡-3 mod 2`; the total sums are `4` and `-2`, both `1 mod 3`. Also `L1=4`, `L_E²=10`, `F=3!=6` and `B=4` for both. Therefore the **entire** published packet and the exposed coordinates in `S` coincide.

After the same `+e_j` operation, the two next absolute-coordinate pairs have magnitudes `(1,4)` and `(1,2)`, so

```text
B(x+e_j) = 5!/4! = 5;    B(y+e_j) = 3!/2! = 3.
```

This contradicts any purported deterministic all-operation scalar updater on that packet. All six choices of missing `j` have explicit integer witnesses in the machine certificate. This lower bound concerns the specifically declared family of **raw signed-coordinate subset supplements**; general encodings and other sufficient statistics are not excluded.

## Sharp bounded-domain contrast

On the finite cube `{-1,0,1}^6`, adding any *five* of the six raw signed coordinates to `P` is enough to predict all twelve next counts. Reason: the other five coordinates and `Σz_i mod 3` recover the omitted coordinate uniquely from `{-1,0,1}`, whose residues mod 3 are pairwise distinct.

Exhaustive checking over 729 states finds the numbers of sufficient fixed coordinate subsets at sizes `0,1,2,3,4,5,6` to be

```text
0, 0, 0, 0, 0, 6, 1.
```

Thus a cube-only five-axis success does not extend to the unbounded signed native Cell torsor: the explicit `±3` witness proves its global failure.

## Exact executed evidence

Standalone standard-library checker: `research_checks/X6_UNIT107_JOHNSON_BRC_NAMED_AXIS_REPAIR_CHECK_20261118.py`, Git blob `7c651e0f853c9620cc578049ff033307d7af1f09`, commit `ea29a83c66b705eae503d7b29ff75e6d9b182886`; executed local SHA256 `1bc44ed4c6741c60cff1293ec9d51107cbce19628382277e776487bde2c5a248`.

- 15,625 states of `[-2,2]^6`, all 12 named signed steps: **187,500 exact comparisons**, zero failures.
- All 64 subsets of six raw axes, 729 states: precise sufficiency census above.
- Six explicit unbounded `±3` obstruction witnesses, each producing current `B=4` and next `5` versus `3`.
- CPython normal, `-O`, `-OO`: byte-identical canonical JSON, SHA256 `3eef377d7682493367106832be48ea536353c85c1850db7846eb76fb6da9dfd8`.
- Machine certificate: `research_checks/X6_UNIT107_JOHNSON_BRC_NAMED_AXIS_REPAIR_RESULTS_20261118.json`, Git blob `534563dce121d4f4b7fd8ecbac63523d83908911`, commit `f6ade3da54202e2e5103baed8bd501568cf9369d`.

## Task-facing disposition and next action

This is a *mathematical interface certificate*, not a finding of an invalid current caller. For `LP019/LP023/LP026`, a consumer requesting **one** named next N-BRC scalar can retain the exact original BRC count, length, and queried signed-axis coordinate. A consumer propagating arbitrary future native operations must provide an operation-preserving state or re-read correctly typed native coordinates. Do not infer path-word identity from the scalar.

The next smallest unfinished task is to classify exact live 28-LP downstream `commit:file:line` consumers into carrier observation, fixed-time N-BRC, one-step scalar N-BRC, and full path provenance demands. LP011/LP019 alleged historical wrong runtime callers remain unlocated; the independent Driver `REQUEST_REVISION` remains open. Original R063/Helly native benchmark support is tracked at Issue #2416 and remains a separate required operation. Do not repeat earlier units or substitute this finite test for that benchmark.

**Original research provenance:** `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956`. Original Unit104 Native PROGRESS `onhour-20261118-0402-x6-own-unit104-native-progress-v1` read back `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED` this turn; Units105–107 require current authenticated same-run semantic linkage if still legitimately owned. Research publication and Activity bookkeeping are independent from that native authorization.

Status remains `AUTHOR-PROVED / EXACT-FINITE-EXECUTED / UNREVIEWED / NOT_ADMITTED`.
