function verify() {
  const ops={c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3]};
  const hist={
    N0:[-2,-2,-1,-1,1,1,-1,2,2,-1],
    N1:[-2,-2,-1,-1,-1,2,2,-1,1,1],
    N2:[-2,-2,-1,-1,-1,1,1,-1,2,2],
    A0:[-2,-2,-1,-1,-1,1,1,2,2,-1],
    A2:[-2,-2,-1,-1,-1,-1,1,1,2,2],
    B0:[-2,-2,-1,-1,-1,2,1,1,-1,2],
    B1:[-2,-2,-1,-1,-1,-1,2,2,1,1],
    AB:[-2,-2,-1,-1,-1,-1,1,2,1,2],
    BA:[-2,-2,-1,-1,-1,-1,2,1,1,2]
  };
  const names=['N0','N1','N2','A0','A2','B0','B1','AB','BA'], buckets=['N','A','B','AB','BA'];
  const assert=(c,m)=>{if(!c) throw Error(m)};
  const steps=w=>[...w].flatMap(c=>ops[c]);
  function classify(seq,st='N',last=0) {
    for(const cur of seq) {
      const a=last===1&&cur===2,b=last===2&&cur===1;
      if(st==='N') st=a?'A':b?'B':st;
      else if(st==='A'&&b) st='AB';
      else if(st==='B'&&a) st='BA';
      last=cur;
    }
    return st;
  }
  function atom(p) {
    const s=classify(p),l=p[p.length-1];
    return s==='N'?(l===1?'N1':l===2?'N2':'N0'):s==='A'?(l===2?'A2':'A0'):s==='B'?(l===1?'B1':'B0'):s;
  }
  for(const name of names) {
    const p=hist[name];
    assert(p.length===10&&atom(p)===name,'invalid historical state '+name);
    assert([1,2,3,4,5,6].every(i=>p.reduce((s,x)=>s+(Math.abs(x)===i?x:0),0)===(i===1?-2:0)),'history endpoint');
    assert(p.filter(x=>x===1).length===2&&p.filter(x=>x===2).length===2,'history counts');
  }
  const sig=w=>{
    const t=steps(w);
    assert([1,2,3,4,5,6].every(i=>t.reduce((s,x)=>s+(Math.abs(x)===i?x:0),0)===(i===1?2:0)),'nonreturn '+w);
    return names.map(n=>classify(t,classify(hist[n]),hist[n].at(-1)));
  };
  const key=s=>s.join('/');
  const cols=s=>buckets.map(b=>s.reduce((m,x,j)=>m|(x===b?1<<j:0),0));
  function rank(M) {
    const mod=1000003, piv={};
    function power(a,n) {let z=1;while(n){if(n%2)z=(z*a)%mod;a=(a*a)%mod;n=Math.floor(n/2)}return z}
    for(const bits of M) {
      let v=names.map((_,j)=>(bits>>j)&1);
      for(const [jstr,row] of Object.entries(piv).sort((a,b)=>+a[0]-+b[0])) {
        const j=+jstr;
        if(v[j]) {const z=v[j];v=v.map((q,i)=>(q-z*row[i]%mod+mod)%mod)}
      }
      const k=v.findIndex(z=>z!==0);
      if(k!==-1) {const r=power(v[k],mod-2);piv[k]=v.map(z=>z*r%mod)}
    }
    return Object.keys(piv).length;
  }
  function det9(M) {
    const a=M.map(r=>r.map(BigInt));let prev=1n,sign=1n;
    for(let k=0;k<8;k++) {
      if(a[k][k]===0n) {let q=k+1;while(q<9&&a[q][k]===0n)q++;if(q===9)return 0;[a[k],a[q]]=[a[q],a[k]];sign=-sign}
      const p=a[k][k];
      for(let i=k+1;i<9;i++){for(let j=k+1;j<9;j++){const z=a[i][j]*p-a[i][k]*a[k][j];assert(z%prev===0n,'noninteger Bareiss');a[i][j]=z/prev}a[i][k]=0n}
      prev=p;
    }
    return Number(sign*a[8][8]);
  }
  const trieCost=ws=>{const prefixes=new Set();for(const w of ws){const q=steps(w);for(let i=1;i<=q.length;i++)prefixes.add(q.slice(0,i).join(','))}return prefixes.size};
  const rows=[];
  for(let h=2;h<=10;h++) {
    const m=h-1, words=[];
    for(let mask=0;mask<2**m;mask++) {
      const s=Array.from({length:m},(_,i)=>mask&(1<<i)?'d':'c').join('');
      for(let i=0;i<h;i++)words.push(s.slice(0,i)+'e'+s.slice(i));
    }
    assert(new Set(words).size===h*2**m,'word duplicate');
    const groups=new Map(),signatures=new Map();
    for(const w of words) {
      const s=sig(w),k=key(s);signatures.set(w,s);
      if(!groups.has(k))groups.set(k,[]);
      groups.get(k).push(w);
      const p=[1,2,3,4,5,6].map(j=>steps(w).filter(t=>t===j).length);
      assert(JSON.stringify(p)===JSON.stringify([h+1,h-1,1,0,0,0]),'positive counts');
    }
    assert(groups.size===(h===2?4:8),'unexpected transfer classes h='+h);
    const reps={C:'e'+'c'.repeat(m),D:'e'+'d'.repeat(m),c:'c'.repeat(m)+'e',d:'d'.repeat(m)+'e'};
    const tags=Object.keys(reps),sigs=Object.fromEntries(tags.map(t=>[t,signatures.get(reps[t])]));
    assert(new Set(tags.map(t=>key(sigs[t]))).size===4,'indispensable classes collapse');
    for(const t of tags) {
      const matching=groups.get(key(sigs[t]));
      assert(matching&&matching.length,'missing type '+t);
      for(const w of matching) {
        if(t==='C'||t==='D') assert(w===reps[t],'incorrect sole C/D word');
        if(t==='c') assert(w[0]==='c'&&[...w].every(c=>c==='c'||c==='e'),'incorrect c word');
        if(t==='d') assert(w[0]==='d'&&[...w].every(c=>c==='d'||c==='e'),'incorrect d word');
      }
    }
    const pairs={C:[4,7],D:[6,8],c:[3,4],d:[5,6]};
    for(const t of tags) {
      const [i,j]=pairs[t];
      for(const w of words)if(key(signatures.get(w))!==key(sigs[t]))assert(signatures.get(w)[i]===signatures.get(w)[j],'left-kernel failure '+h+':'+t+':'+w);
    }
    const choice=[['C','A'],['C','AB'],['C','BA'],['D','B'],['D','AB'],['c','A'],['c','AB'],['d','B'],['d','AB']];
    const masks=choice.map(([t,b])=>cols(sigs[t])[buckets.indexOf(b)]);
    const determinant=det9(names.map((_,i)=>masks.map(mask=>(mask>>i)&1)));
    assert(determinant===-1&&rank(masks)===9,'unimodular rank h='+h);
    const cost=trieCost(tags.map(t=>reps[t]));
    assert(cost===16*h-4,'trie cost mismatch');
    let minCDE=null,numberOptimal=0;
    if(h<=6) {
      const cs=groups.get(key(sigs.c)),ds=groups.get(key(sigs.d));
      minCDE=Infinity;
      for(const cw of cs) for(const dw of ds) {
        const candidate=[reps.C,reps.D,cw,dw];
        const v=trieCost(candidate);
        minCDE=Math.min(minCDE,v);
        if(v===16*h-4)numberOptimal++;
      }
      assert(minCDE===16*h-4,'finite class representative minimum');
    }
    rows.push({h,returning_words:words.length,transfer_classes:groups.size,
      same_positive_counts:[h+1,h-1,1,0,0,0],
      witness:reps,unimodular_minor:determinant,
      primitive_prefix_cost:cost,
      finite_class_representative_minimum:minCDE,
      finite_optimal_representative_pairs:numberOptimal});
  }
  return {status:'EXACT_CHECK_PASS',version:'EC49EE',native_model:'signed X6 ordered primitive paths; first A/B event order including history/future seam',
    history_length:10,history_displacement:[-2,0,0,0,0,0],
    historical_real_path_representatives:hist,rank_field:'Q (0/1 minors bounded by Hadamard 19683 < modular prime 1000003)',
    h1:'only e; five terminal observations, rank5',
    all_h_claim:'T_cde(h)=T_cde_equal(h)=16*h-4 for integer h>=2; analytically proved in README',
    exact_finite_audits:rows};
}
const result=verify();
console.log(JSON.stringify(result,null,2));
