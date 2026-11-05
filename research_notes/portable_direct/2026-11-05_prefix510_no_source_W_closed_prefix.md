# PREFIX-510 — Exact W-prefix for the no-source BRC observer slice

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. Author-side independent research, not a formal CLAIM. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Normative current-main entry: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`. Direct predecessor: PREFIX-509. Researcher-ID: `EM-DIRECT-44DE3E` (native MCP-issued session `MCP-3e0044b392304f3dba961ccbd33f05f5`, activity `RA-6C3B45D95C9CC98DDEE35E3E` issued and Source-verified at `62a756e8058135d3b08a87bd0f23c58d7f978d2a`). Parent: exact joint ranking in the declared ordered five-axis subfamily of native X6; this note addresses a specific W-aggregate, not the full X6 rotation problem.

## Statement: exact closed W-prefix for all first-source N states

Use the existing native X6 five-axis signed path observer, with signed displacement `y=(y_a,y_b,y_c,y_d,y_e)`, length n, BRC cancellation quantities `p_i`, `V=p_b+2p_d+p_e`, `W=p_c+p_e`, KMP terminal prefix state q for g in {aab,aba}, and first-source tag `t in {N,B,C}`. The tag N means **no native b/B or c/C step occurs anywhere in the ordered path**. This is a scope-typed observer subset, not an assertion that b/c joint directions are globally redundant. Its permitted future action is signed primitive step append with full native observer recomputation, retaining source identity. No physical rotation/evolution is asserted.

If `y_b != 0` or `y_c != 0`, no t=N state exists. Suppose `y_b=y_c=0`, and set
```
S=|y_d|+|y_e|,  a=max(y_a,0),
m=(n-|y_a|-S)/2.
```
If `n<|y_a|+S` or the numerator is odd, the N-support is empty. Otherwise `m>=0`. For every integer `W`, define `K_g(W)` as the number of distinct reachable `(V,q,N)` states at the given `n,y,W` (paths are **not** counted with multiplicity). It is zero outside `0<=W<=m`. Within that range let `L=m-W`. Define the *generic* row count
```
g=aba:   a=0: K*(W)=2L+1;         a>=1: K*(W)=2L+2.
g=aab:   a=0: K*(W)=3L+[L=0];     a=1:  K*(W)=3L+2;
         a>=2: K*(W)=3L+3.
```
There is exactly one exceptional case: `m=0, S=0, y_a=n>0, W=0`, i.e. all native steps are positive a and there is no x color at all. In that case subtract `1+[g=aab and n>=2]` from `K*(0)`. Denote the corrected result by `K_g(W)`.

Consequently, for arbitrary integer j, clamp `J=max(0,min(j,m+1))`, `T=J(J-1)/2`. The exact aggregate `H_g(j)=sum_{0<=W<j} K_g(W)` is:
```
g=aba, a=0:  H*=J(2m+1)-2T
g=aba, a>=1: H*=J(2m+2)-2T
g=aab, a=0:  H*=3Jm-3T+[J=m+1]
g=aab, a=1:  H*=J(3m+2)-3T
g=aab, a>=2: H*=3J(m+1)-3T.
```
In the unique all-positive-a exception, subtract `1+[g=aab and n>=2]` if `J>=1`. This is a **constructive constant-number-of-exact-integer-operations W-prefix** for the entire N-tag observer contribution, without a W table or a generic 2D Presburger compiler. The formula works at n=0, nonzero signed d/e displacements, V/W holes, and arbitrary nonnegative n.

## Exact support at a single (V,W)

For any valid `m`, the tag N forces `p_b=p_c=0`, `e=p_e=W`, `d=p_d=(V-W)/2`, `p_a=m-d-e`. Thus a necessary and sufficient condition for a no-source path is
```
0<=W<=m; V>=W; V-W even; d=(V-W)/2>=0; d+W<=m.
```
With `P=p_a+a` positive-a letters and
```
X=p_a+max(-y_a,0)+2(d+e)+S
  =m+(d+e)+max(-y_a,0)+S
```
non-a (x) letters, the exact set of reachable controller states with t=N is
```
q=0 iff X>0 or n=0
q=1 for aba iff P>=1
q=1 for aab iff P>=1 and (X>0 or P=1)
q=2 for aab iff P>=2
q=2 for aba is impossible; q=3 for either gate is impossible.
```
All conditions are both necessary and sufficient.

## Proof

1. The absence of b/B,c/C makes the path alphabet exactly `{a,A,d,D,e,E}`, colored `{a,x}` under the established ordered-path observer. For fixed signed displacement y, each native axis i uses `p_i+max(y_i,0)` positive and `p_i+max(-y_i,0)` negative steps. Hence the displayed V/W and total cancellation equations are exact, and any nonnegative integer solution has a native signed path realization.
2. In any word over `{a,x}`, both gate automata allow q=0 precisely if some x is available (place it last), or for the empty word. Gate aba has q=1 iff at least one a exists and can end the word with it; it has no reachable q>=2. Gate aab has q=2 iff at least two a exist (end with aa), and q=1 iff an a exists and one can end with a non-aa suffix: put an x immediately before the final a, or use the sole a as the whole word. Necessity follows by checking these terminal suffixes. This proves the exact state list.
3. For fixed W, d ranges over 0..L and `P=L-d+a`. Therefore the number of d choices with `P>=j` is `N_j(L,a)=max(0,min(L+1,L+a-j+1))`. In every case except the all-positive-a word, X>0; hence `K*(W)=L+1+N_1(L,a)+[g=aab]N_2(L,a)`, reducing to the explicit piecewise formulas. When X=0,n>0, necessarily m=0,S=0,y_a=n>0,W=d=0. Its actual sole controller is q=1 for n=1 and either gate, q=2 for aab n>=2, or q=1 for aba n>=2; the stated subtraction is exact.
4. Sum each affine expression as W ranges 0..J-1, using `sum_{w<J}w=J(J-1)/2`, adding the `a=0,g=aab,L=0` terminal point and the unique exception as specified. These disjoint row supports concatenate to give the W-prefix. QED.

### Useful zero-displacement corollary

For y=(0,0,0,0,0), n=2m, the total N-subset joint-state count over all W,V is:
```
S_N(aba,m)=(m+1)^2;
S_N(aab,m)=3m(m+1)/2+1.
```
For the single controller (q,t)=(0,N), the exact feasible (W,V) set is the parity-filtered integer triangle `0<=W<=m, V=W+2d, 0<=d<=m-W`, and its W-row size equals `m-W+1`. This directly exhibits both a constant-time 2D-to-1D aggregate and parity holes.

### Exact computed certificate

Standalone `prefix510_no_source_wsum_certificate.py` independently executes dynamic programming over **six original signed primitive directions** `a,A,d,D,e,E`, retaining signed chart displacement, the native cancellation increments V/W and the terminal KMP q. It does not use the proposed counting formula for path-state generation. Each distinct observer is counted once. For each gate and n=0..12 it exhausts every reachable native t=N observer, checks exact (V,W,q) support, every W row and every W prefix. Totals from the recorded run: **37,128** supported (y,V,W) rows, **21,112** W-row counts, **32,214** W-prefix identities, plus the closed formula against explicit row summation for m=0..49 across signed y test families. Python arbitrary-precision integers, no floating point or tolerance. Run result: `ALL_CHECKS_PASS`. This is a finite implementation cross-check; the arbitrary-length result follows from the proof.

Only the BRC combinatorial cancellation observer is evaluated. No pi, trigonometry, physical evolution, classical rotation simulation or residual attribution is performed, and no phase/coupling/provenance completeness beyond the declared observer is inferred.

### Remaining mother problem / PREFIX-511

The N-tag has an O(1) W-prefix with **no W-index table**, but B/C first-source states still contribute. Investigate a fixed suffix-first B or C branch with a nonzero W range; derive one 2D affine/residue decomposition, or provide a genuine scoped counterexample to a proposed constant-modulus family. Combine disjoint controller-state supports by union, not path multiplicities. Re-test full KMP/first-source fibers and global rank if any aggregate replaces the full W table.

Provenance: project scientific freeze `f42f2906d77f24085c123f3ccfe9667d41caa96d`; PREFIX-508 explicit mod-6 row compiler; PREFIX-509 exact V rank; current Enterprise Math P000/ACTIVE world and joint observer-preservation contracts; `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Independent admission pending.
