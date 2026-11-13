#!/usr/bin/env node
'use strict';
// Exact offline unequal-length Euler/J/K enumerator plus bounded online alignment-frontier test.
const assert = require('node:assert/strict');
const D = 12;
function endpoint(word) {
  const z = Array(6).fill(0);
  for (const a of word) z[a >> 1] += a % 2 ? -1 : 1;
  return z;
}
function adjacency(word, alphabet = D) {
  const edges = Array(alphabet * alphabet).fill(0);
  for (let i = 1; i < word.length; i++) edges[word[i - 1] * alphabet + word[i]]++;
  return edges;
}
function kdiag(p, q) {
  let k = 0;
  for (let i = 0; i < Math.min(p.length, q.length); i++) k += +(p[i] === q[i]);
  return k;
}
function enumerator(firstP, firstQ, jp, jq, m, n, alphabet = D) {
  const h = Math.min(m, n), bigZero = () => Array(h + 1).fill(0n);
  assert(Number.isSafeInteger(m) && m >= 0 && Number.isSafeInteger(n) && n >= 0);
  assert(Number.isSafeInteger(alphabet) && alphabet >= 1 && alphabet <= D);
  assert(jp.every(x=>Number.isSafeInteger(x)&&x>=0));
  assert(jq.every(x=>Number.isSafeInteger(x)&&x>=0));
  assert.equal(jp.length, alphabet * alphabet);
  assert.equal(jq.length, alphabet * alphabet);
  assert.equal(jp.reduce((a,b)=>a+b,0), Math.max(0,m-1));
  assert.equal(jq.reduce((a,b)=>a+b,0), Math.max(0,n-1));
  assert.equal(m > 0, firstP >= 0);
  assert.equal(n > 0, firstQ >= 0);
  const directEndpoint = (start, J) => {
    const z = Array(6).fill(0);
    if (start >= 0) z[start >> 1] += start % 2 ? -1 : 1;
    for (let a = 0; a < alphabet; a++) for (let b = 0; b < alphabet; b++) {
      z[b >> 1] += J[a * alphabet + b] * (b % 2 ? -1 : 1);
    }
    return z;
  };
  const memo = new Map(), rp = jp.slice(), rq = jq.slice();
  let transitions = 0;
  function solve(i, lp, lq) {
    const id = i+'|'+lp+'|'+lq+'|'+rp.join(',')+'|'+rq.join(',');
    if (memo.has(id)) return memo.get(id);
    const out = bigZero();
    if (i === Math.max(m,n)) {
      if (rp.every(x=>x===0) && rq.every(x=>x===0)) out[0] = 1n;
      memo.set(id, out);
      return out;
    }
    const nextP = i < m ? [...Array(alphabet).keys()].filter(a=>rp[lp*alphabet+a]>0) : [-1];
    const nextQ = i < n ? [...Array(alphabet).keys()].filter(a=>rq[lq*alphabet+a]>0) : [-1];
    for (const a of nextP) for (const b of nextQ) {
      if (a >= 0) rp[lp*alphabet+a]--;
      if (b >= 0) rq[lq*alphabet+b]--;
      transitions++;
      const tail = solve(i+1, a>=0?a:lp, b>=0?b:lq);
      const gain = +(a >= 0 && b >= 0 && a === b);
      for (let x = 0; x + gain <= h; x++) out[x+gain] += tail[x];
      if (a >= 0) rp[lp*alphabet+a]++;
      if (b >= 0) rq[lq*alphabet+b]++;
    }
    memo.set(id, out);
    return out;
  }
  let dist;
  if (m===0 && n===0) dist=[1n];
  else if (Math.max(m,n)===1) {
    dist=bigZero();dist[+(m>0&&n>0&&firstP===firstQ)]=1n;
  } else {
    const tail = solve(1, firstP, firstQ);
    dist=bigZero();const shift=+(m>0&&n>0&&firstP===firstQ);
    for(let i=0;i+shift<=h;i++)dist[i+shift]+=tail[i];
  }
  return {dist, states:memo.size, transitions,
    endpoints:[directEndpoint(firstP,jp),directEndpoint(firstQ,jq)]};
}
function words(alphabet, maxLength) {
  let out=[[]], row=[[]];
  for (let len=1;len<=maxLength;len++) {
    row=row.flatMap(w=>Array.from({length:alphabet},(_,a)=>[...w,a]));
    out.push(...row);
  }
  return out;
}
function signature(word, alphabet) {
  const es=[];
  for(let i=1;i<word.length;i++)es.push(word[i-1]*alphabet+word[i]);
  es.sort((a,b)=>a-b);
  return [word.length,word[0]??-1,es.join('.')].join(':');
}
function testEnumeration(alphabet,maxLength) {
  const ww=words(alphabet,maxLength), groups=new Map();
  for (const p of ww) for (const q of ww) {
    const key=signature(p,alphabet)+'|'+signature(q,alphabet);
    if(!groups.has(key))groups.set(key,{p,q,distribution:new Map()});
    const d=groups.get(key).distribution, k=kdiag(p,q);
    d.set(k,(d.get(k)||0n)+1n);
  }
  let totalStates=0,totalTransitions=0,matched=0;
  for(const {p,q,distribution} of groups.values()) {
    const calc=enumerator(p[0]??-1,q[0]??-1,
      adjacency(p,alphabet),adjacency(q,alphabet),p.length,q.length,alphabet);
    assert.deepEqual(calc.endpoints,[endpoint(p),endpoint(q)]);
    for(let k=0;k<=Math.min(p.length,q.length);k++)
      assert.equal(calc.dist[k],distribution.get(k)||0n,
        'J/K multiplicity mismatch for '+p+' ; '+q+' ; k='+k);
    matched += Number(calc.dist.reduce((a,b)=>a+b,0n));
    totalStates+=calc.states;totalTransitions+=calc.transitions;
  }
  assert.equal(matched,ww.length**2);
  return {alphabet,maxLength,total_words:ww.length,ordered_pairs:matched,
    distinct_Euler_input_fibers:groups.size,memo_states_summed:totalStates,
    typed_transitions_summed:totalTransitions};
}
function testFrontier() {
  const all=words(3,5), qwords=words(3,2);
  let pairs=0,appendChecks=0,buckets=0;
  for(const m of [2,3,4,5]) for(const n of [0,1,2]) if (m>n)
    for(const q of qwords.filter(w=>w.length===n)) for(const budget of [1,2,3]) {
      const groups=new Map();
      for(const p of all.filter(w=>w.length===m)) {
        const key=signature(p,3)+'|'+kdiag(p,q);
        if(!groups.has(key))groups.set(key,[]);
        groups.get(key).push(p);
      }
      for(const group of groups.values()) {
        buckets++;
        for(let x=0;x<group.length;x++)for(let y=x+1;y<group.length;y++) {
          const p=group[x],pp=group[y],b=Math.min(budget,m-n);
          const equalFrontier=p.slice(n,n+b).join(',')===pp.slice(n,n+b).join(',');
          let sameAll=true;
          for(const ext of words(3,budget)) {
            const eq=kdiag(p,q.concat(ext))===kdiag(pp,q.concat(ext));
            appendChecks++;
            if(!eq)sameAll=false;
          }
          assert.equal(equalFrontier,sameAll,'frontier quotient error');
          pairs++;
        }
      }
    }
  assert(pairs>0);
  return {symbol_alphabet:3,max_P_length:5,max_Q_length:2,append_budget:[1,3],
    matched_observer_P_pairs_checked:pairs,explicit_Q_append_comparisons:appendChecks,
    buckets_evaluated:buckets};
}
function verify() {
  const native=testEnumeration(12,2);
  const three=testEnumeration(3,4);
  const frontier=testFrontier();
  const p=[0,0,0,1,0,0,0,0], pp=[0,1,0,0,0,0,0,0],q=[0];
  assert.deepEqual(adjacency(p),adjacency(pp));
  assert.deepEqual(endpoint(p),endpoint(pp));
  assert.equal(kdiag(p,q),kdiag(pp,q));
  assert.deepEqual([kdiag(p,[0,0]),kdiag(pp,[0,0])],[2,1]);
  const probeP=[0,0,1,0],probeQ=[0,0,1,0];
  const probe=enumerator(0,0,adjacency(probeP),adjacency(probeQ),4,4);
  return {status:'STAGE426B_UNEQUAL_EULER_FRONTIER_EXACT_PASS',
    frozen_science:{global:'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
      em:'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
      p000_blob:'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
    integer_arithmetic:'BigInt DP and exact integer typed X6 endpoints; no floating point',
    differential_checks:[three,native],frontier_exact_tests:frontier,
    fixed_tail_witness:{L:3,observed_after_Q_append:[2,1]},
    same_J_K_histogram_probe:probe.dist.map(v=>v.toString()),
    scope:'Exact complete finite enumeration in listed domains; arbitrary finite inputs via bijection theorem; online frontier theorem via first differing alignment index',
    research_status:'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED'};
}
if(require.main===module)console.log(JSON.stringify(verify(),null,2));
module.exports={enumerator,verify};
