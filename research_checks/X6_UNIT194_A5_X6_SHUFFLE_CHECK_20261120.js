"use strict";
// Unit194: complete A5-root versus signed-X6 path comparison. Node.js BigInt.
// Inputs: six integer coordinates, zero sum, 1/2 sum |z_i| <= 5.
// Independent subproblem DP recurrences, not calls into a rewritten P022 model.
const factorial=n=>{let x=1n;for(let i=2;i<=n;i++)x*=BigInt(i);return x};
function run(){
 const rootMemo=new Map(),signedMemo=new Map(),limit=5,byR={};
 let vectors=0,violations=0,nonadjacent=0n,example=null;
 function root(z){
  const key=z.join(",");if(rootMemo.has(key))return rootMemo.get(key);
  if(z.every(x=>x===0))return 1n;
  let n=0n;for(let i=0;i<6;i++)if(z[i]>0)for(let j=0;j<6;j++)if(z[j]<0){
    const v=z.slice();v[i]--;v[j]++;n+=root(v);
  }rootMemo.set(key,n);return n;
 }
 function signed(c){
  const key=c.join(",");if(signedMemo.has(key))return signedMemo.get(key);
  if(c.every(x=>x===0))return 1n;
  let n=0n;for(let i=0;i<6;i++)if(c[i]>0){const v=c.slice();v[i]--;n+=signed(v);}
  signedMemo.set(key,n);return n;
 }
 function visit(i,z,total,l1){
  if(i===6){
   if(total!==0||l1>2*limit)return;
   const r=l1/2,den=z.reduce((v,x)=>v*factorial(Math.abs(x)),1n);
   const A=(factorial(r)**2n)/den,X=factorial(2*r)/den;
   const aa=root(z),xx=signed(z.map(Math.abs)),bin=factorial(2*r)/(factorial(r)**2n);
   const local=(2n**BigInt(r))*aa;
   if(aa!==A||xx!==X||xx!==bin*aa||local>xx)violations++;
   if(!example&&r>=2&&local<xx)example={z:z.slice(),r,root:String(aa),signed:String(xx),adjacent:String(local),unrepresented:String(xx-local)};
   vectors++;const row=byR[r]??(byR[r]={cases:0,root:0n,signed:0n,adjacent:0n,ratio:bin});
   row.cases++;row.root+=aa;row.signed+=xx;row.adjacent+=local;nonadjacent+=xx-local;return;
  }
  for(let x=-limit;x<=limit;x++){
   if(l1+Math.abs(x)>2*limit)continue;
   z.push(x);visit(i+1,z,total+x,l1+Math.abs(x));z.pop();
  }
 }
 visit(0,[],0,0);
 return {
  schema:"X6_UNIT194_A5_X6_SIGN_SHUFFLE_EXACT_CERT_V1",
  date:"2026-11-20",
  model:"six signed integer coordinates, sum=0, two primitive signed axes per A5 root transfer",
  source_pins:{frozen_science:"59538f585d037d09ef687b28715c4bc1a3f9fe03",frozen_historical:"fd2bcff10ca6e147348b6c1236027fc0d2877df3"},
  max_transfer_radius:limit,
  balanced_vectors:vectors,
  violation_count:violations,
  independent_dp_state_counts:{A5:rootMemo.size,X6:signedMemo.size},
  by_radius:Object.fromEntries(Object.entries(byR).map(([r,v])=>[r,{
   vectors:v.cases,A5_root_mass:String(v.root),signed_X6_mass:String(v.signed),
   adjacent_transfer_lifts:String(v.adjacent),nonadjacent_signed_words:String(v.signed-v.adjacent),
   exact_fiber_size:String(v.ratio)
  }])),
  example,
  total_nonadjacent_signed_words:String(nonadjacent),
  original_R063_native_benchmark_rerun:false,
  original_P022_module_imported_and_executed:false,
  independent_driver_review:"UNREVIEWED / NOT_ADMITTED"
 };
}
if(typeof require!=="undefined"&&require.main===module)console.log(JSON.stringify(run(),null,2));
if(typeof module!=="undefined")module.exports={run};
