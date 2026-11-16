// PREFIX827 — exact integer Q-only BRC named-state trace regression
// Run: node PREFIX827_R6_NAMED_TRACE_CHECK.js
function runChecks() {
  const fact = n => {let z=1n; for(let i=2;i<=n;i++)z*=BigInt(i); return z};
  const binom = (n,k) => {if(k<0||k>n)return 0n; let z=1n; for(let j=1;j<=k;j++)z=z*BigInt(n-j+1)/BigInt(j);return z};
  const choose=(items,k,start=0,p=[],out=[])=>{if(p.length===k){out.push([...p]);return out}for(let i=start;i<=items.length-(k-p.length);i++){p.push(items[i]);choose(items,k,i+1,p,out);p.pop()}return out};
  const moments = betas=>{const e=Array(betas.length+1).fill(0n);e[0]=1n;let seen=0;for(const x of betas){seen++;for(let d=seen;d>=1;d--)e[d]+=BigInt(x)*e[d-1]}return e};
  const direct = (q,S,m,weights,a,b,T)=>{
    let z=new Map([[`${m}|${S.join(",")}`,1n]]),ans=[];
    for(let t=0;t<=T;t++){
      let hist=Array(q+1).fill(0n);
      for(const [key,mass] of z){const pos=key.indexOf("|");const mark=+key.slice(0,pos);const rest=key.slice(pos+1);const ss=rest?rest.split(",").map(Number):[];hist[mark+ss.length]+=mass}
      ans.push(hist);
      if(t===T)break;
      const next=new Map();
      const add=(key,value)=>next.set(key,(next.get(key)||0n)+value);
      for(const [key,mass] of z){
        const pos=key.indexOf("|");const mark=+key.slice(0,pos);
        const rest=key.slice(pos+1);const ss=rest?rest.split(",").map(Number):[];
        for(let j=0;j<ss.length;j++)add(`${mark}|${ss.filter((_,k)=>k!==j).join(",")}`,mass*BigInt(weights[ss[j]]));
        if(mark) add(`0|${ss.join(",")}`,mass*BigInt(b));
        else if(ss.length<q) add(`1|${ss.join(",")}`,mass*BigInt(a));
      }
      z=next;
    }
    return ans;
  };
  const formula=(q,p,m,e,a,b,t)=>{
    const ans=Array(q+1).fill(0n);
    for(let d=0;d<=Math.min(p,t);d++){
      const s=t-d;
      const inter=(m===0&&p===q)?(t===0&&d===0?1n:d===0?0n:binom(t-1,d-1)):binom(t,d);
      if(inter===0n)continue;
      const A=m===0?Math.ceil(s/2):Math.floor(s/2);
      const B=s-A;
      const endmark=(m+s)%2;
      const l=p-d+endmark;
      if(l<0||l>q)throw Error("Illegal count bin");
      ans[l]+=fact(d)*e[d]*inter*BigInt(a)**BigInt(A)*BigInt(b)**BigInt(B);
    }
    return ans;
  };
  const equal=(x,y)=>x.length===y.length&&x.every((v,i)=>v===y[i]);
  let configurations=0,basisStates=0,histogramComparisons=0,scalarAssertions=0;
  let recoveryAssertions=0,annihilatorAssertions=0,equivalenceCases=0,duplicateProfiles=0;
  const snapshots=[];
  for(let q=1;q<=7;q++){
    const families=q<=6?[
      Array.from({length:q+2},(_,i)=>i+1),
      Array.from({length:q+2},(_,i)=>Math.floor(i/2)+1)
    ]:[Array.from({length:q+2},(_,i)=>i+1)];
    const abpairs=q<=5?[[1,1],[2,3],[0,2],[3,0]]:q===6?[[1,1],[2,3]]:[[2,3]];
    for(const weights of families)for(const [a,b] of abpairs){
      configurations++;
      const bucket=new Map();let caseCount=0;
      for(let p=0;p<=q;p++)for(const S of choose(weights.map((_,i)=>i),p)){
        for(let m=0;m<=1;m++){
          if(p+m>q)continue;
          basisStates++;caseCount++;
          const T=3*q+9;
          const e=moments(S.map(i=>weights[i]));
          const histories=direct(q,S,m,weights,a,b,T);
          for(let t=0;t<=T;t++){
            const out=formula(q,p,m,e,a,b,t);
            if(!equal(histories[t],out))throw Error(`Closed form mismatch q=${q},p=${p},m=${m},t=${t},S=${S}`);
            histogramComparisons++;scalarAssertions+=q+1;
          }
          for(let d=1;d<=p;d++){
            const bin=p-d+m;
            const value=histories[d][bin];
            const rec=value/fact(d)-(m?BigInt(b)*e[d-1]:0n);
            if(value%fact(d)!==0n||rec!==e[d])throw Error(`Profile recovery mismatch q=${q},d=${d},m=${m}`);
            recoveryAssertions++;
          }
          if(a>0&&b>0){
            const order=(m===0&&p===q)?q:p+1;
            const start=(m===0&&p===q)?1:0;
            const lam=BigInt(a*b);
            for(let t=start;t+2*order<=T;t++){
              for(let l=0;l<=q;l++){
                let sum=0n;
                for(let j=0;j<=order;j++){
                  const coeff=binom(order,j)*lam**BigInt(order-j)*( (order-j)%2 ? -1n:1n);
                  sum+=coeff*histories[t+2*j][l];
                }
                if(sum!==0n)throw Error(`Temporal annihilator failure q=${q},p=${p},m=${m},t=${t},bin=${l}`);
                annihilatorAssertions++;
              }
            }
          }
          if(q<=5){
            const sig=[q,p,m,a,b,...e.map(x=>x.toString())].join(":");
            const trace=histories.map(x=>x.map(v=>v.toString()).join(",")).join(";");
            if(bucket.has(sig)){
              duplicateProfiles++;
              if(bucket.get(sig)!==trace)throw Error("Same elementary-symmetric profile yielded different trace");
              equivalenceCases++;
            }else bucket.set(sig,trace);
          }
        }
      }
      if((a===2&&b===3)||q===7)snapshots.push({q,weight_family:weights[0]===weights[1]?"duplicates":"distinct",a,b,states:caseCount});
    }
  }
  const large= formula(5,3,0,moments([2,5,11]),2,3,1000);
  return {
    schema:"PREFIX827_R6_EXACT_NAMED_COUNT_FORMULA_REGRESSION_V1",
    status:"ALL_EXACT_ASSERTIONS_PASSED",
    scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    test_scope:"q=1..7, enumerated legal named initial states with distinct/duplicate positive weights; a,b include (1,1),(2,3),(0,2),(3,0) where indicated; t=0..3q+9",
    configurations,basis_states:basisStates,histogram_comparisons:histogramComparisons,scalar_equalities:scalarAssertions,
    recovery_assertions:recoveryAssertions,annihilator_scalar_assertions:annihilatorAssertions,
    repeated_profile_equalities:equivalenceCases,repeated_profiles:duplicateProfiles,
    high_time_example:{q:5,initial_flag:0,source_weights:[2,5,11],a:2,b:3,t:1000,nonzero_bins:large.map((x,i)=>x===0n?null:i).filter(x=>x!==null),output_bin_decimal_digits:large.map(x=>x.toString().length)},
    selected_configurations:snapshots,
    arithmetic:"Exact JavaScript BigInt, direct source-state branching independent of closed formula",
    claim_limit:"Finite regression tests; all-capacity statements require mathematical argument; positive-count Q-only BRC model not native X6 dynamics"
  };
}
console.log(JSON.stringify(runChecks(),null,2));
