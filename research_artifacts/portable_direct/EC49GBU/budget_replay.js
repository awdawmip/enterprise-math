function replay(){
  let state=20261127, models=500, allocations=0, subsetChecks=0, budgetChecks=0, prefixChecks=0, nestingChecks=0, dualChecks=0;
  function rnd(n){state^=state<<13;state^=state>>>17;state^=state<<5;return (state>>>0)%n}
  const pop=x=>{let s=0;while(x){x&=x-1;s++}return s};
  const assert=(b,...x)=>{if(!b)throw Error(JSON.stringify(x))};
  for(let z=0;z<models;z++){
    const n=1+rnd(4),m=rnd(8),c=Array.from({length:n},()=>1+rnd(3)),d=[];
    for(let t=0;t<rnd(7)+1 && d.length<6;t++)d.push(rnd(n));
    const items=Array.from({length:m},(_,i)=>({e:1+rnd((1<<n)-1),w:rnd(10),i})).sort((a,b)=>b.w-a.w||a.i-b.i);
    const D=d.length,L=1<<D,P=1<<m,cap0=c.slice(), full=c.slice();for(const j of d)full[j]++;
    const ranks=[],best=[],chosen=[];
    for(let R=0;R<L;R++){
      const cap=cap0.slice();for(let a=0;a<D;a++)if(R>>a&1)cap[d[a]]++;
      const cc=Array.from({length:1<<n},(_,V)=>cap.reduce((s,x,j)=>s+((V>>j&1)?x:0),0));
      let good=[],maxw=0,rr=Array(m+1).fill(0);
      for(let I=0;I<P;I++){
        subsetChecks++;let ok=true;
        for(let V=1;V<1<<n;V++){let f=0;for(let j=0;j<m;j++)if((I>>j&1)&&(items[j].e&V)===items[j].e)f++;if(f>=cc[V]){ok=false;break}}
        if(!ok)continue;
        good.push(I);
        let w=0;for(let j=0;j<m;j++)if(I>>j&1)w+=items[j].w;maxw=Math.max(maxw,w);
        for(let p=0;p<=m;p++)if((I>>p)===0)rr[p]=Math.max(rr[p],pop(I));
      }
      let chosenMask=0;for(let p=1;p<=m;p++)if(rr[p]>rr[p-1])chosenMask|=1<<(p-1);
      assert(good.includes(chosenMask),z,R,"greedy feasible");
      assert(items.reduce((s,x,i)=>s+((chosenMask>>i&1)?x.w:0),0)===maxw,z,R,"greedy value");
      ranks.push(rr);best.push(maxw);chosen.push(chosenMask);allocations++;
    }
    // Independently compute full-capacity rank of real-prefix plus unreleased dummy labels
    // by brute force only over real subsets: every dummy set is independent, and
    // contraction by it means the all-dummy-constrained rank is dummies + remaining real rank.
    for(let R=0;R<L;R++)for(let e=0;e<D;e++)if(!(R>>e&1)){
      const T=R|(1<<e);
      assert((chosen[R]&~chosen[T])===0,z,R,T,"nested greedy");nestingChecks++;
      let last=0;
      for(let p=0;p<=m;p++){const gain=ranks[T][p]-ranks[R][p];assert(gain===0||gain===1,z,R,T,p);assert(gain>=last,z,R,T,p,"layer lift");last=gain;dualChecks++}
    }
    let R=0;
    for(let k=0;k<=D;k++){
      const v=Math.max(...best.filter((_,a)=>pop(a)<=k));assert(best[R]===v,z,k,"budget optimum");
      for(let p=0;p<=m;p++){
        const expected=Math.min(ranks[0][p]+k,ranks[L-1][p]);
        assert(ranks[R][p]===expected,z,k,p,"simultaneous prefix ranks");
        prefixChecks++;
      }
      budgetChecks++;
      if(k===D)break;
      // Pick earliest prefix where a released label increases rank, even for zero weight.
      let a0=-1,first=m+1;
      for(let a=0;a<D;a++)if(!(R>>a&1)){
        let T=R|(1<<a),p=1;while(p<=m&&ranks[T][p]===ranks[R][p])p++;
        if(a0<0||p<first){a0=a;first=p}
      }
      R|=1<<a0;
    }
  }
  return {seed:20261127,models,allocations,subsetChecks,budgetChecks,prefixChecks,nestingChecks,dualChecks,disagreements:0};
}
console.log(JSON.stringify(replay(),null,2));
