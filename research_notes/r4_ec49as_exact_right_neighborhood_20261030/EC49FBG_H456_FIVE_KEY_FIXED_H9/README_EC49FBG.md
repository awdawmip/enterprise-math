# EC49FBG — H2–H6 exact native signed-prefix optimum, with the H9 cache key fixed

Date: 2026-11-05. Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Author-side exact finite computation/proof; independent Driver review and formal Result admission remain open.

## Theorem

In the frozen seven-operation, signed-native-six-axis BRC path model, each horizon must have terminal signed displacement `(2,0,0,0,0,0)` and observation-matrix rational rank 9. At most five **full six-coordinate positive-step cache keys** are permitted in the complete H2–H9 construction.

Fix `H2={fe,ge}` and `H3={feg,gef}`, costing exactly 16 distinct signed native prefix edges and consuming three keys. Fix the *future H9 key* at `K9=(6,4,1,0,0,0)`; allow all legal H4–H6 word sets under that five-key budget. Then:

**min E(H2,...,H6) = 70.** The H4 cache key `L=(4,2,1,0,0,0)` is the **unique** choice attaining 70 within this family.

This lower bound is also attained by a full H2–H9 admissible extension, since the existing 112-edge witness from EC49FBF has the same 70-edge H2–H6 prefix.

## Complete finite classification

Each primitive signed operation is an ordered sequence of signed axes:
`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.
The seventh operation `b=(-2,-2)` cannot appear in a word whose signed terminal displacement is `(2,0,0,0,0,0)`, since no other operation has positive net second-axis displacement.

For a horizon-h word with complete key `(x,y,z,0,0,0)`, target displacement forces the exact nonnegative integer counts:

```
#a=z-1, #e=z, #c+#d=x+y-h-1,
#f=h+1-y-2z, #g=h+1-x.
```

In particular `x+y>=h+1`. Every fixed H2/H3 key has `x+y<=4`, hence none can occur at H4. The stipulated H9 key cannot occur at H4 either, since its required `#c+#d=5>4`. With the global five-key budget, every H4 word therefore has the **same** one new key L. H5 and H6 may use only L or K9. Complete enumeration of the original nine-state observation automaton leaves exactly nine L values capable of rank-nine H4 coverage.

| Additional H4 key L (trailing coordinates zero) | Exact minimum signed prefix edges H2–H6 |
|---|---:|
| (3,2,1) | 106 |
| (3,3,1) | 96 |
| (4,1,1) | 106 |
| **(4,2,1)** | **70** |
| (4,3,1) | 82 |
| (5,1,1) | 96 |
| (5,1,2) | 120 |
| (5,2,1) | 82 |
| (5,3,1) | 102 |

## Exact finite optimizer

Generate **every ordered operation word** of lengths 4,5,6 with target signed displacement, one of the two permitted keys, and one of the six allowed observation signatures. There are 206, 1062, 5352 valid-signature words over *all* keys at these horizons. Preserve the ordered primitive signed steps in a common trie. Mark the fixed 16 early prefixes as already paid.

A terminal contributes a four-bit signature-clause mask for its own horizon; bit j is set if the signature intersects the corresponding member of `[18,20,33,40]`. The target for H4–H6 is `0xfff=4095`. For each trie node v and mask M, let D_v[M] be the least additional native signed edge cost of the chosen terminals in that subtree producing OR-mask M. Initialize zero and any terminal contribution; combine child subproblems by exact OR/min-plus convolution. Charge a single edge on entry to any non-free node with nonempty selected coverage. Induction on trie height proves the optimizer exhausts all legal terminal subsets and counts every shared signed edge once.

Two actually executed integer implementations agree on all nine minima: a JavaScript direct operation-word DFS with signed-step audit and witness reconstruction, and a separate Python standard-library multiset-count enumeration and unpruned trie DP. Both use the frozen nine-state observation transition matrix; they are computationally independent implementations, not independently frozen semantic models. The checked Python source and its complete results are saved alongside this proof.

## 70-edge attaining prefix

```
H2 fe ge
H3 feg gef
H4 fegc fegd gefc gefd
H5 fegfg geffg
H6 fegccc fegddd gefccc gefddd
```

The directly recounted cumulative native signed-prefix edge costs are `12,16,32,38,70`; every selected word has the required terminal signed displacement, each horizon has rank 9, and exactly five full keys are used. The alternative H5 pair `feggf,gefgf` yields the same 70-edge H2–H6 cost and is part of the existing full-nine 112-edge witness.

## Reproduce and continue

Run `python VERIFY_EC49FBG.py`, which prints the complete nine-case JSON certificate, with expected minimum 70 and reconstructed witness assertions. A separately executed JavaScript counterpart and its execution report are retained as the local author-run crosscheck; the Python program below is a complete reproducible published checker.

**Next EC49FBH:** jointly optimize the H7–H9 suffix over the 70-edge H2–H6 class, then vary H9 key and H2/H3 roots. Seek a full 93-edge witness or an exact broader lower bound. The existing global nine-window author-side scope remains `80<=E*<=94`. Scientific input and P000/ACTIVE worldview are unchanged.