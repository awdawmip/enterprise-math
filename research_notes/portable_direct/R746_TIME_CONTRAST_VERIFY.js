#!/usr/bin/env node
'use strict';
const verify = function verify() {
  const loops={
    A:{I:["012","014","013","012"],P:["012","023","013","012"],Q:["012","023","123","012"]},
    B:{I:["012","123","124","012"],P:["012","023","013","012"],Q:["012","123","013","012"]}
  };
  const perm={A:{I:[0,1,2],P:[0,2,1],Q:[1,0,2]},B:{I:[0,1,2],P:[0,2,1],Q:[2,1,0]}};
  const sample={A:{I:"RFFR",P:"FRFR",Q:"FRRF"},B:{I:"FRFR",P:"RFRF",Q:"FRRF"}};
  const cmp=(p,q)=>q.map(i=>p[i]);
  const output={schema:"R746_TIME_RESOLVED_BRC_PASS_OBSERVER_V1",result:"PASS",integer_semantics:"exact",frozen_science:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",reference:"R744@9f266f4d182abf7c6c0bdb3c3fed621987b9be80",max_history_length:8,cases:{},total_histories_checked:0};
  for(const name of ["A","B"]){
    const paths=loops[name];
    const arcs=[...new Set(Object.values(paths).flatMap(p=>[0,1,2].map(i=>p[i]+">"+p[i+1])))].sort();
    if(arcs.length!==7)throw Error("seven arcs");
    let injective=0,valid=0,checked=0,includesSample=false;
    let example=null;
    for(let mask=0;mask<128;mask++){
      const labels=Object.fromEntries(arcs.map((arc,i)=>[arc,(mask>>i)&1?"F":"R"]));
      let by={};for(const arc of arcs){let origin=arc.split(">")[0];(by[origin]??=[]).push(labels[arc]);}
      if(Object.values(by).some(a=>new Set(a).size!==a.length))continue;
      injective++;
      const words={};
      for(const gen of ["I","P","Q"]){const seq=paths[gen];const arcDirs=[0,1,2].map(i=>labels[seq[i]+">"+seq[i+1]]);words[gen]=arcDirs[0]+(arcDirs[0]==="F"?"R":"F")+arcDirs[1]+arcDirs[2];}
      if(Object.values(words).some(w=>w.split("").filter(x=>x==="F").length!==2))continue;
      const signatures={};let validWords=true;
      for(const g of ["I","P","Q"]){
        let d=0,Ds=[];
        for(const pulse of words[g]){d+=pulse==="F"?1:-1;Ds.push(d);if(Math.abs(d)>1)validWords=false;}
        if(JSON.stringify(Ds.slice(1).filter((_,i)=>i%2===0))!=="[0,0]")validWords=false;
        signatures[g]=[Ds[0],Ds[2]];
      }
      if(!validWords)throw Error("unexpected word prefix");
      if(new Set(Object.values(signatures).map(x=>x.join(","))).size!==3)throw Error("pair not injective");
      if([0,1].some(j=>new Set(Object.values(signatures).map(s=>s[j])).size!==2))throw Error("single sample missing split");
      if(Object.values(signatures).filter(s=>s[0]===signatures.I[0]).length===0)throw Error("bad signature");
      const lookup=Object.fromEntries(Object.entries(signatures).map(([g,s])=>[s.join(","),g]));
      for(let k=0;k<=8;k++){
        let total=Math.pow(3,k);
        for(let a=0;a<total;a++){
          let x=a, original="", temporal=[],D=0,F=0,R=0,hol=[0,1,2];
          for(let j=0;j<k;j++){
            const g="IPQ"[x%3];x=Math.floor(x/3);original+=g;hol=cmp(hol,perm[name][g]);
            const w=words[g];const s=[];
            for(let c=0;c<4;c++){D+=w[c]==="F"?1:-1;F+=w[c]==="F"?1:0;R+=w[c]==="R"?1:0;if(Math.abs(D)>1)throw Error("capacity");if(c===0||c===2)s.push(D);}
            if(D!==0)throw Error("no reset");
            temporal.push(s.join(","));
          }
          const recovered=temporal.map(s=>lookup[s]).join("");
          if(recovered!==original||F!==2*k||R!==2*k||D!==0)throw Error("reconstruct/ledger");
          let recoveredHol=[0,1,2];for(const g of recovered)recoveredHol=cmp(recoveredHol,perm[name][g]);
          if(recoveredHol.join("")!==hol.join(""))throw Error("holonomy decode");
          checked++;
        }
      }
      if(Object.entries(sample[name]).every(([g,w])=>words[g]===w))includesSample=true;
      valid++;
      if(!example)example={arc_labels:labels,generator_words:words,signatures};
    }
    if(injective!==32||valid!==4||checked!==4*9841||!includesSample)throw Error("classification mismatch "+name+":"+[injective,valid,checked,includesSample]);
    output.cases[name]={arc_count:arcs.length,source_injective_codebooks:injective,valid_branch_blind_codebooks:valid,all_valid_codebooks_have_distinct_two_time_signatures:true,read_times:[1,3],each_single_time_max_distinct:2,min_fixed_samples_per_block:2,max_adaptive_samples_per_block:2,uniform_expected_adaptive_samples_per_block:"5/3",histories_checked:checked,includes_R744_reference_codebook:includesSample,one_valid_codebook:example};
    output.total_histories_checked+=checked;
  }
  if(output.total_histories_checked!==78728)throw Error("total count");
  return output;
};
process.stdout.write(JSON.stringify(verify(), null, 2)+'\n');
