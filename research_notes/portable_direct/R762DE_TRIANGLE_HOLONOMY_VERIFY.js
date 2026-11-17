'use strict';
// R762DE exact integer verifier, Node >=18, no external dependencies.
// Does NOT assert that signed frames or triangle probes are native-licensed events.
const assert = require('node:assert/strict');
const n=6, edges=[];
for(let i=0;i<n;i++) for(let j=i+1;j<n;j++) edges.push([i,j]);
const at=new Map(edges.map(([i,j],k)=>[i+','+j,k]));
const mod=(x,q)=>((x%q)+q)%q;
function edge(C,i,j) { return i<j?C[at.get(i+','+j)]:-C[at.get(j+','+i)]; }
function tri(C,i,j,k,signs=Array(n).fill(1)) {
  return signs[i]*signs[j]*edge(C,i,j) + signs[j]*signs[k]*edge(C,j,k) + signs[k]*signs[i]*edge(C,k,i);
}
function row(i,j,k, signs=Array(n).fill(1)) {
  const C=Array(15).fill(0);
  function add(a,b){ C[at.get(a<b?a+','+b:b+','+a)] += (a<b?1:-1)*signs[a]*signs[b]; }
  add(i,j);add(j,k);add(k,i);return C;
}
function rationalRank(matrix) {
  function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b];}return a;}
  function frac(a,b=1n){assert.notEqual(b,0n);if(b<0n){a=-a;b=-b;}const d=gcd(a,b);return [a/d,b/d];}
  function minus(a,b){return frac(a[0]*b[1]-b[0]*a[1],a[1]*b[1]);}
  function times(a,b){return frac(a[0]*b[0],a[1]*b[1]);}
  function divide(a,b){return frac(a[0]*b[1],a[1]*b[0]);}
  const A=matrix.map(x=>x.map(z=>frac(BigInt(z)))); let r=0;
  for(let c=0;c<15;c++) {
    let pivot=r;while(pivot<A.length && A[pivot][c][0]===0n)pivot++;
    if(pivot===A.length)continue;
    [A[r],A[pivot]]=[A[pivot],A[r]];
    const a=A[r][c];for(let j=c;j<15;j++)A[r][j]=divide(A[r][j],a);
    for(let i=r+1;i<A.length;i++){
      let t=A[i][c];if(t[0]===0n)continue;
      for(let j=c;j<15;j++)A[i][j]=minus(A[i][j],times(t,A[r][j]));
    }
    r++;if(r===A.length)break;
  }
  return r;
}
const triples=[];for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++)triples.push([i,j,k]);
const allRows=triples.map(t=>row(...t));
assert.equal(allRows.length,20);assert.equal(rationalRank(allRows),10);
const cycRank=[];for(let h=0;h<=5;h++){
  const rows=Array.from({length:h+1},(_,t)=>row(t%6,(t+1)%6,(t+2)%6));
  const rank=rationalRank(rows);assert.equal(rank,h+1);cycRank.push(rank);
}
const signedRows=[];for(const [i,j,k] of triples){
  signedRows.push(row(i,j,k));
  for(const flip of [i,j,k]){
    const s=Array(n).fill(1);s[flip]=-1;
    signedRows.push(row(i,j,k,s));
  }
}
assert.equal(signedRows.length,80);assert.equal(rationalRank(signedRows),15);
function deltaFromU(u){return edges.map(([i,j])=>u[j]-u[i]);}
const kernelChecks=[];
for(let q=2;q<=7;q++){
  let total=q**5, survived=0, changed=0;
  for(let seed=0;seed<total;seed++){
    let rem=seed;const u=[0];for(let i=1;i<n;i++){u.push(rem%q);rem=Math.floor(rem/q);}
    const C=deltaFromU(u);
    assert(triples.every(t=>mod(tri(C,...t),q)===0));
    const stable=signedRows.every(r=>mod(r.reduce((s,z,k)=>s+z*C[k],0),q)===0);
    const expected=u.every(x=>mod(2*x,q)===0);
    assert.equal(stable,expected);
    survived+=stable?1:0;changed+=stable?0:1;
  }
  const d=q%2?1:2;assert.equal(survived,d**5);
  kernelChecks.push({q,gradients_tested:total,signed_invisible:survived,signed_detected:changed});
}
function base(i,j){return [[i,1],[i,-1],[j,1],[j,-1]];}
function loop(i,j){return [[i,1],[j,1],[i,-1],[j,-1]];}
function area(path){const v=Array(n).fill(0),B=Array.from({length:n},()=>Array(n).fill(0));
  for(const [j,s] of path){for(let i=0;i<n;i++)if(i!==j)B[i][j]+=v[i]*s;v[j]+=s;}
  return {v,B,C:edges.map(([i,j])=>B[i][j])};
}
const q=3,u=[0,0,1,0,0,0],D=deltaFromU(u);
let H=[],K=[];for(let k=0;k<edges.length;k++){
  const [i,j]=edges[k],t=mod(D[k],q);
  for(let z=0;z<q;z++){H.push(...base(i,j));K.push(...(z<t?loop(i,j):base(i,j)));}
}
const a=area(H),b=area(K);
assert.deepEqual(a.v,Array(n).fill(0));assert.deepEqual(b.v,Array(n).fill(0));
const counts=path=>{let out=Array.from({length:n},()=>[0,0]);for(const [i,s] of path)out[i][s===1?0:1]++;return out;};
assert.equal(H.length,180);assert.equal(K.length,180);assert.deepEqual(counts(H),counts(K));
const diff=edges.map((_,k)=>b.C[k]-a.C[k]);
assert(triples.every(t=>mod(tri(diff,...t),q)===0));
const signs=[1,-1,1,1,1,1];const reveal=mod(tri(diff,0,1,2,signs),q);
assert.equal(reveal,1);
let checked=0;
function check(path){const x=area(path);for(let i=0;i<n;i++)for(let j=i+1;j<n;j++){
  assert(x.B[i][j]+x.B[j][i]===x.v[i]*x.v[j]);
}
const perm=[1,2,3,4,5,0],sgn=[-1,1,-1,1,1,-1];
const transformed=path.map(([i,s])=>[perm[i],sgn[i]*s]);const y=area(transformed);
for(let i=0;i<n;i++)assert(y.v[perm[i]]===sgn[i]*x.v[i]);
for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j)assert(y.B[perm[i]][perm[j]]===sgn[i]*sgn[j]*x.B[i][j]);
checked++;
}
function visit(p,depth){check(p);if(depth===3)return;for(let i=0;i<n;i++)for(const s of [-1,1])visit([...p,[i,s]],depth+1);}
visit([],0);assert.equal(checked,1+12+144+1728);
const evidence={schema:'R762DE_EXACT_AUTHOR_CHECK_V1',status:'PASS',date:'2026-11-17',model:'SIGNED_X6_ORDERED_PAIR_AREA_DIAGNOSTIC_NOT_NATIVE_EVENT',pair_coordinates:15,triangles:20,permutation_triangle_rank_over_Q:rationalRank(allRows),cyclic_rank_by_depth_0_to_5:cycRank,signed_triangle_test_rows:signedRows.length,signed_triangle_rank_over_Q:rationalRank(signedRows),kernel_checks:kernelChecks,explicit_common_coarse_fibre:{q:3,word_length:H.length,difference_is_gradient:true,all_unsigned_triangle_differences_zero:true,after_flip_axis_1_triangle_012_difference:reveal},signed_path_covariance_words_checked:checked,independent_review:'NOT_REVIEWED'};
console.log(JSON.stringify(evidence,null,2));
