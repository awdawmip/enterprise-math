# F7 A6 index-16: torsion-lift shear obstruction and exact census
2026-11-28; EM-DVR-DEBB5E informed same-lane continuation; original F7 author EM-CBRCF7-83A1D4. Not an independent review of own prior A6 classification. Frozen science bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md. Prior explicit family and typed gauge: d64dea6d730ef13b11b9060e450e4cdb7010bb4b; dynamics 39c71788171eee57782949d9541cbbc553d482e7. Scope is abstract additive conjugation, a new coarser observer, not a replacement of typed gauge or of the original F7 A6 axiom.

## Exact result
Let H=Z^4 direct sum F3^2, M(x,t)=(Ax,Vx+Ut), with A=2D^{-1} S D, D=diag(C,C), C=[[1,1],[-1,1]], S signed split permutation, U in GL2(F3), V arbitrary 2x4 over F3. Fix A,U. A shear T_W(x,t)=(x,t+Wx) is an additive automorphism with inverse T_{-W}. Direct conjugation gives T_W M T_W^{-1}=(A,V+W Abar-UW,U), where Abar is reduction mod 3. Consequently the exact shear-equivalence classes are coker L, L(W)=W Abar-UW, an F3-vector space of dimension d=dim ker L by rank-nullity on the 8-dimensional space. The lift splits (has an invariant complementary free subgroup) iff [V]=0: any complement is the graph of a homomorphism W:Z^4->F3^2, and invariance is V+UW=WAbar. Every class has 3^(8-d) lifts, with 3^d classes. These statements hold for arbitrary A,U of the indicated sizes, not only minimum index.

For the explicit index-16 family D is invertible mod3, so Abar is similar to 2S. For each signed cycle c of length l and sign product epsilon, write a_c=2^l epsilon mod3. The cyclic module for that cycle has annihilator X^l-a_c: a coordinate vector and its first l-1 iterates are independent. An intertwiner W is determined by the image of the cyclic generator, which is arbitrary in ker(U^l-a_c I). Thus
d = sum_c dim_F3 ker(U^l-a_c I).
No semisimplicity assumed; in particular length 3 in characteristic 3 is handled without replacing repeated roots by distinct ones.

## Exact executed census
Enumerated 256 free matrices and 48 U matrices (12,288 block pairs), computing d both from signed cycle formula and independent 8x8 rank elimination. Zero discrepancies.
| d | h=2 pairs | h=3 pairs | total pairs | shear classes per pair |
|---|---:|---:|---:|---:|
|0|2640|2880|5520|1|
|1|896|512|1408|3|
|2|2032|2176|4208|9|
|3|128|512|640|27|
|4|432|64|496|81|
|6|16|0|16|729|

Sum of classes over fixed (A,U): 116736; not a count of global conjugacy orbits since block centralizers and changes of A,U can merge classes. Of the 80621568 full lifts, 42559488 admit an invariant complement, 38062080 do not. The 5520 nonresonant block pairs have all lifts split; 6768 resonant pairs have nontrivial obstructions. For the 16 d=6 pairs, only 9 of 6561 V split. These are exact counts for the explicit family, exhaustive for all minimum-index A6 models only conditional on prior general necessity. This refines image Smith factors and torsion point periods, which are blind to V. Split/non-split remains invariant under arbitrary additive automorphism conjugation because the torsion subgroup is characteristic and existence of an invariant complement is intrinsic. Shear equivalence is NOT original typed R,J,S gauge equivalence; no claim that these shear maps preserve unary operations.

## Executed JS reproduction
```js
const perms=a=>a.length===0?[[]]:a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[x,...p]));
const mod=x=>(x%3+3)%3, mul=(A,B)=>A.map(r=>B[0].map((_,j)=>mod(r.reduce((s,x,i)=>s+x*B[i][j],0))));
const I=n=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>+(i===j)));
function rank(A){A=A.map(r=>r.map(mod));let k=0;for(let c=0;c<A[0].length&&k<A.length;c++){let j=A.findIndex((r,i)=>i>=k&&r[c]);if(j<0)continue;[A[j],A[k]]=[A[k],A[j]];const a=A[k][c];A[k]=A[k].map(x=>mod(x*a));for(let i=0;i<A.length;i++)if(i!==k){let b=A[i][c];A[i]=A[i].map((x,j)=>mod(x-b*A[k][j]))}k++}return k}
let hist={},byh={},byU={},cases=0,classes=0,nonres=0;
for(const p of perms([0,1,2,3]).filter(p=>(p[0]>>1)!==(p[1]>>1)))for(let m=0;m<16;m++){
 const s=p.map((_,i)=>(m>>i&1)?-1:1),B=I(4).map(r=>r.map(()=>0));p.forEach((j,i)=>B[j][i]=mod(2*s[i]));let cycles=[],seen=new Set;
 for(let i=0;i<4;i++)if(!seen.has(i)){let j=i,l=0,eps=1;do{seen.add(j);l++;eps=mod(eps*2*s[j]);j=p[j]}while(j!==i);cycles.push([l,eps])}
 let h=1,q=p;while((q[0]>>1)!==(q[1]>>1)){q=q.map(i=>p[i]);h++}
 for(let k=0;k<81;k++){let z=k,v=Array.from({length:4},()=>{let a=z%3;z=Math.floor(z/3);return a});let U=[v.slice(0,2),v.slice(2)];if(!mod(v[0]*v[3]-v[1]*v[2]))continue;
 let d=0;for(const [l,eps] of cycles){let T=I(2);for(let i=0;i<l;i++)T=mul(T,U);d+=2-rank(T.map((r,i)=>r.map((x,j)=>mod(x-eps*(i===j)))))}
 let L=Array.from({length:8},(_,i)=>Array.from({length:8},(_,j)=>mod((i>>2)===(j>>2)?B[j&3][i&3]:0)-((i&3)===(j&3)?U[i>>2][j>>2]:0)));
 if(8-rank(L)!==d)throw Error("rank mismatch");
 hist[d]=(hist[d]??0)+1;byh[h]??={};byh[h][d]=(byh[h][d]??0)+1;cases++;classes+=3**d;if(d===0)nonres++;
 let o=0,T=I(2);do{T=mul(T,U);o++}while(String(T)!==String(I(2)));byU[o]??={};byU[o][d]=(byU[o][d]??0)+1;
 }
}
console.log({hist,byh,byU,cases,classes,nonres,splitLifts:Object.entries(hist).reduce((s,[d,n])=>s+n*3**(8-Number(d)),0)})
```

## Control frontier
Verified own managed session recovery dvr-20261128-1158-recovery-read-v1, recent 50 request records no pending writes in returned scope; more historical requests exist. Original T6 synthesis dvr-20261128-0100-t6-scoped-synthesis-v1 SUCCEEDED RVS-CB68113DFE8202D7F2D1, nonterminal, no acceptance. Latest T6 author checkpoint visible at current observed Source 995ae176f73dbff1924baf61120a751f0dda8c6f remains 3f0eec72bb4d842cb63cc8bc3105cd8174aa83d3 for [15000,20000); previous audit already covers it, no repeated search. P12 original task read dvr-20261128-0903-p12-current-owner-v1 SUCCEEDED, READY/NEEDS_DISPATCH as of 01:06:33Z only; no current owner asserted. F7 original review flow dvr-20261128-0602-f7-fresh-flow-v1 SUCCEEDED NO_REVIEW at historical observation; exact Result RR-AA38973D56330E59D315. First review dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1 FAILED NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED, not replayed. No new native Review, claim, Result acceptance, Task completion or parent closure. Next mathematical step: classify residual block-centralizer orbits in coker L and find explicit invariant-complement witnesses distinguishing fixed A,U at unchanged Smith/period profile; retain typed gauge separately. Non-author A6 review and actual P12 worker handoff remain open.
