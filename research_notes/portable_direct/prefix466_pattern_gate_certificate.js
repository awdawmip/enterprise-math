// PREFIX-466: exact integer native-X6 positive-BRC pattern-gate certificate.
// Node.js 18+; no dependencies. The observer is exact endpoint/product-weight/count.
function main() {
  const assert=(c,m)=>{if(!c)throw Error(m)};
  const letters=[
    ["x",0,1,1n],
    ["a",1,1,6n],["-a",1,-1,1n],
    ["b",2,1,12n],["-b",2,-1,1n],
    ["c",3,1,18n],["-c",3,-1,1n],
    ["d",4,1,24n],["-d",4,-1,1n],
    ["e",5,1,36n],["-e",5,-1,1n]
  ];
  const rho=[6n,12n,18n,24n,36n];
  const log=[];
  const key=st=>[st[0],...st[1],st[2],st[3],st[4]].join(",");
  const initial=[0,[0,0,0,0,0],0,0,0]; // x-count, y[5], A, C, suffix-state
  function evolve(st,t,n) {
    const [name,axis,dir]=t;
    const [s,oldY,oldA,oldC,q]=st;
    if(name==="x" && n!==0 && q!==2) return null;
    const y=oldY.slice();let A=oldA,C=oldC;
    if(axis>0) {
      const i=axis-1;
      const createsPair=(dir===1 && y[i]<0)||(dir===-1 && y[i]>0);
      if(createsPair) {
        if(axis===2 || axis===5) A++;
        if(axis===4) A+=2;
        if(axis===3 || axis===5) C++;
      }
      y[i]+=dir;
    }
    const nq=name==="a"?1:name==="b"&&q===1?2:0;
    return [s+(axis===0?1:0),y,A,C,nq];
  }
  function stateWeight(st,n){
    const [s,y,A,C]=st;
    const rem=n-s-y.reduce((u,v)=>u+Math.abs(v),0);
    assert(rem>=0 && rem%2===0,"bad native pair parity");
    let w=6n**BigInt(rem/2)*2n**BigInt(A)*3n**BigInt(C);
    for(let i=0;i<5;i++)w*=rho[i]**BigInt(Math.max(0,y[i]));
    return w;
  }
  // Independent generator for scalar totals, from rational generating function.
  function series(S,c,chi,k,nmax){
    const out=[1n];
    for(let n=1;n<=nmax;n++)
      out[n]=S*out[n-1]+(n>=k+1?c*out[n-k-1]:0n)+(n===1?chi:0n);
    return out;
  }
  const expectedCounts=series(10n,1n,1n,2,8);
  const expectedMass=series(101n,72n,1n,2,8);
  let dist=new Map([[key(initial),{state:initial,n:1n}]]);
  const results=[];
  function brute(n){
    const m=new Map();const word=[];let leaves=0n;
    function add(wprod){
      const y=[0,0,0,0,0],plus=[0,0,0,0,0],minus=[0,0,0,0,0];
      let s=0;
      for(const t of word) {
        if(t[1]===0){s++;continue}
        const i=t[1]-1;y[i]+=t[2];
        if(t[2]===1)plus[i]++;else minus[i]++;
      }
      const p=plus.map((v,i)=>Math.min(v,minus[i]));
      const A=p[1]+2*p[3]+p[4],C=p[2]+p[4];
      const q=word.length>1&&word.at(-2)[0]==="a"&&word.at(-1)[0]==="b"?2
        :word.length&&word.at(-1)[0]==="a"?1:0;
      const st=[s,y,A,C,q],id=key(st);
      assert(stateWeight(st,n)===wprod,"path-product reconstruction fails");
      m.set(id,(m.get(id)||0n)+1n);leaves++;
    }
    function dfs(weight){
      if(word.length===n){add(weight);return}
      for(const t of letters){
        if(t[0]==="x"&&word.length>0&&
           !(word.length>=2&&word.at(-2)[0]==="a"&&word.at(-1)[0]==="b"))
          continue;
        word.push(t);dfs(weight*t[3]);word.pop();
      }
    }
    dfs(1n);
    return {m,leaves};
  }
  for(let n=0;n<=8;n++){
    let count=0n,mass=0n;
    for(const {state,n:mult} of dist.values()){
      count+=mult;mass+=mult*stateWeight(state,n);
    }
    assert(count===expectedCounts[n],"count rational series mismatch at "+n);
    assert(mass===expectedMass[n],"mass rational series mismatch at "+n);
    if(n<=5){
      const b=brute(n);
      assert(b.leaves===count&&b.m.size===dist.size,"brute size mismatch at "+n);
      for(const [id,{n:num}] of dist)assert(b.m.get(id)===num,"brute histogram mismatch at "+n+" key "+id);
    }
    results.push("n="+n+" states="+dist.size+" ordered="+count+" weighted_mass="+mass+
      (n<=5?" brute=PASS":""));
    if(n===8)break;
    const next=new Map();
    for(const {state,n:mult} of dist.values())for(const t of letters){
      const st=evolve(state,t,n);if(!st)continue;
      const id=key(st),old=next.get(id);
      if(old)old.n+=mult;else next.set(id,{state:st,n:mult});
    }
    dist=next;
  }
  // Same endpoint/weight/signature but all 3 suffix states, all at length 3.
  const witnesses=[["a","b","c"],["b","c","a"],["c","a","b"]];
  const states=witnesses.map(w=>{
    let st=initial;
    for(let i=0;i<w.length;i++){
      const t=letters.find(x=>x[0]===w[i]);
      st=evolve(st,t,i);assert(st!==null,"witness rejected");
    }
    return st;
  });
  assert(new Set(states.map(st=>key(st).split(",").slice(0,-1).join(","))).size===1,
    "witness projected states differ");
  assert(states.map(st=>st[4]).join(",")==="0,1,2","suffix witness states differ");
  assert(states.every(st=>stateWeight(st,3)===1296n),"witness weights differ");
  // Generic word-pattern gate over a reduced alphabet: 3 non-x letters, weighted 2,3,5.
  // Completely independent brute enumeration of weighted totals.
  const ordinary=[["a",2n],["b",3n],["c",5n]];
  for(const w of [["a"],["a","b"],["a","b","a"],["a","a"]]){
    const k=w.length,chi=7n,c=w.reduce((x,v)=>x*ordinary.find(t=>t[0]===v)[1],chi);
    const eq=series(10n,c,chi,k,6);
    const actual=[];
    for(let n=0;n<=6;n++){
      let value=0n;const arr=[];
      function dfs(v){
        if(arr.length===n){value+=v;return}
        for(const [name,wt] of [["x",chi],...ordinary]){
          if(name==="x"&&arr.length>0&&
             (arr.length<k||w.some((v,i)=>arr[arr.length-k+i]!==v)))continue;
          arr.push(name);dfs(v*wt);arr.pop();
        }
      }
      dfs(1n);actual[n]=value;
      assert(actual[n]===eq[n],"generic word series mismatch "+w.join("")+" at "+n);
    }
    log.push("generic_pattern="+w.join("")+" weighted_series_0_6="+actual.join(",")+" PASS");
  }
  log.unshift("PREFIX466_NATIVE_X6_PATTERN_GATE_EXACT_CERTIFICATE",
    "model=11 signed-axis directions; x=+e1, a=+e2, b=+e3; first x unrestricted",
    "gate=all later x require immediately previous two letters a,b",
    "weights=x:1, a:6,b:12,c:18,d:24,e:36, all negatives:1",
    "count_F=(1+z)/(1-10z-z^3); mass_F=(1+z)/(1-101z-72z^3)",
    "same_base_witness=abc,bca,cab; q=0,1,2; base_weight=1296",
    "=== exact full X6 dynamic hist ===",...results);
  log.push("ALL_CHECKS_PASS");
  return log.join("\n")+"\n";
}
const certificateOutput=main();
if(typeof console!=="undefined")console.log(certificateOutput);
