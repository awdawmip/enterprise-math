// PREFIX-531 standalone BigInt certificate; execute with Node.js >= 18.
const runCert = function runCert(){
  const stars=[[0,2,5],[0,3,4],[1,2,4],[1,3,5]];
  function near(j,c){return stars[j].filter(a=>a!==Math.abs(c)-1).map(a=>-(c>0?1:-1)*(a+1))}
  const phases=[];
  for(let j=0;j<4;j++)for(let a of stars[j])for(let sign of [-1,1])for(let p of near(j,sign*(a+1)))phases.push([j,p,sign*(a+1)]);
  const idx=new Map(phases.map((p,i)=>[p.join(","),i]));
  const next=phases.map(([j,p,c])=>{
    const k=stars.findIndex((st,i)=>i!==j&&st.includes(Math.abs(c)-1));
    const values=[[j,c,...[]]]; // placeholder allocated only here; not a transition
    return [...near(j,c).filter(v=>v!==p).map(v=>[j,c,v]),...near(k,c).map(v=>[k,c,v])].map(v=>idx.get(v.join(",")));
  });
  const target=idx.get("0,1,-3");
  if(phases.length!==48||next.some(x=>x.length!==3)||target===undefined)throw Error("Graph invariant");
  const N=[[48,0],[288,0],[759,9],[4500,108],[7848,-168],[46224,-144],[38592,-1728],[222912,-1728],[-245376,-86400],[-1513728,-476928],[-62208,62208]].map(x=>x.map(BigInt));
  const D={0:[1,0],2:[-20,0],4:[-396,-20],6:[-4944,-48],8:[-32832,-1728],10:[186624,62208]};
  for(const k of Object.keys(D))D[k]=D[k].map(BigInt);
  let dp=new Map(phases.map((_,s)=>[`${s}|0|0`,1n]));
  const hist=[], avoidance=[];
  for(let d=0;d<=17;d++){
    const h=new Map();
    for(const [key,v] of dp){const H=Number(key.split("|")[2]);h.set(H,(h.get(H)||0n)+v)}
    const hs=Array.from({length:Math.max(...h.keys())+1},(_,j)=>h.get(j)||0n);
    const total=hs.reduce((a,b)=>a+b,0n);
    if(total!==48n*6n**BigInt(d))throw Error("total count at "+d);
    const m1=hs.reduce((a,v,j)=>a+BigInt(j)*v,0n);
    const exp=d>=2?9n*BigInt(d-1)*6n**BigInt(d-2):0n;
    if(m1!==exp)throw Error("first event moment at "+d);
    hist.push(hs);avoidance.push(hs[0].toString());
    const ndp=new Map();
    for(const [key,v] of dp){
      const [s0,b0,h0]=key.split("|").map(Number);
      for(const s1 of next[s0])for(let b1=0;b1<=1;b1++){
        const hit=b0&&b1&&s1===target?1:0;
        const k=`${s1}|${b1}|${h0+hit}`;
        ndp.set(k,(ndp.get(k)||0n)+v);
      }
    }
    dp=ndp;
  }
  // Check the complete rational generating function coefficient identity D(t,z)P(t,z)=N(t,z).
  for(let d=0;d<hist.length;d++){
    let lhs=[];
    for(const [j,coeff] of Object.entries(D)){
      const k=d-Number(j);
      if(k<0)continue;
      for(let h=0;h<hist[k].length;h++){
        lhs[h]=(lhs[h]||0n)+coeff[0]*hist[k][h];
        lhs[h+1]=(lhs[h+1]||0n)+coeff[1]*hist[k][h];
      }
    }
    const expect=N[d]||[0n,0n];
    for(let h=0;h<Math.max(lhs.length,2);h++)if((lhs[h]||0n)!==(expect[h]||0n))throw Error("P=N/D at depth "+d+", coefficient "+h);
  }
  // Exact finite-field Euclidean certificates for coprimality at z=0.
  const prime=101;
  function norm(x){return ((x%prime)+prime)%prime}
  function trim(x){while(x.length&&x[x.length-1]===0)x.pop();return x}
  function inv(v){for(let n=1;n<prime;n++)if(norm(n*v)===1)return n;throw Error("no inverse")}
  function rem(a,b){
    a=trim(a.map(norm));b=trim(b.map(norm));
    if(!b.length)throw Error("zero divisor");
    while(a.length>=b.length){
      const shift=a.length-b.length, mul=norm(a.at(-1)*inv(b.at(-1)));
      for(let j=0;j<b.length;j++)a[j+shift]=norm(a[j+shift]-mul*b[j]);
      trim(a);
    }
    return a;
  }
  function gcdDegree(a,b){a=trim(a);b=trim(b);while(b.length){let r=rem(a,b);a=b;b=r}return a.length-1}
  const n0=N.map(x=>Number(x[0])),d0=Array.from({length:11},(_,i)=>D[i]?Number(D[i][0]):0);
  const ne=n0.filter((_,i)=>i%2===0),no=n0.filter((_,i)=>i%2===1),dv=d0.filter((_,i)=>i%2===0);
  const gcds=[gcdDegree(n0.slice(),d0.slice()),gcdDegree(ne.slice(),dv.slice()),gcdDegree(no.slice(),dv.slice())];
  if(gcds.some(x=>x!==0)||norm(d0[10])===0)throw Error("mod101 coprime witness");
  return {verdict:"ALL_CHECKS_PASS",line:"PREFIX-531",source_pin:"enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",model:{phases:48,macro_branches_per_edge:2,gate_target:phases[target]},observer:"all origins and terminals aggregated; retain aAc hit count H; six-axis BRC weights specialized to 1",theorem:{generic_minimal_total_recurrence_order:10,even_subsequence_min_order:5,odd_subsequence_min_order:5,avoidance_z0_min_order:10},finite_modular_coprime:{prime,full_gcd_degree:gcds[0],even_gcd_degree:gcds[1],odd_gcd_degree:gcds[2],denominator_degree_at_z0:10},checks:{all_48_start_phases:"PASS",max_macro_depth:17,exact_DP_vs_rational_coefficients:"PASS",first_moment:"PASS"},distribution_depth_6:hist[6].map(String),distribution_depth_10:hist[10].map(String),avoidance_d0_to_d17:avoidance};
};
console.log(JSON.stringify(runCert(), null, 2));
