// PREFIX-836 exact independent named-state BigInt verification. Node.js, no dependencies.
// Source: frozen science f42f2906d77f24085c123f3ccfe9667d41caa96d.
function checkPrefix836() {
  const e = a => ({
    e1:a[0]+a[1]+a[2],
    e2:a[0]*a[1]+a[0]*a[2]+a[1]*a[2],
    e3:a[0]*a[1]*a[2]
  });
  function update(states, weights) {
    const next = new Map();
    const put=(key,v)=>next.set(key,(next.get(key)||0n)+v);
    for(const [key,value] of states) {
      const mask=key>>1, marked=key&1;
      const occupied=((mask&1)?1:0)+((mask&2)?1:0)+((mask&4)?1:0)+marked;
      for(let i=0;i<3;i++) if(mask & (1<<i)) put(((mask^(1<<i))<<1)|marked,value*weights[i]);
      if(marked) put(mask<<1,value*2n);
      if(!marked && occupied<3) put((mask<<1)|1,value);
    }
    return next;
  }
  function histogram(states) {
    let h=[0n,0n,0n,0n];
    for(const [key,v] of states) {
      const mask=key>>1,marked=key&1;
      const occ=((mask&1)?1:0)+((mask&2)?1:0)+((mask&4)?1:0)+marked;
      h[occ]+=v;
    }
    return h;
  }
  let x=3n,y=3n; const records=[];let comparisons=0;
  for(let k=1;k<=5;k++){
    [x,y]=[3n*x+2n*y,4n*x+3n*y];
    const c=(y-1n)/2n;
    const A=[1n,x+1n,x+1n], B=[2n,x+c+1n,x-c];
    const ea=e(A),eb=e(B);
    const d1=ea.e1-eb.e1,d2=ea.e2-eb.e2,d3=ea.e3-eb.e3;
    const T=2n+(x-3n)*(x+1n)/6n;
    if(2n*x*x-y*y!==9n||d1!==0n||d2!==(x-3n)*(x+1n)/2n||d3!==-4n||T%2n!==0n||4n*d2+3n*(T-2n)*d3!==0n) throw Error("Algebra mismatch k="+k);
    let equal=null;
    if(k<=2){
      let sA=new Map([[14,1n]]),sB=new Map([[14,1n]]), hits=[];
      for(let t=0;t<=Number(T)+2;t++){
        const hA=histogram(sA),hB=histogram(sB); comparisons+=4;
        if(hA.every((v,i)=>v===hB[i])) hits.push(t);
        if(t<Number(T)+2){sA=update(sA,A);sB=update(sB,B);}
      }
      if(JSON.stringify(hits)!==JSON.stringify([0,1,Number(T)]))throw Error("Recollision mismatch "+k);
      equal=hits;
    }
    const max = A.concat(B).reduce((a,b)=>a>b?a:b,0n);
    records.push({k,x:x.toString(),y:y.toString(),T:T.toString(),A:A.map(String),B:B.map(String),delta_e2:d2.toString(),delta_e3:d3.toString(),M:max.toString(),verified_full_histogram_equality_times:equal});
  }
  return {schema:"PREFIX836_EXACT_CHECK_V1",verified_pell_instances:records.length,independent_named_histogram_scalar_comparisons:comparisons,independent_named_check_range:"t=0..T+2 for k=1,2",all_assertions_passed:true,records};
}
if(typeof process !== 'undefined') process.stdout.write(JSON.stringify(checkPrefix836(),null,2)+'\n');
