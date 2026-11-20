#!/usr/bin/env node
'use strict';
// Stage432-B: exact directed-Euler / indexwise-K / future-quotient transfer.
// The twelve letters A..L denote (+E1,-E1,...,+E6,-E6). All counts are BigInt.
const assert = require('node:assert/strict');
const D = 'ABCDEFGHIJKL'.split('');
function vec(w){const z=[0,0,0,0,0,0];for(const x of w){const j=D.indexOf(x);assert(j>=0);z[Math.floor(j/2)]+=j%2?-1:1;}return z;}
function edges(w){const c=new Map();for(let i=1;i<w.length;i++){const k=w[i-1]+w[i];c.set(k,(c.get(k)||0)+1);}return [...c].sort((a,b)=>a[0].localeCompare(b[0])).map(([ab,n])=>[ab[0],ab[1],n]);}
function edgeMap(E){return new Map(E.map(([a,b,c])=>[a+b,c]));}
function inc(map,key,n){map.set(key,(map.get(key)||0n)+n);}
function canon(map){return [...map].map(([k,v])=>[k,v.toString()]).sort((a,b)=>a[0].localeCompare(b[0]));}
function capture(Qs,Ps,i,Pchar,Qchar,n,p,r){
  if(i>=n-p && i<=n && Qchar!==null) Qs+=Qchar;
  if(i>=n-p+1 && i<=n+r) Ps+=Pchar;
  return [Qs,Ps];
}
function transfer({JP,JQ,endpointP,endpointQ,n,p,r,targetK}){
  assert(Number.isInteger(n)&&Number.isInteger(p)&&Number.isInteger(r));
  assert(p>=0&&r>=1&&n>=p+1);
  const m=1+JP.reduce((s,e)=>s+e[2],0), nq=1+JQ.reduce((s,e)=>s+e[2],0);
  assert.equal(nq,n);assert(m>=n+r);assert(targetK>=0&&targetK<=n);
  const eP=edgeMap(JP),eQ=edgeMap(JQ);
  const expected=(E)=>E.reduce((z,[a,b,count])=>{let j=D.indexOf(b);assert(D.includes(a)&&j>=0&&count>0&&Number.isInteger(count));z[Math.floor(j/2)]+=count*(j%2?-1:1);return z;},[0,0,0,0,0,0]);
  function initial(E,endpoint){const sum=expected(E), rem=endpoint.map((v,i)=>v-sum[i]);const first=D.filter(d=>JSON.stringify(vec(d))===JSON.stringify(rem));assert(first.length<=1);return first[0]||null;}
  const fp=initial(JP,endpointP),fq=initial(JQ,endpointQ);
  const stat={memoStates:0,transitions:0,terminalStates:0,arithmeticAdditions:0,maxMemoGroupEntries:0,maxCountBits:0};
  if(!fp||!fq)return {groups:new Map(),stats:stat,firstP:fp,firstQ:fq,m,n};
  const keyOf=(EP,EQ,lastP,lastQ,k,qs,ps)=>[...EP,...EQ,lastP,lastQ,k,qs,ps].join('|');
  const cp=JP.map(x=>x[2]),cq=JQ.map(x=>x[2]);
  const memo=new Map();
  let baseQ='',baseP='';[baseQ,baseP]=capture(baseQ,baseP,1,fp,fq,n,p,r);
  function walk(EP,EQ,lastP,lastQ,pos,k,qs,ps){
    const key=keyOf(EP,EQ,lastP,lastQ,k,qs,ps);
    if(memo.has(key))return memo.get(key);
    const out=new Map(), doneP=EP.every(v=>v===0),doneQ=EQ.every(v=>v===0);
    if(doneP&&doneQ){
      stat.terminalStates++;
      assert.equal(pos,m);
      assert.equal(qs.length,p+1);assert.equal(ps.length,p+r);
      if(k===targetK)out.set(qs+'|'+ps,1n);
    }else{
      assert(pos<m);
      for(let i=0;i<JP.length;i++)if(EP[i]&&JP[i][0]===lastP){
        const newP=JP[i][1],np=EP.slice();np[i]--;
        if(doneQ){
          const [qs2,ps2]=capture(qs,ps,pos+1,newP,null,n,p,r);
          stat.transitions++;
          for(const [t,v] of walk(np,EQ,newP,lastQ,pos+1,k,qs2,ps2)){inc(out,t,v);stat.arithmeticAdditions++;}
        }else{
          for(let j=0;j<JQ.length;j++)if(EQ[j]&&JQ[j][0]===lastQ){
            const newQ=JQ[j][1],k2=k+(newP===newQ?1:0);
            if(k2>targetK||k2+(n-pos)<targetK)continue;
            const nq=EQ.slice();nq[j]--;
            const [qs2,ps2]=capture(qs,ps,pos+1,newP,newQ,n,p,r);
            stat.transitions++;
            for(const [t,v] of walk(np,nq,newP,newQ,pos+1,k2,qs2,ps2)){inc(out,t,v);stat.arithmeticAdditions++;}
          }
        }
      }
    }
    stat.maxMemoGroupEntries=Math.max(stat.maxMemoGroupEntries,out.size);
    for(const v of out.values())stat.maxCountBits=Math.max(stat.maxCountBits,v.toString(2).length);
    memo.set(key,out);return out;
  }
  const groups=walk(cp,cq,fp,fq,1,fp===fq?1:0,baseQ,baseP);
  stat.memoStates=memo.size;
  return {groups,stats:stat,firstP:fp,firstQ:fq,m,n};
}
// Independent brute force: generate all words over the active X6 letters, filter by full J and endpoint.
function directWords(E,endpoint){
  const L=1+E.reduce((s,e)=>s+e[2],0);
  const active=[...new Set(E.flatMap(e=>[e[0],e[1]]))].sort();
  const expected=new Map(E.map(([a,b,c])=>[a+b,c]));
  const words=[];
  function rec(w){
    if(w.length===L){if(JSON.stringify(vec(w))!==JSON.stringify(endpoint))return;
      const seen=new Map(edges(w).map(([a,b,c])=>[a+b,c]));
      if(seen.size!==expected.size)return;
      for(const [k,v] of seen)if(expected.get(k)!==v)return;
      words.push(w);return;
    }
    for(const x of active)rec(w+x);
  }
  for(const x of active)rec(x);return words;
}
function direct({JP,JQ,endpointP,endpointQ,n,p,r,targetK}){
  const P=directWords(JP,endpointP),Q=directWords(JQ,endpointQ),groups=new Map();
  for(const a of P)for(const b of Q){let k=0;for(let i=0;i<n;i++)k+=(a[i]===b[i]);
    if(k===targetK)inc(groups,b.slice(n-p-1,n)+'|'+a.slice(n-p,n+r),1n);
  }
  return {groups,originalPairs:P.length*Q.length,P:P.length,Q:Q.length};
}
function makeCase(P,Q,p,r,k=null){const n=Q.length,m=P.length;assert(n>=p+1&&m>=n+r);if(k===null){k=0;for(let i=0;i<n;i++)k+=P[i]===Q[i];}
  return {JP:edges(P),JQ:edges(Q),endpointP:vec(P),endpointQ:vec(Q),n,p,r,targetK:k};}
function verify(){
  const templates=[
    ['AABACAA','AABAA',1,2],['ABACABA','ABABA',2,2],['AABABAAA','ABABA',2,3],
    ['AACABA','ABAA',1,2],['AABAA','ABA',0,1],['AABACAA','ABAA',3,2],
    ['ACADACA','ACACA',2,2],['KKLKKKA','KLK',1,2],['AABACAA','ABABA',1,2],
    ['ABACABA','AABAA',1,2],['ABACABA','ABABA',0,1],['AABABAAA','AABAA',1,3]
  ];
  const rows=[];let totalStates=0,totalTransitions=0,totalPairs=0,totalGroups=0,totalAdditions=0,maxBits=0,maxEntries=0,maxInputBits=0,maxOutputBits=0;
  const bw=x=>Math.max(1,Math.ceil(Math.log2(x+1)));
  const inputBits=c=>{const m=1+c.JP.reduce((z,e)=>z+e[2],0),n=c.n;
    return 16 + c.JP.length*(8+bw(m))+c.JQ.length*(8+bw(n)) +
      6*(1+bw(m))+6*(1+bw(n))+2*bw(m)+3*bw(n);};
  for(const [P,Q,p,r] of templates){for(let k=0;k<=Q.length;k++){
    const c=makeCase(P,Q,p,r,k),t=transfer(c),d=direct(c);
    assert.deepEqual(canon(t.groups),canon(d.groups));
    const inBits=inputBits(c),outBits=t.groups.size*(4*(2*p+r+1)+bw(d.originalPairs))+bw(t.groups.size);
    rows.push({template:P+'/'+Q,p,r,k,pairs:d.originalPairs,groups:t.groups.size,states:t.stats.memoStates,transitions:t.stats.transitions,additions:t.stats.arithmeticAdditions,maxMemoCountBits:t.stats.maxCountBits,inputBits:inBits,outputBits:outBits,counts:canon(t.groups)});
    totalStates+=t.stats.memoStates;totalTransitions+=t.stats.transitions;totalPairs+=d.originalPairs;totalGroups+=t.groups.size;totalAdditions+=t.stats.arithmeticAdditions;maxBits=Math.max(maxBits,t.stats.maxCountBits);maxEntries=Math.max(maxEntries,t.stats.maxMemoGroupEntries);maxInputBits=Math.max(maxInputBits,inBits);maxOutputBits=Math.max(maxOutputBits,outBits);
  }}
  // BRC observer regression: matching count K and full J need not determine the future quotient T.
  const reg=makeCase('AABACAA','AABAA',1,2,4),raw=direct(reg);
  const grouped=[...raw.groups].filter(x=>x[1]>0n);
  assert(grouped.length>=2,'requires at least two distinct T in one full-O fiber');
  // Choose two pairs of original words in one complete-O fiber and extract a distinguishing future.
  const P=directWords(reg.JP,reg.endpointP),Q=directWords(reg.JQ,reg.endpointQ);
  const witness=new Map();for(const a of P)for(const b of Q){let K=0;for(let i=0;i<reg.n;i++)K+=a[i]===b[i];if(K!==reg.targetK)continue;
    const T=b.slice(reg.n-reg.p-1,reg.n)+'|'+a.slice(reg.n-reg.p,reg.n+reg.r);if(!witness.has(T))witness.set(T,{P:a,Q:b});}
  assert(witness.size>=2);
  const selected=[...witness].slice(0,2);
  const pureK={P:'AABACAA',P2:'AACAABA',Q:'AABAA',append:'A'};
  assert.deepEqual(edges(pureK.P),edges(pureK.P2));
  assert.deepEqual(vec(pureK.P),vec(pureK.P2));
  const kk=(p,q)=>[...q].reduce((sum,x,i)=>sum+(p[i]===x),0);
  assert.equal(kk(pureK.P,pureK.Q),4);assert.equal(kk(pureK.P2,pureK.Q),4);
  assert.equal(kk(pureK.P,pureK.Q+'A'),5);assert.equal(kk(pureK.P2,pureK.Q+'A'),4);
  // X6 residual recovers unique first direction from endpoint and directed-edge J.
  function residual(w){const J=edges(w);const tail=[];for(const [a,b,z] of J)for(let i=0;i<z;i++)tail.push(b);
    return vec(w).map((x,j)=>x-vec(tail)[j]);}
  for(const [P,Q] of templates)for(const w of [P,Q])assert.deepEqual(residual(w),vec(w[0]));
  return {marker:'STAGE432B_UNEQUAL_EULER_J_K_T_TRANSFER_PASS',arithmetic:'exact BigInt, 12 native signed X6 directions, no floating approximation',
    source_pins:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
    method:'two-source joint directed-edge dynamic programming; source Q completes first and then P alone; same-type edges have unit weight',
    cases:rows.length,unique_templates:templates.length,independent_original_pairs_checked:totalPairs,dp_states:totalStates,dp_transitions:totalTransitions,exact_bigint_additions:totalAdditions,max_memo_count_bits:maxBits,max_memo_output_map_entries:maxEntries,largest_input_bits:maxInputBits,largest_output_bits:maxOutputBits,total_terminal_groups:totalGroups,
    input_encoding:'specified sparse binary codec: 8-bit edge-record count per source, each edge stores 4+4 bits native direction IDs and ceil(log2(length+1)) count bits, each six-axis endpoint component stores sign plus ceil(log2(length+1)) magnitude bits, plus length/p/r/K fields; no compressed-length claim',
    output_encoding:'one exact count per attained T: 4*(2p+r+1) key bits and ceil(log2(original_pair_count+1)) count bits plus a group-count field',
    regression:{observer:'one full endpoint/J/K fiber',p:reg.p,r:reg.r,distinct_T:grouped.length,sample:selected.map(([T,w])=>({T,...w})),group_sizes:canon(raw.groups),pure_K_witness:{...pureK,current_K:4,append_A_future_K:[5,4],current_J_and_endpoint_equal:true}},
    samples:rows.filter(x=>x.k===4&&x.p===1&&x.r===2).slice(0,3),
    bounded_verification:'each specified template all K=0..n; direct full-word enumeration separate from DP',
    mathematical_status:'AUTHOR_EXECUTED_FINITE_EXACT; general bijection proof in PROOF_STAGE432B; prior Stage431 quotient still unreviewed'};
}
if(require.main===module)console.log(JSON.stringify(verify(),null,2));
module.exports={transfer,direct,directWords,makeCase,verify};
