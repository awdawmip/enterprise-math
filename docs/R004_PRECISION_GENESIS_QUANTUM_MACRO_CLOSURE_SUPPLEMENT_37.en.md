# R004 precision genesis — Supplement 37: null-program history collision hierarchy

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + P011-BRIDGE + PRIOR-ART-BOUNDED`
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_36.en.md`
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 35–36 compile additive net semantic actions into primitive instructions using a null-program code. This supplement restores the information deliberately erased by that net-effect quotient: **which bounded primitive programs collide on the same semantic action**.

The collision hierarchy is exactly the earlier P011 object applied to bounded instruction histories.

## 1. Bounded primitive-program multiplicities

Let `H:F_2^s -> F_2^r` be the additive primitive-action map, `C=ker H`, and

`B_D={e in F_2^s : wt(e)<=D}`.

For semantic action y define

`N_D(y)=#{e in B_D : H e=y}`.

Then the bounded program collision spectrum is

`W_k^prog(D)=sum_y binom(N_D(y),k)`.

This is literally P011's collision polynomial coefficient applied to primitive programs rather than path histories.

## 2. Short-program uniqueness gate

Two distinct depth-`<=D` programs e,e' produce the same semantic action iff

`e-e' in C\{0}`.

Their difference has weight at most `2D`. Conversely any nonzero codeword `c in C` with `wt(c)<=2D` can split its support into two sets of size at most D, producing two distinct short programs with the same syndrome.

Therefore

`all depth-<=D programs are unique  <=>  d_min(C)>2D`.

If the same ISA also has covering radius at most D, every semantic action has exactly one short program. This is precisely the perfect packing/covering boundary in coding language.

Typed consequence: a net-effect-only future may quotient all null programs. A path/witness-sensitive future may do so only when its relevant bounded histories are unique or when their identity has separately been preserved.

## 3. Exact pair-collision formula from the ordinary weight spectrum

For a nonzero null word c, ordered program pairs with difference c are in bijection with

`B_D(0) cap B_D(c)`.

Hence

`2 W_2^prog(D) = sum_(0!=c in C) |B_D(0) cap B_D(c)|`.

In the binary Hamming cube the intersection size depends only on `w=wt(c)`:

`I_2(s,D,w) = sum binom(w,a)binom(s-w,b)`

over integer pairs `(a,b)` satisfying

`a+b<=D`,
`w-a+b<=D`.

Therefore

`W_2^prog(D)=1/2 sum_(0!=c in C) I_2(s,D,wt(c))`.

So the ordinary null-code weight enumerator is an exact sufficient state for the entire bounded pair-collision curve.

## 4. Triple collisions require a stronger state

For ordered distinct nonzero null words c,d,

`6 W_3^prog(D) = sum_(c,d) |B_D(0) cap B_D(c) cap B_D(d)|`.

In the binary case this three-ball intersection is determined by the triangle

`(wt(c), wt(d), wt(c+d))`,

because these three distances determine the coordinate counts of patterns `(c_j,d_j) in {00,10,01,11}`.

Thus the ordered triangle profile of the null code is an exact sufficient state for W3.

## 5. Ordinary weight enumerator / W2 does not determine W3

Consider two binary length-6 dimension-3 null codes:

`C0=<15,20,36>`,
`C1=<9,20,34>`.

As sets:

`C0={0,15,20,27,36,43,48,63}`,
`C1={0,9,20,29,34,43,54,63}`.

Both have ordinary weight enumerator

`1 + 3 z^2 + 3 z^4 + z^6`.

Consequently their complete W2 curves agree. For D=1,...,5 both give

`W2=(3,27,97,178,217)`.

But their W3 curves differ:

`C0: (1,17,131,318,427)`,
`C1: (0,16,132,319,427)`.

Already at D=1, one code has a semantic fiber with three short programs while the other only has pair collisions.

Therefore

`ordinary weight spectrum / all pair collisions !=> higher history-collision spectrum`.

The two codes have different triangle profiles, exactly as the W3 formula predicts.

## 6. General k-fold formula

Let `c_2,...,c_k` range over ordered pairwise-distinct nonzero codewords of C. Setting `c_i=e_i-e_1` gives

`k! W_k^prog(D)`

`= sum_(c_2,...,c_k) |B_D(0) cap B_D(c_2) cap ... cap B_D(c_k)|`.

For binary codes, the intersection size is determined by the coordinate-pattern counts

`#{j : (c_(2j),...,c_(kj))=alpha}`

for `alpha in F_2^(k-1)`.

Hence a `(k-1)`-fold complete/joint weight profile is an exact sufficient code state for `W_k^prog(D)`.

Complete joint and r-fold weight enumerators are established coding-theory objects. R004 does not claim them as inventions; the project-local result is their identification as the natural state ladder for P011-style bounded program-history collisions.

## 7. Validation

Executable checks include:

- perfect length-5 repetition-null code at D=2: unique short programs and `W2=0`;
- the S35 rank-5/radius-2 nine-column ISA: direct bounded-program enumeration gives `W2=21`, exactly matching the ordinary-weight formula;
- the two length-6 counterexample codes: identical ordinary weight enumerators and W2, but `W3=1` versus `0` at D=1;
- the triangle-profile formula exactly reproduces those W3 values.

Earlier independent research also checked the pair formula on the rank-7/radius-3 eleven-column covering ISA, giving `W2=164` by both routes.

No fresh full-repository CI is claimed.

## 8. Architecture consequence

The covering-code backend has a typed semantic ladder:

1. **net-effect only** -> quotient by the null code;
2. **bounded pair-history semantics** -> null-code ordinary weight spectrum is sufficient;
3. **bounded triple-history semantics** -> triangle/joint second-order profile;
4. **bounded k-history semantics** -> `(k-1)`-fold joint coordinate profile;
5. **full witness/path identity** -> keep the actual histories or a proven sufficient witness representation.

Thus compression strength must fall as the future asks for higher-order history distinctions. A scalar storage/readout optimum is not a complete history-semantic certificate.
