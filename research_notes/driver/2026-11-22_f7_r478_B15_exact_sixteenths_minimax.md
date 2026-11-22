# CBRC F7 r478 — exact B15 half-error minimax, frozen rational certificate

Date: 2026-11-22 (Asia/Taipei). Scientific contribution: the existing RESEARCH_DRIVER logical lane `EM-DVR-DEBB5E`. Preserve original F7 author `EM-CBRCF7-83A1D4`, original frozen Result `RR-AA38973D56330E59D315`, and all historical review/Source/Activity statuses. This is a finite-box mathematical result, not formal Native acceptance.

## Exact theorem

Under the **unchanged original F7 model**, let `q:Z²→R` satisfy first-coordinate evenness, `q(0,0)=0`, `q(x,0)=1` for `x≠0`, `q(x,y)≥1/2` for `y≠0`, and both markers `q(2,1)=q(-1,-1)=1/2`. Put

`k=a-2b-c+2d`; `D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`,

and `e_B=inf_q max_{a,b,c,d∈[-B,B]∩Z}|D_q(a,b,c,d)|`.

**Theorem r478:**

```text
e_B = 1/2 for every integer 1 <= B <= 15.
```

In particular, **`e_15=1/2` is closed exactly**. This strengthens r469's verified B1–B14 range. It does not determine the infinite-domain optimum or B16.

## Complete lower bound

The original invariant test `(a,b,c,d)=(1,-1,0,0)` gives `k=3` and

`D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2+1/2-1/2-0=1/2`.

This quadruple lies in every B≥1 box. Thus `e_B≥1/2` uniformly, without relying on any computation.

## Fixed globally admissible rational upper witness

Define `Q(x,y)=16q(x,y)`. Enforce `Q(0,0)=0`, `Q(x,0)=16` for nonzero x, `Q(2,1)=Q(±1,-1)=8`, first-coordinate evenness and `Q(x,y)≥8` for y≠0. Assign the 4,730 remaining finite evenness-identified `(|x|,y)` coordinates using a **fixed certificate of integers**, in the explicitly documented deterministic enumeration order of r476. Outside those coordinates set `Q=8` off-axis (with the listed axis and marker rules). Thus the witness is defined on *all* `Z²`, satisfies every original scalar condition, and has values among `{0,8,9,10,11,12,13,14,15,16}/16`.

The 4,730 free certificate entries, represented as little-endian signed 16-bit integers, have SHA256

```text
281b5bd19664a6e31d0ddff5f5ef1ff56deab5b4fc47814bf366407ba370d180
```

They occupy 9,460 raw bytes. The repository stores their exact immutable compressed Base85/zlib serialization (1,007 ASCII characters), which decodes to precisely those bytes:

- `research_artifacts/F7_R478_B15_Exact_Sixteenths_Witness_20261122.b85`
- `research_checks/CBRC_F7_R478_B15_EXACT_SIXTEENTHS_CERT_20261122.py` (standalone Python-standard-library verifier; no solver, NumPy, SciPy or floating arithmetic)

The checker reconstructs the finite coordinate index from the original B15 inputs, verifies the certificate SHA256, checks scalar bounds, and evaluates **every one of `31^4=923,521` original integer quadruples** with integer-only operations. Actual executed result:

```text
certificate entries: 4,730
min/max free Q: 8 / 16
max |16 D_q|: 8
inputs attaining |16 D_q|=8: 33,416
inputs with nonzero 16 D_q: 627,428
one attaining input: (-15,-15,-8,-4)
exhaustive original quadruple count: 923,521
```

Because `|16D_q|≤8` everywhere in B15, the displayed globally admissible rational q gives `e_15≤1/2`. Together with the marked universal lower bound, `e_15=1/2`. Monotonicity in B gives the entire smaller-box theorem.

The actual remote certificate was read back by fixed GitHub commit and its 1,007-character encoded content independently compared to the locally checked source (matching length and FNV1a32 0x1ad311db); the standalone checker independently validates the decoded raw SHA256.

## Search provenance and research frontier

The previous r476 exact extended LP had 115,320 inequalities, 4,730 q variables and 3,660 pair auxiliaries at B15. Here, **minimizing the sum of its 4,730 free q variables** (rather than solving zero-objective feasibility) produced a numerical HiGHS-IPM solution in about 6 seconds whose free coordinates are within 5.5e-14 of integers divided by 4 in q4 units. Rounding to the sixteenth grid produced the fixed integer certificate above; the subsequent exhaustive verifier, not the numerical LP result, proves the theorem.

Earlier r477 computed a rigorously verified near-half upper bound `0.5000000025` with a more complicated candidate. **r478 supersedes its finite upper-bound strength**, while retaining r477's own correct evidence and source history.

Still open: exact B16 optimization, and global `e_infty`, presently `1/2≤e_infty≤4/7`. A B15 witness need not remain feasible at B16 or over the entire infinite lattice. The original author's F7 theorem/Result is not automatically admitted by this separate Driver proof.

## Classification and control

One **new exact mathematical proof subunit completed**, certificate and independently executable checker saved. Native Review newly admitted: 0; Native Result newly admitted: 0; formal Task completion: 0; mother objective completion: 0. Other Researcher/Activity/CLAIM ownership and schedule untouched. Keep ongoing authority/integrity review work separated from this mathematical closure.
