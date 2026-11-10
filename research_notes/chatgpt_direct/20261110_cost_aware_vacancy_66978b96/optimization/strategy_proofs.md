# Cost-aware vacancy evidence: exact control optima

Date: 2026-11-10, Asia/Hong_Kong. Status: author derivation with separately
identified finite integer control checks. Scientific parent:
`enterprise-math@9bb764203fcb2f1ec6ec5c82b76219f951c033f4`.

## 1. Original model and the optimized strategy class

There are `r >= 2` request slots, `M=r+1` legal colors per target,
`b=ceil(log2 M)`, `B=2^b`, and `q=(3M).bit_length()` full-key bits in the inherited
three-target instance. Target 0 has legal complete keys `1,...,M`. Put
`h=2^(b-1)`. Both `h` and `h+1` are legal and distinct because `b>=2` and
`h<M<=B`.

Every round has the prescribed business effects

```text
reserve target 0 -> bind slot 0 to the created source -> release source member 1.
```

The initial sources are absent. The source-conflict check, chosen creation word,
addressed binding word and source release word are the original inherited
programs. The control strategy chooses extra individual request-bit reads and
the safe complete key. It can place its extra reads before the round's one
conflict check. Every individual bit read costs eight original commands.

A complete key may be selected only when its absence follows for every request
table compatible with the actual observations and prescribed controlled updates.
Before the first creation, the initial request slots have no supplied key or
alias observations. Benchmark preparations below describe the actual input;
they are not free promises supplied to the controller. The strategy may read
any exposed bit position `0,...,q-1`. The original compiler exposes such readers already;
the previous `observe_next` restriction belonged to its low-prefix cache.

These conditions define the **fixed-business-word, individual-bit-observation
control class** used by the optimality statements. The exact statements optimize
observation and key choice at that interface. The triadic source and request
semantics remain those of the parent model. The native Cell/field/support bridge
remains the separately identified parent research unit.

## 2. The actual key weight includes the final binding bit

Let `pc(K)` denote the population count and `top(K)=bit_(b-1)(K)`. Once the
physical Boolean before creation is 1, the key-dependent cost of one complete
round is

\[
\boxed{w_b(K)=2\operatorname{pc}(K)+4(1-\operatorname{top}(K)).}
\]

The first population count is in the creation suffix. The second is in the
request identity write. The term `4(1-top(K))` is the actual output correction
after addressed binding, whose last physical read is bit `b-1`.

For default target 0 the conflict check has length 15, creation length is
`q+2+pc(K)`, binding length is

\[
8b+q+10+\operatorname{pc}(K)+4(1-\operatorname{top}(K)),
\]

and release length is 11. Therefore one round costs

\[
\boxed{D_r+w_b(K),\qquad D_r=8b+2q+38,}
\]

plus its extra request-bit reads. A creation reached with Boolean 0 adds four
commands. Reading extra request bits **before** the already required conflict
check makes the latter's successful result the actual Boolean immediately
before creation. It uses one conflict check and removes that correction cost.
The conflict check still governs whether source creation occurs.

The weight may also be written as an additive bit weight: coefficient `-2` on
bit `b-1`, coefficient `+2` on every other bit, and constant 4. Thus minimizing
numeric key or population count alone need not minimize the original word.

### Lemma 1: the two lowest round weights

Among all target-0 legal keys, `h` uniquely has weight 2; every other key has
weight at least 4, and `h+1` has weight 4.

**Proof.** A key with top bit zero has weight at least 6. A key with top bit one
has weight twice its population count. The sole population-one key with that
bit is `h`; `h+1` has population count two. Both are legal. This also covers
`M=B`: the additional endpoint key `B` has top bit zero and weight 6. ∎

## 3. A one-bit slab already contains an optimal reusable pair

Suppose the actual initial request keys, including zero for empty requests,
all satisfy

\[
\operatorname{bit}_{b-1}(K_i)=0.
\]

Read this bit once in each of the `r` slots. The `r` actual zero answers prove
that the residue slab

\[
S=\{x\in\mathbb Z/B\mathbb Z:\operatorname{bit}_{b-1}(x)=1\}
=[h,B)
\]

is free of all initial nonempty requests. In particular, it certifies `h` and
`h+1` simultaneously. All original BRC readers and their eight-command lengths
are unchanged. The proof stored by the controller has an arbitrary specified
bit position, rather than only a least-significant contiguous prefix.

After a round, slot 0 is the sole changed request slot. It retains the selected
key even though the source was released. Alternate

\[
\boxed{h,h+1,h,h+1,\ldots.}
\]

The other `r-1` requests remain outside the slab. At every step the alternating
key differs from slot 0's retained key. The newly overwritten key becomes free
again. Hence no later vacancy read is needed. This argument depends only on
the observed slab and actual prescribed updates, not on reconstructing the old
keys.

The initial requests may belong to different targets or be empty, and their
other bits may differ arbitrarily. Only the observed bit condition is used.

## 4. Exact optimum for every horizon

### Lemma 2: at least one initial observation per slot

Before the first safe key is selected in the class of Section 1, every initial
request slot must have supplied at least one request-bit observation.

**Proof.** If slot `i` has never been read, replace that slot's key by the
candidate complete key, leaving all other slots and sources unchanged. It is
an admissible request table and has the same observations and source-conflict
result. The candidate is retained in that completion, so its absence has not
been established. This contradicts the admissible selection rule. ∎

Thus every successful run of positive horizon pays at least `r` such reads,
or `8r` original commands. A known input promise or supplied initial aliases
would define different input information; neither is supplied here.

### Lemma 3: the exact weight lower bound over all legal key schedules

For `T>=1`, every safe selected-key sequence satisfies

\[
\boxed{\sum_{j=1}^T w_b(K_j)\ge3T-(T\bmod2).}
\]

**Proof.** Slot 0 retains the previous round's selected key. Therefore adjacent
selected keys differ. By Lemma 1, `h` is the unique weight-2 key and can occur
at most `ceil(T/2)` times. Every other selected key costs at least 4. Hence

\[
\sum_jw_b(K_j)\ge
2\lceil T/2\rceil+4\lfloor T/2\rfloor
=3T-(T\bmod2).
\]

The alternating `h,h+1` schedule attains equality. The argument considers all
legal keys, including keys not yet certified at a particular time. ∎

### Theorem 1: pointwise optimal cost on the observed high-bit family

Under the hypotheses of Sections 1 and 3, for every `T>=1` the minimum original
core-command total over the full stated control class is

\[
\boxed{C^*(r,T)=8r+(8b+2q+41)T-(T\bmod2).}
\]

**Proof.** Lemmas 2 and 3, plus the fixed original business words, give the
lower bound `8r+D_r T+3T-(T mod2)`. Any creation-output correction only adds
commands. Read the high bit of every initial slot before the first conflict
check, then use the schedule in Section 3. Its observation cost is exactly
`8r`, the conflict result before each creation is actually 1, and its weights
attain Lemma 3. Every term of the lower bound is attained. ∎

The same strategy attains this value for every horizon, without receiving `T`.
Thus horizon knowledge offers no further original-command saving on this
family in this interface. The acquisition and the continuing key schedule are
both optimal by separate lower bounds.

### The inherited two-cluster family

Let `r=2^b-2`, `b>=3`, and let half of the original requests retain key 2 and
half key 3. Their bit `b-1` is zero. Here `q=b+2`, so Theorem 1 becomes

\[
\boxed{C^*(r,T)=8r+(10b+45)T-(T\bmod2).}
\]

| r | T | Exact optimum in the stated control class |
|---:|---:|---:|
| 6 | 1 | 122 |
| 6 | 8 | 648 |
| 6 | 32 | 2,448 |
| 14 | 1 | 196 |
| 14 | 8 | 792 |
| 14 | 32 | 2,832 |

The numbers in this table are formula values. The original-core integration
records separately identify which preparations and horizons were physically
executed. `strategy_checks.json` checks the integer formulas, legal-key minima
and finite information states; it does not claim additional original-core runs.

## 5. What is optimal after committing to the previous low-prefix entry?

This section fixes a different, explicitly already acquired information state.
It explains the earlier crossover and the value of improving the entry itself.

Use the two-cluster family, let `k=r/2`, and suppose the previous first query
has already read `3k` bits. The `k` old even labels are known through bit 0;
the `k` old odd labels are known through bit 1 and have prefix `11`. The whole
class `P={x:x=1 mod4}` is certified empty, before the first creation.

Further observations in this section extend the original low-prefix labels one
next bit at a time. Any legal certified key may be chosen. The controller can
read any number of labels at any time; no single-switch assumption is imposed.

Put `a=h+1`, which is the unique weight-4 key in `P`. Every other odd key has
weight at least 6, and key 1 attains 6. With no newly certified even key, the
minimum cumulative key weight is therefore

\[
N(T)=4\lceil T/2\rceil+6\lfloor T/2\rfloor
=5T-(T\bmod2),
\]

attained by `a,1,a,1,...`. This corrects the earlier numeric-first choice
`1,5,1,5,...` without paying another observation.

After the first binding, the remaining `k-1` initial even labels are all still
potentially any even candidate. Every newly certified even key requires at
least one further observation from each. Thus its acquisition costs at least

\[
A=8(k-1)=4r-8.
\]

Reading their next bit, whose actual value is 1, proves the whole class
`E={x:x=0 mod4}` empty and certifies `h`. Both `P` and `E` observations are
retained. Acquire `E` before round 2 and alternate `a,h,a,h,...`. The cost
after the common `3k` initial observations and the fixed business-word
constant is

\[
I(T)=A+4\lceil T/2\rceil+2\lfloor T/2\rfloor
=A+3T+(T\bmod2)\quad(T\ge2).
\]

### Theorem 2: exact continuation optimum after the fixed P entry

For `T=1`, the minimum additional key/observation cost is 4. For `T>=2`, it is

\[
\boxed{\min\{N(T),I(T)\}.}
\]

**Proof.** If no even key is ever used, all selected keys are odd; the unique
weight-4 odd key cannot be used consecutively, so `N(T)` is a lower bound.
Extra odd-key observations cannot lower that bound.

If the first even key is used after `j>=1` initial rounds, at least `A` read
cost has been paid, regardless of how those observations were split up or
interleaved. The first `j` odd rounds have weight at least `N(j)`. The final
`T-j` rounds have weight at least `3(T-j)-((T-j) mod2)` by Lemma 3. Consequently
the total is at least

\[
A+3T+2j-(j\bmod2)-((T-j)\bmod2).
\]

For every `1<=j<T`, this is minimized at `j=1`, giving `I(T)`. Indeed, subtract
the `j=1` value: for even `T` the difference is `2j-2(j mod2)`, and for odd
`T` it is `2j-2`; both are nonnegative and vanish at `j=1`.

If an even key is used in the first round, all `k` old even labels remain and
at least `8k=A+8` observation cost is required. Even granting the global weight
minimum gives `A+8+3T-(T mod2)`, which exceeds `I(T)` by 8 for even `T` and by
6 for odd `T`. For `T=1` it exceeds 4. Thus that case cannot improve the claimed
minimum. The two displayed schedules attain both alternatives. ∎

The exact comparison is

\[
\boxed{I(T)-N(T)=A-4\lfloor T/2\rfloor.}
\]

The equality horizons are `T=2r-4` and `T=2r-3`: 8/9 for six slots and 24/25
for fourteen slots. These belong to the fixed P-entry continuation problem.
The arbitrary-bit entry of Theorem 1 obtains a lower cost directly.

### An intermediate improvement within low-prefix acquisition

For `b>=4`, after the initial parity split one may probe the even group next,
without requiring that its candidate count already exceed its blocker count.
The actual next bits certify `E={0 mod4}` after the same `3k` total reads.
The legal keys `h,h+4` have weights 2 and 4 and alternate safely. Any first
safe key under sequential low-prefix observations costs at least `3k` reads:
all `2k` slots need the parity bit, and the `k` labels of the candidate's parity
need at least one further bit. Thus, for `b>=4`, this entry attains the exact
optimum of the whole sequential-low-prefix class:

\[
\boxed{C^*_{\rm low}(r,T)=24k+D_rT+3T-(T\bmod2).}
\]

The arbitrary-bit high-slab entry saves exactly `8k=4r` commands against it,
while the ensuing optimal weight schedules coincide in cost. For `b=3`, `E`
contains only one legal target-0 key; the stated intermediate theorem uses
`b>=4`. Theorem 1 already covers `b=3` through its high-slab pair `4,5`.

## 6. Finite integer verification

`strategy_checks.py` verifies:

1. All legal-key weights for `r=2,...,63`, the unique weight-2 key, and a dynamic
   program over **all** legal keys and all horizons through 64 with adjacent
   equality excluded. It checks the exact global weight minimum.
2. Every compatible bit-mask state on the declared small actual high-slab
   preparations, including the exact witness showing that fewer than `r`
   queried slots cannot certify any first key.
3. The fixed-P-entry schedules, all potential first-even-use times and the
   before-first acquisition case over `b=3,...,8` and horizons through 256.
4. The fixed-word arithmetic values used for the inherited cost comparisons.

All calculations are integer and the result file declares its actual domain.
The general assertions above are proved by their stated arguments. Original
BRC words and resulting full states are checked by the separately recorded
integration program.

## 7. Exact finite-horizon minimax planning over masked observations

This section describes the separate knowledge-state planner implemented in
`bellman_planner.py`. It permits `r>=1`, uses the `b` low residue bits, and
certifies a chosen residue only when every request slot excludes it. Complete
key identity is still used for business writes and key weight. The planner's
observation interface is therefore the declared residue-absence interface;
Theorem 1's complete-key-safe control class permits more information and is
larger. The family attaining Theorem 1 lies in both interfaces.

### Knowledge states and permitted round language

Let

\[
S=((m_i,v_i))_{i=0}^{r-1},\qquad v_i\mathbin{\&}\neg m_i=0,
\]

where the set bits of `m_i` identify observed low-bit positions, and `v_i`
contains their actual answers. The compatible residue tables are exactly the
Cartesian product

\[
\Gamma(S)=\prod_i\{x\in[0,B):x\mathbin{\&}m_i=v_i\}.
\]

The prescribed target sequence is `t_0,...,t_(T-1)`. Each round creates that
target, binds slot 0 to its actual key and releases its source. It has the
already declared source-availability conditions. There are no supplied alias
correlations between the initial slots, and the round language introduces no
cross-slot copies. Thus the product knowledge representation is exact for this
interface.

The candidate complete keys at position `a` are

\[
\mathcal K_a=\{1+t_aM,\ldots,(t_a+1)M\}.
\]

Write `rho(K)=K mod B`. A candidate is certified when

\[
\forall i:\quad(v_i\mathbin{\oplus}\rho(K))\mathbin{\&}m_i\ne0.
\]

The actual slot-0 update sets its pattern to `(B-1,rho(K))`. This records all
low bits of the business key that the controller itself selected and whose
binding is delivered by the original program. Any unobserved bits of the old
slot-0 request are retired by the prescribed overwrite; they cannot influence
future residue observations.

### The Bellman recurrence

Let `V(S,a)` count the minimum worst-case sum of additional request reads and
key-dependent business weights for the remaining suffix. The fixed original
business-word constants are added separately. Put `V(S,T)=0`.

For every unread `(i,j)`, let `S[i,j←epsilon]` be the state extended by the
actual bit answer `epsilon`. For a legal certified key, let `W_0(S,K)` replace
slot 0 by its fully known residue. Then

\[
\boxed{
V(S,a)=\min\left\{
\begin{array}{l}
w_b(K)+V(W_0(S,K),a+1),\quad K\in\mathcal K_a\text{ certified};\\[2pt]
8+\displaystyle\max_{\epsilon\in\{0,1\}}
V(S[i,j\leftarrow\epsilon],a),\quad j\notin m_i.
\end{array}\right.
}
\]

An unread bit has both answers among the compatible residues. The maximum is
taken **after** the chosen query, and each successor has its own optimized
continuation. This order lets the policy adapt to an actually returned bit.
The outer minimum chooses the next control action without that unseen answer.

The weight uses the complete key:

\[
w_b(K)=2\operatorname{pc}(K)+4(1-\operatorname{bit}_{b-1}(K)).
\]

Its population count includes carries and all bits above the low residue. For
example, complete keys differing by `B` can have the same residue but different
creation and binding write lengths. Applying the weight to `rho(K)` would
discard part of the actual original-command cost.

### Theorem 3: correctness and termination of the recurrence

For a finite target sequence, the recurrence terminates and equals the minimum
worst-case variable original-command cost over the stated residue-interface
policies. Its minimizing actions form an executable policy that consumes
actual bit answers.

**Proof.** Let `L=T-a` and let

\[
U(S)=rb-\sum_i\operatorname{pc}(m_i).
\]

Every query keeps `L` fixed and decreases `U` by one. Every creation decreases
`L` by one and makes slot 0 fully known, so `U` does not increase. Consequently
the nonnegative integer rank `(rb+1)L+U` strictly decreases along every edge.
This proves well-founded recursion. A coarse state bound is
`(T+1)3^(rb)`: each bit is unknown, observed zero or observed one.

At full observation each target has `M=r+1` distinct legal residues and there
are at most `r` occupied residues. Hence at least one candidate is certified.
Repeatedly revealing unread bits and then using such a candidate gives a finite
policy, so the minimum is always finite.

Prove equality to the minimax value by induction on the rank. Any policy's next
action is either a certified creation or an unread-bit query. A creation has
the displayed immediate cost and a deterministic successor. A query pays eight
commands and faces either compatible answer, after which it may use a separate
continuation policy. The induction hypothesis gives exactly the scores in the
recurrence. Every policy is bounded below by the minimum of those scores;
choosing a minimizing action and the minimizing successor policies attains it.

The adversarial choices at successive query nodes can be realized by a single
compatible initial table. Along a run, repeated observations agree and each
unread query fixes one previously free bit. An old slot-0 value can be completed
arbitrarily after it is overwritten; the surviving slots retain their compatible
patterns. No observation introduces a cross-slot correlation. Thus every
adversarial path used by the maximum has a consistent initial residue table,
and the recurrence's worst case is also a worst case over static initial inputs.
The prescribed deterministic writes then realize the rest of that path. ∎

Putting the planner's query block before the round's required source-conflict
check yields a physical last Boolean of 1 whenever that round creates a source.
For any target `t`, the key-independent constant can be taken from the original
compiled words as

\[
D_t=|\mathrm{free}_t|+(q+2)+(8b+q+10)+|\mathrm{release}_t|.
\]

Adding `sum_a D_(t_a)` to the planner value therefore gives the corresponding
worst-case full core-command total under this business-word schedule. The
planning computation itself is a separately measured control/preprocessing
cost. The finite state bound makes exact small-domain policy generation useful;
it does not remove that state-space cost.

Theorem 3 minimizes the worst initial-input cost. Theorem 1 instead exhibits one
policy that attains a universal lower bound at every actual input in its stated
high-bit family and at every horizon. These are two explicit optimization
quantifiers, both supported by their own constructions.
