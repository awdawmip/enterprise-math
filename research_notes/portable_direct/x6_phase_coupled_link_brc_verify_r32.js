function cloneS(s){return {c:s.c,p:s.p.slice(),u:s.u};}

function acts(cfg,s,theta,nonprobe=false){
 const out=[],n=cfg.n,base=3**n;
 let ix=0;for(let i=0;i<n;i++)ix+=s.p[i]*3**i;
 for(let j=0;j<cfg.delta.length;j++){const t=cfg.delta[j][s.c*base+ix];if(t!==-1){const v=cloneS(s);v.c=t;out.push(["A"+j,v]);}}
 for(let i=0;i<n;i++){if(s.p[i]===0){const v=cloneS(s);v.p[i]=1;out.push(["P"+i+"+",v]);}else if(s.p[i]===1){const v=cloneS(s);v.p[i]=2;out.push(["P"+i+"-",v]);}}
 if(!nonprobe){for(let i=0;i<n;i++)if(s.p[i]===2&&!(s.u&(1<<i))&&((theta&(1<<i))||(cfg.link[s.c]&(1<<i)))){const v=cloneS(s);v.u|=1<<i;out.push(["Q"+i,v]);}}
 return out;
}

function dist(cfg,initial,i){
 if(initial.u&(1<<i))return Infinity;
 let todo=[[initial,0]], seen=new Set();
 while(todo.length){const [s,d]=todo.shift();const key=s.c+":"+s.p.join("");if(seen.has(key))continue;seen.add(key);
 if(s.p[i]===2 && !(cfg.link[s.c]&(1<<i)))return d;
 for(const [_,v] of acts(cfg,s,0,true))todo.push([v,d+1]);
 }return Infinity;
}

function langSig(cfg,initial,theta,maxH){
 const result=[""],words=[];let front=[["",initial]];
 for(let h=1;h<=maxH;h++){let next=[];for(const [word,s] of front){for(const [a,v] of acts(cfg,s,theta)){const w=word?word+","+a:a;next.push([w,v]);}}
 let ws=next.map(x=>x[0]).sort();words.push(ws.join("|"));result.push(words.join("||"));front=next;}
 return result;
}

function verifyCfg(cfg,maxH){
 const init={c:cfg.c0,p:Array(cfg.n).fill(0),u:0},d=Array.from({length:cfg.n},(_,i)=>dist(cfg,init,i));
 const sigs=Array.from({length:2**cfg.n},(_,th)=>langSig(cfg,init,th,maxH));
 let comparisons=0;
 for(let a=0;a<sigs.length;a++)for(let b=a+1;b<sigs.length;b++)for(let h=0;h<=maxH;h++){
   const exp=d.every((di,i)=>di+1>h || ((a>>i&1)===(b>>i&1)));
   const got=sigs[a][h]===sigs[b][h];comparisons++;
   if(exp!==got) return {ok:false,error:{cfg,d,a,b,h,exp,got},comparisons};
 }
 return {ok:true,comparisons,distances:d.map(x=>Number.isFinite(x)?x:null),classCounts:Array.from({length:maxH+1},(_,h)=>new Set(sigs.map(s=>s[h])).size)};
}

function makeResults(){
 const n1H=6,n2H=7,rng={s:20261119};
 function rand(){rng.s=(Math.imul(rng.s,1664525)+1013904223)>>>0;return rng.s;}
 let exhaustiveCases=0,seededCases=0,comparisons=0;
 for(let v=0;v<729;v++){
   let x=v,d=[];for(let k=0;k<6;k++){d.push(x%3-1);x=Math.floor(x/3);}
   for(let mask=0;mask<4;mask++)for(let c0=0;c0<2;c0++){
     const z=verifyCfg({n:1,c0,link:[mask&1,(mask>>1)&1],delta:[d]},n1H);
     if(!z.ok)throw Error("EXHAUSTIVE_COUNTEREXAMPLE "+JSON.stringify(z.error));
     exhaustiveCases++;comparisons+=z.comparisons;
   }
 }
 for(let k=0;k<128;k++){
   const d=Array.from({length:18},()=>rand()%3-1);
   const z=verifyCfg({n:2,c0:rand()%2,link:[rand()%4,rand()%4],delta:[d]},n2H);
   if(!z.ok)throw Error("SEEDED_COUNTEREXAMPLE "+JSON.stringify(z.error));
   seededCases++;comparisons+=z.comparisons;
 }
 const one={n:1,c0:0,link:[1,0],delta:[[-1,-1,1,-1,-1,-1]]};
 const joint={n:2,c0:0,link:[3,0],delta:[Array.from({length:18},(_,i)=>i===8?1:-1)]};
 const oneCheck=verifyCfg(one,n2H),jointCheck=verifyCfg(joint,n2H);
 if(!oneCheck.ok||!jointCheck.ok)throw Error("EXAMPLE_FAILED");
 comparisons+=oneCheck.comparisons+jointCheck.comparisons;
 const out={
  schema:"X6_R32_PHASE_COUPLED_LINK_BOOLEAN_BRC_CHECK_V1",
  model:"Deterministic labelled finite public controller, phase-dependent hidden-independent controls, one-use inert probes",
  method:"Exact enumeration of all successful labelled words, not sampled word equivalence; BFS of nonprobe control/phase graph",
  exhaustive:{n:1,public_states:2,one_public_action:true,partial_action_tables:729,link_assignments:4,initial_controller_choices:2,configurations:exhaustiveCases,max_h:n1H},
  seeded:{n:2,public_states:2,one_public_action:true,configurations:seededCases,seed:20261119,prng:"LCG 1664525*x+1013904223 modulo 2^32",max_h:n2H},
  witnesses:{
   one_source:{d:oneCheck.distances,first_distinguishing_depth:4,class_counts:oneCheck.classCounts,witness:["P0+","P0-","A0","Q0"]},
   two_source_joint_gate:{d:jointCheck.distances,first_distinguishing_depth:6,class_counts:jointCheck.classCounts,witness_for_0:["P0+","P0-","P1+","P1-","A0","Q0"]}
  },
  hidden_pair_horizon_comparisons:comparisons,
  all_checks:"PASS",
  status:"FINITE_EXACT_CHECK_ONLY; GENERAL_THEOREM_HAS_SEPARATE_SYMBOLIC_PROOF; NOT_INDEPENDENTLY_REVIEWED",
  frozen_p000:"a72226e2430ffa4786321ac86e7f0c599d5f0389"
 };
 return out;
}

console.log(JSON.stringify(makeResults(), null, 2));
