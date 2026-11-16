// R210 exact independent checker; run: node R210_reachable_action_descriptor_check.mjs
// The function source is the same algorithm actually executed in this author run.
const output = (function R210_test() {
 const assert=(v,msg)=>{if(!v)throw Error(msg)};
 const eq=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
 const bitWidth=a=>Math.ceil(Math.log2(a+1));
 const falling=(k,r)=>{let z=1n;for(let i=0;i<r;i++)z*=BigInt(k-i);return z};
 const stirling=(n,r)=>{let arr=Array.from({length:n+1},()=>0n);arr[0]=1n;for(let i=1;i<=n;i++){let next=Array.from({length:n+1},()=>0n);for(let j=1;j<=i;j++)next[j]=arr[j-1]+BigInt(j)*arr[j];arr=next}return arr[r]||0n};
 const count=(m,k,L)=>{const a=BigInt(m*(k+1));let z=0n;for(let h=0;h<L;h++)z+=a**BigInt(h);let z2=0n;for(let r=0;r<=k;r++){let c=0n;for(let j=0;j<=Math.min(r,L);j++)c+=stirling(L+1,j+1);z2+=falling(k,r)*c}return z+BigInt(m)**BigInt(L)*z2};
 const state=(word,m,k,L)=>{let s=[];for(const x of word){const p=x%(k+1);if(p>0){s=s.filter(v=>v!==p);s.push(p)}}return {s,t:L?word.slice(-L):[]}};
 const concat=(f,g,L)=>({s:f.s.filter(i=>!g.s.includes(i)).concat(g.s),t:L?f.t.concat(g.t).slice(-L):[]});
 const desc=(f,m,k,L)=>{const b=bitWidth(m*(k+1)),D=k+k*(k-1)/2+L*b;const d=Array.from({length:D},(_,i)=>i);const zero=D,one=D+1;const where=new Map(f.s.map((i,j)=>[i,j]));for(let i=1;i<=k;i++)if(where.has(i))d[i-1]=one;let r=k;for(let i=1;i<=k;i++)for(let j=i+1;j<=k;j++){if(where.has(i)||where.has(j))d[r]=(where.get(i)??-1)>(where.get(j)??-1)?one:zero;r++}const h=f.t.length;const start=k+k*(k-1)/2;for(let slot=0;slot<L;slot++)for(let bit=0;bit<b;bit++){const row=start+slot*b+bit;if(slot<L-h)d[row]=start+(slot+h)*b+bit;else d[row]=((f.t[slot-(L-h)]+1)>>bit)&1?one:zero}return d};
 const then=(A,B)=>{const D=A.length;return B.map(v=>v<D?A[v]:v)};
 let models=0, words=0,states=0,pairs=0,maxN=0;
 for(let m=1;m<=3;m++)for(let k=0;k<=2;k++)for(let L=0;L<=3;L++){
  const a=m*(k+1), maxlen=k+L;
  if(a**maxlen>110000)continue;
  const bag=new Map();
  function visit(w){
   const f=state(w,m,k,L),id=JSON.stringify(f),d=desc(f,m,k,L);
   const D=k+k*(k-1)/2+L*bitWidth(a);
   let action=Array.from({length:D},(_,i)=>i);
   for(const x of w)action=then(action,desc(state([x],m,k,L),m,k,L));
   assert(eq(d,action),`action descent failed ${m}/${k}/${L} ${w}`);
   const existing=bag.get(id);
   if(existing) assert(eq(existing.d,d),"same-state action mismatch");else bag.set(id,{f,d});
   words++;
   if(w.length<maxlen)for(let x=0;x<a;x++)visit(w.concat([x]));
  }
  visit([]);
  const n=count(m,k,L);
  assert(BigInt(bag.size)===n,`state count mismatch ${m}/${k}/${L}: ${bag.size} != ${n}`);
  const acts=new Set([...bag.values()].map(z=>JSON.stringify(z.d)));
  assert(acts.size===bag.size,`action not faithful ${m}/${k}/${L}`);
  const items=[...bag.values()];
  for(let z=0;z<Math.min(160,items.length*items.length);z++){
   const f=items[(z*37+11)%items.length],g=items[(z*79+3)%items.length];
   const h=concat(f.f,g.f,L);
   assert(eq(desc(h,m,k,L),then(f.d,g.d)),`state product failed ${m}/${k}/${L}`);
   pairs++;
  }
  models++;states+=items.length;maxN=Math.max(maxN,items.length)
 }
 const xN=count(12,6,2);assert(xN===1407685n,"X6 count");
 const xBits=(xN-1n).toString(2).length;assert(xBits===21,"X6 bits");
 let xActions=0;let seed=8576137;
 const rand=n=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%n};
 for(let t=0;t<800;t++){
  const w=Array.from({length:rand(25)},()=>rand(84)),f=state(w,12,6,2);
  let A=Array.from({length:35},(_,i)=>i);
  for(const x of w)A=then(A,desc(state([x],12,6,2),12,6,2));
  assert(eq(A,desc(f,12,6,2)),"X6 descent failed");xActions++;
 }
 return {status:"PASS",model_count:models,exhaustive_history_checks:words,reachable_states_checked:states,semigroup_pairs_checked:pairs,max_model_states:maxN,x6_random_history_checks:xActions,x6_observer_action_count:xN.toString(),x6_action_min_fixed_bits:xBits,x6_d35_uniform_row_descriptor_upper_bits:210,check_scope:"independent exact integer/selector tests, not installed native package",frozen_science_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34"};
})();
console.log(JSON.stringify(output, null, 2));
