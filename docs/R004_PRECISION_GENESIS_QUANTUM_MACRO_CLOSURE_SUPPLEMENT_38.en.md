# R004 precision genesis — Supplement 38: collision polynomial sufficiency and depth-shell birth

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + P011-SECOND-ORDER BRIDGE`
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_37.en.md`

Supplement 37 identified which null-code profiles are needed to compute bounded program collisions. This supplement asks what the complete collision hierarchy itself remembers and what it still forgets.

## 1. Collision polynomial equals the multiplicity histogram transform

For a fixed readout budget D, let

`N_D(y)=# short primitive programs producing semantic action y`.

Define

`W_k(D)=sum_y binom(N_D(y),k)`

including `W_0(D)=# semantic labels`, and the polynomial

`C_D(z)=sum_k W_k(D) z^k`.

Then

`C_D(z)=sum_y (1+z)^(N_D(y))`.

Let

`h_m(D)=#{y:N_D(y)=m}`.

Then

`W_k(D)=sum_(m>=k) h_m(D) binom(m,k)`.

Finite binomial inversion gives

`h_m(D)=sum_(k>=m)(-1)^(k-m) binom(k,m) W_k(D)`.

Therefore the full collision hierarchy at one depth is exactly equivalent to the **unlabeled multiplicity histogram** of the short-program fibers.

It is stronger than any fixed finite list of moments, but weaker than the labeled map `y -> N_D(y)`.

## 2. Endpoint boundaries

At depth zero only the zero instruction word is available, so one semantic label has multiplicity one and all others zero.

At full binary depth `D=s`, every coefficient word is available. If the semantic map is surjective with null-code size `|C|=2^(s-r)`, every semantic action has exactly `|C|` programs. Hence

`W_k(s)=2^r binom(|C|,k)`.

The depth filtration therefore runs from a maximally sparse multiplicity histogram to a uniform full-coset histogram.

## 3. Depth-shell birth decomposition

Let

`A_D(y)=#{e: wt(e)=D, H e=y}`.

Then

`N_D(y)=N_(D-1)(y)+A_D(y)`.

By Vandermonde,

`W_k(D)-W_k(D-1)`

`= sum_y sum_(j=1)^k binom(A_D(y),j) binom(N_(D-1)(y),k-j)`.

Define the j-new-program birth component

`J_(k,j)(D)=sum_y binom(A_D(y),j) binom(N_(D-1)(y),k-j)`.

Then

`Delta W_k(D)=sum_(j=1)^k J_(k,j)(D)`.

For k=2:

- `J_(2,1)=sum_y A_D(y)N_(D-1)(y)` counts new programs colliding into old fibers;
- `J_(2,2)=sum_y binom(A_D(y),2)` counts collisions born wholly inside the new depth shell.

This is the primitive-program analogue of P011's exact collision-growth decompositions.

## 4. Transition state is stronger than endpoint histograms

Let

`g_(a,b)(D)=#{y:N_(D-1)(y)=a, A_D(y)=b}`.

Then every birth component is recovered by

`J_(k,j)(D)=sum_(a,b) g_(a,b)(D) binom(b,j) binom(a,k-j)`.

The endpoint multiplicity histograms at depths D-1 and D do **not** determine this transition state.

Example: take previous multiplicities `(0,1,3)`. Two shell assignments

`A=(2,2,1)` and `A'=(3,1,1)`

both produce the same new unlabeled multiplicity histogram `{2,3,4}`. Therefore every endpoint `W_k` agrees at both depths.

But for pair collisions the birth decompositions differ:

`A: (J_(2,1),J_(2,2))=(5,2)`,
`A': (4,3)`.

Both have the same total `Delta W_2=7`, but the mechanism is different.

Thus even the full collision hierarchy at adjacent endpoints does not determine how collisions were born. The exact unlabeled transition state is the joint histogram `g_(a,b)`.

## 5. Typed semantic ladder

The compiler therefore has another strict hierarchy:

1. one fixed `W_k` -> one collision statistic;
2. all `W_k` at fixed D -> unlabeled multiplicity histogram;
3. endpoint hierarchies across two depths -> still not enough for birth mechanism;
4. joint transition histogram `(N_(D-1),A_D)` -> exact unlabeled collision-birth decomposition;
5. labeled semantic map -> required when future refers to specific semantic actions;
6. primitive-program identity -> required when actual histories/witnesses matter.

This is another instance of the project rule that equal resource profiles do not identify typed semantics.

## 6. Validation

The reference module checks the binomial inversion exactly, verifies the Vandermonde birth formula, and includes the same-endpoint/different-birth counterexample above.

No novelty is claimed for binomial inversion or Vandermonde's identity. R004's addition is their placement as an exact P011/certificate-state interface for primitive instruction histories.
