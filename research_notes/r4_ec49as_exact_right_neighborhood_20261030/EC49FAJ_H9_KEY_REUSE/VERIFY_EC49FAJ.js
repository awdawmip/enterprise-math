"use strict";
// Exact integer / modular-rank audit for four H9 five-key witnesses.
// Reuses author-side EC49FAB first seven horizons; alters h8 and adds h9.
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const START=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
const BUCKETS=["N","A","B","AB","BA"];
const B2=["de","ed","ce","ec"], B3=["feg","gef"];
const CASES={
 "1512":{4:["defg","edfg","fegc","gefc"],5:["fegfg","geffg"],6:["fegfgg","geffgg"],7:["fegfggg","geffggg"]},
 "1513":{4:["defg","edfg","fegc","gefc"],5:["fegfg","geffg"],6:["fegfgf","geffgf"],7:["fegfgff","geffgff"]},
 "2200":{4:["fegg","gefg"],5:["feggd","gefgd","feggc","gefgc"],6:["fegggf","gefggf"],7:["fegggfg","gefggfg"]},
 "2203":{4:["fegf","geff"],5:["fegfd","geffd","fegfc","geffc"],6:["fegfgf","geffgf"],7:["fegfgff","geffgff"]}
};
const P=1000003;
function expand(w){return [...w].flatMap(c=>OPS[c]);}
function output(st){return START.map(([name,prev0])=>{
 let e=name,prev=prev0;
 for(const s of st){
  if(prev===1&&s===2){if(e==="N")e="A";else if(e==="B")e="BA";}
  else if(prev===2&&s===1){if(e==="N")e="B";else if(e==="A")e="AB";}
  prev=s;
 }
 return BUCKETS.indexOf(e);
});}
function signature(out){let s=0,p=1;for(const x of out){s+=x*p;p*=5;}return s;}
function rank(ws){
 const os=ws.map(w=>output(expand(w)));
 const M=Array.from({length:9},(_,i)=>os.flatMap(o=>Array.from({length:5},(_,j)=>+(o[i]===j))));
 let r=0;
 for(let col=0;col<M[0].length&&r<9;col++){
  let j=r;while(j<9&&!M[j][col])j++;
  if(j===9)continue;
  [M[r],M[j]]=[M[j],M[r]];
  let inv=1,ex=P-2,a=M[r][col];while(ex){if(ex%2)inv=inv*a%P;a=a*a%P;ex=Math.floor(ex/2);}
  for(let k=col;k<M[r].length;k++)M[r][k]=M[r][k]*inv%P;
  for(let i=r+1;i<9;i++){
   const f=M[i][col];if(!f)continue;
   for(let k=col;k<M[i].length;k++)M[i][k]=(M[i][k]-f*M[r][k]%P+P)%P;
  }
  r++;
 }
 return r;
}
function primitivePrefixes(ws){const s=new Set();for(const w of ws){const st=expand(w);for(let j=1;j<=st.length;j++)s.add(st.slice(0,j).join(","));}return s;}
function keysForHorizon(h){const out=new Set();for(let z=1;2*z-1<=h;z++)for(let r=0;r<=h-2*z+1;r++)for(let f=0;f<=h-2*z+1-r;f++){
 const g=h-2*z+1-r-f;out.add([2*z+r+f,r+g,z].join(","));}return out;}
function check(){
 const key8=keysForHorizon(8),key9=keysForHorizon(9),intersection=[...key8].filter(x=>key9.has(x));
 if(key8.size!==70||key9.size!==95||intersection.length!==50)throw Error("key census changed");
 const report={scope:"H9 native signed X6, M=5, S<=6; author-side constructions",frozen_parent:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",arithmetic:"signed integer steps; rank over F_1000003 implies rank 9 over Q",key_census:{h8:key8.size,h9:key9.size,overlap:intersection.length},cases:[]};
 for(const [id,src] of Object.entries(CASES)){
  const h={2:B2,3:B3,...src};const roots=src[7];
  h[8]=roots.flatMap(w=>[w+"c",w+"d"]);
  h[9]=roots.map(w=>w+"fg");
  const allP=new Set(),kset=new Set(),sset=new Set(),per=[];
  for(let horizon=2;horizon<=9;horizon++){
   const ks=new Set(),sigs=new Set();
   for(const w of h[horizon]){
    if(w.length!==horizon)throw Error("horizon mismatch");
    const steps=expand(w);
    const key=Array.from({length:6},(_,i)=>steps.filter(x=>x===i+1).length);
    const net=Array.from({length:6},(_,i)=>steps.filter(x=>x===i+1).length-steps.filter(x=>x===-i-1).length);
    if(net.join()!=="2,0,0,0,0,0")throw Error("signed displacement mismatch");
    ks.add(key.join());kset.add(key.join());
    const sig=signature(output(steps));sigs.add(sig);sset.add(sig);
    for(const pre of primitivePrefixes([w]))allP.add(pre);
   }
   const rk=rank(h[horizon]);if(ks.size!==1||rk!==9)throw Error("horizon key or rank failure "+id+"/"+horizon);
   per.push({h:horizon,words:h[horizon],key:[...ks][0],signatures:[...sigs].sort((a,b)=>a-b),rank_mod_P:rk,prefix_edges:allP.size});
  }
  if(kset.size!==5||sset.size!==6||per[5].prefix_edges!==72||per[6].prefix_edges!==88||per[7].prefix_edges!==94)
   throw Error("global constraint or cost mismatch "+id);
  if(per[6].key!==per[7].key)throw Error("key not reused at h9");
  report.cases.push({source_rank:Number(id),key_h8_h9:per[7].key,edge_progression:per.map(x=>x.prefix_edges),rank_all_horizons:per.map(x=>x.rank_mod_P),h8:h[8],h9:h[9],signature_count:sset.size,key_count:kset.size});
 }
 return report;
}
if(require.main===module)console.log(JSON.stringify(check(),null,2));
module.exports={check};
