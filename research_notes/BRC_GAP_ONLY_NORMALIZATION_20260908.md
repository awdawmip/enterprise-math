# Completion-gap-only state normalization

Researcher: `EM-HME-0CE4FD / TASK_RESEARCH`  
Global read snapshot: `dd32c654bc48def291fcb1383c87ecdaa342493c`  
Project input frontier: `2e45c3dace447e8af4be28675a4d2589b45c2744`  
Status: exact representation result and fixed archived-state audit; no theorem promotion or public factorization claim.

## Result and supplied information

The existing odd-N ceiling-state reduction can be expressed using only the multiplier and its already prepared completion gap. The ceiling-root coordinate is unnecessary for selecting this reduction. On the 60 previously saved public-puzzle states, the two representations agree exactly. Seven states have a modularly impossible square gap, and three additional records duplicate a surviving normalized state, leaving 50 distinct predicate inputs in the completed batch.

The supplied state is

\[
N\text{ odd},\quad m\ge1,\quad a=\lceil\sqrt{mN}\rceil,
\qquad A=a^2-mN\ge0.
\]

Here **A is the upward completion gap**, not the downward remainder R. For a nonsquare target, with J=floor(sqrt(mN)),

\[
R=mN-J^2,\qquad A=2J+1-R.
\]

For a square target A=0. Its canonical next-square addition cost is a different quantity. This note does not equate the two.

The representation operation reads (m,A) and the odd-N type. It assumes the immediate-ceiling-state contract has already been established. N-to-A preparation remains an upstream cost; this is not an N-only hidden-moment extraction.

## Exact reduction

Whenever 4 divides m,

\[
A=a^2-mN\equiv a^2\pmod4,
\]

so 4 divides A if and only if a is even. Consequently a legal reduction is

\[
(m,A)\longmapsto(m/4,A/4).
\]

Although the operation does not read a, its associated ceiling changes exactly to a/2. Indeed, from a-1<sqrt(mN)<=a, dividing by 2 gives

\[
a/2-1/2<\sqrt{(m/4)N}\le a/2,
\]

and a/2 is an integer. Thus it is the actual immediate ceiling, rather than a different square above the target.

Let k be the largest nonnegative integer such that 4^k divides both m and A. This definition is finite because m>0, including when A=0. Write

\[
m'=m/4^k,\quad A'=A/4^k,\quad a'=a/2^k.
\]

Then a' is the immediate ceiling at m'N, and

\[
A\text{ is a square}\iff A'\text{ is a square}.
\]

When square, its nonnegative root scales by 2^k. An integer square divisible by 4^k has an integer square root divisible by 2^k, proving the reverse direction as well as the forward one.

Two exact modular exits match the existing source implementation:

- If m'=2 mod 4, an integer square gap would express m'N as a difference of two squares congruent to 2 mod 4, which is impossible.
- If m'=4 mod 8, maximality makes a' odd. Since N is odd, A'=a'^2-m'N=5 mod 8, which is not a square residue.

These are inherited exact rules, not a newly independent filtering method. Otherwise the reduction returns the normalized multiplier and gap. It preserves the square predicate for every valid supplied state, not merely the audited finite set.

## Existing-tool reuse

The unchanged reference is
`odd_n_ceiling_state_scan_representative(multiplier, ceiling_root)` in
`src/enterprise_math/brc_multiplier_priority_jump.py`.

Source blob: `f78379664b074b7f40879d4f24af94b48df8fc3b`.  
Local SHA-256: `ee4a01822ff9e5e33b602b5e834a6902dbd848d0258b981503cea3df513d1a0d`.

Reuse resolution: **COMPOSE_APPLIED**. The source already provides the exact mathematical reduction with (m,a). This audit changes the supplied carrier to (m,A), proves equivalence, and executes the existing helper as a reference. No production source or general target-input interface is added.

## Positive preservation

The preceding certificate supplies 15 successful m=8 constructions

\[
N=t(2t+1),\quad t\ge3\text{ odd},\qquad 8N=(4t+1)^2-1.
\]

Their A=1 is retained, so all 15 positive witnesses survive without reduction. These cases remain at the transformed U boundary. Their previous witness-generation calls are consumed rather than rerun.

A separate positive family demonstrates successful reduction. For even t>=4,

\[
N=t^2-1=(t-1)(t+1),\qquad16N=(4t)^2-16.
\]

Both 4t and t are the relevant immediate ceilings. The state (m,A)=(16,16) reduces to (1,1), and the witness root changes from 4 to 1. The fixed even t=4,6,...,34 supply 16 exact positive controls. Example: N=35, 16N=24^2-4^2, and N=6^2-1^2. The assertion concerns integer factors; no infinite prime-pair statement is made.

One additional exact-square boundary uses N=9,m=16,A=0. It reduces to m'=1,A'=0 and verifies termination when A has no finite 2-adic valuation. Total: 32 retained positive/boundary states, comprising 15 reused, 16 newly constructed and one zero-gap state.

## Fixed archived public states

Input certificates are guarded by their exact Git blobs:

- `brc_public_rsa_fixed_predicates_20260908.json`: `e56cfc8457e2398b5de3c90182c2b37824580ef3`.
- `brc_public_frozen_prefix_20260908.json`: `c4b201e608167cfff96c5a141bd9e26b575dad69`.

These contain the literal mathematical puzzle integers and all 60 already evaluated gaps. They preserve the RSA Inc-attributed [RSA-270](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-09-en.pdf), [RSA-896](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-10-en.pdf) and [RSA-2048](https://mysterytwister.org/media/challenges/pdf/mtc3-rsa-38-en.pdf) source PDFs read in the preceding experiment. No current challenge-resolution status is inferred from those historical PDFs.

| Saved public input | Saved states | Modular exits | Duplicate surviving records | Distinct remaining predicate inputs |
|---|---:|---:|---:|---:|
| RSA-270 | 20 | 3 | 2 | 15 |
| RSA-896 | 20 | 1 | 0 | 19 |
| RSA-2048 | 20 | 3 | 1 | 16 |
| Total | 60 | 7 | 3 | 50 |

The three actual aliases are RSA-270 m=16 -> 1, RSA-270 m=96 -> 24, and RSA-2048 m=96 -> 24. The reduced gaps equal the gaps already recorded at their representative slots. No representative outside the saved prefix occurs in these data.

Two alias references point to later prefix slots. Completed-batch deduplication is valid, but an earlier one-pass position cannot read a future cached result for free. If no result is yet available, the current scaled gap supplies a predicate input; its result still has to be determined. Outside-prefix representatives, if encountered elsewhere, similarly would not justify silently dropping a candidate.

Original multiplied-state directions remain metadata and are not assumed invariant under the reduction:

| Original multiplied direction | Saved states | Modular exits | Alias records | Unchanged records |
|---|---:|---:|---:|---:|
| D | 22 | 1 | 1 | 20 |
| U | 38 | 6 | 2 | 30 |

These counts describe this fixed collection. They do not establish a general D/U advantage or a distributional estimate.

## Verification and cost interpretation

The checker uses N only on the verification side to restore a=isqrt(mN+A), check the exact immediate-ceiling inequality, and compare the original source helper. The carrier-reduction block itself reads only m,A. Each normalized identity and square status is checked exactly. All 60 public comparisons and all 32 controls pass, totaling 92 reference comparisons.

Public coverage added: zero integers, zero multiplier positions, zero ceiling advances, zero witness-API calls and zero factors. The existing public non-hit observations remain unchanged.

The reduction from 60 records to 50 distinct predicate inputs is a 1/6 input-count reduction after states have already been materialized. It is not a measured 1/6 runtime saving, and it does not save the preceding root/preparation work. Normalization and cache costs remain unmeasured.

All seven modular exits already fail the existing LOW12 first condition modulo 4096. The checker confirms this with a complete small residue set. Therefore their rejection benefit must not be added to LOW12's earlier recorded benefit. Three alias records are a separate deduplication count, not three demonstrated expensive square-root savings. Source/input verification, restored roots, direct audit square roots, residue-set construction and serialization are verification costs, not a production benchmark.

Reproduction:

```powershell
python brc_gap_only_normalization_20260908.py --enterprise-root <existing-checkout> --output-dir <artifact-directory>
```

The two pinned input JSON files must sit alongside the checker. The script accepts an execution-source path and an output path only. Companion JSON records all state classifications, exact normalized gaps, source comparisons and constructive controls.

The usable result is a precise division of information: a prepared completion gap suffices for this state normalization, while D/U labels and N-to-gap preparation have separate roles and costs. Full library verification and the broader active research objective remain unfinished.
