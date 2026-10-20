# E001/E002 — Predictive Boolean-Contact Bridge

Status: `ACTIVE CROSS-ROUTE ENGINEERING NOTE`  
Scope: E001 coarse-contact candidate under one-direction gap motion, compiled by the E002/P023 predictive quotient  
Dependencies: E001 `Contact_d(g) iff g<d`; E002 Stage-6 finite predictive quotient compiler

## 1. Purpose

E001 previously found that a current coarse contact bit is not generally future-sufficient: two positive gap details can both satisfy `g<d` now yet react differently after the same gap update.

This bridge turns that counterexample into an exact horizon-indexed result. It does **not** define rebound, material response, or full collision dynamics. The future observation language is only

`CONTACT / SEPARATE`.

## 2. Separating motion from the contact fiber

Fix contact precision `d>=1` and one positive separating step `a>=1`:

`g -> g+a`.

For a currently-contact gap `0<=g<d`, define the first exit sample

`tau_out(g) = ceil((d-g)/a)`.

Exactly at samples below `tau_out`, contact remains true; from `tau_out` onward it is false.

For horizon `h`, all exit times later than `h` are one terminal future class. Therefore the coarsest predictive rank is

`rho_out,h(g) = min(tau_out(g), h+1)`.

The exact class count inside the whole coarse contact fiber is

`C_out(h) = min(h+1, ceil(d/a))`.

The arbitrary-future Boolean-contact count is therefore

`C_out(infinity) = ceil(d/a)`.

Thus the original `d` fine integer gaps need not all survive for this query. When `a=1`, arbitrary-future contact history eventually exposes every gap. When `a>=d`, every current contact gap exits at the next sample and the whole contact fiber remains one predictive class even for arbitrary future time.

## 3. Closing motion from a separated shell

Now fix a separated shell

`g=d+j`, `0<=j<R`,

and one positive closing step

`g -> max(0,g-a)`.

The first entry sample is

`tau_in(j) = floor(j/a)+1`.

For horizon `h`, the coarsest predictive rank is

`rho_in,h(j) = min(tau_in(j), h+1)`

and the exact number of predictive classes in the width-`R` separated shell is

`C_in(h) = min(h+1, ceil(R/a))`.

The arbitrary-future count is

`C_in(infinity) = ceil(R/a)`.

So both sides of the same Boolean boundary have the same finite-horizon structure: the minimal state is a capped first-boundary-crossing time.

## 4. Relation to the old E001 counterexample

Take `d=3`, separating step `a=1`, and horizon one.

Both `g=0` and `g=2` are current coarse contact states. After one update:

- `0 -> 1` remains contact;
- `2 -> 3` becomes separate.

The current contact bit therefore has one class at horizon zero but must split into

`C_out(1)=min(2,3)=2`

classes when one future step is declared.

This is exactly the old E001 future-sufficiency failure, now embedded in a complete class-count law.

## 5. Compiler reconstruction

The generic Stage-6 compiler is given only:

- a finite gap state set;
- a saturating separating action `g -> min(G,g+a)`;
- observation `g<d`;
- a declared horizon.

It is not given the closed form above.

Tests require the compiler's number of blocks intersecting the initial contact fiber to equal

`min(h+1, ceil(d/a))`

across bounded integer domains. Stable compiler blocks must equal `ceil(d/a)`.

This makes the bridge a cross-domain falsification test for the predictive quotient compiler rather than a collision-specific duplicate of its logic.

## 6. Precision is query-relative, not arbitrary

For the Boolean contact future, the retained coordinate can be only the capped boundary-crossing time. This may be much smaller than the complete gap detail.

That does **not** license deleting gap information for every collision problem.

If a future response law reads any additional state, such as:

- exact penetration/clearance;
- impact phase;
- velocity or momentum;
- material/deformation state;
- response direction or rebound magnitude;

then the declared future language is richer and must be recompiled. The Boolean-contact quotient is safe only for the Boolean-contact language proved here.

## 7. Engineering interpretation

The result suggests a practical rule for a finite world engine:

1. declare the collision query and future motion language;
2. compile or derive the smallest predictive state for that language;
3. retain full gap/position detail only when the future operations actually read it;
4. refine when the declared horizon or response language expands.

For one-direction gap motion, the exact closed form avoids enumerating every fine gap:

`fine gap -> capped time-to-contact-boundary`.

This is a task-relative state compression, not a claim that the physical gap itself ceases to exist for every possible future operation.

## 8. Executable assets

- `src/enterprise_math/predictive_contact.py`
- `tests/test_predictive_contact.py`
- `experiments/e001_e002_predictive_contact_probe.py`

The tests independently compare the closed forms against direct Boolean future signatures and against the generic finite predictive quotient compiler.

## 9. Next pressure tests

1. allow both closing and separating actions and derive the predictive partition for arbitrary motion words;
2. add a response bit/rebound state and measure the exact extra precision required beyond contact alone;
3. lift from scalar gap to vector position while observing only pairwise collision predicates;
4. compare compiler-generated collision quotients with E001 hand-derived contact/carry summaries;
5. benchmark compiled Boolean-collision state against full fine-coordinate simulation.
