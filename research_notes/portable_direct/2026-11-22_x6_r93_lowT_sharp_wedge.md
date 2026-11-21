# X6 R93 — The low-T two-weight wedge, sharp Port thresholds 16 and 27

Date: 2026-11-22 (Asia/Shanghai). Status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED. This is independent portable scientific work, not a formal CLAIM, PROGRESS, Result or Review. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json⟧. Follows R91–R92. Conditional positive-count degree-four BRC star-histogram observer only.

## Theorem

Use R91's definitions `q(x,y,z)⟧, moments `u=x+3y+6z⟧, `v=3x+12y+30z⟧, `h=7x+39y+126z⟧, six gaps and `F(a;(1,1,S,T))⟧. Fix real `0<T<1⟧, `S>=5⟧, integer Port budget `p>=11⟧. Set `R=1/(1+T)⟧, `A=5+6T⟧, `B=6+5T⟧. Notice `5<=A<B⟧.

Define the unoriented differences `s=(10,-5,1)⟧ (q=11), `b=(14,-9,2)⟧ (q=16), and `c=(24,-14,3)⟧ (q=27).

1. For `11<=p<=15⟧, the global optimum is exactly `eta*=R⟧ for **all** `S>=5⟧, attained only by `s⟧.
2. For `16<=p<=26⟧, the global optimum is exactly `eta*=R⟧ for **all** `S>=5⟧; the full minimizer set is `{s}⟧ for `5<=S<A⟧ and `{s,b}⟧ for `S>=A⟧.
3. For `p>=27⟧ and `5<=S<B⟧, `eta*=R⟧ with the same `{s}⟧ / `{s,b}⟧ split at `A⟧. At `S=B⟧, the global value remains `R⟧ and the full tie set is **`{s,b,c}⟧**.
4. For `p>=27⟧ and `S>B⟧, `eta*<R⟧, with the explicit feasible improvement `F(c)=6/(S+T)<R⟧. The new optimum beyond the wall is left open.

Consequently, at the small-T side of the sigma-five boundary, the exact tie wall is `S=5+6T⟧ once 16 Ports are available, and the exact *loss of the old optimal value* occurs at `S=6+5T⟧ once 27 Ports are available. These are different boundaries.

## Proof on the whole integer lattice

Since `F(s)=R⟧, any `F(a)<=R⟧ satisfies `|h|,|h-u|<=1⟧. The moment congruences `h≡u(mod2)⟧, `h≡u+6v(mod12)⟧, and `v in 3Z⟧ yield `h=u in {-1,0,1}⟧ and `v=6m⟧ for `m in Z⟧. Applying the exact inverse integer moment map gives

```
a=(10u-24m, -5u+14m, u-3m),  u in {-1,0,1}, m in Z.
```

At `m=0⟧, the only nonzero candidate is `±s⟧. For `|m|=1⟧, up to sign, candidates are `b⟧ (q=16), `c⟧ (q=27), `e=(34,-19,4)⟧ (q=38). For `|m|>=2⟧, `|x|=|10u-24m|>=38⟧, so `q>=38⟧. Hence with `p<=26⟧ the complete possible minimizer pool is `s⟧, or `s,b⟧ when `p>=16⟧. Directly,

```
F(b)=max(R,6/(1+S),5/(S+T)),
```

so `F(b)=R⟧ iff `S>=5+6T=A⟧ (the required other inequality `S>=5+4T⟧ is weaker). This proves claims 1 and 2 and excludes every strictly better integer difference.

Now assume `p>=27⟧ and `S<=B=6+5T⟧. The `v⟧-gap bound gives

```
|v|<=(1+S)/(1+T)<7,
```

so `m in {-1,0,1}⟧ even without any Port cutoff. Candidate `e⟧ cannot tie because its 34-gap is 7, while `S+T<=6(1+T)<7(1+T)⟧, so `F(e)>R⟧. Candidate `c⟧ has gaps `(0,6,0,6,0,6)⟧ and

```
F(c)=max(6/(1+S),6/(S+T))=6/(S+T)
```

for `T<1⟧. Thus `F(c)>R⟧ for `S<B⟧, `F(c)=R⟧ at `S=B⟧, and `F(c)<R⟧ for `S>B⟧. With `F(b)⟧ as above this yields all stated values and complete ties for `S<=B⟧, and a strict counter-witness after the boundary. QED.

## Exact author verification and next problem

The independent companion `x6_r93_lowT_wedge_verify.py⟧ enumerated 34,677 unoriented differences with `q<=27⟧, using exact rational arithmetic for `T=1/3,1/2,3/4⟧, six S points per T (including both walls), and `p=11,15,16,26,27⟧: 90 parameter/Port cases, 3,120,930 upper-bound comparisons. All flat-optimum and strict-improvement assertions passed. `x6_r93_lowT_wedge_results.json⟧ holds the compact result. The general theorem is symbolic; these tests are author-side checks only.

Next determine the **actual** optimum and complete competing lattice directions for `S>B⟧, separated by Port, and test whether the two-wall geometry survives a P000-native observer with joint triadic events and provenance. No claim of a native P000 operation-preserving map is made.
