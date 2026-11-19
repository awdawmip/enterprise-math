// R42: exact named-Port BRC action conflict graph enumeration; Node.js >=18
// Declared conditional whole-triad transfer; not verified native inter-Cell dynamics.
function r42Verify(){
 const pop=x=>{let n=0;while(x){n++;x&=x-1;}return n};
 const distribution={}, cases={}, byEdgeCount={}, aggregate={configurations:0,serialHistories:0};
 function test(mask){
   let adj=Array(6).fill(0);
   for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)if(Math.floor(i/3)===Math.floor(j/3)){adj[i]|=1<<j;adj[j]|=1<<i;}
   for(let i=0;i<3;i++)for(let j=0;j<3;j++)if(mask&(1<<(3*i+j))){adj[i]|=1<<(j+3);adj[j+3]|=1<<i;}
   const enabled=done=>{let v=0;for(let i=0;i<6;i++)if(!(done&(1<<i))&&!(adj[i]&done))v|=1<<i;return v};
   const independent=done=>{for(let i=0;i<6;i++)if((done&(1<<i))&&(adj[i]&done))return false;return true};
   let configs=[0,0,0],hist=[0,0,0],classes=new Set();
   for(let done=0;done<64;done++)if(independent(done)){
      const k=pop(done);if(k>2)throw Error("source cannot fire twice");
      configs[k]++;let e=enabled(done);classes.add(e);
      for(let i=0;i<6;i++)if(e&(1<<i))if(enabled(done|(1<<i))!==(e&~(1<<i)&~adj[i]))throw Error("Markov quotient mismatch");
   }
   function dfs(done,k){hist[k]++;let e=enabled(done);for(let i=0;i<6;i++)if(e&(1<<i))dfs(done|(1<<i),k+1);}
   dfs(0,0);
   const e=pop(mask);
   if(configs.join(",")!==[1,6,9-e].join(",")||hist.join(",")!==[1,6,2*(9-e)].join(","))throw Error("count mismatch");
   return {crossEdges:e,configurationsBySize:configs,serialHistoriesBySize:hist,futureNamedLanguageClasses:classes.size};
 }
 for(let mask=0;mask<512;mask++){
   let d=test(mask),n=d.futureNamedLanguageClasses;
   distribution[n]=(distribution[n]||0)+1;
   byEdgeCount[d.crossEdges]=(byEdgeCount[d.crossEdges]||0)+1;
   aggregate.configurations+=d.configurationsBySize.reduce((a,b)=>a+b,0);
   aggregate.serialHistories+=d.serialHistoriesBySize.reduce((a,b)=>a+b,0);
   if(mask===0)cases.noCross=d;
   if(mask===1)cases.oneCross=d;
   if(mask===511)cases.allCross=d;
 }
 if(aggregate.configurations!==5888||aggregate.serialHistories!==8192||cases.oneCross.futureNamedLanguageClasses!==6)throw Error("aggregate check");
 return {schema:"EM_X6_R42_PORT_CONFLICT_BRC_V1",status:"PASS",graphs:512,byCrossEdgeCount:byEdgeCount,futureNamedLanguageClassDistribution:distribution,aggregate,cases};
}
process.stdout.write(JSON.stringify(r42Verify(),null,2)+"\n");
