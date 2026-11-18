// EC49FAI H9: explicit signed-X6 BRC 94-edge witness verifier; run: node VERIFY_EC49FAI_H9.js
// All arithmetic is exact integer (including rank modulo 1000003), no external libraries.
"use strict";
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],
 e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const H=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
const B=["N","A","B","AB","BA"];
const W={
 2:["ce","de","ec","ed"],
 3:["feg","gef"],
 4:["fegd","gefd","gefc","fegc"],
 5:["fegfg","geffg"],
 6:["geffgd","geffgc","fegfgd","fegfgc"],
 7:["fegfgfg","geffgfg"],
 8:["fegfgfgg","geffgfgg"],
 9:["fegfgfggg","geffgfggg"]
};
const expand=w=>[...w].flatMap(c=>OPS[c]);
function outputs(st) {
 return H.map(([start,p0])=>{
  let e=start,prev=p0;
  for(const s of st) {
   if(prev===1&&s===2){if(e==="N")e="A";else if(e==="B")e="BA";}
   else if(prev===2&&s===1){if(e==="N")e="B";else if(e==="A")e="AB";}
   prev=s;
  }
  return B.indexOf(e);
 });
}
function sign(obs){let n=0,m=1;for(const e of obs){n+=m*e;m*=5;}return n;}
const P=1000003;
function modpow(a,e){let r=1;while(e){if(e%2)r=(r*a)%P;a=(a*a)%P;e=Math.floor(e/2);}return r;}
function rank(ws){
 const outs=ws.map(w=>outputs(expand(w)));
 const mat=Array.from({length:9},(_,i)=>outs.flatMap(x=>B.map((_,j)=>+(x[i]===j))));
 const nr=mat.length,nc=mat[0].length;let r=0;
 for(let col=0;col<nc&&r<nr;col++){
  let pivot=r;while(pivot<nr&&mat[pivot][col]===0)pivot++;
  if(pivot===nr)continue;
  [mat[pivot],mat[r]]=[mat[r],mat[pivot]];
  const inv=modpow(mat[r][col],P-2);
  for(let j=col;j<nc;j++)mat[r][j]=(mat[r][j]*inv)%P;
  for(let i=r+1;i<nr;i++){const t=mat[i][col];if(!t)continue;
   for(let j=col;j<nc;j++)mat[i][j]=(mat[i][j]-t*mat[r][j]%P+P)%P;
  }
  r++;
 }
 return r;
}
function stepKey(st){return Array.from({length:6},(_,i)=>st.filter(s=>s===i+1).length);}
function signedNet(st){return Array.from({length:6},(_,i)=>st.filter(s=>s===i+1).length-st.filter(s=>s===-i-1).length);}
function run(){
 const firstTwo=Object.entries(OPS).map(([c,st])=>[c,st.slice(0,2).join(",")]);
 if(new Set(firstTwo.map(x=>x[1])).size!==7||Object.values(OPS).some(x=>x.length<2))
  throw Error("native terminal code not first-two distinguishing");
 const prefix=new Set(),keys=new Set(),signatures=new Set(),per=[];
 for(let h=2;h<=9;h++){
  const paths=W[h],ks=new Set(),sig=new Set();
  for(const word of paths){
   if(word.length!==h)throw Error("operation horizon mismatch");
   const st=expand(word),key=stepKey(st),net=signedNet(st);
   if(net.join(",")!=="2,0,0,0,0,0")throw Error("nonreturn");
   ks.add(key.join(","));keys.add(key.join(","));
   const s=sign(outputs(st));sig.add(s);signatures.add(s);
   for(let d=1;d<=st.length;d++)prefix.add(st.slice(0,d).join(","));
  }
  if(ks.size!==1||rank(paths)!==9)throw Error("key or rational rank failure at "+h);
  per.push({h,words:paths,positive_BRC_cache_key:[...ks][0].split(",").map(Number),
   observer_signatures:[...sig].sort((a,b)=>a-b),rank_mod_1000003:9,
   cumulative_primitive_prefix_edges:prefix.size});
 }
 const penultimate=per[6].cumulative_primitive_prefix_edges,final=per[7].cumulative_primitive_prefix_edges;
 if(penultimate!==90||final!==94||keys.size!==5||signatures.size!==6||final-penultimate!==4)
  throw Error("H9 resource regression");
 return {status:"EXPLICIT_H9_WITNESS_EXACT_PASS",scientific_scope:"new compatible H9 auxiliary signed-X6 BRC model",
  frozen_parent_science:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
  operation_code_first_two_unique:true,rank_prime:P,
  declared_horizon:9,distinct_complete_positive_BRC_keys:keys.size,
  distinct_nine_history_transfer_signatures:signatures.size,
  prefix_edges_H8:penultimate,prefix_edges_H9:final,increment:final-penultimate,
  lower_bound_from_EC49EXJ_M4_and_EC49FAH_M5:80,
  upper_bound_explicit:final,per_horizon:per,
  classification:"AUTHOR_EXPLICIT_CONSTRUCTION_AND_TRANSFER_PROOF_UNREVIEWED_NOT_ADMITTED"};
}
if(typeof require!=="undefined"&&typeof module!=="undefined"&&require.main===module)
 process.stdout.write(JSON.stringify(run(),null,2)+"\n");
