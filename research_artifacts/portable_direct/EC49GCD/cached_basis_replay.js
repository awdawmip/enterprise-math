function replay(){
  let seed=20261128; const rnd=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
  const pop=x=>{let n=0;for(;x;x&=x-1)n++;return n};
  const bits=function*(x){for(;x;x&=x-1)yield x&-x};
  const low=x=>x&-x;
  const stats={models:0,stages:0,coordinates:0,initialBases:0,skipChecks:0,takeChecks:0,skipExchange:0,skipColoop:0,takeExchange:0,takeFree:0,takeInBasis:0,cachedConstraintVisits:0,greedyConstraintVisits:0,greedyCalls:0,originalHallChecks:0,languageChecks:0,disagreements:0,cacheBasisBits:0};
  function ck(x,msg){if(!x)throw Error(msg)}
  for(let rep=0;rep<500;rep++){
    const n=2+rnd(6),m=5+rnd(8),C=(1<<n)-1,F0=(1<<m)-1;
    const caps=Array.from({length:n},()=>1+rnd(4)),E=Array.from({length:m},()=>1+rnd(C));
    const ports=Array.from({length:C+1},(_,u)=>E.reduce((a,e,i)=>a|((e&u)===e?1<<i:0),0));
    const cap=Array.from({length:C+1},(_,u)=>caps.reduce((a,c,i)=>a+((u>>i)&1)*c,0));
    function independent(s){for(let u=1;u<=C;u++){stats.originalHallChecks++;if(pop(s&ports[u])>=cap[u])return false}return true}
    function unions(F){let ws=new Set([0]);for(const bit of bits(F)){const e=E[31-Math.clz32(bit)];for(const w of [...ws])ws.add(w|e)}return [...ws].filter(Boolean).sort((a,b)=>a-b)}
    function directBasis(S,Q){let b=0;for(const bit of bits(Q))if(independent(S|b|bit))b|=bit;return b}
    function constraints(F,cache){return [...cache].map(([w,b])=>[ports[w]&F,pop(b)])}
    function pIndependent(Q,cs,count){for(const [L,r] of cs){if(count)stats.greedyConstraintVisits++;if(pop(Q&L)>r)return false}return true}
    function pBasis(Q,cs){stats.greedyCalls++;let b=0;for(const bit of bits(Q))if(pIndependent(b|bit,cs,true))b|=bit;return b}
    let S=0,F=F0,cache=new Map(unions(F).map(w=>[w,directBasis(0,ports[w]&F)]));stats.initialBases+=cache.size;
    stats.models++;
    while(F){
      stats.stages++;const x=low(F),nextF=F^x,cs=constraints(F,cache),takeOK=pIndependent(x,cs,false);
      ck(takeOK===independent(S|x),"singleton");
      // A direct finite observer-language check on small suffixes.
      if(pop(F)<=7){for(let Q=F;;Q=(Q-1)&F){stats.languageChecks++;ck(pIndependent(Q,cs,false)===independent(S|Q),"language");if(!Q)break}}
      const skip=new Map(),take=new Map();
      for(const w of unions(nextF)){
        stats.coordinates++;const B=cache.get(w),Q=ports[w]&nextF;
        stats.cacheBasisBits+=m;
        let blocked=0,common=B,hasTightX=false;
        // Both updates share this single sweep; no fresh greedy rank computation.
        if((B&x)||takeOK){for(const [L,r] of cs){stats.cachedConstraintVisits++;if(pop(B&L)!==r)continue;
          if(L&x){hasTightX=true;common&=L}else blocked|=L;
        }}
        let bs=B;
        if(B&x){const y=low(Q&~B&~blocked);bs=(B^x)|y;if(y)stats.skipExchange++;else stats.skipColoop++}
        skip.set(w,bs);
        const skipRef=directBasis(S,Q);stats.skipChecks++;
        ck((bs&~Q)===0&&independent(S|bs)&&pop(bs)===pop(skipRef),"skip basis");
        if((ports[w]&x)!==0){const bg=pBasis(Q,cs);ck(pop(bg)===pop(bs),"skip greedy")}
        if(takeOK){
          let bt;
          if(B&x){bt=B^x;stats.takeInBasis++}
          else if(!hasTightX){bt=B;stats.takeFree++}
          else {ck(common!==0,"fundamental circuit empty");bt=B^low(common);stats.takeExchange++}
          take.set(w,bt);
          const tr=directBasis(S|x,Q);stats.takeChecks++;
          ck((bt&~Q)===0&&independent(S|x|bt)&&pop(bt)===pop(tr),"take basis");
          if(!(ports[w]&x)){const bg=pBasis(Q|x,cs);ck(pop(bg)-1===pop(bt),"take greedy")}
        }
      }
      // Carry the actual cached witnesses through one deterministic path, while checking both children.
      if(takeOK&&rnd(2)){S|=x;cache=take}else cache=skip;
      F=nextF;
    }
  }
  return stats;
}
console.log(JSON.stringify(replay(), null, 2));
