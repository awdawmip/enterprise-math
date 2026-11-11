"use strict";
// Exact enumeration of the R735 signed X6 six-step N-BRC carrier. No external libraries.
// Run: node research_notes/R735_X6_SIGNED_LOOP_CIRCULATION_VERIFY.js
function verifyR735() {
  const moves=[0,1,2].flatMap(i=>[[i,1],[i,-1]]);
  const pairs=[[0,1],[0,2],[1,2]];
  const buckets={},joint={},signCounts={};
  let countAll=0,countNB=0,first6=0,nbFirst6=0;
  const w=[];
  const assert=(test,msg)=>{if(!test)throw Error(msg)};
  function checkWord(){
    countAll++;
    const x=[0,0,0], twiceJ=[0,0,0], signs=[0,0,0];
    let hasReverse=false,firstReturn=0;
    for(let t=0;t<6;t++){
      const [i,s]=w[t];
      if(signs[i]===0)signs[i]=s;
      if(t>0&&w[t-1][0]===i&&w[t-1][1]===-s)hasReverse=true;
      for(let p=0;p<3;p++){
        const [a,b]=pairs[p];
        if(i===a)twiceJ[p]-=x[b]*s;
        if(i===b)twiceJ[p]+=x[a]*s;
      }
      x[i]+=s;
      if(!firstReturn&&x.every(z=>z===0))firstReturn=t+1;
    }
    assert(x.every(z=>z===0),"not closed");
    if(firstReturn===6)first6++;
    if(hasReverse)return;
    countNB++;
    if(firstReturn===6)nbFirst6++;
    assert(twiceJ.every(z=>z%2===0),"odd antisymmetric circulation");
    const J=twiceJ.map(z=>z/2), jk=signs.join(",")+"|"+J.join(",");
    const areaKey=J.join(","), signKey=signs.join(",");
    buckets[areaKey]=(buckets[areaKey]||0)+1;
    signCounts[signKey]=(signCounts[signKey]||0)+1;
    (joint[jk] ||= []).push(w.map(([i,s])=>(s>0?"+":"-")+i).join(" "));
  }
  function permute(rest){
    if(!rest.length){checkWord();return;}
    for(let p=0;p<rest.length;p++){
      w.push(rest[p]);
      permute(rest.slice(0,p).concat(rest.slice(p+1)));
      w.pop();
    }
  }
  permute(moves);
  assert(countAll===720&&countNB===240&&first6===480&&nbFirst6===240,"R734 regression");
  const supportTotals={1:0,2:0,3:0},multiplicities={1:new Set(),2:new Set(),3:new Set()};
  for(const [k,n] of Object.entries(buckets)){
    const s=k.split(",").map(Number).filter(z=>z!==0).length;
    assert(s>=1&&s<=3,"unexpected zero-current or range");
    assert(k.split(",").map(Number).every(z=>z>=-1&&z<=1),"current out of range");
    supportTotals[s]+=n; multiplicities[s].add(n);
  }
  assert(Object.keys(buckets).length===26,"not 26 current signatures");
  for(const [support,wantTotal,wantCount] of [[1,48,8],[2,144,12],[3,48,6]]){
    assert(supportTotals[support]===wantTotal,"support total "+support);
    assert(multiplicities[support].size===1&&multiplicities[support].has(wantCount),"multiplicity "+support);
  }
  assert(Object.keys(signCounts).length===8&&Object.values(signCounts).every(n=>n===30),"source signs");
  const jointFibers={};
  for(const words of Object.values(joint)){jointFibers[words.length]=(jointFibers[words.length]||0)+1;}
  assert(Object.keys(joint).length===192&&jointFibers[1]===144&&jointFibers[2]===48&&Object.keys(jointFibers).length===2,"joint fibers");
  const x=joint["1,1,1|1,1,0"];
  assert(x&&x.length===2,"collision not present");
  return {schema:"R735_X6_SIGNED_LOOP_CIRCULATION_EXACT_V1",date:"2026-11-12",frozen_science:"a72226e2430ffa4786321ac86e7f0c599d5f0389",previous_research_commit:"c598be3c00b39bf8ddcbf70d2edef7b25dd1caa3",scope:"three fixed distinct signed axes, all six +i,-i once, ordered words, NB prohibits adjacent inverse",total_words:countAll,first_return_six:first6,nonbacktracking:countNB,nb_first_return_six:nbFirst6,source_signatures:8,nb_per_signature:30,distinct_integer_signed_circulations:Object.keys(buckets).length,circulation_support_totals:supportTotals,area_fiber_size_by_support:{1:8,2:12,3:6},joint_source_circulation_fibers:Object.keys(joint).length,joint_fiber_counts:jointFibers,maximum_current_only_fiber:12,maximum_joint_fiber:2,worst_case_repair_bits:{current_only:4,source_and_current:1},collision:{observer:"1,1,1|1,1,0",path_a:x[0],path_b:x[1]},check:"R735_X6_SIGNED_LOOP_CIRCULATION_EXACT_PASS",physical_triadic_closure_verified:false,real_V29_V39_update_verified:false};
}
console.log(JSON.stringify(verifyR735(), null, 2));
