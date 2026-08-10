# P025 Supplement 70 — Derivative Gain on the Exactly-Two-Nonsquarefree Slice

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplements 64, 66, 69  
Hard block: `NONE`

## 1. The first hard structural slice after the squarefree basin

Stage 69 proves that a non-unit activated triple must have nonsquarefree `c` and at least one nonsquarefree side.

The next simplest case is therefore:

- `c` nonsquarefree;
- exactly one of `a,b` nonsquarefree;
- the remaining side `s` squarefree.

Let `y` denote the nonsquarefree side. Then the repeated pair is `(y,c)`.

Because `s` is squarefree, its block capacity is exactly the standard arithmetic derivative

\[
\boxed{C(s)=s'.}
\]

This creates a new exact gain in the pair-radical compiler.

## 2. P025-T139 — exact derivative-gain pair-radical bound

Fix an integer threshold

\[
T\ge1
\]

and suppose

\[
\sigma_{\rm proj}\ge T.
\]

The squarefree-side projective term cannot be active because its residual is one. Thus the active term is either `c`-oriented or `y`-oriented.

### Case 1: c-oriented activation

The denominator contains

\[
R_y C(s)=R_y s'.
\]

Therefore

\[
m(c)\ge T R_y s'.
\]

Since `m(c)=c/R_c`,

\[
\boxed{
R_yR_c\le\frac{c}{T s'}.
}
\]

### Case 2: y-oriented activation

Now the denominator contains

\[
R_c C(s)=R_c s'.
\]

Hence

\[
m(y)\ge T R_c s'.
\]

Using `m(y)=y/R_y`,

\[
R_yR_c\le\frac{y}{T s'}<\frac{c}{T s'}.
\]

Therefore both orientations give the common exact envelope

\[
\boxed{
\operatorname{rad}(yc)
=R_yR_c
\le
\frac{c}{T s'}.
}
\]

On `c<=X`, this is

\[
\boxed{
\operatorname{rad}(yc)
\le
\frac{X}{T s'}.
}
\]

Compared with Stage 64's generic `O(X/T)` pair-radical state, the exactly-two-nonsquarefree slice gains the explicit factor `s'`.

## 3. P025-C15 — prime squarefree sides are the lowest-capacity branch

If `s` is prime, then

\[
s'=1.
\]

No extra derivative gain is available.

If `s` is composite squarefree, let `r=Omega(s)>=2`. The classical arithmetic-derivative lower bound gives

\[
s'\ge r s^{(r-1)/r}\ge2\sqrt s.
\]

Thus

\[
\boxed{
\operatorname{rad}(yc)
\le
\frac{X}{2T\sqrt s}
}
\]

for every composite squarefree side.

So the genuinely low-capacity exactly-two-nonsquarefree branch is concentrated at prime `s` or, more generally, very small standard arithmetic derivative.

## 4. Conditional de Bruijn tail refinement

If one additionally restricts to states with

\[
s'\ge H,
\]

then P025-T139 compiles the repeated pair to

\[
\operatorname{rad}(yc)\le\frac{X}{TH}.
\]

Applying the same external de Bruijn pair-product count used in Stage 64 gives the conditional tail scale

\[
\boxed{
N_X(\sigma_{\rm proj}\ge T,\ s'\ge H,\ \text{exactly two nonsquarefree})
\ll_\varepsilon
\frac{X^{1+\varepsilon}}{TH}.
}
\]

This is not a new radical-counting theorem. It is the old theorem applied after a sharper project-specific compiler.

For composite squarefree sides with `s>=Y`, the standard derivative lower bound gives formally

\[
s'\ge2\sqrt Y,
\]

and hence an additional `Y^-1/2` saving in this restricted slice.

## 5. Exact examples

### Prime-side branch

\[
3+125=128.
\]

The unique squarefree side is `s=3`, so

\[
s'=1.
\]

At threshold `T=4`, the repeated pair is `(125,128)` and

\[
\operatorname{rad}(125\cdot128)=5\cdot2=10
\le
128/4=32.
\]

No derivative-side improvement appears because the squarefree side is prime.

### Composite squarefree side

\[
10+2187=2197.
\]

Here

\[
10'=7,
\]

and the active projective value is `729/121>6`. For `T=6`,

\[
\operatorname{rad}(2187\cdot2197)=3\cdot13=39,
\]

while

\[
\frac{2197}{6\cdot7}>52.
\]

The factor `s'=7` is a real gain over the generic Stage-64 envelope.

Another example is

\[
22+2187=2209=47^2,
\]

where `22'=13` and threshold one gives

\[
3\cdot47=141<2209/13.
\]

## 6. Empirical routing signal

A finite exact scan through `c<=10^4` found that among activated non-unit triples with exactly two nonsquarefree components, the unique squarefree side was prime in the overwhelming majority of observed states; only a few composite-side examples appeared, including the two above.

This is **not** a theorem and is not used in any proof. It only supports the research routing suggested by P025-C15: if one wants a difficult structured family after Stage 69, prime-side or very-low-`s'` states are the natural branch to inspect first.

## 7. Precision architecture consequence

The Stage-69 Boolean squarefree pattern can be refined only when needed:

\[
\text{exactly two nonsquarefree}
\to
\text{identify squarefree side }s
\to
\text{read one old observable }s'
\to
\text{sharpen pair-radical precision by }1/s'.
\]

Thus a single classical arithmetic-derivative value becomes the exact extra coordinate needed to improve the theorem-native pair-radical state on this structural slice.

## 8. Prior-art discipline

The arithmetic derivative and its lower bounds are prior art [SRC-MERIKOSKI-HAUKKANEN-TOSSAVAINEN-2019-ARITHMETIC-SUBDERIVATIVES]. De Bruijn radical counting is also prior art.

P025 owns only the exact conditional reduction `rad(yc)<=c/(T s')` inside its projective activation system. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_projective_two_nonsquarefree.py`;
- `tests/test_abc_projective_two_nonsquarefree.py`.

## 10. Next frontier

No hard block exists. Continue with:

1. isolate the prime-squarefree-side branch `s'=1` and search exact families/obstructions;
2. study whether the all-three-nonsquarefree slice admits an analogous cheapest-side derivative gain;
3. replace empirical prevalence by an actual count only if a theorem stronger than the generic Stage-64 tail emerges;
4. use the result as another example of conditional/adaptive precision refinement rather than a generic arithmetic-derivative novelty claim.
