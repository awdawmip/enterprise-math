# BRC-X6: 12-bit full-positive native 13-minimal strategy (2026-11-10)

**Status:** AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-portable only; does not assert Source CLAIM, native checkpoint, freeze, admission or independent review.

**Frozen science:** SHA-256 `f42f2906d77f24085c123f3ccfe9667d41caa96d`; original 96 native ports, six labeled actions, nine signed roots and complete seven-variable next-port/reward joint observation. Source ports `(6,7,28,29)`, signs `(+,-,-,+)`. All 38 deterministic policies are checked at all nine original roots.

## Theorem

The four source-port distributions are

```text
X=(1/3523)*[
 [3013,    2,    4,    8, 112, 384],
 [2015, 1128,    4,    8,  48, 320],
 [ 592, 1128, 1001,    2, 504, 296],
 [ 528, 1064,    3, 1128, 504, 296]
]
```

All 24 action probabilities are strictly positive and each row sums to 3523. For admissible policy IDs

`I=(2,8,15,21,24,28,29,31,37,0,1,3,5)`,

the exact nonzero weights are

`w=(1,2,4,8,16,32,64,128,256,512,1000,500,1000)`,

and their sum is **D=3523 (12 bits)**. They reproduce the displayed matrix and all nine native signed joint observations. Hence `minSupport(X)<=13`.

Let `C` be the 24×38 native source-action indicator matrix, `R=(0,1,2,3,4,5,18,19,20,21,22,6,10)`, `A=C[R,:]`, `B=A[:,I]`, and `Q=B^{-1}A`. Exact checks give `rank(C)=rank(A)=13`, `det(B)=-1` and integer `|Q_ij|<=2`. In these coordinates the target is `w`.

Reuse the separately verified author-side exact native sharp 13-minor bound `|det(A[:,S])|<=3` for all `|S|=13` (commit `e38d623754636b3e2c2d31935752295e12a27023`). Any hypothetical nonnegative representation by at most 12 native columns extends to 12 independent columns `T`; its cofactor vector `d_i=det([A[:,T]|B[:,i]])` is nonzero, `d in {-3,-2,-1,0,1,2,3}^13`, `d·w=0`, and `rank(Q[:,Z(d)])>=12`, where `Z(d)={j:d^T Q[:,j]=0}`.

Two **independent exact integer** meet-in-the-middle enumerators (6+7 and 7+6) exhaust all bounded `d` satisfying `d·w=0`. They agree byte-for-byte on every eligible sorted zero-column mask (SHA-256 `74297c5ca091f6a90372a4473c428e233b9e1e18103b2ae7c25ff919840cd006`).

| Quantity | Exact count |
| --- | ---: |
| Bounded relations including zero | 10,295,277 |
| Nonzero bounded relations | 10,295,276 |
| Nonzero relations with >=12 zero columns | 56,482 |
| Distinct zero masks | 22,032 |
| Zero-mask ranks 6,7,8,9,10,11,12 | 60, 882, 7288, 9673, 3719, 404, **6** |

Ranks used exact modular elimination at `p=2^61-1` and were verified over rational integers for the six rank-12 masks. Because `|Q_ij|<=2`, Hadamard bounds any nonzero 12×12 minor by `48^6=12,230,590,464<p`, so reduction modulo `p` cannot lose a rational rank-12 minor. All zero-mask ranks are <=12 from their nonzero witness `d`.

Each of the six rank-12 cones has a **small integer Farkas separator** `y` with `y^T Q[:,j]>=0` for every column in the mask but `y^T w<0`. These six masks and exact negative margins are:

```text
mask          y·w
7389346183    -1488
68854841335    -384
77041923943    -496
217008203078  -1904
217008281670  -1900
252287114717   -744
```

The corresponding full `y` vectors are respectively

```text
[0,0,-1,0,1,0,0,0,0,0,0,-1,-1]
[0,0,-1,1,1,1,-1,-1,1,0,0,-1,0]
[0,0,-1,-1,1,0,0,0,0,0,0,-1,0]
[0,0,-1,0,1,1,1,0,0,-1,0,-1,-1]
[0,0,0,0,1,1,1,0,0,-1,0,-1,-1]
[0,0,0,0,0,0,0,0,1,0,-1,0,0]
```

Each separator inequality has been checked with exact integer multiplication and all six masks have exact rational rank 12. Thus no at-most-12-term native representation exists:

`minSupport(X) = 13, with denominator 3523 (12 bits)`.

## Reproduction and lineage

The author-portable reproducible research bundle includes the original frozen kernel, exact chart `Q`, two independent C++17 bounded-relation enumerators, a modular rank enumerator, all sorted masks, six explicit integer duals, a Python exact native nine-root and SymPy verifier, a JSON certificate, and the full written theorem. The final JSON certificate SHA-256 is `98bd091c83b7162131191957ad48fb594513686580b7544d64aa49fd34a2139f`.

The new scientific increment over the prior 13-bit/8191 author certificate (commit `173ff38f6a1472a828d4088dc15166f717bdcb2e`) is the 12-bit witness and its independent finite cofactor/rank/cone-exclusion proof. Prior policy discovery and sharp-minor mathematics retain their original attribution.

**Task boundary:** Source D25/H0-B0 native execution frontier remains separate and requires an own issued session and winning CLAIM. Historical UR four-file V2 authentic bytes remain missing (94,687 bytes, SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). Next portable objective: a shorter 11-bit witness with exact nonnegative-support exclusion, or a derived lower bound for minimal full-positive denominator.
