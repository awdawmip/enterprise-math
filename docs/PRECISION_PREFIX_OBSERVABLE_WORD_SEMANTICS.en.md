# Prefix-Observable Word Semantics versus Terminal Operation Effects

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The commuting-idempotent OR normal form is exact for a word's **terminal transformation**. It is not automatically exact for a richer future language that observes the state after every action prefix.

This distinction supplies a sharp boundary for semantic word quotienting: finite terminal effect algebra does not imply finite prefix-observable operation-word semantics.

## 1. Terminal effect semantics

With k singleton OR generators, a word w has terminal normal form

`nu(w)=OR of all generator bits occurring in w`.

Only the set of generators that ever occur matters. Order and repetition are erased.

The generated terminal transformation monoid has exactly

`2^k`

effects including identity.

## 2. Prefix-observable normal form

For word

`w=a_1...a_H`,

define cumulative masks

`U_t = mask(a_1) OR ... OR mask(a_t)`.

The exact prefix-observable normal form is

`tau(w)=(U_1,...,U_H)`.

For any initial state x, the full prefix-state trace is

`(x OR U_1,...,x OR U_H)`.

Therefore tau is sufficient for every initial state.

It is also extensionally minimal under full prefix-state observation: choosing x=0 recovers tau itself.

## 3. Same terminal effect can have different prefix semantics

For two generators a,b:

`ab` has trace

`(a, a OR b)`,

while `ba` has

`(b, a OR b)`.

The terminal effect is identical, but the prefix-observable operations are different.

Thus commutativity of terminal transformations does not make action order semantically irrelevant when intermediate state is visible.

## 4. Prefix normal forms still compose exactly

Let `tau(u)` end at mask F and let

`tau(v)=(V_1,...,V_r)`.

Then

`tau(uv)=tau(u) ++ (F OR V_1,...,F OR V_r)`.

So prefix-observable semantics still has a closed exact composition law; it simply requires a richer, variable-length operation state.

The executable compiler cross-checks this formula against literal concatenation over exhaustive small words.

## 5. Finite terminal monoid, infinite prefix-word semantics

Take only one idempotent generator a.

All nonempty words

`a, a^2, a^3, ...`

have the same terminal transformation.

But their prefix traces have different lengths:

`(1)`,

`(1,1)`,

`(1,1,1)`, ...

Therefore the prefix-observable operation algebra is infinite over unbounded word length even though:

- fine state set is finite;
- terminal transformation monoid is finite;
- the generator itself is idempotent.

This proves:

`finite state/effect monoid`

does not imply

`finite operation-word semantics`

once timing/prefix output is declared visible.

## 6. Exact count of length-H prefix traces

Suppose exactly s distinct generators appear for the first time during a length-H word.

Their ordered identities can be chosen in

`P(k,s)=k!/(k-s)!`

ways.

The first action must introduce the first generator at position1. Choose the remaining `s-1` first-appearance times among positions2..H:

`C(H-1,s-1)`.

All other positions are stutters using already-seen generators and do not change the prefix mask.

Hence the exact number of distinct prefix traces of length H>=1 is

`N_prefix(k,H)=sum_(s=1)^min(k,H) P(k,s) C(H-1,s-1)`.

## 7. Terminal effect count is much smaller

At exact word length H, possible terminal masks are simply nonempty subsets of size at most H:

`N_terminal(k,H)=sum_(s=1)^min(k,H) C(k,s)`.

Always

`N_terminal <= N_prefix <= k^H`.

The left inequality can be very strict because prefix semantics retains order-of-discovery and timing information.

## 8. Sharp k=5,H=5 counts

For k=5,H=5:

- literal words: `5^5=3125`;
- terminal semantic effects:31;
- prefix-observable traces:1045.

Among words whose terminal effect is the full five-bit mask, there are already

`5! = 120`

distinct prefix traces at H=5, corresponding to the 120 generator introduction orders.

So terminal quotienting removes large amounts of behavior that become immediately observable once prefixes are exposed.

## 9. Full-support traces with stuttering

For H>=k, prefix traces that eventually reach the full mask are counted by

`k! * C(H-1,k-1)`.

The factor `k!` chooses first-introduction order; the binomial factor chooses when the remaining introductions happen among the H positions.

Thus even after the final terminal effect has saturated, prefix timing continues to generate new word semantics with horizon.

## 10. Relationship to guarded/partial semantics

Earlier P024/FQ-006 results require prefix information because action legality can fail at intermediate states.

The present result is sharper in a different direction: **even total everywhere-defined idempotent actions** can require prefix-sensitive operation semantics when the future language explicitly reads intermediate states.

So prefix complexity is not caused only by DOMAIN/guards; it can arise purely from the observation language.

## 11. Semantic quotient must name the observation interface

A statement such as

`word normal form = final OR mask`

is correct only for terminal-transformation semantics.

If the declared future language includes:

- prefix states;
- prefix observations;
- timing of newly visible distinctions;
- intermediate costs/rewards;
- prefix legality or witness events;

then a terminal operation quotient may be too coarse even when it is exact extensionally as a final state transformation.

## 12. Representation-resource versus semantic change

This is **not** another representation Pareto inside one semantic-equivalence fiber.

Terminal-only and prefix-observable languages retain different semantic information. Moving between them changes the declared future theory itself.

Only after the prefix semantic object has been fixed should caches, scans, tables or formulaic representations of that object be compared by resource cost.

## 13. Stage131 consequence

Stage131 now has a hard ordering rule:

1. first declare whether operation semantics are terminal, prefix-observable, guarded, witness-sensitive, etc.;
2. compute the correct semantic word quotient/normal form;
3. only then optimize storage/work/depth representations of that quotient.

Precomputing the wrong terminal quotient more efficiently cannot repair a semantic loss of prefix information.

## Owner-local assets

- `src/enterprise_math/prefix_observable_or_word_semantics.py`;
- `tests/test_prefix_observable_or_word_semantics.py`;
- this bilingual theorem note.

## Prior art / status

Prefix traces, semilattice actions, trace semantics and cumulative scans are standard prior mathematics/CS. P023/A2 retains future-signature/precision ownership. This Draft owns only the explicit terminal-effect versus prefix-observable semantic boundary in the Stage131 line.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
