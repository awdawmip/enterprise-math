# Exact slot-permutation quotients for vacancy planning

Date: 2026-11-10, Asia/Hong_Kong. Status: author derivation. This note uses the
masked-observation Bellman model proved in `strategy_proofs.md`, Section 7, and
implemented in `bellman_planner.py`. The finite implementation and measurements
are recorded separately by `symmetry_planner.py` and its result files.

## 1. Round language and the observer being preserved

There are `r` request slots and `b` residue bits. A slot pattern is

\[
p=(m,v),\qquad 0\le m<2^b,\quad v\mathbin{\&}\neg m=0.
\]

It represents the residue set `Gamma(p)={x:x&m=v}`. There are exactly

\[
N=3^b
\]

patterns, since each bit is unknown, observed zero or observed one.

The future target sequence is fixed. In each round the controller may query
unknown bits of any request, then create a certified key for the target, bind
**actual slot 0** to it, and release the source. The other `r-1` slots undergo
no addressed business writes. Queries cost eight original commands; complete
key `K` has weight `w_b(K)` as in the parent proof. The fixed business-word
constants depend on the prescribed target, not on the request slot queried.

The preserved planner observation is the remaining minimax command cost and
the available certified creation actions. The actual executor continues to
perform and retain the prescribed writes to the real slot 0. At the end of the
specified horizon the planner continuation value is zero.

## 2. Permutations fixing slot 0 are exact automorphisms

Let `G=S_(r-1)` act by permuting slots `1,...,r-1` and fixing slot 0. It acts on
both ordered knowledge states `S=(p_0,...,p_(r-1))` and compatible actual residue
tables in the same way.

### Lemma 1: compatible tables correspond bijectively

For every `pi in G`,

\[
\Gamma(\pi S)=\pi\Gamma(S).
\]

**Proof.** Slot `pi(i)` in the permuted state carries exactly the pattern that
slot `i` carried before. Its actual residue must therefore satisfy exactly the
same mask equations. Permutation and inverse permutation map the product
completion sets to each other. ∎

### Lemma 2: every action and answer branch corresponds in both directions

1. A certified complete key `K` is available at `S` exactly when it is available
   at `pi S`, because certification excludes its residue from every slot.
   Its weight is unchanged.
2. Querying unknown bit `j` of slot `i` corresponds to querying the same bit of
   slot `pi(i)`. The read length is unchanged. For either answer `epsilon`,

   \[
   \pi\,O_{i,j,\epsilon}(S)
   =O_{\pi(i),j,\epsilon}(\pi S).
   \]

3. Creating and binding `K` commutes with the permutation:

   \[
   \pi\,W_0(S,K)=W_0(\pi S,K),
   \]

   since `pi(0)=0`. The remaining target suffix is the same.

All correspondences have inverses obtained from `pi^(-1)`. They preserve actual
query answers under the compatible-table bijection in Lemma 1.

### Theorem 1: Bellman values and optimal policy existence are preserved

For every remaining target suffix,

\[
\boxed{V(\pi S,a)=V(S,a)\qquad(\pi\in G).}
\]

**Proof.** Use the same well-founded rank `(rb+1)L+U` as in the parent Bellman
proof. The terminal values are equal. At a nonterminal state, Lemma 2 pairs
every creation score and every query score, including its two answer
continuations. By induction those continuations have equal values. Taking the
maximum over each query's answers, then the minimum over all paired actions,
gives equal values. An action attaining the minimum transfers with the same
value, and so do its answer-dependent continuation policies. ∎

## 3. The exact quotient state is a distinguished pattern and a multiset

Write

\[
Q(S)=\bigl(p_0,\;(n_p)_{p\in\mathcal P_b}\bigr),\qquad
n_p=\#\{i\ne0:p_i=p\},\quad\sum_pn_p=r-1.
\]

Two ordered states have the same `Q` exactly when they are in the same orbit of
`G`. The forward direction follows because a permutation preserves pattern
counts. For the reverse direction, match the equal-pattern nonzero slots in
the two states separately for each pattern, producing a permutation fixing 0.

The quotient transitions are explicit:

- A query of slot 0 changes only its distinguished pattern.
- A query of a nonzero slot with pattern `p` is available when `n_p>0` and the
  queried bit is unknown in `p`. For answer `epsilon`, decrement `n_p` by one
  and increment the resulting pattern count `n_(p')` by one.
- A creation replaces `p_0` by the full pattern `(B-1,K mod B)` and advances
  the target suffix. The remaining multiset is unchanged.

Multiplicity is essential. One read refines **one** actual request slot. It
does not refine every member of an equal-pattern bucket.

Because the two concrete action/answer directions of Lemma 2 are preserved,
the Bellman recurrence can be evaluated directly on `Q`. Its value is exactly
the ordered-state value, and a minimizing quotient policy can be executed on
every concrete representative of that quotient state.

### Runtime address realization

The policy cache stores a pattern class instead of a chosen nonzero slot
number. The executor retains a bucket of actual slot numbers for each live
pattern. To execute a quotient query `(p,j)`, it chooses one real slot from that
bucket, runs the original reader for that slot, and moves that slot to the
answer-refined bucket. Slot 0 remains individually identified.

Every chosen slot realizes the same quotient transition for its actual answer.
Thus the lifted policy attains the quotient minimax value. Different bucket
representatives can produce different answer orders on a particular ordered
input; their minimax value is the same. The executor retains the addresses
needed by the original reading and binding operations.

## 4. The final round admits the full slot-permutation group

When one round remains, creation is followed by terminal planner value zero.
The location of the resulting business overwrite cannot change any remaining
planning decision. Before that creation, all certified-key predicates and
query costs are symmetric in all `r` slots.

Therefore the last-round quotient is the full multiset

\[
\boxed{Q_{\rm last}(S)=(n_p)_{p\in\mathcal P_b},\qquad\sum_pn_p=r.}
\]

The proof uses all permutations `S_r`: query actions and their answer branches
still correspond by relabeling. A creation by either representative has the
same weight and reaches the common zero-valued terminal class. This gives a
two-way cost-preserving correspondence for the remaining decision game.

The runtime still binds the selected key to actual slot 0. The full original
request state remains available to the execution harness; the last-round
policy cache only uses its multiset to plan the remaining reads and key.

### Crossing into the final round

At the preceding creation, form the next multiset by adding one copy of the
new full pattern `(B-1,K mod B)` to the existing nonzero-slot multiset. This
is exactly the multiset of the concrete updated state. The actual slot-0
address can then join the corresponding runtime pattern bucket for future
queries in the last round.

### Why the earlier rounds distinguish slot 0

The write operator `W_0` commutes with permutations fixing 0. A permutation
that moves 0 changes which acquired information is retired by the next
business overwrite, and need not preserve a multi-round value.

A small exact example in the original planner has `r=2`, `M=3`, `b=2` and
remaining targets `(0,1)`:

\[
S=((0,0),(1,0)),\qquad S'=((1,0),(0,0)).
\]

The full-slot pattern multisets agree. Direct Bellman evaluation gives
`V(S,0)=28` and `V(S',0)=20`. Thus a two-round cache must retain which pattern
belongs to the slot that will be overwritten. This example was checked by
calling the current `Planner.value` on the two displayed states; the symmetry
implementation records its own finite comparisons separately.

## 5. State and action bounds

For a fixed remaining suffix, ordered states have at most `N^r=3^(br)` pattern
tuples. Stars and bars gives the exact numbers of all permutation orbits:

\[
\boxed{
\#Q=N\binom{N+r-2}{r-1},\qquad
\#Q_{\rm last}=\binom{N+r-1}{r}.
}
\]

These are upper bounds on reachable memoized states. With `T>=1` target rounds,
a coarse total bound, identifying all terminal planner states, is

\[
\boxed{
(T-1)N\binom{N+r-2}{r-1}
 +\binom{N+r-1}{r}+1.
}
\]

For `b=3`, `N=27`, the last-round knowledge-state counts compare as follows:

| r | Ordered `N^r` | Full-multiset `C(N+r-1,r)` |
|---:|---:|---:|
| 4 | 531,441 | 27,405 |
| 5 | 14,348,907 | 169,911 |
| 6 | 387,420,489 | 906,192 |

Let `u(p)` be the number of unknown bits in a pattern. A distinguished-slot
state has only

\[
u(p_0)+\sum_{p:n_p>0}u(p)
\]

distinct query actions to consider, plus at most `M` candidate creations. A
last-round state has `sum_(p:n_p>0) u(p)` query actions. Each query has two
answer successors. Equal-pattern multiplicity affects the successor counts,
but does not create more decision alternatives.

### A tighter bound after the first prescribed overwrite

At every subsequent nonfinal position, slot 0 is fully known and its residue
lies in the previous target's `M` legal residues. Thus the factor `N` in the
distinguished-slot bound may be replaced by `M` at those positions. In the
final multiset after a preceding creation, at least one full pattern belongs
to that same set of `M` patterns. The number of such multisets is at most

\[
\binom{N+r-1}{r}-\binom{N-M+r-1}{r}.
\]

For `T>=2`, a corresponding total upper bound is

\[
\boxed{
\bigl(N+(T-2)M\bigr)\binom{N+r-2}{r-1}
+\binom{N+r-1}{r}-\binom{N-M+r-1}{r}+1.
}
\]

The concrete planner's measured state counts and CPU time remain separately
reported. The quotient preserves the original Bellman command value while
reducing the state and action representation used to compute the policy.

## 6. Named future writes determine which slots stay distinguishable

The symmetry above uses the stated future language: only slot 0 receives
business writes. If a future operation names another slot, its address may
distinguish two members of the same former pattern multiset.

Here is a minimal example for permutations fixing 0, requiring two other
slots. Let `r=3`, `b=2`, and consider fully known residues

\[
R=(0,1,2),\qquad R'=(0,2,1).
\]

They have the same distinguished slot-0 pattern and the same remaining
multiset. Perform the prescribed addressed operation `drop slot 1`. The first
state then excludes residues `{0,2}` from reuse, while the second excludes
`{0,1}`; the zero at slot 0 can be realized by the nonempty complete key 4.
For target 0, the available key minima are respectively key 3 of weight 4 and
key 2 of weight 2. The future planning values differ.

In the action correspondence, permuting slots 1 and 2 transforms `drop 1`
into `drop 2`, which is a different specified future operation. An addressed
copy has the analogous source/destination distinction and can also introduce
shared identity information. Such languages retain the corresponding address
and relation state in their own quotient construction.

## 7. Two exact final-round pruning rules

The following rules apply when one creation round remains. They can accompany
the permutation quotient while preserving the same Bellman value.

### Existing safe-key cutoff

Let `c` be the minimum weight of a currently certified key, and let `w_min`
be the minimum complete-key weight over all legal keys of this target. If

\[
c\le8+w_{\min},
\]

immediate creation attains an optimum. Every continuation beginning with a new
request-bit query costs at least eight commands and must eventually select a
key of weight at least `w_min`. Equality uses the existing tie convention that
prefers an already certified creation.

### Compatible-slot lower bound

For a candidate `K`, let `n_K` count the actual request slots whose current
patterns are still compatible with `rho(K)`. A full pattern equal to `rho(K)`
makes that candidate unavailable throughout the final observation phase: no
further request write precedes the final creation.

Over the remaining candidates, define

\[
\boxed{L(S)=\min_K\bigl(8n_K+w_b(K)\bigr).}
\]

Then `L(S)` is a lower bound on the final-round Bellman value.

**Proof.** Consider any realized safe policy path and its eventual chosen
key `K`. Every slot initially compatible with `rho(K)` must cease to be
compatible before that creation. At least one new bit of each such slot must
therefore have been observed. The path pays at least `8n_K+w_b(K)`, hence at
least its minimum over `K`. The bound holds for every path and thus for the
worst path of any policy. ∎

In histogram form,

\[
n_K=\sum_{p:\rho(K)\in\Gamma(p)}n_p.
\]

The pattern multiplicity is retained in this sum. A shared pattern is a shared
knowledge description; each of its actual slots still requires its own
observation when the chosen candidate is to be excluded from that slot.
