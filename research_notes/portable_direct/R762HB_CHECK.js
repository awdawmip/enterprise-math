// R762HB dependency-free exact integer checker (Node 18+)
// Scope: P000-compatible spatial typing of a candidate, not native triadic admission.
function verify(){
const V=[0,1,2,3],E=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]], A=E.map(e=>V.map(v=>+e.includes(v)));
const subsets=(arr,k)=>k===0?[[]]:arr.flatMap((x,i)=>subsets(arr.slice(i+1),k-1).map(t=>[x,...t]));
const det=M=>M.length===1?M[0][0]:M[0].reduce((s,x,j)=>s+(j%2?-1:1)*x*det(M.slice(1).map(row=>row.filter((_,c)=>c!==j))),0);
const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
const gd=V.map((_,ik)=>{const k=ik+1;return subsets([0,1,2,3,4,5],k).flatMap(rs=>subsets(V,k).map(cs=>det(rs.map(i=>cs.map(j=>A[i][j]))))).reduce((d,x)=>gcd(d,x),0)});
if(JSON.stringify(gd)!=="[1,1,1,2]")throw Error("Wrong Smith minors "+gd);
const perms=a=>a.length===0?[[]]:a.flatMap((x,i)=>perms(a.filter((_,j)=>i!==j)).map(q=>[x,...q]));
for(const v of V){
 const h=A.map(row=>row[v]),p=E.filter((_,i)=>h[i]).map(e=>e.join(""));
 if(h.reduce((s,x)=>s+x,0)!==3||new Set(perms(p).map(a=>a.join("|"))).size!==6)throw Error("Refinement count");
 for(const sig of [-1,1]){
  const l=[-1,2,0,1],c=[3,2,1,0,4,5];
  const K=c.map((x,i)=>x+A[i].reduce((s,a,j)=>s+a*l[j],0));
  const c2=c.map((x,i)=>x+sig*h[i]),l2=l.map((x,j)=>x-sig*+(v===j));
  const K2=c2.map((x,i)=>x+A[i].reduce((s,a,j)=>s+a*l2[j],0));
  if(K.some((x,i)=>x!==K2[i]))throw Error("Invariance fails");
 }
}
let recon=0;
for(let a=-2;a<=2;a++)for(let b=-2;b<=2;b++)for(let c=-2;c<=2;c++)for(let d=-2;d<=2;d++){
 const z=[a,b,c,d],y=A.map(row=>row.reduce((s,x,j)=>s+x*z[j],0));const [p,q,r,s,t,u]=y;
 if(t!==r+s-q||u!==r+s-p||(p+q+s)%2!==0)throw Error("Lattice constraints");
 const z2=[(p+q-s)/2,(p-q+s)/2,(-p+q+s)/2,r-(p+q-s)/2];
 if(z.some((x,i)=>x!==z2[i]))throw Error("Reconstruction");
 recon++;
}
let dp=new Map([["0,0,0,0",1]]),Z=[1];
for(let m=1;m<=4;m++){
 const n=new Map();
 for(const [key,num] of dp){const z=key.split(",").map(Number);
  for(const v of V)for(const sig of [-1,1]){const w=z.slice();w[v]+=sig;const k=w.join(",");n.set(k,(n.get(k)||0)+num);}
 }dp=n;Z.push(dp.get("0,0,0,0")||0);
}
if(JSON.stringify(Z)!=="[1,0,8,0,168]")throw Error("BRC exact counts");
return {schema:"R762HB_EXACT_LINK_REPAIR_V1",verification:"PASS",model:"K4-STAR raw-X6 candidate; not native TRIADIC_CLOSURE_E permission",axes:E.map(e=>e.join("")),incidence_matrix:A,determinantal_divisors:gd,smith_factors:[1,1,1,2],additive_link_rank_min:4,primitive_steps_per_composite:3,ordered_shortest_native_paths_per_event:6,signed_source_zero_counts_m0_m4:Z,decorated_zero_count_m2:Z[2]*6**2,decorated_zero_count_m4:Z[4]*6**4,inventory_test_cases:recon,event_invariant_cases:8,review:"NOT_REVIEWED",scope_limit:"Free abelian Link with linear decoding; unrestricted signed candidate alphabet; future legal Link/Port/time gates unresolved"};
}
console.log(JSON.stringify(verify(),null,2));
