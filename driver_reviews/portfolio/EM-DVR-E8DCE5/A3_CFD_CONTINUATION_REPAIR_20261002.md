# A3 / CFD bounded continuation repair — 2026-10-02

Status: `DELEGATED_LOCAL_REPAIR_AND_SOURCE_ROUTING / NOT_A_RESULT_OR_FORMAL_DRIVER_REVIEW`.

Prepared by delegated reviewer `/root/readonly_runtime_review`, with the parent
Driver retaining its own identity and write authority. This packet has no
independently registered Researcher/Driver authority, no Claim, no task
publication and no acceptance disposition. It neither changes original author
Result bytes nor upgrades mathematical, Working Truth or Foundation status.
Native current-task/owner observations must be supplied by the parent before
execution; immutable Source is not live ownership evidence.

## A3: exact domain correction, preserving the operator result

Inspected PR1491 head `9c482061b4fc64b3ef936d90a9e21590d52f16f8`, especially
`research_artifacts/A3_SHELL_PARTIAL_MOVE_SCALE_COHERENCE_7A41D2_20260917/result.md`
§1, §3 and §5, and author Result `RR-9FF7F84F01C577774649` at that head.
The Result binds publication `TP2-D2D715EB36415B0CA0C5`. On the coherent read
snapshot `origin/main@3920cc33ca6fa586dc1d9b13b4292ab11ddd4cf7`, that generation-2
record explicitly supersedes generation 1 `TP2-E6E8A3DC37930B4CF4AA`.
The older portfolio report's generation-1 routing pointer must not be used as
the current publication. The exact author Result is absent from this main
snapshot; this remains a concrete ordinary review-binding/admission prerequisite.

The parent additionally obtained native exact-task request `#2639`, reporting
`SUCCEEDED` at Source `3920cc33ca6fa586dc1d9b13b4292ab11ddd4cf7`, observed
`2026-10-02T14:41:23Z`. That readback identifies current generation 2
`TP2-D2D715EB36415B0CA0C5`, state `FROZEN_RETURN / AWAITING_REVIEW`, no live
Claim, and the same frozen branch Result. Its next action is independent
Driver review, not READY research dispatch or rerunning the completed author
enumeration. The parent retains the complete native receipt; this delegated
packet does not pretend the agent performed that native request itself.

Let `B=B_n`, `q=n-d+1`, and let `U,L` be the author's exact upper and lower
carrier permutations. With push-forward `(F_*s)(x)=s(F^-1 x)`, the identity

`L_* = K_* U_*`, where `K=L U^-1`,

is valid for **every** alphabet and every state in its domain. Its shell profile
is unchanged: identity below `q`, `R_(g_minus)` on shell `q`, and
`R_(g_minus g_plus^-1)` above `q`. This operator statement does not need a
two-label assumption.

The corrected raw universal-state claim is:

> For a label alphabet `A` with at least two elements, `U_*s=L_*s` for every
> `s in A^B` if and only if `U=L`, equivalently `K=id`.

Proof: if `U != L`, choose `p` with `U(p) != L(p)` and distinct labels `a,b`.
The state equal to `b` at `p` and `a` elsewhere has its exceptional label at
different output points. Conversely identical carrier permutations have identical
push-forwards. Such a state on `B_n` extends to `B_(n+1)` by the background label,
so this also proves the adjacent-scale statement with literal restriction.
The author's consequences remain correct on this domain: for `d=1`, raw descent
iff `g_minus=e`; for `d>=2`, iff `g_minus=g_plus=e`, by faithfulness on each
nonzero shell.

For `|A|=1`, every state is constant, so all carrier permutations induce the
same state operation. Explicitly `n=d=1`, `g_minus=(23)`, `g_plus=e` gives
`U=id` while `L(1,-1,0,0)=(-1,0,1,0)`: nonidentity `K` is invisible to the sole
state. For `A` empty, `A^B` is empty because `B` contains zero, and universal
state equality is vacuous. These are domain boundaries, not a failure of the
radial identity or the existing two-label frozen counterexample.

The quotient claim needs its own quantifier. For a **single** state, agreement
in `A^B/H` only gives a state-dependent witness `h`: `(h^-1 K)_*` stabilizes
that state. It does not normally imply `K=R_h`. A sufficient rigorous meaning
of "rigidly labelled" is an injective state on `B` (available when
`|A|>=|B|`), or explicitly trivial stabilizer under the entire relevant carrier
operator group. Trivial stabilizer under `H` alone is insufficient. With that
full rigidity, equality of the two state orbits implies `K=R_h` for one common
global `h in H`, and the author's §5 shellwise criterion is preserved.

For the actual `H={id,R_(12)}` of order two, the stronger universal quotient
statement also holds with just `|A|>=2`: all states agree modulo `H` iff
`K in H`. To prove necessity, identify binary states with subsets of `B`.
Singleton subsets force `K(p)` to be either `p` or `h(p)`; hence `K` fixes
every `h`-fixed point and either fixes or swaps each two-point `h` orbit. If
some nontrivial orbit is fixed and another is swapped, one marker from each
gives a subset whose image equals neither itself nor its global `h` image.
Thus one common choice acts on every nontrivial orbit, making `K=id` or `h`.
Sufficiency is immediate. This short proof is special to the order-two quotient,
not a general small-alphabet theorem for arbitrary quotient groups.

Practical repair: publish this named quantifier/domain correction as an own
scoped packet attached to the **existing** A3 revision; preserve author RR/ER,
return, checker and certificate unchanged. Any later formal disposition requires
an authorized ordinary new review against admitted exact current-main Result
bytes with a fresh digest/CAS boundary. This packet is not `REQUEST_REVISION`
authority and does not create a third task or rewrite the author's identity.

## CFD: recover the later frontier before consuming the old handoff

Inspected PR1492 head `7a594142c816700cd4ddc9959a126313826974c3`. Its return's
"wire this static-carrier detector into the adapter" next action is superseded
by code already in the above main snapshot:

`research_artifacts/CFD_SPECTRAL_HYBRID_292BCE_20260917/static_carrier_native_adapter.py`
and the pinned copy
`research_artifacts/CFD_POLARIZATION_SUPPORT_20260923/static_carrier_native_adapter_source.py`.

The actual code contains one-time exact closure, initial validation, fixed rFFT
gather, and both unchanged-dense fallback and sparse kernel dispatch. This is
implementation coverage, not an independent native trajectory acceptance.
The Sep23 `PROOF.md` explicitly identifies R23 and states that neither R19 nor
R23 supplies the matched native `32^3` Taylor-Green benchmark.

Recovered the exact authorized official-repository material commit
`51ee293c8537b86e5e922f9f379f9d0d2ab7b981` using read-only Git fetch. The
referenced branch head is `1b47d2cf8ec96868cf49722617e9f90ae7464a9c`; this packet
pins the actual bytes read at the material commit, rather than assuming head
contents. All three originals were fully read; no scientific checker was rerun.

| Exact path at material commit | Git blob | SHA-256 |
|---|---|---|
| `research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_B7E2C1_20260922_R23.md` | `1e3fef6483ea55f4b745fc82f313b2cc266e4cd1` | `db47f89e48a5aff640e780a8cc65eff2c3d2b13e4bd27265d856d188628062c0` |
| `research_checks/RS_CFD_SPECTRAL_HYBRID_B7E2C1_R23.py` | `328a4267bd59f22b1fd052bb42a8825f4e675f3e` | `81a52e0306deff061a966ce6aaf3db15af2956aec8c409a86e94e166a0e12559` |
| `research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_B7E2C1_R23/robust_attribution_certificate.json` | `1eceb647ef6d490753b113bf634782c32781f80a` | `f7ce985dacc85e63906aa15aff6f76ad140ac1c30a4638eef375c78edf53fc97` |

None of these exact three blobs occurs anywhere in the inspected main tree.
Main has routing references and the adapter, not the recovered full R23 packet.
The source originals remain retrievable at their immutable commit; source
recovery must not silently become admission or author-result replacement.

R23 consumes R19 `043e0a563c60dabc141a51387865feb364a4cc6a` and sharpens its
timing-attribution ceiling under deterministic measurement-error boxes. With
`A=alpha_bar*w_bar`, `N_-=H_- - A D_+`, its worst denominator is
`g_rob=1+N_-/T_+` when `N_- >=0`, otherwise `1+N_-/T_-`, under its stated
positive-baseline/box consistency conditions. `g_rob>1/q` rejects target
speedup `q`; the reported `1/134` timing-error threshold is an illustration,
not measured hardware evidence. Its saved host probe reports
`native_ready=false`. That is the author's 2026-09-22 runtime observation,
not a new test or assertion about the present environment.

Remaining decisive unit: on an already provisioned, pinned
spectralDNS/shenfun/MPI/FFTW host, perform the matched `32^3` Taylor-Green
dense / guarded-hybrid / forced-fallback RK4 A/B/C experiment. Independently
verify velocity, raw Vortex/pressure interface, de-aliasing/Nyquist policy,
new modes and fallback correctness. Charge detector, gather, pair-kernel,
fallback and whole-trajectory cost, and publish timing uncertainty compatible
with R23 before interpreting a target ceiling. No scalar support or floating
agreement substitutes for a trajectory/PDE certificate.

Reuse `RS-CFD-TRAJECTORY-VERIFY-20260910 / TP2-499BEE22860EFD4AD321` rather than
publishing another synonymous verifier task. The parent spectral task's
Sep22 MCP checkpoint pointer names claim `MCP-6013e6f1c2aebe02f5689869`,
ownership epoch `5785350221` and session `MCP-0e6fcaa5c5a3425cbe4259abf1694b46`,
but explicitly has `authority_granted=false`. It cannot prove current liveness
or authorize takeover. Current native task/owner/session evidence controls;
an active exact owner must be preserved.

## Actual bounded validation and limits

Only the new standard-library script
`driver_reviews/portfolio/EM-DVR-E8DCE5/a3_alphabet_domain_repair_check.py`
is run for this packet. It checks all `G x G` pairs and `1<=d<=n<=2` for
singleton state invisibility, one-marker binary faithfulness and one/two-marker
global-`H` witnesses; the mathematical conclusion uses the proofs above,
not extrapolation from this finite test. It writes no files. The original A3
checker/counterexample and all CFD programs are retained and not rerun.

Actual command:

```bash
python3 -B /workspace/enterprise-math/driver_reviews/portfolio/EM-DVR-E8DCE5/a3_alphabet_domain_repair_check.py
```

Exit code `0`, status `PASS`: `B1=19`, `B2=85`; 1,728 carrier/path cases;
all 1,728 singleton alphabets give equal state paths; 108,864 binary one-marker
checks separate all 1,679 nonidentity raw defects. The global-H probe separates
1,654 nonglobal operators, using 1,628 one-marker and 26 two-marker witnesses;
injective rigid-state checks agree with operator membership in every case.
This is the new bounded probe's actual execution, not a replay of the original
5,760-case author checker or any CFD experiment.

This packet does not certify host readiness, measured
speedup, continuous PDE correctness, current Claim ownership or formal Result
acceptance. No original author file, taskbook or immutable record is modified.
