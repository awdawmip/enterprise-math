# Independent audit of the conditional six-channel BRC geometry result

Status: **PASS_WITH_EXPLICIT_CONTRACT / INDEPENDENT_DERIVATION_CHECK**.
Date: 2026-09-07. Role: `ANCHOR_EXPOSED` internal owner helper, not an
allocated Researcher-ID, official review, registered claim, or new tool family.

**Conclusion.** The audited conditional obstruction, the A_i mixing example,
the reversible linear quotient bound, and the visible-identity/microbranch
counterexample are correct. No mathematical correction to the target note
is required. The conclusions depend on the explicitly declared six-channel
mass transfer contract and do not follow from native spatial adjacency alone.

## Audited source bytes and original contracts

The following files were read directly; the two author inputs were not
modified or executed by this independent audit.

| File | SHA256 |
|---|---|
| `OWNER_GEOMETRY_FRONTIER_20260907.md` | `9c7d54b65cc65c3723076186675cb3ec3f744709da2b73c1d82c5d1105bd450e` |
| `owner_geometry_20260907_check.py` | `d92a45acb9c455b88a3786ce99ae919cbfbd5a0b09b55ce3dfeb6b39b633c4a7` |
| `X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md` | `9d718ab2de19235b8e0958b8605f3c7c3cf2d0ebcca5f4dbb001088fb8905dfd` |
| `X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md` | `6c4173ff1d1bb9e30fa25cae83673c1eb24b364349fe289dc61d69486bf8c8b6` |
| `ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` | `519a16725156be5461c6e28a0dcef664e267cff4e85120cfb257d5d540ec459e` |
| `ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json` | `22e17d9bf7f3cb644f5f91785b8c80f82820462d7ddefc72abf2d1acc7da033b` |

The independent checker is
`owner_geometry_independent_audit_20260907.py`, SHA256
`248a5d9b37c83b244f6a1b506d27965d42fdd642d1079ec568340578619de7f8`.
Its complete output is
`owner_geometry_independent_audit_20260907.json`. It uses only standard-library
integer/Fraction arithmetic and independently enumerated branch histories;
it imports neither the author code nor production tools. The JSON also hashes
the three inspected production modules. All recorded input hashes were checked
again at the end of execution.

Original V1R §5 and V2R §1 distinguish abstract PF-10 channels C from native
unsigned axes A. Each has cardinality six, but a bijection beta must be chosen;
equal cardinality does not supply a canonical one. The native torsor contract
separately specifies the twelve signed primitive coordinate actions
`z -> z ± e_i`. Thus the correct types in the new result are:

- C: six unsigned channel labels, carrying a nonnegative rational mass vector;
- `{±E_i}`: twelve signed native step labels, indexing operations;
- z: a chart-relative point in the native signed six-axis spatial torsor;
- T: additional internal BRC transfer data over each native step.

The occurrence of six channel components and six spatial coordinates does
not identify these state spaces or introduce extra spatial axes. The note
preserves this distinction and explicitly chooses its beta convention.

One source-contract detail is important. The literal V2R frame formula
`U_(x,i)=beta_(x+e_i)^(-1) beta_x` telescopes along a path to
`beta_endpoint^(-1) beta_start`. Such pure frame transport is already flat;
nontrivial mixing cannot be obtained merely by composing those beta maps.
The new note correctly declares T as additional data and explicitly denies
that it is another beta composition. Therefore its noncommuting A_i example
does not contradict the original pure-frame formula. A future extension must
retain this distinction when discussing connections or holonomy.

## 1. Conditional positive-inverse obstruction

The author uses the column-as-input convention consistently:
`T[d,c]` sends mass from c to d and `v'=Tv`. Each nonzero coefficient is the
sum of positive rational branch weights; zero entries denote absent branches.
Column normalization `L T=L`, for `L=(1,...,1)`, preserves total mass for
every nonnegative rational input, not just for a single probability vector.

The proof chain is valid with the following separate premise uses.

1. For square nonnegative A and B with `AB=BA=I`, if `A_ij>0`, every
   off-diagonal equation `(AB)_ik=0` forces `B_jk=0` for `k!=i`. Invertibility
   makes row j of B nonzero, hence `B_ji>0`. The off-diagonal equations in BA
   then force every other entry in row i of A to vanish. Every row has one
   positive entry, and invertibility prevents repeated occupied columns.
   Therefore A is positive monomial. No cancellation or hidden negative
   BRC weight is used in this inference.
2. Column normalization makes each monomial coefficient exactly one, leaving
   a permutation matrix.
3. Translation invariance gives one fixed matrix for each signed direction,
   independent of the spatial point. Full simultaneous S6 covariance implies
   that the permutation for direction +i commutes with the entire stabilizer
   of i, which is S5. A commuting permutation preserves the unique common
   fixed point i. Its restriction to the other five labels lies in the center
   of the full symmetric group on those labels, which is trivial. Thus the
   positive-direction permutation is identity; the inverse condition gives
   the same for the negative direction.

This reproduces the applicable centralizer step from V2R without treating
the new T as frame transport. No extra commutativity or square-flatness
premise is needed for the obstruction. The S6 action relabels unsigned axes
and channels together and preserves the step sign. It is not an assertion
of covariance under the independent sign changes in the larger signed B6
action, nor a classification of every native rotation.

The unnormalized boundary is also correct. Conjugation preserves the unique
permutation support of a monomial matrix, so that support still centralizes
S5 and must be diagonal. The two stabilizer orbits are `{i}` and its five-point
complement. Full S6 covariance makes the two positive diagonal values a,b
common to all positive directions; negative directions use their inverses.
These matrices commute, and finite signed path multiplication gives

`T(z)[c,c] = b^(sum_i z_i) (a/b)^z_c`.

Negative exponents are valid positive rational inverse weights. Imposing
normalization again forces a=b=1. This is diagonal reweighting, not mixing.

The inverse's nonnegativity is essential. For an exact algebraic check,
`A=I/2+J/12` is a nonnegative column-normalized mixing matrix, with
`A^(-1)=2I-J/6`. Both products are identity and both matrices have column sums
one, but the inverse has negative off-diagonal entries. This is a countermodel
outside the positive BRC contract, not a proposed physical negative branch.

## 2. The A_i example and its exact BRC observer

A_i fixes the distinguished channel i and averages the other five channels
within their complement. It is symmetric, column normalized, rank two, and
idempotent. Taking both signed steps on axis i to carry A_i preserves every
declared premise except the positive exact inverse condition. It does not
silently retain flatness, which the declared contract never required.

For i different from j and input channel i, the +i then +j path has a single
weight-one first transition followed by five weight-1/5 choices. Thus its
output is uniform on channels other than j, with exactly five paths of
weight 1/5.

For +j then +i, the first step has five choices. One reaches i and is then
fixed, giving one weight-1/5 path. Each of the other four choices has five
continuations, giving twenty weight-1/25 paths. The output at i is 1/5 and
at each other channel is 4/25. Hence the two output vectors agree at i,
differ by 4/25 at j, and differ by 1/25 at each of the remaining four
channels. Their l1 difference is exactly `8/25`.

| Path | Count | Total mass | Largest individual path mass | Full weight histogram |
|---|---:|---:|---:|---|
| i then j | 5 | 1 | 1/5 | `5[1/5]` |
| j then i | 21 | 1 | 1/5 | `[1/5]+20[1/25]` |
| +i then -i, input c!=i | 25 | 1 | 1/25 | `25[1/25]` |

The last path returns to the same raw spatial point, but its channel output
is the five-channel average A_i e_c, not e_c. The first two paths have equal
raw spatial endpoint `z+e_i+e_j`. These endpoint statements use native signed
unit steps and do not replace branch histories or channel state with a
spatial coordinate. Because positive and negative directions share A_i,
the same channel calculations hold for all four choices of signs in an
ordered different-axis square.

The CWM interpretation matches the inspected production definitions:
serial propagation multiplies count, total, and dominant mass; alternative
recoalescence adds count and total and takes the maximum individual weight.
It does not merge equal endpoint branches into one branch. The author
checker actually calls these production functions, WeightHistogram.from_weights,
and the exact finite matrix-power function. Its recurrent-matrix use is only
for finite powers 0 and 2; there is no unproved convergence or infinite
recurrent-port closure claim.

The A_i are singular. Calling their order dependence a square-path defect
is appropriate; a group holonomy expression requiring inverse matrices
would be undefined here.

## 3. Reversible linear quotient: onto, idempotence, and fixed rows

For a surjective linear observation `q:Q^6 -> Q^r` with
`qA_i=R_i q`, idempotence gives

`R_i^2 q = q A_i^2 = q A_i = R_i q`.

Surjectivity allows equality to be tested on all of Q^r, yielding
`R_i^2=R_i`. An invertible idempotent is identity. Thus `qA_i=q` for every
i, and each row l of q is fixed on the right by every A_i.

For fixed i, all columns c different from i in A_i are equal, so
`lA_i=l` makes all `l_c`, c!=i, equal. Given any pair c,d, there is an actual
axis i outside that pair, making `l_c=l_d`. The common fixed row space is
therefore precisely span(L): L is fixed, and the preceding argument leaves
no second direction. It follows that `rank(q)<=1`, and since q is onto,
also `r<=1`. Total mass realizes the nontrivial one-dimensional case.

The independent code constructs the full 36-by-6 constraint matrix
consisting of the rows of `A_i^T-I`. Its exact rational rank is five and its
kernel contains the all-ones column, corroborating the same one-dimensional
fixed-row space without relying on the author's selected column witnesses.

The role of onto-ness should remain explicit when asserting `R_i=I` on the
entire target. For example, the non-surjective
`q(v)=(Lv,0)` and `R=diag(1,2)` satisfy `qA_i=Rq`, yet R is not globally
identity. Its restriction to im(q) is identity and q still has rank one.
This is consistent with, rather than an exception to, the stated theorem.
Without requiring invertible R_i, q=I permits rank six with R_i=A_i; the
invertibility assumption cannot be removed. A single named-channel readout
also need not factor: under A_1 in zero-based code labels, inputs e_1 and
e_2 both have channel-0 mass zero but produce channel-0 masses 0 and 1/5.

The exact identity `L A_i=L` extends by induction to every finite future
word in the twelve signed step operations. It certifies the total-mass
observer for that declared language. It is not inferred from the finite
word enumeration. If native position is retained too, the observation is
`(z,W)` and each step updates only z by its signed native unit vector;
positive and negative steps are then exact inverses on this observation.
The rank bound applies to q on channel mass, not to a larger observation
that also includes z, nonlinear data, or history registers.

The state domain is all nonnegative rational mass vectors as declared.
On the separately restricted probability-simplex domain W=1, total mass
would be a constant readout; the note does not assume that smaller domain.
Linear equalities on nonnegative inputs imply the stated matrix equalities
because all six basis vectors e_c are admitted inputs. This algebraic
extension to Q^6 introduces no signed physical branch weights.

## 4. Matrix identity is not microbranch identity

The final counterexample obeys the mass-matrix contract. Two parallel c-to-c
branches of weight 1/2 implement each positive step, and one c-to-c branch
of weight one implements each negative step. Their total-mass matrices are
both identity, with no cross-channel mixing. Nevertheless the round trip
contains two weight-1/2 branches, so its CWM is `(2,1,1/2)` and its histogram
is `2[1/2]`. The BRC identity has `(1,1,1)` and histogram `[1]`.

This is a concrete failure of microscopic inversion. It does not invalidate
matrix inversion, because the matrix was only the observer summing weights
by terminal channel. If future readouts include count, maximum weight,
histograms, or branch labels, the total-mass projection does not certify
erasure of that information. The target note explicitly preserves this
boundary, as required by the joint-observer contract. Even CWM is a partial
observer of history; the note does not promote it to full provenance.

## Independent executable evidence and remaining boundary

Actual execution from `D:\em\owner-20260907`:

```text
python -X utf8 research_notes/owner_geometry_independent_audit_20260907.py
exit_code: 0
status: PASS
elapsed_seconds: 0.465
rank_two_idempotent_kernels: 6
full_S6_signed_covariance: 8640
full_S5_stabilizer_size: 120
centralizer_size: 1
signed_ordered_squares: 120
signed_backtracks: 60
all_signed_words_through_length_2_with_start_channel: 942
joint_fixed_row_constraint_rank: 5
joint_fixed_row_kernel_dimension: 1
unnormalized_signed_displacement_coordinates: 18
```

The 8,640 covariance checks cover every S6 permutation and every one of the
twelve signed operation labels. The 120 squares verify full histograms and
vectors, not merely CWM. The 60 backtracks cover each signed direction and
all five nonfixed input channels. The 942 short-word cases include the six
start channels and every signed word of lengths zero through two. The
universal positive-inverse and linear-quotient conclusions rest on the
proofs above; these finite computations are independent regression evidence.
The elapsed time is an observed run value, not a complexity guarantee.

No target-note or author-code defect was found. The classic nonnegative
inverse lemma is reused with a self-contained proof; this audit does not
certify external priority or the exhaustiveness of the author's literature
and toolbox searches. The original V2R pure-frame transport and the new
independent T must remain differently typed. General non-permutation
dynamics, larger signed-symmetry contracts, nonlinear observable quotients,
physical calibration, and full history reversibility remain outside the
closed result. No author material, weighted-audit material, path-monitor
directory, production source, remote, or formal research registration was
changed by this work package.

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
