"use strict";
const verify = function verify(){
  "use strict";
  const M=[[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]];
  const ok=(b,msg)=>{if(!b)throw Error(msg)};
  let maxGrid=0,nRows=0;
  for(let n=0;n<15625;n++){
    let t=n,k=[];
    for(let j=0;j<6;j++){k.push(t%5);t=Math.floor(t/5);}
    for(const row of M){
      const t3=row.reduce((s,w,j)=>s+w*k[j],0);
      const direct=(Math.abs(t3-40)+Math.abs(80-t3-40))/2;
      const linear=Math.abs(row.reduce((s,w,j)=>s+w*(k[j]-2),0));
      ok(direct===linear&&direct<=40,"grid TV discrepancy");
      maxGrid=Math.max(maxGrid,direct);nRows++;
    }
  }
  ok(maxGrid===40,"radius");
  const minima=Array(7).fill(Infinity),minMasks=Array.from({length:7},()=>[]);
  let vertexChecks=0,strict=0;
  for(let mask=0;mask<64;mask++){
    const k=mask.toString(2).replace(/0/g,"").length;
    const predicted=Math.max(...M.map(row=>row.reduce((s,w,j)=>s+w*(2-((mask>>j)&1)),0)));
    let actual=0;
    for(let v=0;v<64;v++){
      for(const row of M){
        const diff=row.reduce((s,w,j)=>s+w*((((v>>j)&1)?(((mask>>j)&1)?2:4):0)-(((mask>>j)&1)?1:2)),0);
        actual=Math.max(actual,Math.abs(diff));vertexChecks++;
      }
    }
    ok(predicted===actual,"vertex: "+mask);
    const hits=!!(mask&3)&&!!(mask&4)&&!!(mask&24)&&!!(mask&32);
    ok((predicted<40)===hits,"group criterion: "+mask);
    if(predicted<40)strict++;
    if(predicted<minima[k]){minima[k]=predicted;minMasks[k]=[mask];}
    else if(predicted===minima[k])minMasks[k].push(mask);
  }
  ok(JSON.stringify(minima)==="[40,40,40,40,30,30,20]","size optimum");
  ok(JSON.stringify(minMasks[4])==="[54]","unique best four");
  const D=[[11,-9,0,0,0,0],[1,-1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,9,-1,0],[0,0,0,1,-1,0],[0,0,0,0,0,1]];
  for(let j=0;j<6;j++){
    ok(D[j].every(q=>Math.abs(q)<=16),"illegal witness "+j);
    for(let i=0;i<6;i++){
      const dot=M[i].reduce((s,w,x)=>s+w*D[j][x],0);
      ok(i===j ? dot!==0 : dot===0,"row deletion "+j);
    }
  }
  return {pass:"PASS_BRC_N4_S23_SIX_CONTROL_BOX_SPLIT_ERASURE_20261101",environment:"V8 JavaScript exact integer arithmetic",grid_points:15625,grid_row_checks:nRows,split_subsets:64,split_vertex_row_checks:vertexChecks,minimum_radius_numerator_over_160_by_split_count:minima,optimal_four_split_mask:54,optimal_four_split_sources:["AU1","AV","BU1","BV"],best_four_split_radius:"3/16",grid_radius:"1/4",erasure_witnesses:6,all_real_parameters:"proved analytically; grid is not the proof"};
};
const result = verify();
console.log(JSON.stringify(result, null, 2));
