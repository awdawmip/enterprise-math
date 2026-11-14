"use strict";
function assert(ok,message){if(!ok)throw Error(message)}
function comb(n,k){
  const out=[];
  function walk(prefix,start){
    if(prefix.length===k){out.push(prefix);return}
    for(let i=start;i<n;i++)walk(prefix.concat(i),i+1)
  }
  walk([],0);return out
}
const states=comb(6,3);
const matchings=[
 [[0,1],[2,3],[4,5]],[[0,2],[1,4],[3,5]],
 [[0,3],[1,5],[2,4]],[[0,4],[1,3],[2,5]]
];
const pairs=comb(4,2);
const probes=[
 ["145","125","014"],["013","014","012"],["023","034","012"],
 ["024","045","012"],["345","135","034"],["012","025","013"],
 ["025","245","012"],["245","125","024"],["034","234","013"],
 ["245","345","024"]
];
const digits=s=>s.split("").map(Number);
const intersection=(a,b)=>a.filter(x=>b.includes(x)).length;
function code(S){
 return matchings.map(m=>{
   if(!m.every(([a,b])=>S.includes(a)!==S.includes(b)))return 0;
   return (m.filter(([a,b])=>S.includes(b)).length%2)?-1:1
 })
}
function coeff(S,T){
 const x=code(S),y=code(T);
 return y.concat(pairs.map(([i,j])=>x[i]*y[j]-x[j]*y[i]))
}
function subtract(a,b){return a.map((v,i)=>v-b[i])}
function row(s,t,u){
 const S=digits(s),T=digits(t),U=digits(u);
 assert(intersection(S,T)===2&&intersection(S,U)===2,"invalid edge");
 return subtract(coeff(S,T),coeff(S,U))
}
function bareiss(a){
 const m=a.map(r=>r.map(BigInt)),n=m.length;
 let divisor=1n,sign=1n;
 for(let k=0;k<n-1;k++){
   if(m[k][k]===0n){
     let p=k+1;while(p<n&&m[p][k]===0n)p++;
     if(p===n)return 0n;
     [m[k],m[p]]=[m[p],m[k]];sign=-sign
   }
   const pivot=m[k][k];
   for(let i=k+1;i<n;i++){
     for(let j=k+1;j<n;j++){
       const numerator=m[i][j]*pivot-m[i][k]*m[k][j];
       assert(numerator%divisor===0n,"non-exact Bareiss step");
       m[i][j]=numerator/divisor
     }
     m[i][k]=0n
   }
   divisor=pivot
 }
 return sign*m[n-1][n-1]
}
const matrix=probes.map(([s,t,u])=>row(s,t,u));
const determinant=bareiss(matrix);
const dot=(v,w)=>v.reduce((x,a,i)=>x+BigInt(a)*BigInt(w[i]),0n);
function decode(observations){
 const det=determinant;
 assert(det===1n||det===-1n,"not unimodular");
 return matrix[0].map((_,j)=>{
   const replaced=matrix.map((r,i)=>r.map((v,k)=>k===j?observations[i]:BigInt(v)));
   const num=bareiss(replaced);
   assert(num%det===0n,"nonintegral decoded coordinate");
   return num/det
 })
}
const omegaOf=theta=>{
 const O=Array.from({length:4},()=>Array(4).fill(0n));
 pairs.forEach(([i,j],k)=>{O[i][j]=theta[4+k];O[j][i]=-theta[4+k]});
 return O
};
function realize(theta){
 const M=Array.from({length:4},()=>Array(4).fill(0n));
 const O=omegaOf(theta);
 for(const [i,j] of pairs){
   if(O[i][j]>=0n)M[i][j]=O[i][j];else M[j][i]=-O[i][j]
 }
 const inner=Array.from({length:4},(_,i)=>M[i].reduce((z,v,j)=>z+v-M[j][i],0n));
 const rin=theta.slice(0,4).map((u,i)=>u>inner[i]?u-inner[i]:0n);
 const rout=theta.slice(0,4).map((u,i)=>inner[i]>u?inner[i]-u:0n);
 return {M,rin,rout}
}
function observe(L){
 const u=Array.from({length:4},(_,i)=>L.M[i].reduce((z,v,j)=>z+v-L.M[j][i],L.rin[i]-L.rout[i]));
 const omega=pairs.map(([i,j])=>L.M[i][j]-L.M[j][i]);
 return u.concat(omega)
}
function norm(a){return a.map(x=>x.toString())}
function equal(a,b){return norm(a).join(",")===norm(b).join(",")}
function copyLedger(L){return {M:L.M.map(x=>x.slice()),rin:L.rin.slice(),rout:L.rout.slice()}}
function main(){
 assert(states.length===20&&new Set(states.map(s=>code(s).join(","))).size===20,"V23 code enumeration");
 const edges=states.flatMap(S=>states.filter(T=>intersection(S,T)===2).map(T=>[S,T]));
 assert(edges.length===180,"directed edges");
 const all=states.flatMap(S=>{
   const near=states.filter(T=>intersection(S,T)===2);
   assert(near.length===9,"neighbors");
   return near.slice(1).map(T=>subtract(coeff(S,T),coeff(S,near[0])))
 });
 assert(all.length===160,"differences");
 assert(determinant===-1n,"ten-probe determinant");
 const testTheta=[-2,-4,-3,10,0,0,0,0,0,0].map(BigInt);
 const cyclicTheta=[-2,-4,-3,10,1,-1,0,1,0,0].map(BigInt);
 let checks=0;
 for(let n=0;n<51;n++){
   const th=Array.from({length:10},(_,i)=>BigInt(((n+3)*(i+7)+i*i*3)%29-14));
   const L=realize(th);
   assert(equal(observe(L),th),"realization failed");
   assert(equal(decode(matrix.map(r=>dot(r,th))),th),"decode failed");
   checks++
 }
 for(const th of [testTheta,cyclicTheta]){
   assert(equal(observe(realize(th)),th),"PF10 ledger witness");
   assert(equal(decode(matrix.map(r=>dot(r,th))),th),"PF10 readout witness");
   checks++
 }
 const events=[];
 const base=realize(cyclicTheta);
 for(let a=0;a<4;a++){
   for(let b=0;b<4;b++)if(a!==b){
     const L=copyLedger(base);L.M[a][b]++;
     const after=observe(L),before=observe(base),delta=after.map((x,i)=>x-before[i]);
     assert(equal(matrix.map(r=>dot(r,after)),matrix.map((r,i)=>dot(r,before)+dot(r,delta))),"PASS intertwining");
     events.push("PASS("+a+","+b+")")
   }
   for(const kind of ["IN","OUT"]){
     const L=copyLedger(base);
     if(kind==="IN")L.rin[a]++;else L.rout[a]++;
     const after=observe(L),before=observe(base),delta=after.map((x,i)=>x-before[i]);
     assert(equal(matrix.map(r=>dot(r,after)),matrix.map((r,i)=>dot(r,before)+dot(r,delta))),"boundary intertwining");
     events.push(kind+"("+a+")")
   }
 }
 assert(events.length===20,"event coverage");
 const d0=matrix.map(r=>dot(r,testTheta));
 const d1=matrix.map(r=>dot(r,cyclicTheta));
 assert(equal(d0,[-9,-4,-1,-14,-4,9,-3,-4,10,-5].map(BigInt)),"AT baseline");
 assert(equal(d1,[-9,-6,-1,-13,-3,9,-4,-4,10,-5].map(BigInt)),"AT first macro");
 return {
  result:"PASS",input:"V23 four matchings / V25 exponent differences / V29 signed contrast",
  method:"Exact BigInt Bareiss determinant, exact Cramer decoding, nonnegative ledger realization",
  state_count:states.length,directed_edges:edges.length,difference_rows:all.length,
  contrast_coordinates:10,determinant:determinant.toString(),
  coordinate_order:["u0","u1","u2","u3","Omega01","Omega02","Omega03","Omega12","Omega13","Omega23"],
  probes:probes.map((p,i)=>({S:p[0],T:p[1],U:p[2],row:matrix[i]})),
  at_baseline_d0:norm(d0),at_macro_d1:norm(d1),
  at_macro_slope:norm(d1.map((x,i)=>x-d0[i])),
  exact_decoding_and_realization_witnesses:checks,
  exact_event_increment_witnesses:events.length,
  events
 }
}
const output=main();
if(typeof console!=="undefined")console.log(JSON.stringify(output,null,2));
