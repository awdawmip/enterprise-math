# Structure-First Compiler from Small Local Precision to Exact Infinite Traces

Status: `RESEARCH BRIDGE / NONCANONICAL`

A finite relation system offers two exact routes to its natural path-count trace semantics.

One route observes increasingly large accumulated counts directly. The other retains enough branching structure that **small local counts become exact**, then derives arbitrarily large future counts inside the recovered weighted machine.

The second route proves an important precision principle:

> large derived values do not necessarily require equally large observational coefficient range if the state retains the compositional structure that generates them.

## 1. Exact count-stable branching quotient

Let E be the stable natural-count branching equivalence.

For each action a, source E-class D and target E-class C define

`B_a[C,D] = #{ y in C : x R_a y }`,

for any representative `x in D`.

Count-stability makes this number representative-independent.

Therefore every raw relation action descends to an integer weighted transition matrix B_a on the finite quotient classes.

This quotient is not merely observational. It is an exact executable weighted machine.

## 2. Exact path-count factorization through the weighted quotient

Start with one raw source state x and its quotient class D.

After one action, B_a gives exactly how many raw successors of x land in every quotient class.

Assume a quotient count vector exactly represents the number of raw paths currently ending in each class. Multiplying by the next weighted matrix sums, for every old class, the number of paths times the representative-independent number of raw successors into each new class.

By induction, for every literal word w:

`raw path counts by quotient/observation class`

are exactly equal to

`weighted quotient matrix path counts`.

The owner branch contains a separate oracle that compares raw dynamic-programming traces with quotient matrix execution for exhaustive tiny relation families.

## 3. Small modular branching precision reconstructs the exact weighted machine

Let

`Delta=max raw outdegree`.

The finite count-branching cutoff theorem says every modulus

`M>Delta`

produces exactly the same branching refinement sequence and final partition as natural counts.

On that final partition, every local target-block weight is an integer in

`0..Delta`.

Its mod-M residue therefore has one unique lift back into that interval.

Consequently a mod-M branching representation with `M>Delta` determines:

- the exact natural count-stable state partition;
- every exact integer quotient transition weight;
- hence the complete exact weighted quotient machine.

No larger arithmetic observation is needed to identify those local laws.

## 4. Exact infinite traces can then be generated internally

Once the exact integer quotient matrices B_a are recovered, future path counts are obtained by ordinary exact integer matrix multiplication.

These derived integers may become much larger than M.

This does not contradict the observational cutoff because M was only used to identify the **local one-step coefficients**, all of which were bounded by Delta.

The larger values are deterministic consequences of the recovered exact machine, not additional hidden measurements.

Thus:

`small local coefficient precision + compositional structure`

can generate

`unbounded derived exact count values`.

## 5. Trace-equivalence closure can run on quotient dimension

Let

`b=#(exact count-branching classes)`.

The weighted quotient has b states. Current observation is constant on every branching class because the quotient refines the original observation.

Run rational terminal-trace row-space closure on the b-dimensional weighted matrices.

If the observation has `c_0` independent classes, the quotient trace closure stabilizes by

`b-c_0`,

rather than the raw-state bound

`n-c_0`.

So exact branching minimization can reduce both:

- arithmetic observation range;
- linear trace-analysis dimension/horizon.

## 6. Pullback recovers the raw infinite trace partition

The quotient rational closure produces a terminal-trace equivalence among branching quotient classes.

Take the pullback of that partition along

`raw state -> count-branching class`.

Because all raw word counts factor exactly through the weighted quotient, the pullback equals the raw infinite exact natural terminal-trace partition.

The executable compiler asserts this equality directly against the independent raw rational-trace compiler.

## 7. Twenty-to-two dimension-collapse witness

Use twenty raw states:

- ten states `a_i`, each with one successor to one terminal-type state;
- ten states `b_j`, all with no successor;
- constant present observation.

Raw state count:

`n=20`.

Exact count branching has only two classes:

- all `a_i`;
- all `b_j`.

So

`b=2`, `Delta=1`.

### Raw theorem bound

With one current observation class, the generic raw trace dimension bound is

`n-c_0=19`.

### Structure-first quotient

mod2 is already exact because `2>Delta`.

The recovered weighted quotient has two states and trace closure bound

`b-c_0=1`.

It actually stabilizes in one step.

Thus the structural quotient reduces a nominal 20-state trace analysis to a two-state weighted machine while using only one-bit local count precision.

## 8. Fixed branching-versus-trace witness

For the earlier Delta=2 world:

- mod3 exactizes branching structure;
- direct mod3 terminal traces are wrong because `4==1 mod3`;
- structure-first mod3 recovers the exact local quotient matrices;
- quotient execution then produces exact integer path totals 4 and1;
- rational quotient analysis recovers the exact infinite trace partition.

So **the same mod3 data is insufficient as a flattened terminal trace but sufficient as a structured branching machine state**.

This is the cleanest direct proof that precision cannot be classified by modulus alone.

## 9. Direct-trace route versus structure-first route

### Direct trace observation

To reflect every terminal count through closure horizon h, a safe modulus is

`M > Delta^h`.

The representation stores little branching structure but asks the coefficient channel to carry the accumulated value.

### Structure-first route

Use only

`M > Delta`

to reconstruct the exact weighted branching quotient. Then calculate all future counts inside that quotient using exact arithmetic.

The representation stores more compositional structure and therefore needs less observational arithmetic range.

These are two exact implementations of different precision resource allocations.

## 10. This is not free exact arithmetic from a lossy residue

The unique lift from mod M to exact local count uses an explicit prior bound:

`0 <= local count <= Delta < M`.

Without that bound, a residue would not determine its integer lift.

So the compiler follows the general reflection architecture already established elsewhere:

`quotient value + independent finite bound -> exact local reflection`.

The new point is that once the **local law** is reflected exactly, compositional structure propagates it to unbounded future derived values.

## 11. Relation to Markov/state sufficiency

The weighted branching quotient is a sufficient continuation state for the count-valued relation interface.

A terminal trace value is only one output of that state under one word.

Flattening the machine into outputs can increase the numeric range required to represent those outputs even while it removes structural state.

This is another exact instance of the project principle:

> a sufficient state and a sufficient answer are different objects.

## 12. Prior-art boundary

Equitable partitions, weighted lumping, quotient automata, integer matrix path counting and observability reduction are standard prior mathematics/computer science. A4 retains relation/witness ownership; P023/A2 retains future-signature and precision ownership.

The project value is the exact compiler/resource theorem:

> **modulus `Delta+1` plus exact branching structure is enough to reconstruct the weighted quotient and thereby generate the complete infinite exact natural path-count language, even when the same small modulus is insufficient for flattened terminal count traces.**