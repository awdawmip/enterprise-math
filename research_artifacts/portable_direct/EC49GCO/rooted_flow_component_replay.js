function replay(){
  const stats={seed:20261128,models:350,originalSubsets:0,states:0,minorStates:0,rejectedMinor:0,flowCalls:0,augmentations:0,rootCutChecks:0,blockedClasses:0,persistentCutChecks:0,exchangeChecks:0,rankChecks:0,partitionChecks:0,productChecks:0,large:[]};
  let seed=stats.seed;
  const rnd=n=>{seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return(seed>>>0)%n};
  const check=(v,msg)=>{if(!v)throw Error(msg)};
  const sum=x=>x.reduce((s,v)=>s+v,0);
  const subset=(a,b)=>a.every(p=>b[p]);
  const ports=(mask,n)=>Array.from({length:n},(_,p)=>p).filter(p=>mask>>>p&1);
  function rooted(c,E,v,i){
    // source -> class nodes (multiplicity), class -> incident ports (INF),
    // source -> forced ports (INF), port -> sink (capacity).
    const k=E.length,n=c.length,s=k+n,t=s+1,g=Array.from({length:t+1},()=>[]);
    const INF=sum(c)+sum(v)+1;
    check(Number.isSafeInteger(INF),"integer capacity overflow");
    function edge(a,b,w){const x={to:b,rev:g[b].length,w},y={to:a,rev:g[a].length,w:0};g[a].push(x);g[b].push(y)}
    for(let j=0;j<k;j++)if(v[j]){edge(s,j,v[j]);for(let p of E[j])edge(j,k+p,INF)}
    for(let p=0;p<n;p++)edge(k+p,t,c[p]);
    for(let p of E[i])edge(s,k+p,INF);
    let flow=0,steps=0,seen;
    while(true){
      let prev=Array(t+1).fill(-1),idx=Array(t+1).fill(-1),q=[s];prev[s]=s;
      for(let a=0;a<q.length&&prev[t]<0;a++){let u=q[a];for(let j=0;j<g[u].length;j++){let e=g[u][j];if(e.w>0&&prev[e.to]<0){prev[e.to]=u;idx[e.to]=j;q.push(e.to)}}}
      if(prev[t]<0){seen=prev.map(x=>x>=0);break}
      let d=INF;for(let u=t;u!==s;u=prev[u])d=Math.min(d,g[prev[u]][idx[u]].w);
      for(let u=t;u!==s;u=prev[u]){let e=g[prev[u]][idx[u]];e.w-=d;g[u][e.rev].w+=d}
      flow+=d;steps++;
    }
    stats.flowCalls++;stats.augmentations+=steps;
    let U=c.map((_,p)=>seen[k+p]),slack=flow-sum(v);
    check(subset(E[i],U),"root missing");
    check(sum(c.filter((_,p)=>U[p]))-sum(v.filter((_,j)=>subset(E[j],U)))===slack,"flow/cut identity");
    return {U,slack};
  }
  function basisComponents(c,E,S,m,oracle=null){
    const k=E.length,B=m.map(()=>0),v=S.slice(),cuts=[],parent=m.map((_,i)=>i);
    const find=i=>{while(parent[i]!==i)i=parent[i];return i};
    const join=(i,j)=>{i=find(i);j=find(j);if(i!==j)parent[j]=i};
    for(let i=0;i<k;i++)if(m[i]){
      const {U,slack}=rooted(c,E,v,i);
      if(oracle)oracle(v,i,U,slack,"initial");
      check(slack>=1,"infeasible prefix");
      let a=Math.min(m[i],slack-1);B[i]=a;v[i]+=a;
      if(a<m[i]){
        stats.blockedClasses++;
        cuts.push({i,U,at:v.slice()});
        // No later basis label can lie inside this already tight U.
        for(let j=0;j<k;j++)if(B[j]&&subset(E[j],U))join(i,j);
      }
    }
    for(let {i,U,at} of cuts){
      check(v.every((x,j)=>!subset(E[j],U)||x===at[j]),"later insertion in tight cut");
      if(oracle)oracle(v,i,U,1,"persistent");
    }
    let group=new Map();
    for(let i=0;i<k;i++)if(m[i]){let p=find(i);if(!group.has(p))group.set(p,[]);group.get(p).push(i)}
    return {B,cuts,groups:[...group.values()]};
  }
  // Same 350 synthetic inputs as pinned GCN; generate all before sampling minors.
  const models=[];
  for(let it=0;it<350;it++){
    let n=2+rnd(6),m=5+rnd(8),c=Array.from({length:n},()=>1+rnd(4)),N=1<<n,M=1<<m,A=[];
    for(let j=0;j<m;j++){let aux=rnd(3)===0;A.push({e:aux?1<<rnd(n):1+rnd(N-1),p:aux?0:1+rnd(15),s:aux?1+rnd(9):0})}
    for(let x of A)if(x.s)c[Math.log2(x.e)]++;
    models.push({n,m,c,N,M,A});
  }
  for(let {n,m,c,N,M,A} of models){
    const pop=new Uint8Array(M),cap=new Int16Array(N),L=new Int32Array(N);
    for(let z=1;z<M;z++)pop[z]=pop[z>>1]+(z&1);
    for(let u=1;u<N;u++){cap[u]=sum(ports(u,n).map(p=>c[p]));for(let j=0;j<m;j++)if((A[j].e&u)===A[j].e)L[u]|=1<<j}
    const ok=new Uint8Array(M);
    for(let z=0;z<M;z++){ok[z]=1;for(let u=1;u<N;u++)if(pop[z&L[u]]>=cap[u]){ok[z]=0;break}stats.originalSubsets++}
    let groups=new Map();for(let j=0;j<m;j++)groups.set(A[j].e,(groups.get(A[j].e)||0)|(1<<j));
    const masks=[...groups.keys()],H=[...groups.values()],E=masks.map(x=>ports(x,n)),vec=z=>H.map(h=>pop[h&z]);
    const groupMask=js=>js.reduce((z,j)=>z|H[j],0);
    function verify(R,F){
      stats.states++;const S=vec(R),mm=vec(F),before=stats.flowCalls;
      function oracle(v,i,U,slack,kind){
        let min=Infinity,inter=N-1;
        for(let u=1;u<N;u++)if((u&masks[i])===masks[i]){
          let z=cap[u]-sum(v.filter((_,j)=>(masks[j]&u)===masks[j]));
          if(z<min){min=z;inter=u}else if(z===min)inter&=u;
        }
        let got=U.reduce((z,b,p)=>z|(b?1<<p:0),0);
        check(min===slack&&inter===got,"rooted minimum/intersection");
        if(kind==="initial")stats.rootCutChecks++;else stats.persistentCutChecks++;
      }
      const result=basisComponents(c,E,S,mm,oracle),{B,cuts}=result;
      check(stats.flowCalls-before===mm.filter(x=>x>0).length,"one flow per active class");
      let Z=0;for(let j=0;j<H.length;j++){let h=F&H[j];for(let a=0;a<B[j];a++){let b=h&-h;check(b!==0,"lift");Z|=b;h^=b}}
      check(ok[R|Z],"basis infeasible");
      let maxRank=0,part=mm.map((_,i)=>1<<i);
      let gs=result.groups.map(js=>groupMask(js));
      for(let x=F;;x=(x-1)&F){
        let f=!!ok[R|x];if(f)maxRank=Math.max(maxRank,pop[x]);
        check(gs.every(h=>!!ok[R|(x&h)])===f,"product language");stats.productChecks++;
        if(x&&!f){
          let cir=true;for(let b=x;b;b&=b-1)if(!ok[R|(x^(b&-b))]){cir=false;break}
          if(cir){let J=vec(x).reduce((z,a,i)=>z|(a?1<<i:0),0),u=J;for(let i=0;i<mm.length;i++)if(J>>>i&1)u|=part[i];for(let i=0;i<mm.length;i++)if(u>>>i&1)part[i]=u}
        }
        if(!x)break;
      }
      check(sum(B)===maxRank,"basis rank");stats.rankChecks++;
      let expected=[...new Set(part.filter((_,i)=>mm[i]))].sort((a,b)=>a-b);
      let actual=result.groups.map(js=>js.reduce((z,j)=>z|1<<j,0)).sort((a,b)=>a-b);
      check(JSON.stringify(expected)===JSON.stringify(actual),"component partition");stats.partitionChecks++;
      for(let {i,U} of cuts){
        let h=H[i]&F&~Z,x=h&-h;check(x!==0,"nonbasis witness");
        check(!ok[R|Z|x],"nonbasis should block");
        for(let j=0;j<H.length;j++)for(let y=Z&H[j];y;y&=y-1){
          check(!!ok[R|(Z^(y&-y))|x]===subset(E[j],U),"exchange witness");stats.exchangeChecks++;
        }
      }
    }
    verify(0,M-1);
    for(let tr=0;tr<8;tr++){
      let P=rnd(M),F=(M-1)^P,R=rnd(M)&P;
      // Consume same random third draw as GCN and condition on both legal.
      let R2=rnd(M)&P;if(!ok[R]||!ok[R2]){stats.rejectedMinor++;continue}
      stats.minorStates++;verify(R,F);
    }
  }
  for(let d of [10,30,60,100]){
    const c=Array(d).fill(1),E=[];
    for(let i=0;i<d;i++)E.push(c.map((_,p)=>p).filter(p=>p!==i));
    for(let i=0;i<d;i++)E.push(c.map((_,p)=>p).filter(p=>p!==i&&p!==(i+1)%d));
    const before=stats.flowCalls,aug=stats.augmentations,k=E.length;
    const res=basisComponents(c,E,Array(k).fill(0),Array(k).fill(1));
    check(sum(res.B)===d-1&&res.groups.length===1&&res.groups[0].length===k,"uniform family rank or component");
    check(res.cuts.every(({U})=>U.every(Boolean)),"uniform family minimal tight cut");
    stats.large.push({ports:d,classes:k,rank:sum(res.B),components:res.groups.length,flows:stats.flowCalls-before,augmentations:stats.augmentations-aug,rawNonemptyPortCuts:(2n**BigInt(d)-1n).toString()});
  }
  return stats;
}
console.log(JSON.stringify(replay(),null,2));
