# CBRC F7 r479 — exact B20 finite-box minimax on a quarter grid

Date: 2026-11-22, Asia/Taipei. Research by the existing RESEARCH_DRIVER logical lane `EM-DVR-DEBB5E`; original F7 author `EM-CBRCF7-83A1D4`, frozen Result `RR-AA38973D56330E59D315`, and independent Source/Activity/Native review statuses preserved.

## Main theorem

Under the unchanged original F7 model, let `q:Z²→R` obey `q(-x,y)=q(x,y)`, `q(0,0)=0`, `q(x,0)=1` for x≠0, `q(x,y)≥1/2` for y≠0, and the two marked equalities `q(2,1)=q(-1,-1)=1/2`. Put `k=a-2b-c+2d`, `D_q=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`, and `e_B=inf_q max_{(a,b,c,d)∈([-B,B]∩Z)^4}|D_q|`.

**Theorem r479:**

```text
e_B = 1/2  for every integer 1 <= B <= 20.
```

The new exact B20 certificate subsumes all prior B1–B15 results, and closes B16, B17, B18, B19 and B20 together. It makes no claim about B≥21 or the infinite-domain optimum.

## Lower bound

The unchanged marked input `(1,-1,0,0)`, present for every B≥1, forces `D_q=q(4,2)+q(-3,-3)-q(1,-1)-q(0,0)≥1/2`. Thus `e_B≥1/2`.

## Exact rational upper witness

Set `Q=4q`. For all `(x,y)`, enforce first-coordinate evenness; set `Q(0,0)=0`, `Q(x,0)=4` for x≠0, and `Q(±2,1)=Q(±1,-1)=2`. All other off-axis coordinates take values in `{2,3,4}`, so `q≥1/2` automatically.

For B=20, the original r476 fiber coordinate enumeration identifies **8,358 distinct free (|x|,y) coordinates**. Assign them from the fixed certified unsigned-byte array in that order, and put the baseline Q=2 elsewhere off-axis. The raw array's SHA256 is:

```text
c393685154755cf9f5c943334ceb247fe1c2ad73bcf8835fcdb41c1087012a36
```

The verified raw array comprises 8,358 bytes, with 5,888 entries Q=2, 1,940 entries Q=3, and 530 entries Q=4. Its immutable Base85/zlib encoding occupies 823 ASCII characters and is published as:

`research_artifacts/F7_R479_B20_Exact_Quarter_Witness_20261122.b85`

A **standalone Python standard-library exact-integer checker** (no SciPy, no NumPy, no LP solver, no floats) reconstructs the index, decodes the SHA-verified bytes and enumerates every original B20 input:

`research_checks/CBRC_F7_R479_B20_EXACT_QUARTER_CERT_20261122.py`

Actual executed checks over **41^4 = 2,825,761 quadruples**:

```text
min/max free Q: 2 / 4
exact maximum |4 D_q|: 2
tight (|4 D_q|=2): 158624 inputs
nonzero D_q: 1453374 inputs
one equality input: (-20,-20,-20,-10)
signed distribution:
  -2: 87796; -1: 671582; 0: 1372387; +1: 623168; +2: 70828
```

The actual GitHub data file and checker were read back at immutable commits. The archived 823-character encoded certificate matches the locally independently checked candidate (length and exact FNV1a32 digest `e2aafd25`), and the checker establishes its stronger decoded SHA256 identity. This proves the fixed global q has `E_20(q)=1/2`. Combining the lower bound and monotonicity proves the theorem.

## Discovery provenance and boundary

The r476 B20 extended LP comprises `8·20·41²=268,960` scalar inequalities (rather than `2·41^4` original signed inequalities). A numeric search with objective minimize the sum of free `4q` coordinates (rather than a zero objective) reached a point whose entire free q4 vector differs from integers by at most 3.9e-14. Rounding yielded **this fixed quarter-grid witness**, and the independent exact checker is the theorem-bearing step. The original numerical result by itself is not a proof.

The successive feasible searches B16–B19 are subsumed by this B20 theorem. A B21 numerical attempt hit a 30-second solver limit without returning a result; that is not mathematical infeasibility.

Prior r478 B15 exact sixteenth-grid certificate and r477 near-half rational candidate remain preserved as historical research artifacts; B20 supersedes their finite-range frontier.

**Open scientific frontier**: B21 full-variable half-error primal or an exact obstruction, then larger B; global `1/2≤e_infty≤4/7` remains unchanged. The original F7 task scope and evidence origins are not modified by this Driver contribution.

## Control status

One new completed exact mathematical subunit (r479), with static verified integer certificate and standalone proof checker. New Native Review admissions 0; new Result admissions 0; formal Tasks completed 0; mother goals completed 0. This does not manufacture CLAIM, Activity attachment or author-independent acceptance. No schedule or owner changes.
