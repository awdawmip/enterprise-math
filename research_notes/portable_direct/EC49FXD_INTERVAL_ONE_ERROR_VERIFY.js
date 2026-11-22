'use strict';
// Self-contained exact verification of EC49FXD; no external dependencies.
const result = (function verify() {
  const mod=(a,n)=>(a%n+n)%n;
  const layout=(k)=>{
    const s=Math.max(0,Math.min(5,Math.floor((46-k)/2)));
    const sites=[],light=[];
    for(let x=23-s;x<=22;x++){sites.push(x,x+5);light.push([x,x+5]);}
    const occupied=new Set(light.map(p=>p[0]%5));
    for(let i=0;i<5;i++)if(!occupied.has(i))sites.push(i,i+5,i+10);
    sites.sort((a,b)=>a-b);
    return {k,light_blocks:s,optimal_activations:15-s,sites};
  };
  const distance=(sites,d,i,j)=>{
    let n=0;
    for(const t of sites){
      if(t%5===i && t%11!==j)n++;
      if(mod(d-t,5)===i && mod(d-t,11)!==j)n++;
    }
    return n;
  };
  const rows=[];let checks=0;
  for(let k=1;k<=55;k++){
    const row=layout(k),S=row.sites;
    if(S.length!==row.optimal_activations||new Set(S).size!==S.length)throw Error("bad layout k="+k);
    let minimum=100;
    for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
      const f=distance(S,d,i,j);
      minimum=Math.min(minimum,f);
      checks++;
      if(f<3)throw Error("insufficient distance "+[k,d,i,j,f].join(","));
    }
    rows.push({...row,minimum_sampled_distance:minimum});
  }
  if(checks!==84700)throw Error("expected 84700 constraints, got "+checks);
  const admissible=(k)=>{
    const out=[];
    for(let i=0;i<5;i++)for(let x=i;x<55;x+=5)for(let y=x+5;y<55;y+=5){
      if([2*x,x+y,2*y].every(v=>mod(v,55)>=k))out.push({i,x,y});
    }
    return out;
  };
  const compatible=(k,p,q)=>p.i!==q.i&&[p.x,p.y].every(x=>[q.x,q.y].every(y=>mod(x+y,55)>=k));
  const clique=(k,pairs)=>{
    let maximum=0,witness=[],nodes=0;
    const rec=(start,used,chosen)=>{
      nodes++;
      if(chosen.length>maximum){maximum=chosen.length;witness=chosen.map(j=>pairs[j]);}
      for(let j=start;j<pairs.length;j++){
        if(used&(1<<pairs[j].i))continue;
        if(chosen.every(n=>compatible(k,pairs[n],pairs[j])))
          rec(j+1,used|(1<<pairs[j].i),[...chosen,j]);
      }
    };
    rec(0,0,[]);
    return {maximum_compatible_light_blocks:maximum,witness,visited_subsets:nodes};
  };
  const thresholds=[37,39,41,43,45].map(k=>{
    const pairs=admissible(k),res=clique(k,pairs);
    if(res.maximum_compatible_light_blocks!==Math.max(0,Math.floor((46-k)/2))) throw Error("clique error k="+k);
    return {k,admissible_light_pairs:pairs,...res};
  });
  return {schema:"EC49FXD_R3_INTERVAL_CERTIFICATE_V1",frozen_scientific_pin:"BRC16943",model:"two-channel CRT, D_k=[0,k-1], Hamming distance r=3",exact_arithmetic:true,all_pass:true,distance_checks:checks,threshold_obstructions:thresholds,rows};
})();
console.log(JSON.stringify(result,null,2));
