#!/usr/bin/env node
// PREFIX-855 exact five-source adaptive-observer finite game.
'use strict';
const assert=require('node:assert/strict'),crypto=require('node:crypto');
const P=5,N=1<<P,Q=[3,5,7,9,11,13,15],FULL=(1n<<BigInt(N))-1n;
const MOVES=Array.from({length:N},(_,x)=>[x,...Array.from({length:P},(_,i)=>x^(1<<i))]);
const R=Object.fromEntries(Q.map(q=>[q,Array.from({length:q},(_,r)=>Array.from({length:N},(_,x)=>x%q===r?1n<<BigInt(x):0n).reduce((a,b)=>a|b,0n))]));
function count(x){let k=0;while(x){x&=x-1n;k++}return k}
function post(b){let z=0n;for(let x=0;x<N;x++)if(b&(1n<<BigInt(x)))for(const u of MOVES[x])z|=1n<<BigInt(u);return z}
function children(b,q){const z=post(b);return R[q].map(m=>z&m).filter(m=>m!==0n)}
function oracle(b,q){const s=new Set();for(let x=0;x<N;x++)if(b&(1n<<BigInt(x)))for(const u of MOVES[x])s.add(u);return Array.from({length:q},(_,r)=>Array.from(s).filter(x=>x%q===r).reduce((a,x)=>a|(1n<<BigInt(x)),0n)).filter(m=>m!==0n)}
const states=[FULL],index=new Map([[FULL,0]]),edges=[];
for(let i=0;i<states.length;i++){const tr=[];for(const q of Q){const cs=children(states[i],q);assert.deepEqual(cs,oracle(states[i],q));tr.push(cs.map(c=>{if(!index.has(c)){index.set(c,states.length);states.push(c)}return index.get(c)}))}edges.push(tr)}
assert.equal(states.length,1944);
const winning=new Set(states.flatMap((s,i)=>count(s)===1?[i]:[])),layers=[winning.size];
while(true){const add=[];for(let i=0;i<states.length;i++)if(!winning.has(i)&&edges[i].some(cs=>cs.every(j=>winning.has(j))))add.push(i);if(!add.length)break;for(const i of add)winning.add(i);layers.push(winning.size)}
assert.deepEqual(layers,[32,48]);assert(!winning.has(0));
const losing=new Set(states.map((_,i)=>i).filter(i=>!winning.has(i)));
assert.equal(losing.size,1896);
for(const i of losing)for(const cs of edges[i])assert(cs.some(j=>losing.has(j)));
const pairs=Array.from(winning).filter(i=>count(states[i])===2).map(i=>Array.from({length:N},(_,x)=>x).filter(x=>(states[i]&(1n<<BigInt(x)))!==0n));
pairs.sort((a,b)=>a[0]-b[0]||a[1]-b[1]);assert.equal(pairs.length,16);
function pairTest(a,b){let total=0,off=0;for(let x=0;x<N;x++)for(let y=0;y<N;y++)if(x%a===y%a)for(const u of MOVES[x])for(const v of MOVES[y])if(u%b===v%b){total++;if(u!==v)off++}return {total,off}}
assert.equal(pairTest(17,31).off,0);assert(pairTest(31,17).off>0);
for(let x=0;x<N;x++)assert.equal(new Set(MOVES[x].map(u=>u%11)).size,P+1);
const graph={state_masks:states.map(s=>s.toString(16)),transitions:edges};
const digest=crypto.createHash('sha256').update(JSON.stringify(graph)).digest('hex');
const result={status:'ALL_EXACT_ASSERTIONS_PASSED',model:{p:P,N,Q4:Q,step:'no-op or one named bit flip',observer:'U mod q, adaptive q may depend on all past residues'},game:{reachable_information_sets:states.length,action_rows:states.length*Q.length,winning_layers_cumulative:layers,winning_sets:winning.size,losing_sets:losing.size,winning_two_state_sets:pairs,all_direct_transition_oracles_passed:true,all_losing_action_rows_have_losing_successor:true,initial_set_losing:true,graph_sha256:digest,graph_encoding:'JSON.stringify({state_masks: BFS-order lowercase hex,transitions: indexed residue-child arrays in Q4 order})'},construction:{cold_start_moduli:[17,31],cold_start_width_bits:5,offdiagonal_trajectory_pairs:0,reverse_offdiagonal_trajectory_pairs:pairTest(31,17).off,steady_modulus:11,steady_width_bits:4,steady_states_verified:N},scope:'Exact finite named binary BRC scalar; no native X6 mapping'};
if(process.argv.includes('--full'))result.graph=graph;
process.stdout.write(JSON.stringify(result,null,2)+'\n');
