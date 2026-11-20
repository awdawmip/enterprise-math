'use strict';
// Stage498-B: exact deterministic bounded-future BRC quotient.
// Signed-X6 chart: 12 directed steps on six coordinates; all 144 ordered pairs.
const SIGMA='ABCDEFGHIJKL', LETTERS='ABC', MAXLEN=8;
const ACTIONS=['POP','SET_END_MINUS_2_C','INSERT_BEFORE_LAST2_C','DELETE_END_MINUS_1','DELETE_LAST_PUBLIC'];
const idx=Object.fromEntries([...SIGMA].map((x,i)=>[x,i]));
function observe(word) {
  const d=Array(6).fill(0), e=Array(144).fill(0);
  for (const a of word) {const k=idx[a];d[k%6]+=(k<6?1:-1);}
  for (let i=1;i<word.length;i++) e[12*idx[word[i-1]]+idx[word[i]]]++;
  return JSON.stringify([d,e]);
}
function step(state,action) {
  const [w,p]=state, n=w.length;
  if(action==='POP') return n?[w.slice(0,-1),p.slice(0,-1)]:null;
  if(action==='SET_END_MINUS_2_C') {
    if(n<3)return null;const k=n-3;
    return [w.slice(0,k)+'C'+w.slice(k+1),p];
  }
  if(action==='INSERT_BEFORE_LAST2_C') {
    if(n<2||n>=MAXLEN)return null;const k=n-2;
    return [w.slice(0,k)+'C'+w.slice(k),p.slice(0,k)+'P'+p.slice(k)];
  }
  if(action==='DELETE_END_MINUS_1') {
    if(n<2)return null;const k=n-2;
    return [w.slice(0,k)+w.slice(k+1),p.slice(0,k)+p.slice(k+1)];
  }
  if(action==='DELETE_LAST_PUBLIC') {
    const k=p.lastIndexOf('P');return k<0?null:[w.slice(0,k)+w.slice(k+1),p.slice(0,k)+p.slice(k+1)];
  }
  throw Error('unknown action');
}
const memo=new Map(), intern=Array.from({length:5},()=>new Map());
function signature(state,h) {
  const key=JSON.stringify([h,...state]);
  if(memo.has(key)) return memo.get(key);
  const sig=h===0?observe(state[0]):JSON.stringify([signature(state,0),ACTIONS.map(a=>{
    const t=step(state,a);return t===null?null:signature(t,h-1);
  })]);
  const dict=intern[h];if(!dict.has(sig))dict.set(sig,dict.size);
  const id=dict.get(sig);memo.set(key,id);return id;
}
function* words(length,prefix=''){
  if(!length){yield prefix;return;}
  for(const x of LETTERS)yield* words(length-1,prefix+x);
}
function pairEquivalent(a,b,h) { // independently recurse through entire action tree
  if(observe(a[0])!==observe(b[0]))return false;
  if(h===0)return true;
  for(const action of ACTIONS){
    const x=step(a,action),y=step(b,action);
    if((x===null)!==(y===null))return false;
    if(x!==null&&!pairEquivalent(x,y,h-1))return false;
  }
  return true;
}
function witness(a,b,depth){
  const queue=[[a,b,[]]];
  while(queue.length){
    const [x,y,trace]=queue.shift();if(trace.length===depth)continue;
    for(const action of ACTIONS){
      const u=step(x,action),v=step(y,action),t=[...trace,action];
      if((u===null)!==(v===null))return {trace:t,reason:'legality'};
      if(u===null)continue;
      if(observe(u[0])!==observe(v[0]))return {trace:t,reason:'observation',end_words:[u[0],v[0]]};
      queue.push([u,v,t]);
    }
  }
  return null;
}
const table=[];let checkedPairs=0;
for(const n of [4,5,6,7]){
  const grouped=Array.from({length:5},()=>new Map());
  const base=new Map();
  for(const w of words(n)){
    const init=[w,'O'.repeat(n)];
    for(let h=0;h<=4;h++){
      const id=signature(init,h),g=grouped[h];if(!g.has(id))g.set(id,[]);g.get(id).push(w);
    }
    const f=observe(w);if(!base.has(f))base.set(f,[]);base.get(f).push(w);
  }
  if(n<=6){ // direct uninterned recursion checks all same-F pairs, horizons 0,1,2
    for(const fiber of base.values())for(let i=0;i<fiber.length;i++)for(let j=i+1;j<fiber.length;j++){
      for(let h=0;h<=2;h++){
        const p=[fiber[i],'O'.repeat(n)],q=[fiber[j],'O'.repeat(n)];
        if((signature(p,h)===signature(q,h))!==pairEquivalent(p,q,h))throw Error('pair mismatch at n='+n+' h='+h);
        checkedPairs++;
      }
    }
  }
  table.push({length:n,population:3**n,classes:[0,1,2,3,4].map(h=>grouped[h].size),
    non_singleton_classes:[0,1,2,3,4].map(h=>[...grouped[h].values()].filter(ws=>ws.length>1).length),
    non_singleton_population:[0,1,2,3,4].map(h=>[...grouped[h].values()].filter(ws=>ws.length>1).reduce((t,ws)=>t+ws.length,0)),
    largest_initial_F_fiber:Math.max(...[...base.values()].map(ws=>ws.length))});
}
const examples=[['AABA','ABAA',1],['CACCAA','CCACAA',2],['CACCAAA','CCACAAA',3]];
for(const [a,b,h] of examples){
  if(observe(a)!==observe(b))throw Error('bad base fiber');
  if(signature([a,'O'.repeat(a.length)],h-1)!==signature([b,'O'.repeat(b.length)],h-1))throw Error('bad depth lower bound');
  if(signature([a,'O'.repeat(a.length)],h)===signature([b,'O'.repeat(b.length)],h))throw Error('bad depth upper bound');
}
const provenance_a=['A','O'], provenance_b=['A','P'];
if(observe(provenance_a[0])!==observe(provenance_b[0]))throw Error('provenance initial mismatch');
if(step(provenance_a,'DELETE_LAST_PUBLIC')!==null||step(provenance_b,'DELETE_LAST_PUBLIC')===null)throw Error('provenance legality');
const result={schema:'EM_STAGE498B_EXECUTED_V1',kind:'exact_integer_full_fiber_enumeration',date:'2026-11-07',
  signed_directions:12,directed_pairs:144,finite_alphabet:LETTERS,max_word_length:MAXLEN,
  public_actions:ACTIONS,initial_provenance:'O',insert_provenance:'P',
  signature:'S_0=F; S_{h+1}=(F, ordered legal-action S_h successor signatures)',
  table,independent_bfs_pair_horizon_checks:checkedPairs,
  witnesses:examples.map(([a,b,h])=>({a,b,first_distinguishing_horizon:h,detail:witness([a,'O'.repeat(a.length)],[b,'O'.repeat(b.length)],h)})),
  provenance_witness:{initial_word:'A',source_labels:['O','P'],different_legality_of:'DELETE_LAST_PUBLIC'},
  verdict:'ALL_ASSERTIONS_PASSED',test_scope:'All 3^n initial O-labeled words n=4,5,6,7; all five public actions; horizons 0..4; independent exhaustive trace comparison on every same-F pair n<=6, horizons<=2.'};
console.log(JSON.stringify(result,null,2));
