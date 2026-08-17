# R059D Stage AT3-HI — Proof

Researcher-ID: `EM-R059D-AT3HI-4D6B21`

Task: `RS-R059D-STAGE-AT3-HI-HIDDEN-INTERIOR-FIRST-APPEARANCE`

Taskbook source: `5c05b8127b70543ba3df2e5c28fcced862fb035e`

Frozen parent: `58e82206b691ac49c98307efd798f9cfd1a78bc7`

## 1. Scope before any census

The frozen foundation canonizes only

`CIRCLE_E(1)={O_E}`

with the four primitive unit invariants. For `n>=2`, the same foundation explicitly leaves open whether

`EXISTENCE_SPHERE_E(n)`

is the canonical higher Enterprise circle and how higher perimeter/area are generated.

Therefore no canonical `PERIMETER_PATH_FAMILY_E(n)` for all `n>=2` can be imported without either consuming the parallel AT3 main result or leaking historical AK/AL membership. The canonical first-hidden question is consequently underdefined at this frozen point.

The taskbook nevertheless requires every noncircular candidate trace to be audited. The strongest foundation-native candidate is the fixed-existence shell itself.

Everything below is an exact theorem for that explicitly typed arm:

`EXISTENCE_SHELL_INDUCED_CYCLE_TRACE + ALL_SHORTEST_GEODESIC_HULL`.

It is not promoted to canonical `CIRCLE_E(n)`.

## 2. Auxiliary A2 certificate

Use auxiliary A2 labels `(a,b) in Z^2` only as incidence/computation labels. Native coordinates are obtained through the already frozen signed-origin encoding. Auxiliary `0` never becomes native coordinate zero.

Primitive A2 neighbors are

`(a+1,b), (a-1,b), (a,b+1), (a,b-1), (a+1,b-1), (a-1,b+1)`.

Define

`h(a,b)=max(|a|,|b|,|a+b|)`.

The native graph distance from the glued origin is exactly `h`. Under the void-first foundation,

`ELL_E(P)=1+h(P)`.

Hence for existence level `n`, writing

`r=n-1`,

the fixed-existence endpoint shell is

`S_r={v:h(v)=r}`.

Let

`B_r={v:h(v)<=r}`.

## 3. Candidate perimeter shell is a unique support cycle

For `r=0`, `S_0={O_E}`.

For `r>=1`, the six Weyl sectors give six lattice side chains of `r` primitive edges each. Their union is `S_r`. Every shell vertex has exactly two native neighbors still in `S_r`, and the shell graph is connected. Therefore the induced shell graph is exactly

`C_(6r)`.

Consequences:

1. `|S_r|=6r` for `r>=1`.
2. The shell has exactly `6r` induced perimeter edges.
3. A primitive simple closed traversal of the induced shell graph must traverse the unique cycle support.
4. The only path-sequence freedom is start position and orientation. If retained as provenance there are `2*(6r)=12r` sequences.
5. All admitted candidate perimeter traversals have identical vertex and edge support.

Thus no `SOMETIMES_TRACED` shell vertex exists in this arm.

Freeze

`TRACE_CAND(n)=S_(n-1)`.

At `n=1`, ordinary graph trace edge count is zero although the primitive invariant `PERIMETER_E(CIRCLE_E(1))=1`; those are different types by the base-circle foundation.

## 4. Geodesic hull equals the full ball

The candidate interior is the taskbook's mandatory first audit:

`GEODESIC_HULL_CAND(n)`

= union of all vertices on all shortest `VOID_E -> P` segments for `P in S_r`.

Deleting the unique `VOID_E -> O_E` first edge gives the complete all-shortest spatial tail family.

### 4.1 Hull is contained in B_r

Every vertex on a shortest origin-to-`S_r` path has origin distance at most `r`. Therefore

`GEODESIC_HULL_CAND(n) subseteq B_r`.

### 4.2 Every B_r vertex occurs on a boundary geodesic

Take `v` with `h(v)=s<=r`. Choose a Weyl sector containing `v`. Within that sector there exists a primitive outward direction that increases `h` by exactly one while extending a shortest origin-to-`v` path. Repeat `r-s` times. This produces a shell endpoint `P in S_r` and a shortest path

`O_E -> ... -> v -> ... -> P`

of length `r`.

Prepending the unique existence edge gives a shortest `VOID_E -> P` segment containing `v`.

Therefore

`B_r subseteq GEODESIC_HULL_CAND(n)`.

Hence

`INTERIOR_CAND(n)=GEODESIC_HULL_CAND(n)=B_r`.

This proof uses only native adjacency and all-shortest-path semantics.

## 5. Exact hidden-set identities

By definition,

`HIDDEN_CAND(n)=B_r \ S_r`.

For `n=1`, this is empty.

For `n>=2`,

`B_r \ S_r = B_(r-1)`.

Therefore

`HIDDEN_CAND(n)=INTERIOR_CAND(n-1)`.

So current hiddenness begins immediately at `n=2`, with

`HIDDEN_CAND(2)={O_E}`.

But current hiddenness is not the principal lifetime notion.

The perimeter trace history is

`TRACE_HISTORY_CAND(n)=union_{k=1}^n TRACE_CAND(k)`

`= union_{s=0}^r S_s`

`= B_r`.

Since `INTERIOR_CAND(n)=B_r`,

`LIFETIME_HIDDEN_CAND(n)=INTERIOR_CAND(n) \ TRACE_HISTORY_CAND(n)=empty`

for every `n>=1`.

For `n>=2`,

`FRESH_HIDDEN_CAND(n)`

`= B_r \ (B_(r-1) union TRACE_HISTORY_CAND(n))`

`= B_r \ (B_(r-1) union B_r)`

`= empty`.

At `n=1` the base convention is likewise empty.

Thus there is no first fresh-hidden level in this arm.

## 6. Stronger generation-history theorem

Let `x` have shell index `s=h(x)`.

Then:

- `x` first belongs to the candidate interior at level `s+1`;
- at that same level `x in TRACE_CAND(s+1)=S_s`;
- every primitive perimeter realization at that level visits `x`, because the induced shell graph is one cycle;
- from level `s+2` onward, `x` is current-hidden because it lies strictly inside the new shell;
- nevertheless `x` remains in `TRACE_HISTORY` forever.

Hence every current-hidden point is hidden only **after** a perimeter exposure.

There is no candidate-arm vertex that first enters the interior without having belonged to a perimeter trace.

This proves the exact mechanism:

`BOUNDARY_AGING_OF_PREVIOUSLY_TRACED_GENERATIONS`.

## 7. D6 and orbit counts

The D6 action preserves `h`, hence every `S_r`, `B_r`, trace, interior and hidden identity.

For `r>=1`, a D6 fundamental half-sector contains

`floor(r/2)+1`

shell orbit representatives. Thus

`ORB_D6(S_r)=floor(r/2)+1`.

Including the origin, the number of D6 orbits in the ball is

- if `r=2m`: `(m+1)^2`;
- if `r=2m+1`: `(m+1)(m+2)`.

The current hidden orbit count at level `n>=2` is the ball-orbit count for `r-1`.

Fresh-hidden and lifetime-hidden orbit counts are always zero.

`S_r` is connected (a cycle for `r>=1`), and `B_(r-1)` is connected whenever nonempty.

## 8. Counting recurrence audit

For `n>=2`, define the taskbook's diagnostic perimeter trace count as the number of newly traced shell vertices:

`P_trace_count(n)=|S_(n-1)|=6(n-1)`.

This equals the ordinary shell-edge count for `n>=2`.

With

`A_naive(1)=1`,

`A_naive(n)=A_naive(n-1)+6(n-1)`

gives

`A_naive(n)=1+3n(n-1)`.

Independently,

`|B_(n-1)|=1+3(n-1)n`.

And because trace history partitions the ball into generation shells,

`|TRACE_HISTORY_CAND(n)|=|B_(n-1)|`.

Therefore in this candidate arm

`A_naive(n)=|TRACE_HISTORY_CAND(n)|=|INTERIOR_CAND(n)|`.

No hidden-support correction appears because fresh/lifetime hidden sets are empty.

This is **not** a proof that native `AREA_E(CIRCLE_E(n))` equals the vertex count. Higher native area remains underdefined independently of this counting identity.

## 9. Robustness over all perimeter traversals

Because the induced shell graph is exactly a cycle, all primitive closed perimeter traversals have the same support.

For the current shell:

- every shell vertex is `ALWAYS_TRACED`;
- none is `SOMETIMES_TRACED`;
- no interior vertex is `NEVER_TRACED` over trace history, because it was `ALWAYS_TRACED` at its own generation shell.

Thus the no-fresh-hidden result is not a clockwise/counterclockwise artifact.

## 10. Historical comparison after freeze

The candidate arm is not retroactively identified with historical AK/AL/N circles.

Post hoc, its internal-radius-`r` perimeter support has exactly `6r` edges/vertices. Historical N circumference was `6(r+J_N(r))`; therefore the two visible counts already diverge once historical `J_N(r)>0` (first at `r=5` under the accepted old formula). This confirms that the existence-shell arm is a genuinely separate diagnostic, not a hidden reuse of the old perimeter oracle.

The geodesic-hull interior is generated directly by the current all-shortest-path segment ontology. No first fresh-hidden point exists to classify against historical UP/DOWN, escape, or support objects.

## 11. Final logical status

Two statements must be kept together:

1. **Canonical status:** under the current frozen foundation, higher-circle perimeter/interior are not uniquely selected, so the canonical AT3-HI first-hidden level is underdefined.
2. **Exact noncircular arm theorem:** for the fixed-existence shell perimeter candidate and all-shortest geodesic hull interior,

   `FRESH_HIDDEN_CAND(n)=LIFETIME_HIDDEN_CAND(n)=empty`

   for every `n>=1`.

Current hidden points do occur from `n=2`, but every one is a previously traced generation that became interior when the boundary moved outward.

No source Euclidean inside/outside test, source angle, standard pi, AK tau, historical N membership, AL A8, or guessed area formula is used to define any set above.
