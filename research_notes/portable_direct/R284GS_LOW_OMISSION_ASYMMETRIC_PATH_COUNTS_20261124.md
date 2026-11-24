# R284GS — Low-omission asymmetric safe-word counts and observer-dependent optimum

2026-11-24. Independent informed portable continuation, author proof NOT_REVIEWED, auxiliary four-phase binary fixed-tag model. Original own registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED (EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4); no shared CLAIM. Owner inventory r1-20261124-1600-owner-read RUNNING during derivation. P000/ACTIVE worldview unchanged. Exact unit-weight branch counting on a retained residual coordinate, not native physical attribution.

Frozen references:
- GL @5f74ba8a545788cc3fdb080f9953bbe5a0926531:research_notes/portable_direct/R284GL_ASYMMETRIC_THREE_PATTERN_SHARP_CAPACITY_20261124.md (exact prefix distances).
- GQ @9f74833b63383390e436542669d7601834a0b2ea:research_notes/portable_direct/R284GQ_ALL_PARAMETER_MINIMIZER_RIGIDITY_20261124.md (three minimizers for 0<=q<u).
- GR @e72cd4e1806d52fdc27923852e7e8fa49720b0ab:research_notes/portable_direct/R284GR_EXACT_OPTIMAL_MODE_WORD_COUNTS_20261124.md (middle/transition regime and distinction of observables).
- GE @a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md (cycle criterion, inherited via GR and GL).

## All-parameter low-omission count theorem

For integers 0<=q<u, u>=1, put H=2q+u+1, J=q+3u. The GQ low-omission minimizers (A,B,C) are (H,J,H), (H-1,J+1,H), (H,J+1,H-1). Count safe attempted mode words on edge updating A,B, leaving C. Set r=2u+1, e=A-2q, d=C-2q, s=r-d, t=e-s (0 or 1), h=B-q-s, W=h-2q+t. Let binom(n,k)=0 outside 0<=k<=n. Define strip kernel T_W(m;i,j), number of unit +/-1 walks of length m on integer heights 0..W from i to j, zero for invalid endpoints, negative m or wrong parity. Its exact image sum is

T_W(m;i,j) = sum_{v in Z} [binom(m,(m+j-i)/2+v(W+2))-binom(m,(m+j+i+2)/2+v(W+2))].

Only finitely many summands are nonzero. The formula follows alternatively by checking recurrence T(m+1;i,j)=T(m;i,j-1)+T(m;i,j+1), zero at j=-1,W+1 by reindexing and binomial symmetry, and delta initial data. This is an exact positive-branch multiplicity carrier (the image formula uses subtraction for count evaluation, not signed physical branches).

For q=0, N(A,B,C)=T_W(A+B;t,t+B-A).

For q>=1, sum over 0<=k<=min(B,h), with k>=2q-t if q>t. Define
P(k)=binom(q-1+k,k) if k<q and q<=t; P(k)=0 if k<q and q>t; otherwise
P(k)=sum_{i=0}^{min(t,q-1)} binom(i+q-1,i) [binom(q-1-i+k-q,k-q)-binom(q-1-i+k-q,q-t-2)].
Set k0=max(k,2q-t). Then

N(A,B,C)= sum_k P(k) sum_{j=max(k0,q+s)}^{min(B,h+e-q)}
 T_W(e-1-q+j-k0; k0-2q+t, j-(e-1)-q+t)
 * [binom(2q+B-j,2q)-binom(2q+B-j,2q-t-1)].

Proof: GL gives D2=[e-a]+ + [b-q]+ +d, D3=max(0,d,[a-q]+-q,B-b+[a-q]+-q+d). Since e,d<r and a<=2q+e, safety is exactly [e-a]+ + [b-q]+>=s and b<=h+[a-q]+. For a<=t lower bound vacuous, t<a<e lower b>=q+a-t, a>=e lower b>=q+s. For q=0 the whole path is a strip in height t+b-a. For q>=1, e>q, split uniquely at the first A step reaching a=q at b=k, then first A step reaching a=e at b=j. Before the first cut, upper b<=h is automatic for endpoints k<=h. If k<q, paths are unrestricted precisely when q<=t (otherwise no safe endpoint). For k>=q mark first B step reaching b=q at a=i<=min(t,q-1); prefix to (i,q-1) is unrestricted, remaining prefix to (q-1,k) must stay at height t+b-q-a>=0. Single-barrier reflection counts its forbidden walks as binom(q-1-i+k-q,q-t-2); final A step to (q,k) is valid by the chosen k constraint. This proves P(k). In the middle the height b-a-q+t is restricted to 0..W, except for q=1,t=1,k=0: the unique next step is B reaching k0=1 before any A step. This follows from a=q+1=2 requiring b>=q+2-t=2. For all other allowed k, k0=k. Stop the strip walk at (e-1,j), then take one A step to (e,j). The stated j bounds make this last step safe; strip walk length and endpoint heights fix the A and B counts uniquely. In the suffix b>=q+s is automatic; reverse from (A,B) to (e,j) with reversed counts a',b'. Upper b<=h+a-q becomes b'>=a'-t. Initial reverse height t, final counts a'=2q,b'=B-j. Single-barrier reflection yields the last bracket. Unique cuts prevent duplication; all constraints are necessary and sufficient at every prefix. Multiplication composes independent word choices at exact retained ports; summation preserves their multiplicity. No reduction to a scalar residual total was used.

## Cycle counts and different observers

Let S=N(H,J,H), P=N(H-1,J+1,H), Q=N(H,J+1,H-1). Rotations exchange A,C, so symmetric cycle count is S^4 and either asymmetric cycle count is (P Q)^2; no quotient by cycle rotations. Physical-coordinate orders multiply the per-edge count by A!B!, exactly as in GR. Thus compare absolute mode-word counts by PQ versus S^2; compare labeled counts by PQ*(J+1)^2 versus S^2*H. For uniform mode-word safe fraction compare PQ*binom(H+J,H)^2 versus S^2*binom(H+J,H-1)*binom(H+J+1,H). These are distinct exact observers.

At (q,u)=(0,1), S=8,P=3,Q=4: the symmetric histogram has more safe mode words, but asymmetric has 9/4 times as many safe physical-coordinate cycle orders. At (1,2), S=266,P=75,Q=70, H=5,J=7: symmetric wins both metrics (336000<353780 in the labeled comparison). This proves there is no uniform observer-independent winner, and the labeled ordering itself reverses with parameters. These are exact examples of minimum-width histograms, not altered capacities.

## Executed cross-check

All 759 edge-count comparisons (u=1..22, q=0..u-1, three histograms/orientations) matched independently accumulated lattice DP using original GL exact distances. Both Python arbitrary precision and the equivalent JavaScript BigInt calculation were executed; the JS implementation is reproduced below. The exact sign triples (asymmetric minus symmetric for absolute, physical-labeled, normalized mode fraction) and frequencies, plus examples, are:
{"checks":759,"stats":{"-1,1,-1":164,"-1,-1,-1":89},"examples":[[0,1,"8","3","4"],[1,2,"266","75","70"],[7,8,"2147789878260","240905872740","171908991540"]]}
In all 253 parameter pairs, symmetry wins absolute and normalized mode counts. The labeled count favors asymmetry in 164, symmetry in 89, no tie. The universal ordering and boundary of the labeled phase are open; finite comparisons do not prove them.

```javascript
const C=(n,k)=>{if(k<0||k>n)return 0n;let z=1n;for(let i=1;i<=Math.min(k,n-k);i++)z=z*BigInt(n-i+1)/BigInt(i);return z};
const memo=new Map();
function strip(w,m,h,k){if(h<0||h>w||k<0||k>w||m<0||(m+k-h)%2)return 0n;let key=[w,m,h,k].join(",");if(memo.has(key))return memo.get(key);let z=(m+k-h)/2,y=(m+k+h+2)/2,P=w+2,v=0n;for(let i=-Math.ceil(m/P)-2;i<=Math.ceil(m/P)+2;i++)v+=C(m,z+i*P)-C(m,y+i*P);memo.set(key,v);return v}
function closed(q,u,A,B,D){let r=2*u+1,e=A-2*q,d=D-2*q,s=r-d,t=e-s,h=B-q-s,W=h-2*q+t;if(q===0)return strip(W,A+B,t,t+B-A);
function pre(k){if(k<q)return q<=t?C(q-1+k,k):0n;let p=0n;for(let i=0;i<=Math.min(t,q-1);i++)p+=C(i+q-1,i)*(C(q-1-i+k-q,k-q)-C(q-1-i+k-q,q-t-2));return p}
let ans=0n;for(let k=0;k<=Math.min(B,h);k++){if(q>t&&k<2*q-t)continue;let p=pre(k);if(!p)continue;let k0=Math.max(k,2*q-t);for(let j=Math.max(k0,q+s);j<=Math.min(B,h+e-q);j++){let m=e-1-q+j-k0,z=2*q+B-j;ans+=p*strip(W,m,k0-2*q+t,j-(e-1)-q+t)*(C(z,2*q)-C(z,2*q-t-1))}}return ans}
function dp(q,u,A,B,D){let r=2*u+1,p=x=>Math.max(0,x),M=p(D-q),v=Array(B+1).fill(0n);for(let a=0;a<=A;a++)for(let b=0;b<=B;b++){let D2=p(A-a-2*q)+p(p(b-q)+M-q),D3=Math.max(0,D-2*q,p(a-q)-q,B-b+p(a-q)-2*q+M);v[b]=D2<r||D3<r?0n:a===0&&b===0?1n:v[b]+(b?v[b-1]:0n)}return v[B]}
function run(){let checks=0,stats={},examples=[];const sign=(a,b)=>a>b?1:a<b?-1:0;for(let u=1;u<=22;u++)for(let q=0;q<u;q++){let H=2*q+u+1,J=q+3*u,S=closed(q,u,H,J,H),P=closed(q,u,H-1,J+1,H),Q=closed(q,u,H,J+1,H-1);for(let [a,b,c,n] of [[H,J,H,S],[H-1,J+1,H,P],[H,J+1,H-1,Q]]){if(n!==dp(q,u,a,b,c))throw Error([q,u,a,b,c]);checks++}
let k=[sign(P*Q,S*S),sign(P*Q*BigInt((J+1)**2),S*S*BigInt(H)),sign(P*Q*C(H+J,H)**2n,S*S*C(H+J,H-1)*C(H+J+1,H))].join(",");stats[k]=(stats[k]||0)+1;if((q===0&&u===1)||(q===1&&u===2)||(q===7&&u===8))examples.push([q,u,String(S),String(P),String(Q)])}return {checks,stats,examples}}
console.log(run());
```

## Next

Prove or refute the universal low-omission absolute/fraction ordering; locate the asymptotic labeled-count transition; optimize the symmetric middle-regime count using GR. Independent GP/GQ rational certificate verification remains open. No new capacity scan or formal Result/Review.
