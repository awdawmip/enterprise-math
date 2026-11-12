'use strict';
// R742 exact source-compatible exhaustive checker. Node.js standard runtime only.
const result=(function validate(){
 const net={A:{I:{code:"FRR",perm:[0,1,2]},P:{code:"RFR",perm:[0,2,1]},Q:{code:"RRF",perm:[1,0,2]}},B:{I:{code:"RRF",perm:[0,1,2]},P:{code:"FRR",perm:[0,2,1]},Q:{code:"RFR",perm:[2,1,0]}}};
 const mul=(a,b)=>b.map(i=>a[i]);
 const eq=(a,b,msg)=>{if(JSON.stringify(a)!==JSON.stringify(b))throw Error(msg+" "+JSON.stringify(a)+" != "+JSON.stringify(b));};
 const out={schema:"R742_PERIODIC_TWO_PORT_EXACT_CHECK_V1",status:"PASS",model:"conditional stock-moving refinement of V29 PASS with an identity-guarded return PASS at each 012-root",max_k_exhaustive:8,histories_each_carrier:0,carriers:{},witness_words:["III","IIP","IIQ","IPQ","IQP","PQP"]};
 for(const [carrier,gens] of Object.entries(net)){
  const samples=[], witness={};let totalHist=0;
  for(let k=0;k<=8;k++){
   let histories=0;const states=new Set();
   const run=w=>{
    histories++;let n0=1,n1=2,F=0,R=0,h=[0,1,2],un0=1,un1=k+1;
    for(const symbol of w){
     const {code,perm}=gens[symbol];
     eq([...code].sort(),["F","R","R"].sort(),"word symbols");
     for(const pulse of code+"F"){
      if(pulse==="F"){if(n0<1)throw Error("underflow 0 "+carrier+w);n0--;n1++;F++;}
      else {if(n1<1)throw Error("underflow 1 "+carrier+w);n1--;n0++;R++;}
      if(n0<0||n1<0||n0>3||n1>3)throw Error("capacity violation "+carrier+w);
     }
     eq([n0,n1],[1,2],"not periodic "+carrier+w);
     for(const pulse of code){
      if(pulse==="F"){if(un0<1)throw Error("unpumped underflow 0");un0--;un1++;}
      else {if(un1<1)throw Error("unpumped underflow 1");un1--;un0++;}
     }
     h=mul(h,perm);
    }
    eq([F,R],[2*k,2*k],"ledger "+carrier+w);
    eq([un0,un1],[k+1,1],"unpumped endpoint "+carrier+w);
    const name=h.join("");states.add(name);
    if(k===3&&out.witness_words.includes(w))witness[w]=name;
   };
   const dfs=s=>{if(s.length===k){run(s);return;}for(const c of ["I","P","Q"])dfs(s+c);};
   dfs("");
   if(histories!==3**k)throw Error("enumeration count mismatch");
   const target=k===0?1:k===1?3:k===2?5:6;
   if(states.size!==target)throw Error("six-state scope "+carrier+" "+k+" got "+states.size);
   samples.push({k,histories,distinct_final_relations:states.size});totalHist+=histories;
  }
  eq(Object.keys(witness).sort(),out.witness_words.slice().sort(),"missing witnesses");
  if(new Set(Object.values(witness)).size!==6)throw Error("witness not complete");
  out.carriers[carrier]={samples,witness,all_checks:"PASS"};
  if(totalHist!==9841)throw Error("histories total mismatch");
  out.histories_each_carrier=totalHist;
 }
 return out;
})();
console.log(JSON.stringify(result,null,2));
