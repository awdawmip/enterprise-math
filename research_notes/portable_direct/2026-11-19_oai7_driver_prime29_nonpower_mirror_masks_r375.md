# OAI7 r375 — Prime-29 non-power-of-two mirror-mask witness and fixed-offset rigidity

Date: 2026-11-19. Shared-context RESEARCH_DRIVER author-side work, continuing r360, corrected r372, r373 and r374. Original OAI7 Researcher EM-EMF6D046-5A2844; Task RS-OAI7-028-C-20261007-6F2A81; publication TP2-96FAC49786245691AE19. This is not an independent Native Result review.

## Exact p=29 geometric theorem

For G=Z/29Z take the ordered residue path

\[
v=(23,4,5,2,21,8,15,28,11,12,6,7,18,1,20,25,19,0,3,13,17,10,22,9,14,27,24,16,26).
\]

Define g_j=v_j-v_{j-1} modulo 29, 1<=j<=28. Given a 14-bit mask b with b_1 the least significant bit, set

\[
h_j(b)=\begin{cases}g_j&b_{\min(j,29-j)}=0,\\-g_{29-j}&b_{\min(j,29-j)}=1,\end{cases}
\quad y_0=0,\quad y_j=\sum_{s=1}^j h_s(b)\pmod {29}.
\]

A mask is admissible if and only if y_0,...,y_28 are distinct. **Exact finite conclusion:**

\[
\boxed{\mathcal A_{29}(v)=\{0,2,15,16368,16381,16383\}.}
\]

The r373 path-reversal symmetry pairs these six masks as {0,16383}, {2,16381}, {15,16368}; hence the precise orientation-quotient count is **three**. This is a prime-29 counterexample to extrapolating the power-of-two mask counts seen in r373's initial 64-path sample. The earlier r374 counterexample used prime 13, not the original OAI7 modulus.

The following complete integer certificate enumerates all 2^14=16,384 masks; it computes admissibility both by the original partial sums and by r374's 406 modular affine collision exclusions. Exhaustive coverage proves the stated finite counterexample, while the two implementations cross-check the arithmetic of one already proved equivalence.

~~~python
p=29
v=(23,4,5,2,21,8,15,28,11,12,6,7,18,1,20,25,19,0,
   3,13,17,10,22,9,14,27,24,16,26)
assert len(v)==p and sorted(v)==list(range(p))
r=(p-1)//2
g=[(v[j]-v[j-1])%p for j in range(1,p)]
u=[(g[k-1]+g[p-k-1])%p for k in range(1,r+1)]
def walk(mask):
    y=[0]
    for j in range(1,p):
        bit=(mask>>(min(j,p-j)-1))&1
        step=g[j-1] if bit==0 else -g[p-j-1]
        y.append((y[-1]+step)%p)
    return y
def no_affine_collision(mask):
    for a in range(p):
        for c in range(a+1,p):
            val=sum((int(a<k<=c)+int(a<p-k<=c))*u[k-1]
                    *((mask>>(k-1))&1) for k in range(1,r+1))%p
            if val==(v[c]-v[a])%p:
                return False
    return True
hits=[]
for mask in range(1<<r):
    unique=(len(set(walk(mask)))==p)
    assert unique==no_affine_collision(mask)
    if unique:
        hits.append(mask)
assert hits==[0,2,15,16368,16381,16383]
allbits=(1<<r)-1
assert {b^allbits for b in hits}==set(hits)
assert {min(b,b^allbits) for b in hits}=={0,2,15}
def connector_shifts(mask):
    y=walk(mask)
    out=[]
    for k in range(1,p):
        bit=(mask>>(min(k,p-k)-1))&1
        j=k if bit==0 else p-k
        minus=y[j-1] if bit==0 else y[j]
        plus=y[j] if bit==0 else y[j-1]
        delta=(minus-v[k-1])%p
        assert delta==(plus-v[k])%p
        out.append(delta)
    return tuple(out)
assert len(set(tuple((t-connector_shifts(b)[0])%p
                     for t in connector_shifts(b)) for b in [0,2,15]))==3
print("r375 PASS: 16384 exact masks, six admissible, three quotient classes")
~~~

## Fixed-offset compatibility theorem (same path / labeled profile assignment)

Let x_k be the distinct degree-two profile connecting the atoms at v_{k-1},v_k in coordinate 1. For prescribed ordered shape W_x, write \(\Delta_{x,i}=w_{x,i}-w_{x,1}\in G\). At coordinate i, the two *actual* atom destinations are fixed to
\(v_{k-1}+\Delta_{x_k,i},v_k+\Delta_{x_k,i}\).

For an admissible mask b, define its connector-atom shift

\[
d_k(b)=\begin{cases}
y_{k-1}(b)-v_{k-1},& b_{\min(k,29-k)}=0,\\
y_{29-k}(b)-v_{k-1},& b_{\min(k,29-k)}=1.
\end{cases}
\]

This matches the plus atom as well, since the flipped connector is reversed. **The mask fits all prescribed connector offsets if and only if** there is a *single* common c in G such that

\[
\boxed{\Delta_{x_k,i}=c+d_k(b)\pmod{29}\quad\text{for every }k=1,\ldots,28.}\tag{F}
\]

For one fully specified first-coordinate labeled path and fixed offsets, **at most one admissible complement class** can satisfy (F). Indeed, both matching masks would place every labeled connector atom at the same fixed residues; the r373 exact orientation-quotient theorem forces them to be identical or complements. This removes redundant geometric mask search when the labeled support is already specified, while permitting enumeration during the search for *unknown* connectors/offsets.

To verify the complete five-uniform 378-atom claim one must additionally check fixed singleton destinations, the positive exact cut weights and all coordinate mass equalities of r359/r360. None of these is inferred from six geometrically valid masks. The currently established global five-uniform OAI7 support interval remains \(378\le S_{\min}\le490\).

## Provenance and research use

The 29-residue witness is a new scoped correction of the sample-based power-of-two speculation, not a rejection of r373's orientation quotient. Its complement classes supply three exact fixed-offset template candidates for future profile assignment tests. These are shared-context author-side calculations, not independent review, Source/Activity linkage, Result acceptance, Task closure or parent-objective completion. Reuse previously frozen contributor identities and results.

Sources:
- r359: https://github.com/awdawmip/enterprise-math/blob/12c7809e30111287c70430fdaae51bd402be626d/research_notes/portable_direct/2026-11-19_oai7_driver_tree_cut_congruence_r359.md
- r360: https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md
- corrected r372: https://github.com/awdawmip/enterprise-math/blob/6ba73383f3e87b5f0e90aca1392044fa717ef362/research_notes/portable_direct/2026-11-19_oai7_driver_path_mirror_pair_reduction_r372.md
- r373: https://github.com/awdawmip/enterprise-math/blob/ec905e2b63a533d6234e2471b23107cefc5a1035/research_notes/portable_direct/2026-11-19_oai7_driver_mirror_path_orientation_quotient_r373.md
- r374: https://github.com/awdawmip/enterprise-math/blob/2e55182098f88ad5a30e55e1f761c89e2c0149ba/research_notes/portable_direct/2026-11-19_oai7_driver_mirror_mask_affine_collision_counterexample_r374.md
