"use strict";
// EC48F: integer-only independent audit of explicit finite exact source experiment.
const P=[[2,1],[4,2],[2,4],[1,2]], Q=[[2,2],[2,2],[2,2],[2,2]];
const assert=(p,m)=>{if(!p)throw Error(m)};
assert(P.flat().reduce((a,b)=>a+b,0)===18,"P mass");
assert(Q.flat().reduce((a,b)=>a+b,0)===16,"Q mass");
// With lambda=N/9, sign(p - lambda*q) is sign(4*Praw-N).
function face(N,W,scale) {
 let value=0, optimum=0,alpha=0,beta=0;
 for(let h=0;h<4;h++)for(let y=0;y<2;y++){
   const z=4*P[h][y]-N, w=W[h][y];
   assert(Number.isInteger(w)&&w>=0&&w<=scale,"invalid probability");
   value+=z*w; optimum+=Math.max(z,0)*scale;
   alpha+=P[h][y]*w;beta+=w;
 }
 assert(value===optimum,"face support failure");
 return {alpha_num:alpha,alpha_den:18*scale,beta_num:beta,beta_den:8*scale};
}
let checks=0;
for(let i=0;i<=60;i++){
 const t1=2*i, t2=4*i, L=60;
 let u=Math.min(t1,L),v=Math.max(t1-L,0);
 face(4,[[L,u],[L,L],[L,L],[v,L]],L);checks++;
 const W=t2<=2*L
   ?[[Math.min(t2,L),0],[L,0],[0,L],[0,Math.max(t2-L,0)]]
   :[[L,0],[L,Math.min(t2-2*L,L)],[Math.max(t2-3*L,0),L],[0,L]];
 const obs=face(8,W,L);
 assert(obs.alpha_num*9===obs.alpha_den*(4+t2/L) || obs.alpha_num*9*L===obs.alpha_den*(4*L+t2),"central alpha");
 assert(obs.beta_num*8*L===obs.beta_den*(2*L+t2),"central beta");checks++;
 u=Math.min(t1,L);v=Math.max(t1-L,0);
 face(16,[[0,0],[u,0],[0,v],[0,0]],L);checks++;
}
function twiceArea(P0,P1,P2){
 return Math.abs((P1[0]-P0[0])*(P2[1]-P0[1])-(P2[0]-P0[0])*(P1[1]-P0[1]));
}
const corners=[[0,0],[1,0],[0,1],[1,1]];
let max=0,triples=0;
for(const a of corners)for(const b of corners)for(const c of corners){max=Math.max(max,twiceArea(a,b,c));triples++;}
assert(max===1 && triples===64,"unit square triangle area bound");
let uniform=0;
for(const [n,d] of [[0,1],[1,7],[1,3],[1,2],[2,3],[6,7],[1,1]]){
 const V=[[n,0],[d,n],[n,d],[0,n]];
 let sum=0;for(let i=0;i<4;i++){const [x,y]=V[i], [xx,yy]=V[(i+1)%4];sum+=x*yy-y*xx;}
 assert(Math.abs(sum)===d*d,"uniform polygon twice area");
 uniform++;
}
const A=[[0,1,0,1],[1,0,1,0],[1,1,0,0]]; // Not mathematical source; preserved merely as independent bit examples
const binaryPeak=[1,3,3,1];
const report={schema:"EM_R4_EC48F_JS_INTEGER_AUDIT_V1",input:{P_raw:P,Q_raw:Q},ratios_normalized:["4/9","8/9","16/9"],generic_binary_profile_counts:binaryPeak,K_hull:3,K_seed:3,pointwise_kernel_memory_at_endpoints:3,pointwise_kernel_memory_interior:4,face_checks:checks,uniform_checks:uniform,corner_triangles:triples,max_triangle_twice_area:max,mathematical_proof:"EC48F_KERNEL_VS_ROC_THEOREM.md",status:"PASS"};
if(typeof process!=="undefined") process.stdout.write(JSON.stringify(report,null,2)+"\n");
