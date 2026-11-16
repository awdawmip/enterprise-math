// R206: exact finite checks of the depth-one source/event affine observer.
// Standard Node.js, no dependencies; digit codes use only resets/identities.
const assert = (c, message) => { if (!c) throw Error(message); };
const states = k => {
  const out = [[]];
  const visit = (s, unused) => {
    for (const x of unused) {
      const next = [...s, x]; out.push(next);
      visit(next, unused.filter(y => y !== x));
    }
  };
  visit([], Array.from({length:k}, (_, i) => i));
  return out;
};
const pairs = k => {
  const f = Array.from({length:k}, (_,i) => [i]);
  for (let i=0;i<k;i++) for(let j=i+1;j<k;j++) f.push([i,j]);
  return f;
};
const dimension = (q,n) => { let r=0,v=1;while(v<n){v*=q;r++}return r;};
const digits = (v,q,r) => Array.from({length:r},()=> {const z=v%q;v=Math.floor(v/q);return z;});
const orderProduct = (s,t) => [...s.filter(x=>!t.includes(x)),...t];
const srcOrbit = (s,f) => f.map(a=> {
  const encountered=s.filter(x=>a.includes(x));
  if (!encountered.length) return 1;
  if (a.length===1) return 0;
  return encountered.at(-1)===a[0]?0:1;
});
const tailCode = (tail,m,q,r) => digits((tail.selected?m:0)+tail.direction,q,r);
const orbit = (state,features,m,q,r) => [...srcOrbit(state.s,features),...(state.tail?tailCode(state.tail,m,q,r):digits(m,q,r))];
const srcDescriptor = (s,f) => f.map(a=> {
  const v=s.filter(x=>a.includes(x));
  if (!v.length) return 'I';
  if (a.length===1) return '0';
  return v.at(-1)===a[0]?'0':'1';
});
const descriptor = (state, features,m,q,r) => [...srcDescriptor(state.s,features), ...Array.from({length:r},(_,i)=>state.tail?String(tailCode(state.tail,m,q,r)[i]):'I')];
const composeDesc = (a,b) => a.map((x,i) => b[i]==='I'?x:b[i]);
const concatState = (a,b) => ({s:orderProduct(a.s,b.s),tail:b.tail||a.tail});
const key = st => st.s.join(',')+'|'+(st.tail?(st.tail.selected?'S':'N')+st.tail.direction:'empty');
const enumerate = (k,m) => {
  const out=[{s:[],tail:null}];
  for(const s of states(k)){
    for(let dir=0;dir<m;dir++) out.push({s,tail:{selected:false,direction:dir}});
    if(s.length) for(let dir=0;dir<m;dir++) out.push({s,tail:{selected:true,direction:dir}});
  }
  return out;
};
const N = k => states(k).length;
function verify(q,m,k,large=false){
  const f=pairs(k), r=dimension(q,2*m), all=enumerate(k,m), seen=new Set();
  assert(all.length===m+1+(N(k)-1)*2*m,'count formula');
  for(const st of all){ const o=orbit(st,f,m,q,r).join(',');assert(!seen.has(o),'orbit collision: '+key(st));seen.add(o);}
  const checked=new Set(all.map(key));
  let transitions=0, compositions=0;
  const step=(v,d,label)=>{
    const s=v.slice(0,f.length),t=digits((label===null?0:m)+d,q,r);
    if(label!==null){for(let i=0;i<f.length;i++)if(f[i].includes(label))s[i]=f[i].length===1||label===f[i][0]?0:1;}
    return [...s,...t];
  };
  const selected=large?all.filter((_,i)=>i%29===0||i<50):all;
  for(const st of selected)for(let d=0;d<m;d++)for(let label=-1;label<k;label++){
    const src=label===-1?null:label, s2=src===null?st.s:orderProduct(st.s,[src]);
    const after={s:s2,tail:{selected:src!==null,direction:d}};
    assert(checked.has(key(after)),'closure');
    assert(step(orbit(st,f,m,q,r),d,src).join(',')===orbit(after,f,m,q,r).join(','),'step mismatch');
    transitions++;
  }
  const cands=large?all.filter((_,i)=>i%997===0||i<20):all;
  for(const u of cands)for(const v of cands){
    const lhs=descriptor(concatState(u,v),f,m,q,r);
    const rhs=composeDesc(descriptor(u,f,m,q,r),descriptor(v,f,m,q,r));
    assert(lhs.join(',')===rhs.join(','),'factorisation/composition mismatch');compositions++;
  }
  return {q,m,k,states:all.length,dimension:f.length+r,tail_digits:r,transitions,compositions};
}
const stirling=(n,r)=>{
  const table=Array.from({length:n+1},()=>Array(n+1).fill(0n));table[0][0]=1n;
  for(let i=1;i<=n;i++)for(let j=1;j<=i;j++)
    table[i][j]=table[i-1][j-1]+BigInt(j)*table[i-1][j];
  return table[n][r];
};
const fibreCount=(k,L)=>{
  let c=0n;for(let j=0;j<=Math.min(k,L);j++)c+=stirling(L+1,j+1);
  return c;
};
const countFibreBrute=(k,L)=>{
  const prefix=Array.from({length:k},(_,i)=>i), alphabet=[-1,...prefix];
  let n=0;
  const recur=(depth,s)=>{
    if(depth===L){if(s.join(',')===prefix.join(','))n++;return;}
    for(const a of alphabet){const nxt=a===-1?s:orderProduct(s,[a]);recur(depth+1,nxt);}
  };
  recur(0,prefix);return n;
};
let fibre_model_checks=0;
for(let k=1;k<=4;k++)for(let L=1;L<=5;L++){
  assert(BigInt(countFibreBrute(k,L))===fibreCount(k,L),'Stirling fibre count mismatch');
  fibre_model_checks++;
}
const ceilLog2BigInt = n => (n<=1n?0:(n-1n).toString(2).length);
const x6fibre=Array.from({length:8},(_,i)=>{
  const L=i+1, C=fibreCount(6,L),total=12n**BigInt(L)*C;
  return {L,source_tail_patterns:C.toString(),paired_tail_fibre:total.toString(),kernel_dimension_lower:ceilLog2BigInt(total),previous_nilpotent_lower:5*L};
});
const results=[];
for(const q of [2,3,4])for(let m=1;m<=3;m++)for(let k=1;k<=3;k++)results.push(verify(q,m,k));
results.push(verify(2,12,6,true));
const total=(name)=>results.reduce((s,x)=>s+x[name],0);
const output={status:'PASS',models:results.length,small_models:27,fibre_model_checks,x6fibre,full_state_orbit_checks:total('states'),event_transition_checks:total('transitions'),pair_composition_checks:total('compositions'),native_12_directions_6_sources:results.at(-1),scope:'Every state checked for orbit injectivity in each model; all events and ordered pairs in small models; deterministic subsets of events/pairs at k=6,m=12; arithmetic consists of exact integer digits, 0/1 feature resets and equality, valid over any field with q elements.',models_detail:results};
console.log(JSON.stringify(output,null,2));
