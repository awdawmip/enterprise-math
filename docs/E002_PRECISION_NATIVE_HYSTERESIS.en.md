# E002 — Precision-Native Threshold Control and Hysteresis

Status: `ACTIVE ENGINEERING RESEARCH`  
Program: `E002`  
Scope: finite integer threshold control, chattering pressure test, task-relative precision sufficiency  
Novelty: `NOVELTY_UNVERIFIED`

## 1. Engineering question

E002 asks whether a common control-engineering patch can be reconstructed from the finite-precision ontology rather than inserted after the fact.

A memoryless relay at target zero changes state whenever the measured signed error changes sign. Under finite measurement disturbance this can chatter rapidly. Classical engineering already uses hysteresis, deadbands, hysteretic quantizers, filters, dwell times, and related mechanisms to prevent unwanted switching. Hysteretic quantization and chattering suppression are established prior art, not an Enterprise Math invention [SRC-CERAGIOLI-DEPERSIS-FRASCA-2011-HYSTERESIS] [SRC-DEPERSIS-MAZENC-2010-QUANTIZED-HYSTERESIS].

The Enterprise Math pressure test is narrower:

> If precision is already part of the represented state, does a target-centered precision fiber induce the same finite switching geometry without separately postulating an epsilon band?

The answer is partly yes and partly no. Precision collapse creates the indistinguishable target region. Hysteresis additionally requires a response law that preserves the previous relay state inside that region. Once plant dynamics are admitted, the coarse region label is not in general sufficient to predict the future; bounded repair detail may have to be retained.

## 2. Integer model

Let the signed target error be

\[
e\in\mathbb Z,
\]

and let the explicit precision half-width be

\[
d\in\mathbb N_{>0}.
\]

Define the target-centered observation

\[
H_d(e)=
\begin{cases}
\mathrm{BELOW}, & e\le -d,\\
\mathrm{COLLAPSED}, & -d<e<d,\\
\mathrm{ABOVE}, & e\ge d.
\end{cases}
\]

Let the relay state be

\[
u\in\{\mathrm{OFF},\mathrm{ON}\}.
\]

The E002 response law is

\[
R_d(e,u)=
\begin{cases}
\mathrm{ON}, & e\le-d,\\
u, & |e|<d,\\
\mathrm{OFF}, & e\ge d.
\end{cases}
\]

The three layers are deliberately separated:

\[
\boxed{
\text{precision collapse}
\to
\text{finite observation}
\to
\text{response law}
\to
\text{next state}.
}
\]

This mirrors the separation already exposed by E001 between collapse contact and the selected collision response. Precision determines which differences are represented; it does not by itself choose what an actuator must do.

## 3. E002-T01 — Target-centered precision partition

Status: `PROVED`.

For every integer `d>=1`, the three regions above form a partition of `Z`. The collapsed fiber is exactly

\[
\{-d+1,-d+2,\ldots,d-1\},
\]

so its cardinality is

\[
\boxed{2d-1}.
\]

The observation is sign symmetric: reflecting `e` to `-e` swaps `BELOW` with `ABOVE` and fixes `COLLAPSED`.

This target-centered construction avoids dependence on an arbitrary global quotient origin. It is a relation to the declared control target, not a claim that every application must use the same scalar precision axis.

## 4. E002-T02 — Precision plus persistence is a hysteretic relay

Status: `PROVED BY DEFINITIONAL EQUIVALENCE`.

The response `R_d` is exactly the ordinary symmetric two-threshold relay with lower switching threshold `-d`, upper switching threshold `+d`, and state persistence between the thresholds.

Therefore E002 does not claim a new hysteresis input-output law. Its engineering distinction exists only when `d` is already an intrinsic resolution coordinate of the represented variable. If `d` is tuned solely to suppress chatter, the construction is simply a symmetric classical hysteresis relay written in Enterprise Math notation.

This is an important falsification boundary: a benchmark against the mathematically equivalent classical relay must produce identical trajectories.

## 5. E002-T03 — Exact bounded-noise immunity threshold

Status: `PROVED`.

Assume the true target error is zero and measurement disturbance is an arbitrary integer

\[
\eta\in[-N,N],
\qquad N\in\mathbb N.
\]

The current relay state is preserved for every admissible disturbance if and only if

\[
\boxed{d>N}.
\]

Hence the smallest integer precision with complete target-noise immunity is

\[
\boxed{d_{\mathrm{noise}}=N+1}.
\]

Proof. If `d>N`, every admissible disturbance satisfies `|eta|<d`, so every measurement remains in the collapsed fiber and persistence keeps the state unchanged. Conversely, if `d<=N`, the admissible disturbance `+d` reaches the upper switching threshold and `-d` reaches the lower switching threshold. At least one initial relay state can therefore be changed. No limiting argument or hidden real-valued epsilon is required. ∎

## 6. E002-T04 — Switch-spacing theorem

Status: `PROVED`.

Let a measured-error sequence satisfy

\[
|e_{t+1}-e_t|\le V,
\qquad V\in\mathbb N_{>0}.
\]

Two consecutive relay switches must be separated by a traversal from one threshold side to the other. The endpoint errors therefore differ by at least `2d`. If the two switch times are `s<t`, then

\[
(t-s)V\ge 2d.
\]

Thus

\[
\boxed{
t-s\ge\left\lceil\frac{2d}{V}\right\rceil.
}
\]

The implementation evaluates this ceiling by integer division only.

A direct corollary is that if `V<2d`, opposite switching cannot occur on consecutive samples.

## 7. E002-T05 — Total-variation switch bound

Status: `PROVED`.

For a finite measured-error sequence, define the integer total variation

\[
\operatorname{TV}(e)=\sum_t |e_{t+1}-e_t|.
\]

If the relay switches `K` times, every interval between two consecutive switches consumes at least `2d` variation. Those intervals are disjoint, so

\[
(K-1)2d\le \operatorname{TV}(e).
\]

Therefore

\[
\boxed{
K\le 1+\left\lfloor\frac{\operatorname{TV}(e)}{2d}\right\rfloor.
}
\]

The first switch need not consume a full threshold-to-threshold traversal because the initial state may be inconsistent with the first sample; this is why the bound contains the leading `1`.

## 8. E002-T06 — Exact disturbance relation and MAY/MUST bands

Status: `PROVED`.

Now let the true error be `x` and the measured error be

\[
x+\eta,
\qquad -N\le\eta\le N.
\]

For current state `OFF`:

- output is MUST `ON` when `x<=-d-N`;
- output is MUST `OFF` when `x>=-d+N+1`;
- both outputs are possible in the finite strip

\[
-d-N+1\le x\le-d+N.
\]

For current state `ON`:

- output is MUST `ON` when `x<=d-N-1`;
- output is MUST `OFF` when `x>=d+N`;
- both outputs are possible in the strip

\[
d-N\le x\le d+N-1.
\]

If `d>N`, the two persistence certificates overlap around the target on

\[
\boxed{
-d+N+1\le x\le d-N-1,
}
\]

which contains exactly

\[
\boxed{2(d-N)-1}
\]

integer true-error states.

This gives an exact finite MAY/MUST control relation under bounded measurement disturbance rather than a probabilistic noise model.

## 9. E002-T07 — Coarse relay state is not future-sufficient

Status: `COUNTEREXAMPLE PROVED`.

The pair

\[
(H_d(e),u)
\]

is sufficient to determine the immediate relay output, but it is not generally sufficient for future thermostat evolution.

Take

\[
d=2,
\qquad h=1,
\qquad c=1,
\qquad u=\mathrm{ON},
\]

where an `ON` plant step adds `h` to the error and an `OFF` step subtracts `c`.

The two errors

\[
e=0
\qquad\text{and}\qquad
e=1
\]

have the same coarse observation `COLLAPSED`, the same input mode `ON`, and the same immediate output `ON`. After one identical `ON` plant update, however,

\[
0\mapsto1
\qquad\text{while}\qquad
1\mapsto2.
\]

At the next decision, error `1` remains `ON` while error `2` reaches the upper threshold and switches `OFF`.

Thus the current collapsed label erased detail that the declared future plant operation later reads. This is the threshold-control analogue of E001's already observed fact that a coarse contact bit need not be future-sufficient under gap updates. The general lesson belongs to the future-sufficiency program rather than to E002 alone.

## 10. E002-T08 — One-bit repair for one additional thermostat decision

Status: `PROVED FOR THE DECLARED ONE-STEP FUTURE LANGUAGE`.

For positive plant increments `h,c`, first compute the current relay output

\[
u'=R_d(e,u).
\]

Define one witness bit

\[
W=
\begin{cases}
1, & u'=\mathrm{ON}\text{ and }e+h\ge d,\\
1, & u'=\mathrm{OFF}\text{ and }e-c\le-d,\\
0, & \text{otherwise}.
\end{cases}
\]

Then the repaired finite key

\[
\boxed{(H_d(e),u,W)}
\]

determines both the current relay output and the relay output at the next sampled decision.

Whenever one coarse `(H_d(e),u)` class contains states with both values of `W`, at least two distinguishable repair states are necessary to represent the two different future output pairs. In that restricted cardinality sense, one bit is minimal for this one-step output language.

This theorem must not be generalized silently. A longer future horizon or a richer plant operation language may require more detail. E002 therefore treats it as a task-relative specialization of the broader future-sufficiency problem.

## 11. E002-T09 — Finite absorbing band and eventual periodicity

Status: `PROVED`.

Consider the noiseless deterministic thermostat update:

1. evaluate `u'=R_d(e,u)`;
2. if `u'=ON`, set `e'=e+h`;
3. if `u'=OFF`, set `e'=e-c`,

with positive integers `h,c`.

Define

\[
B=[-d-c+1,\ d+h-1]\cap\mathbb Z.
\]

Then `B x {OFF,ON}` is forward invariant. Moreover every starting error outside `B` enters `B` after finitely many steps: sufficiently high states repeatedly decrease by `c`, and sufficiently low states repeatedly increase by `h`; the first entry cannot jump across the entire finite band.

Because the restricted state space is finite and the update is deterministic, every noiseless trajectory is eventually periodic.

This is a negative boundary as well as a positive theorem:

> eliminating rapid chatter does not imply convergence to a fixed point.

Established on-off control literature likewise distinguishes chattering avoidance from possible limit-cycle behavior [SRC-KASIS-MONSHIZADEH-LESTAS-2021-ONOFF]. E002 does not claim that its periodicity theorem is a new discovery of control-theoretic limit cycles; it records the exact finite consequence of this particular integer world engine.

## 12. E002-T10 — Switch-return arithmetic

Status: `PROVED`.

An upper switching sample must lie in

\[
H\in[d,d+h-1].
\]

Starting from such an upper switch, the exact number of `OFF` plant steps before the lower threshold is reached is

\[
m=\left\lceil\frac{H+d}{c}\right\rceil,
\]

and the lower switching sample is

\[
L=H-mc
\in[-d-c+1,-d].
\]

The exact number of subsequent `ON` plant steps is

\[
n=\left\lceil\frac{d-L}{h}\right\rceil,
\]

and the next upper switching sample is

\[
H'=L+nh
\in[d,d+h-1].
\]

Furthermore

\[
H'-H=-mc+nh,
\]

so

\[
\boxed{
H'\equiv H\pmod{\gcd(h,c)}.
}
\]

When `h=c=s`, the upper window contains exactly one representative of each residue modulo `s`. Residue invariance therefore forces

\[
\boxed{H'=H}.
\]

The switching cycle is then locked to its upper switching sample after one full OFF/ON excursion.

## 13. Engineering benchmark

The executable benchmark uses a deterministic 200-sample disturbance cycle

```text
(2, -2, 1, -1, 2, -2, -1, 1)
```

with unit heating/cooling steps and initial physical error zero.

The current smoke result is:

```text
samples=200
precision=4
memoryless_switches=150
precision_switches=33
classical_symmetric_hysteresis_switches=33
measured_total_variation=550
measured_max_step=5
guaranteed_switch_spacing=2
observed_min_switch_spacing=5
variation_switch_bound=69
physical_error_min=-3
physical_error_max=4
```

The exact trajectory equality between E002 and the classical symmetric hysteresis comparator is intentional. The benchmark rejects any claim that merely renaming the same relay law creates a performance advantage. Its useful comparison is against the memoryless sign relay and against the hypothesis that a separate deadband parameter is unnecessary when the represented variable already carries the same intrinsic precision `d`.

The variation and spacing bounds are universal integer certificates for the measured sequence; they are not fitted to the observed switch count.

## 14. Relation to E001, P018, and P023

E001 and E002 now expose the same four-stage architecture in different engineering domains:

```text
finite precision collapse
-> scale-level observable
-> declared response law
-> finite next state
```

For E001, a positive spatial clearance can collapse to coarse contact and trigger a collision response. For E002, a signed target error can collapse to a target-equivalence fiber and trigger persistence.

The second shared lesson is more important: a coarse observable that is sufficient now may be insufficient after a declared future update. E001 found this for contact under gap addition; E002 finds it for a collapsed target error under plant motion. P018 already supplies exact quotient/detail/carry language for information crossing precision fibers. The general criterion for what may be safely forgotten belongs to the task-relative future-sufficiency line, not to a collision-specific or thermostat-specific remainder calculus.

E002 should therefore consume general future-sufficiency theorems and contribute concrete engineering specializations, counterexamples, and benchmarks back to that line.

## 15. Prior-art boundary and novelty status

Hysteresis, hysteretic quantizers, relay deadbands, and their use in reducing or preventing chattering are established control ideas [SRC-CERAGIOLI-DEPERSIS-FRASCA-2011-HYSTERESIS] [SRC-DEPERSIS-MAZENC-2010-QUANTIZED-HYSTERESIS]. Hysteretic on-off control can also retain nontrivial limit-cycle behavior [SRC-KASIS-MONSHIZADEH-LESTAS-2021-ONOFF].

E002 therefore makes no historical priority claim for the relay law or for chatter suppression.

The project-specific question is the finite-only synthesis:

\[
\boxed{
\text{intrinsic represented precision}
+
\text{target-centered collapse}
+
\text{persistence response}
+
\text{exact integer switching certificates}
+
\text{future-sufficiency repair}.
}
\]

Whether this integrated interpretation has historical novelty is `NOVELTY_UNVERIFIED`. More importantly, its engineering value must be tested in systems where the precision coordinate is independently justified by sensing, actuation, representation, or physical resolution. Otherwise `d` is merely a renamed tuning parameter.

## 16. Next pressure tests

The next high-value E002 tests are deliberately chosen to attack the interpretation rather than protect it:

1. multi-level relays and quantized actuators, where one symmetric two-state band is insufficient;
2. asymmetric heating/cooling and asymmetric measurement precision;
3. actuator delay and finite transport lag, to test how much future repair state is required;
4. multiple coupled thermostats or load controllers, where local persistence may create collective oscillations;
5. adaptive precision, with an explicit rule for when the world engine coarsens or refines the control variable;
6. comparison with a fixed classical hysteresis controller when the sensor precision changes independently;
7. exact state-minimization for finite future horizons, consuming the general future-sufficiency machinery rather than inventing route-local indexes;
8. hardware or fixed-point implementation benchmarks measuring switching, energy, memory, latency, and arithmetic cost without floating point.

A successful E002 route is not one that always reduces switching. It is one that states exactly when finite precision is sufficient, when it is not, what minimal additional state is required for the declared future language, and which observed behavior differs from an ordinary independently tuned hysteresis controller.
