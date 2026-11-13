// R762J — exact typed positive-branch N-BRC census (Node.js >= 16).
// Reproduces R762J_EVIDENCE.json. No physical-time or V29/V39 computation.
function verify(){
  const fact=n=>{let x=1n;for(let i=2;i<=n;i++)x*=BigInt(i);return x;};
  const pow=(n,k)=>BigInt(n)**BigInt(k);
  const assert=(cond,msg)=>{if(!cond)throw Error(msg);};
  function dp(n){
    let frontier=new Map([["0".repeat(n)+"|0",1n]]);
    const prefixTotals=[1n];
    let checkedStates=1;
    for(let t=0;t<2*n;t++){
      const nextFrontier=new Map();
      for(const [key,weight] of frontier){
        const [status,peakS]=key.split("|");
        const oldPeak=Number(peakS);
        for(let i=0;i<n;i++){
          const v=status[i];
          if(v==="2")continue;
          const after=status.slice(0,i)+(v==="0"?"1":"2")+status.slice(i+1);
          const occupancy=[...after].filter(x=>x==="1").length;
          const target=after+"|"+Math.max(oldPeak,occupancy);
          nextFrontier.set(target,(nextFrontier.get(target)||0n)+weight);
        }
      }
      const stateWeights=new Map();
      for(const [key,weight] of nextFrontier){
        const status=key.split("|")[0];
        stateWeights.set(status,(stateWeights.get(status)||0n)+weight);
      }
      for(const [status,weight] of stateWeights){
        const a=[...status].filter(x=>x==="1").length;
        const c=[...status].filter(x=>x==="2").length;
        assert(a+2*c===t+1,"prefix length");
        assert(weight===fact(t+1)/pow(2,c),"named-prefix multiplicity");
        checkedStates++;
      }
      prefixTotals.push([...nextFrontier.values()].reduce((a,b)=>a+b,0n));
      frontier=nextFrontier;
    }
    const hist=new Map();
    for(const [key,weight] of frontier){
      const [status,peak]=key.split("|");
      assert(status==="2".repeat(n),"terminal carrier state");
      hist.set(peak,(hist.get(peak)||0n)+weight);
    }
    const total=[...hist.values()].reduce((a,b)=>a+b,0n);
    assert(total===fact(2*n)/pow(2,n),"total schedules");
    assert(hist.get(String(n))===fact(n)*fact(n),"full co-presence schedules");
    assert(checkedStates===3**n,"all source-labelled ternary states");
    return {n,total,hist:Object.fromEntries([...hist].sort((a,b)=>Number(a[0])-Number(b[0]))),prefixTotals,checkedStates};
  }
  function boundedDyck(n,k){
    function walk(up,down,height,weight){
      if(up===n&&down===n)return weight;
      let sum=0n;
      if(up<n&&height<k)sum+=walk(up+1,down,height+1,weight);
      if(down<up)sum+=walk(up,down+1,height-1,weight*BigInt(height));
      return sum;
    }
    return walk(0,0,0,1n);
  }
  const rows=[];
  for(let n=1;n<=8;n++){
    const r=dp(n);
    let capped=0n;
    for(let k=1;k<=n;k++){
      capped+=r.hist[String(k)]||0n;
      assert(capped===fact(n)*boundedDyck(n,k),"independent weighted-Dyck census");
    }
    assert(r.hist["1"]===fact(n),"one-slot capacity");
    if(n>=2)assert((r.hist["1"]||0n)+(r.hist["2"]||0n)===fact(n)*pow(3,n-1),"two-slot capacity");
    rows.push({n,total:String(r.total),peakHistogram:Object.fromEntries(Object.entries(r.hist).map(([k,v])=>[k,String(v)])),prefixTotals:r.prefixTotals.map(String),allTriStatesChecked:r.checkedStates});
  }
  return {schema:"R762J_TYPED_BRC_TRISTATE_CENSUS_V1",scope:"Finite positive N-BRC source-tagged O_i/I_i branch counts; no native force-event admission or physical heartbeat dynamics",nRange:[1,8],minimalFutureLegalStates:"3^n",minimalFixedWidthBitsForThreeSources:5,capAtMostTwoFormula:"n!*3^(n-1) for n>=1",proofStatus:"Author-side exact proof plus independent two-way integer verification",allChecks:"PASS",rows};
}
console.log(JSON.stringify(verify(), null, 2));
