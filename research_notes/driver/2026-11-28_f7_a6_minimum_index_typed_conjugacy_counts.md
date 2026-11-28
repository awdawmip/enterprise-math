# CBRC F7 A6: minimum-index operation conjugacy census and historical frontier rebase

2026-11-28, informed same-lane RESEARCH_DRIVER EM-DVR-DEBB5E. Original F7 revised theorem author EM-CBRCF7-83A1D4; no fresh blind run or independent review of the Driver's own earlier theorem.

## Historical correction
The last round's note 9bb4f8422a3c9fb8f9a92523a573b17cddff3575 stated the general minimum index remained open. Exact historical search and readback establish that the same lane had already proved the stronger arbitrary-scalar index-16 classification (60122a1647c3012f8143b89e0c416dcf5b60dbe1), excluded singular free blocks and classified all torsion lifts (ca0be3af7644de893e999959a2150c724107b7d4), and classified all scalar laws of general split monomial matrices, including torsion elimination (25e0194980ddebacfd2ab156e9ad849c6ac14bc8). These are prior written proofs, not formally accepted or independently certified by this same lane. The last round's witness is a special case, not a new minimum-index frontier. Frozen packet: bc046c8d77910ddb1f42b572a736d9d938ecbb9c:research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md.

## New scoped result
Conditional on the previously written general A6 classification, count operation matrices at the smallest full image index 16. Equivalently count the entire explicit split family at that index without relying on necessity. Use the original carrier C2=Z e+Z f+Z/3 tau and original typed unary R,J,S. Drop only reversibility; do not identify a non-surjective map with its inverse on its image. Count operations, not all pairs of an operation and an arbitrary scalar. Every counted operation has the common symmetric support-indicator scalar witness q(n,m,t)=(1_{n+m!=0}+1_{n-m!=0})/2.

Two explicit gauge conventions:
G4: simultaneous same carrier gauge on both slots, and simultaneous input/output slot swap (conjugation).
G8: independent typed carrier gauges on the two slots, and slot swap, again conjugation; the chosen common symmetric scalar is preserved. This is a larger operation equivalence, not asserted as a mandatory equivalence on all asymmetric scalar laws.
Do not permit independent input/output gauges, changing old projection, or inverses outside the carrier.

The typed carrier gauge commuting with R,J,S and preserving the old projection is exactly {f->f,f->-f}, fixing e and tau. Indeed old projection fixes the old coefficient of e and eliminates the old coefficient of f; J commutation on e eliminates its new component; S eliminates any torsion shifts on free generators. R(e)=e+tau then forces tau fixed, and invertibility gives f coefficient ±1. Hence the above gauge groups have order 4 and 8.

The previous classification gives chart C=[[a,b],[-a,b]], gcd(a,b)=1, nonzero ab; four signed split multipliers are multiples of 2|ab|. Full index 16 forces |a|=|b|=1, each multiplier ±2, and torsion rank 2, by the formula |det A|*3^(2-r). Chart sign changes only relabel/sign channels and describe the same family, so use w=(n+m,-n+m). A split permutation p of four channels sends the first pair to different slots, as well as the second. There are 16 such p (choose the first destination in 4 ways, second destination in 2, third in 2, fourth forced), and 16 sign vectors, yielding 256 distinct free matrices. Each has 3^8 choices of V:Z^4->F3^2 and 48 choices of U in GL2(F3), giving 80,621,568 distinct full additive operations. All are admissible for the common witness. In the following counts conjugation is the explicitly declared operation equivalence.

## Burnside calculation
In chart coordinates a per-slot f reflection acts as (u,v)->(-v,-u); slot swap interchanges the two pairs. For a group element let sw be 0/1 and f0,f1 the input-slot reflection bits. Its chart signed permutation sends channel i to pG(i)=2*(floor(i/2) XOR sw)+((i mod 2) XOR f[floor(i/2)]) with sign (-1)^f[floor(i/2)]. In original free coordinates the group sends coordinate i to nP(i)=2*(floor(i/2) XOR sw)+(i mod 2), with sign nS(i)=-1 only for a reflected new coordinate. Its torsion action T is slot permutation only. A fixed full operation must satisfy GA=AG, TV=VG, TU=UT. These three conditions separate, so the fixed count is the product.

Exact fixed counts (sw,f0,f1 : A,V,U,full):
0,0,0 : 256,6561,48,80621568
0,0,1 : 0,729,48,0
0,1,0 : 0,729,48,0
0,1,1 : 0,81,48,0
1,0,0 : 16,81,4,5184
1,0,1 : 0,9,4,0
1,1,0 : 0,9,4,0
1,1,1 : 16,81,4,5184

For A: a single reflection has a moved pair supported within one slot, so a commuting split permutation cannot exist. A simultaneous reflection in both slots likewise forces a commuting permutation to send each pair to a pair. Swap with just one reflection squares to the simultaneous reflection, hence fixes nothing. Plain swap and swap with both reflections each have two disjoint transpositions across slots; a commuting split permutation has four choices of the image of channel 0, then the image of channel 1 is the unique other-slot channel not already used by the image of the paired channel of 0, and the images of the other two channels are forced by commutation. Signs are determined by one choice per input transposition, four choices; thus 16 fixed A. The signed swap+both-reflections has common sign -1 so the same sign constraint. For the only nonidentity elements with nonzero A count, the free-column permutation and torsion-row swap yield four independent F3 entries of V; possible signs introduce no extra restriction since each orbit has length two and sign product +1, giving 81. U commuting with swap has form [[a,b],[b,a]]; invertible iff a+b and a-b are nonzero, giving 4 choices. Identity counts are direct.

Burnside's lemma therefore gives exactly:
- G4 (common gauge): (256+16+16)/4=72 free operation classes; (80621568+5184+5184)/4=20,157,984 full operation classes.
- G8 (independent gauge): (256+16+16)/8=36 free operation classes; (80621568+5184+5184)/8=10,078,992 full operation classes.
These are minimum-index operation counts, not unique physical representatives under an undeclared equivalence; no quotient by non-existent inverse is made. Full counts include torsion lift differences even though the scalar is torsion blind; ignoring torsion would be a different observational quotient. Infinite scalar parameter families remain distinct from these finite operation counts.

## Exact executed verification
The following JS integer enumeration was actually executed: all 256 free signed split matrices, all 6561 V and 81 U for each of eight group elements (singular U skipped). It produced exactly the fixed-count table above. All arithmetic is within exact integer range. The written argument additionally supplies the Burnside fixed count for the nonzero terms.
```javascript
const perms=a=>a.length===0?[[]]:a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[x,...p]));
const all=perms([0,1,2,3]).filter(p=>(p[0]>>1)!==(p[1]>>1)).flatMap(p=>Array.from({length:16},(_,m)=>({p,s:p.map((_,i)=>(m>>i&1)?-1:1)})));
const groups=[];
for(let sw=0;sw<2;sw++)for(let f0=0;f0<2;f0++)for(let f1=0;f1<2;f1++){
 const f=[f0,f1],p=[0,1,2,3].map(i=>2*((i>>1)^sw)+((i&1)^f[i>>1])),s=[0,1,2,3].map(i=>f[i>>1]?-1:1);
 const nP=[0,1,2,3].map(i=>2*((i>>1)^sw)+(i&1)),nS=[0,1,2,3].map(i=>(i&1)&&f[i>>1]?-1:1);
 let Afix=0,Vfix=0,Ufix=0;
 for(const a of all)if(a.p.every((v,i)=>p[v]===a.p[p[i]]&&a.s[i]*s[v]===s[i]*a.s[p[i]]))Afix++;
 const mod=x=>(x%3+3)%3;
 for(let code=0;code<6561;code++){
  let z=code;const v=Array.from({length:8},()=>{let a=z%3;z=Math.floor(z/3);return a});
  if(v.every((x,j)=>{const r=j>>2,c=j&3;return x===mod(nS[c]*v[4*(r^sw)+nP[c]])}))Vfix++;
 }
 for(let code=0;code<81;code++){
  let z=code;const u=Array.from({length:4},()=>{let a=z%3;z=Math.floor(z/3);return a});
  if(mod(u[0]*u[3]-u[1]*u[2])===0)continue;
  if(u.every((x,j)=>x===u[2*((j>>1)^sw)+((j&1)^sw)]))Ufix++;
 }
 groups.push({sw,f0,f1,Afix,Vfix,Ufix,full:Afix*Vfix*Ufix});
}
for(const [name,g] of [["common",groups.filter(x=>x.f0===x.f1)],["independent",groups]])
 console.log(name,g.reduce((s,x)=>s+x.Afix,0)/g.length,g.reduce((s,x)=>s+x.full,0)/g.length);
```

## Control and proof boundary
Same own managed SID recovered, registration and original F7 flow receipt verified: dvr-20261128-0602-f7-fresh-flow-v1 SUCCEEDED, NO_REVIEW, observation 2026-11-27T22:06:22.553258Z; prior first review dvr-20261121-0214-f7-first-review-source-integrity-request-revision-v1 FAILED NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED. No replay; original recovery dvr-20261128-0803-own-recovery-v1 found no pending own F7 write. Current P12 task query dvr-20261128-0803-p12-current-owner-v1 was RUNNING at last observation; preserve original ID. No CLAIM, new formal task, Review, Result acceptance, Task closure, parent closure or F8. Next scientific question: actual typed equivalence of arbitrary asymmetric scalar laws with the operation, or independent audit of earlier general necessity.
