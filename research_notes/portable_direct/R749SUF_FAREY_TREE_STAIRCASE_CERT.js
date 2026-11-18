function histogram(M) {
  const stack=[[1,0,0,1]], bins=new Map(); let nodes=0, positive=0;
  while(stack.length){
    const [a,u,v,d]=stack.pop(); nodes++;
    if(a>0&&u>0&&v>0&&d>0) {
      positive++;
      const t=Math.max(u,v)*a*d;
      bins.set(t,(bins.get(t)||0)+1);
    }
    const l=[a,a+u,v,v+d], r=[a+u,u,v+d,d];
    if(Math.max(...l)<=M) stack.push(l);
    if(Math.max(...r)<=M) stack.push(r);
  }
  return {nodes,positive,bins:Array.from(bins.entries()).sort((x,y)=>y[0]-x[0])};
}

function brute(M) {
  const bins=new Map();
  for(let a=1;a<=M;a++)for(let d=1;d<=M;d++)for(let u=1;u<=M;u++){
    const p=a*d-1;
    if(p%u!==0)continue;
    const v=p/u;
    if(v<1||v>M)continue;
    const t=Math.max(u,v)*a*d;
    bins.set(t,(bins.get(t)||0)+1);
  }
  return Array.from(bins.entries()).sort((x,y)=>y[0]-x[0]);
}

function phi(n){
  let c=0;
  for(let a=1;a<=n;a++){
    let x=a,y=n; while(y){const t=x%y;x=y;y=t}
    if(x===1)c++;
  }
  return c;
}

function fullDeficit(M,K){
  let count=0;
  for(let a=1;a<=M;a++)for(let d=1;d<=M;d++)for(let u=1;u<=M;u++)for(let v=1;v<=M;v++){
    const delta=a*d-u*v;
    if(delta>0&&K*delta<=Math.max(u,v)*a*d)count++;
  }
  return count;
}

function verify(){
  let totalPhi=0, pairs=0, directChecks=0;
  const sample={}, counts={};
  for(let M=1;M<=64;M++){
    const t=histogram(M), b=brute(M);
    if(JSON.stringify(t.bins)!==JSON.stringify(b))throw Error("independent histogram mismatch M="+M);
    if(t.positive+2*M+1!==t.nodes)throw Error("tree node count M="+M);
    totalPhi+=phi(M);
    if(t.positive!==4*totalPhi-2*M-2)throw Error("totient mismatch M="+M);
    if(t.bins.some(([k,v])=>v%2!==0))throw Error("odd threshold multiplicity M="+M);
    pairs++;
    if(M<=16){
      const sat=M===1?2:M===2?5:M*(M-1)*(M-1)+1;
      const probes=new Set([M+1, Math.floor(M**3/2)+1,Math.max(M+1,sat-1),sat,sat+1]);
      for(const K of probes){
        if(K<=M || 2*K<=M**3)continue;
        const treeD=t.bins.filter(([z])=>z>=K).reduce((s,[,c])=>s+c,0);
        const direct=fullDeficit(M,K);
        if(treeD!==direct)throw Error("late direct deficit mismatch M="+M+" K="+K+" tree="+treeD+" direct="+direct);
        directChecks++;
      }
    }
    if([5,10,16,32,64].includes(M)){
      const first=Math.floor(M**3/2)+1, late=t.bins.filter(([z])=>z>=first);
      sample[M]={positive_matrices:t.positive,tree_nodes:t.nodes,distinct_thresholds:t.bins.length,late_start:first,late_deficit:late.reduce((s,[,c])=>s+c,0),late_jump_bins:late.length,highest_thresholds:t.bins.slice(0,6)};
    }
  }
  return {status:"PASS",input_domain:{M_min:1,M_max:64},tests:{independent_histogram_equalities:pairs,totient_checks:pairs,even_jumps:pairs,direct_four_loop_late_deficit_checks:directChecks},sample,scope:"Exact integer arithmetic within JS Number safe integer range for M<=64; general theorem proved symbolically; no independent review."};
}

console.log(JSON.stringify(verify(),null,2));
