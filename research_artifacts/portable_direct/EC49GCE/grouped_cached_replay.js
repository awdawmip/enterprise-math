function replay(){
 let seed=20261128;const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
 const stats={seed:20261128,models:0,budgets:0,bruteSubsets:0,witnessChecks:0,rankChecks:0,blockFormulaChecks:0,repeatedSupportModels:0,maxGroup:0,disagreements:0};
 const modes=["greedy","cached","grouped"];
 for(const mode of modes)stats[mode]={stages:0,generated:0,states:0,peak:0,rankCalls:0,greedyTests:0,tightScans:0,comparisons:0,comparisonCoordinates:0,rankEntries:0,nominalBasisBits:0,elapsedMs:0};
 const check=(p,m)=>{if(!p){stats.disagreements++;throw Error(m)}};
 const sub=(a,b)=>(a&b)===a;
 for(let it=0;it<350;it++){
  let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
  for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
  for(let x of A)if(x.s)c[Math.log2(x.e)]++;
  let cc=Array.from({length:N},(_,v)=>c.reduce((s,a,i)=>s+((v>>i&1)*a),0)),pop=new Uint8Array(M),contained=Array(N).fill(0);
  for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
  for(let v=0;v<N;v++)for(let j=0;j<m;j++)if(sub(A[j].e,v))contained[v]|=1<<j;
  const independent=z=>cc.every((cv,v)=>!v||pop[z&contained[v]]<cv);
  const basisDirect=(z,Q)=>{let I=0;for(let q=Q;q;q&=q-1){let bit=q&-q;if(independent(z|I|bit))I|=bit}return I};
  const rankDirect=(z,Q)=>pop[basisDirect(z,Q)];
  const singles=A.map((_,j)=>1<<j),groups=new Map();
  for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
  let blocks=[...groups.values()];if(blocks.length<m)stats.repeatedSupportModels++;
  stats.maxGroup=Math.max(stats.maxGroup,...blocks.map(x=>pop[x]));
  function stage(F){let unions=new Set([0]);for(let q=F;q;q&=q-1){let bit=q&-q,j=31-Math.clz32(bit);for(let w of [...unions])unions.add(w|A[j].e)}
   let w=[...unions].filter(x=>x!==0).sort((a,b)=>a-b);return {F,w,f:w.map(x=>contained[x]&F)}}
  function value(z){let p=0,s=0;for(let j=0;j<m;j++)if(z>>j&1){p+=A[j].p;s+=A[j].s}return {p,s}}
  function options(H){let real=[],aux=[];for(let j=0;j<m;j++)if(H>>j&1)(A[j].s?aux:real).push(j);
   real.sort((i,j)=>A[j].p-A[i].p||i-j);aux.sort((i,j)=>A[j].s-A[i].s||i-j);
   const prefixes=ls=>{let v=[0];for(let j of ls)v.push(v[v.length-1]|(1<<j));return v};
   let out=[];for(let r of prefixes(real))for(let a of prefixes(aux)){let mask=r|a;out.push({mask,t:pop[mask],...value(mask)})}return out
  }
  function dp(mode){
   let st=stats[mode],start=Date.now(),F=M-1,old=stage(F),bs=old.f.map(Q=>basisDirect(0,Q)),states=[{v:bs.map(b=>pop[b]),b:mode==="cached"?bs:null,p:0,s:0,mask:0}];
   for(let H of mode==="grouped"?blocks:singles){
    F^=H;let next=stage(F),prior=next.w.map(w=>old.w.indexOf(w)),map=new Map(),opts=options(H);
    function add(z){st.generated++;let key=z.v.join(",")+"|"+z.s,prev=map.get(key);if(!prev||z.p>prev.p)map.set(key,z)}
    for(let a of states){
     const feasible=Q=>{for(let i=0;i<old.f.length;i++){st.greedyTests++;if(pop[Q&old.f[i]]>a.v[i])return false}return true};
     const memo=new Map(),rank=Q=>{if(memo.has(Q))return memo.get(Q);st.rankCalls++;let I=0;for(let q=Q;q;q&=q-1){let y=q&-q;if(feasible(I|y))I|=y}let r=pop[I];memo.set(Q,r);return r};
     if(mode==="grouped"){
      let maxTake=rank(H),pairs=next.f.map((Q,i)=>old.f[prior[i]]&H?[rank(Q),a.v[prior[i]]]:[a.v[prior[i]],rank(Q|H)]);
      for(let o of opts)if(o.t<=maxTake){let v=pairs.map(([r,u])=>Math.min(r,u-o.t));add({v,p:a.p+o.p,s:a.s+o.s,mask:a.mask|o.mask});
       for(let i=0;i<v.length;i++){stats.blockFormulaChecks++;check(v[i]===rankDirect(a.mask|o.mask,next.f[i]),"grouped rank formula")}
      }
     }else{
      let bit=H,x=A[31-Math.clz32(bit)],can=feasible(bit);
      if(mode==="greedy"){
       add({...a,v:next.f.map((Q,i)=>(old.f[prior[i]]&bit)?rank(Q):a.v[prior[i]])});
       if(can)add({v:next.f.map((Q,i)=>(old.f[prior[i]]&bit)?a.v[prior[i]]-1:rank(Q|bit)-1),p:a.p+x.p,s:a.s+x.s,mask:a.mask|bit});
      }else{
       let skip=[],take=[];
       for(let i=0;i<next.f.length;i++){
        let B=a.b[prior[i]],Q=next.f[i],D=0,C=B,tight=false;
        if((B&bit)||can)for(let j=0;j<old.f.length;j++){st.tightScans++;let L=old.f[j];if(pop[B&L]!==a.v[j])continue;if(L&bit){tight=true;C&=L}else D|=L}
        if(B&bit){let Y=Q&~(B|D);skip.push((B^bit)|(Y&-Y));if(can)take.push(B^bit)}
        else{skip.push(B);if(can){check(!tight||C!==0,"empty circuit");take.push(tight?B^(C&-C):B)}}
       }
       add({...a,b:skip,v:skip.map(b=>pop[b])});
       if(can)add({b:take,v:take.map(b=>pop[b]),p:a.p+x.p,s:a.s+x.s,mask:a.mask|bit});
      }
     }
    }
    let vals=[...map.values()].sort((a,b)=>b.p-a.p||b.s-a.s),keep=[];
    for(let a of vals){let dominated=false;for(let q of keep){if(q.s<a.s||q.p<a.p)continue;st.comparisons++;let ok=true;for(let i=0;i<a.v.length;i++){st.comparisonCoordinates++;if(q.v[i]<a.v[i]){ok=false;break}}if(ok){dominated=true;break}}if(!dominated)keep.push(a)}
    states=keep;st.stages++;st.states+=states.length;st.peak=Math.max(st.peak,states.length);st.rankEntries+=states.length*next.f.length;if(mode==="cached")st.nominalBasisBits+=states.length*next.f.length*pop[F];
    for(let a of states)for(let i=0;i<next.f.length;i++){stats.rankChecks++;check(a.v[i]===rankDirect(a.mask,next.f[i]),"retained rank");if(mode==="cached")check(sub(a.b[i],next.f[i])&&pop[a.b[i]]===a.v[i]&&independent(a.mask|a.b[i]),"cached witness")}
    old=next;
   }
   st.elapsedMs+=Date.now()-start;return states;
  }
  let D=A.reduce((s,x)=>s+x.s,0),best=Array(D+1).fill(-1);
  for(let z=0;z<M;z++){stats.bruteSubsets++;if(!independent(z))continue;let {p,s}=value(z);best[D-s]=Math.max(best[D-s],p)}
  for(let k=1;k<=D;k++)best[k]=Math.max(best[k],best[k-1]);
  let runs=modes.map(dp);
  for(let k=0;k<=D;k++){stats.budgets++;for(let states of runs){let winner=states.find(x=>D-x.s<=k);check(winner&&winner.p===best[k],"budget optimum");let v=value(winner.mask);check(independent(winner.mask)&&v.p===winner.p&&v.s===winner.s&&D-v.s<=k,"label witness");stats.witnessChecks++}}
  stats.models++;
 }
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
