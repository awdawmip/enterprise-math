# X6 r417 — Exact future-context repair budget for non-invariant regular event languages

Date: 2026-11-20. Status: **author-side theorem / human-proof candidate**, not a Native Result, independent review, formal checker certificate, or a claim of native physical triadic dynamics.

Provenance: extension by the existing RESEARCH_DRIVER `EM-DVR-DEBB5E` in the same shared logical research context as r411–r416. In particular r416 (Source commit `c630a0ee31990e5187f1fc44a6798b886d2f5a7f`, blob `1f1934cca3e01b3f4c7326cdcddba2ef068e2fef`) supplies the exact static fiber formula and DFA state machine. This note does not assert reviewer independence. Earlier X6 contributor identities remain with their original work.

## Question and precise model

r416 computes extra bits needed to recover the **literal legal prefix** from the fixed-suffix orbit observation. In a continuation system, literal recovery is sometimes stronger than needed: distinct prefixes may induce exactly the same legality and observations under *every identical future continuation*. Compute the sharp auxiliary tag cost for that weaker, future-sound requirement.

Let a finite group H act letterwise on finite event alphabet E, and let `c:E -> Sigma^ell` be a fixed-block-length, injective H-equivariant event encoding. Let a complete DFA `A=(Q,E,delta,q0,F)` recognize arbitrary regular `L subset E*`, with no H-invariance assumption. Fix `s in E*`, write `K=Stab_H(s)`, and set `U_s={u: us in L}`, `O_s(u)=[c(us)]_H`.

For a legal u, define its *future signature* `Phi_s(u)` as the function on all `w in E*` with value `BOTTOM` if `u w s notin L`, and otherwise `[c(u w s)]_H`. The empty future is included, so `Phi_s(u)` determines `O_s(u)`. Two legal prefixes are **future-equivalent** iff their signatures agree for every common future word, comparing legality as well as the orbit output.

For each fixed observed orbit `o`, the encoder may append a tag depending on the actual prefix to identify its future-equivalence class within `O_s^{-1}(o)`; the decoder receives the orbit observation and tag. The tag need not reconstruct the literal prefix. Fixed-width tags are measured in bits, with arbitrary exact computation allowed.

## Theorem (sharp future-safe tag budget; arbitrary regular L)

For `u in U_s`, let
`J(u)={k in K: k.u=u}`,
`G(u)={g in K:(g.u)s in L}`.
Then `G(u)/J(u)` denotes the set of right cosets represented by elements of G(u) (G(u) is a union of these cosets), and it bijects with the legal orbit fiber from r416.

For g,h in G(u), declare `g ~_u h` precisely when, for **every** `w in E*`,

1. `(g.u)w s in L` iff `(h.u)w s in L`;
2. whenever both words are legal, `Stab_K(w) intersect (h J(u) g^{-1}) != empty`.

This relation on right-coset representatives is an equivalence relation. It is exactly equality of future signatures of the distinct lawful prefixes `g.u` and `h.u`. Let `C(u)` be the number of its equivalence classes in `G(u)/J(u)`.

If `U_s` is nonempty, the sharp worst-case fixed-width extra tag budget for predicting all future legality and orbit readouts is

```
    B_future(s,L) = ceil(log2 max_{u in U_s} C(u)).
```

For `U_s=empty`, set `B_future=0`. The maximum is attained, is computable by a finite algorithm, and obeys

```
    0 <= B_future(s,L) <= B_literal(s,L) = ceil(log2 max_u |G(u)|/|J(u)|).
```

The rightmost quantity is exactly r416's literal-reconstruction budget.

### Finite decision procedure and bounded witnesses

Reuse r416's prefix machine state
`S(u)=((q_g)_{g in K},J(u))`, with `q_g=delta*(q0,g.u)`. There are at most

```
    R = |Q|^{|K|} * |Sub(K)|
```

states. For each reachable eligible state (`delta*(q_identity,s) in F`), determine G(u) from the acceptance of `delta*(q_g,s)`, deduplicate the cosets modulo J, and decide each pair g,h by the following finite *common-future test*.

Start in `(p_g,p_h,W)=(q_g,q_h,K)`. For each future event e update
`(p_g,p_h,W) -> (delta(p_g,e),delta(p_h,e), W intersect Stab_K(e))`.
At any reachable future state, put
`a_g=[delta*(p_g,s) in F]` and `a_h=[delta*(p_h,s) in F]`.
The pair is distinguished exactly when either `a_g != a_h`, or both equal 1 and
`W intersect (h J g^{-1})=empty`.
Otherwise the pair is future-equivalent. Because the test visits at most
`T=|Q|^2 * |Sub(K)|` states, a distinguishing future can be selected with length at most `T-1` event blocks.

All pairwise results give the finite partition of G(u)/J and hence C(u). Since all tests depend only on S(u), the maximum C is obtained on a reachable eligible prefix-machine state. By cycle deletion a maximizing prefix u has length at most `R-1`. This is a **decidability / finite-witness bound**, not a polynomial-time assertion in a succinct encoding of H, the DFA or the action.

## Proof

By fixed-block injectivity and equivariance, `O_s(u)=O_s(v)` with the same appended suffix s holds exactly when `v=g.u` for some `g in K` (r416). The valid elements of that static fiber are the G(u) images, with repeats exactly along right cosets of J(u). For any common future w, equal orbit outputs for `(g.u) w s` and `(h.u) w s` mean that some `t in H` maps the former coded word onto the latter. Exact end-block equality forces `t.s=s`, so t lies in K. Exact equality of the shared future event blocks forces `t.w=w`, i.e. `t in Stab_K(w)`. Finally `t.(g.u)=h.u` is equivalent to `h^{-1} t g in J(u)`, or `t in h J(u) g^{-1}`. This proves the stated orbit test, without assuming that L is invariant.

Comparison of the two DFA acceptances proves the legality clause. The two clauses for every w are precisely equality of the functions `Phi_s(g.u)` and `Phi_s(h.u)`, hence form an equivalence relation and are independent of which representative of a right coset was used.

For each fixed orbit, the number of future signatures among its lawful prefixes is exactly C(u) for any u in that fiber. A fixed-width tag differentiating all these signatures requires at least ceil(log2 C(u)) bits by pigeonhole; enumeration of the signatures and tagging their indices attains that bound. Taking the maximum over fibers proves the sharp formula. A signature class cannot outnumber its literal members, proving the r416 comparison.

The prefix DFA state S(u) evolves exactly as in r416. In the future test, `p_g` and `p_h` read the **same future letters** (not g-transformed futures), while W updates to the pointwise stabilizer of the common future. Induction proves the two test acceptances and the exact subgroup condition for every w. Finite reachability therefore decides indistinguishability. Cycle deletion gives the two witness bounds and shows that C(u) is constant for all prefixes realizing one S-state. QED.

## Two exact discriminating examples

Use H=C3 acting by cyclic renaming `a -> b -> c -> a` on E={a,b,c}, the identity code, and empty suffix s.

* **Future-silent finite prefix-closed language:** `L={epsilon,a,b}`. Static fiber at a is {a,b}, so r416 requires `B_literal=1`. But for a and b, the empty future has the same orbit, while every nonempty future is illegal from both. Their complete future signatures coincide. The empty prefix has a singleton orbit fiber. Therefore `B_future=0`. A zero-bit observer is sufficient to predict all admitted future continuations and orbit readouts, though it cannot reconstruct whether the literal prefix was a or b.
* **Continuable prefix-closed language:** `L={a,b}*`. At u=a, the legal static fiber is {a,b}. With shared future w=a, both aa and ba are legal but lie in different C3 word orbits (one is constant, the other contains two different letters). Therefore their signatures differ and `B_future=1=B_literal`.

These are exact event-language results; they do not depend on enumeration truncation.

## Scientific limits / next genuine transfer dependency

The semantic tag is for the specified future interface (admissibility plus full H-orbit of the concatenation). It does not serialize the orbit, recover the exact path, preserve an undisclosed time/Cell/Port/branch readout, or show that physical native X6 triadic events form a finite regular language. Adding more readouts can refine future equivalence and change the required bits. For a native transfer, establish an exact Source-pinned event alphabet/codec, `TRIADIC_CLOSURE_E` admissibility, Cell/Port/branch/time continuation, the physical observer map and preservation of its operations; P000 is retained without changing any axiom.

This note is author-side proof evidence only. Formal Native Result acceptance, independent review, Activity semantic linkage, Task completion and parent Objective completion are **not** asserted. No CLAIM, owner, source authority, or scheduling state is changed.
