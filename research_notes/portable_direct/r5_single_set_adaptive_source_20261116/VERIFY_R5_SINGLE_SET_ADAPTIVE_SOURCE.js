// Reproduce: node VERIFY_R5_SINGLE_SET_ADAPTIVE_SOURCE.js > reproduced.json

// All arithmetic is exact (integer/Boolean). No external dependencies.

function must(c,m){if(!c)throw Error("VERIFY_FAILED "+m)}

function q(u,k){let v=0;for(let i=0;i<k;i++)v+=((u>>i)&1)*((u>>((i+1)%k))&1);return v}

function qa(z,k){return q(z<<1,k)}

function qb(z,k){return q((z<<1)|1,k)}

function good(z,n){for(let i=0;i<n-2;i++)if(((z>>i)&7)===0)return false;return true}

function maximum(z,k){for(let i=0;i<k-1;i++){const w=z|(1<<i);if(qb(w,k)===qb(z,k))z=w}return z}

function edges(k){const a=[];for(let i=0;i<k;i++){const j=(i+1)%k;a.push([i,j],[i,k+i],[j,k+i])}return a}

function sources(k,u){const e=edges(k),L=new Set();for(let i=0;i<k;i++)if(!((u>>i)&1)){L.add("O0-helper:"+i);L.add("O4-helper:"+i)}for(let t=0;t<e.length;t++){const [a,b]=e[t];L.add("O1-edge:"+t);if(!(a<k&&!((u>>a)&1))&&!(b<k&&!((u>>b)&1)))L.add("O0-edge:"+t)}return L}

function usable(L,u,k){for(let i=0;i<k;i++)if((u>>i)&1)if(L.has("O0-helper:"+i)||L.has("O4-helper:"+i))return false;const e=edges(k);for(let t=0;t<e.length;t++){const [a,b]=e[t];if(!L.has("O1-edge:"+t))return false;if(!L.has("O0-edge:"+t)&&!(a<k&&L.has("O0-helper:"+a)&&L.has("O4-helper:"+a))&&!(b<k&&L.has("O0-helper:"+b)&&L.has("O4-helper:"+b)))return false}return true}

function brute(k){const m=1<<(k-1),lim=1<<m,byFirst=Array.from({length:m},()=>[]);let groups=0;for(let mask=1;mask<lim;mask++){let zu=0,aval=-1,bval=-1,ok=true;for(let z=0;z<m;z++)if((mask>>>z)&1){zu|=z;const a=qa(z,k),b=qb(z,k);if(aval<0){aval=a;bval=b}else if(a!==aval||b!==bval){ok=false;break}}if(ok&&qa(zu,k)===aval&&qb(zu,k)===bval){groups++;const cost=aval===bval?1:2;for(let z=0;z<m;z++)if((mask>>>z)&1)byFirst[z].push([mask,cost])}}const memo=new Map([[0,0]]);function rec(mask){if(memo.has(mask))return memo.get(mask);const first=31-Math.clz32(mask&-mask);let best=Infinity;for(const [g,c] of byFirst[first])if((mask&g)===g)best=Math.min(best,c+rec(mask^g));memo.set(mask,best);return best}return {minimum:rec(lim-1),compatible_groups:groups,subsets_solved:memo.size}}

function verify(maxK=11){const rows=[];let masks=0,libraries=0,transitions=0,maximalPairs=0;for(let k=3;k<=maxK;k++){const n=k-1,m=1<<n,ms=[];for(let z=0;z<m;z++)if(good(z,n))ms.push(z);const grp=new Map(ms.map(z=>[z,[]]));for(let z=0;z<m;z++){const w=maximum(z,k);must(grp.has(w),"maximal word");must((w&z)===z&&qb(w,k)===qb(z,k),"maximal source");must(qa(w,k)===qa(z,k),"monotone decomposition");grp.get(w).push(z)}let A=0,N=0;for(const w of ms){const s=qb(w,k)-qa(w,k),L0=sources(k,w<<1),L1=sources(k,(w<<1)|1);must(s>=0&&s<=2&&L0.size===5*k+qa(w,k)&&L1.size===5*k+qb(w,k),"size");N+=s===0?1:2;if(s===0)A++;for(const z of grp.get(w))for(let b=0;b<2;b++){const u=(z<<1)|b,L=(s===0||b===1)?L1:L0;must(usable(L,u,k)&&L.size===5*k+q(u,k),"source output");masks++;libraries++;for(let target=0;target<2;target++){const z2=((u&~1)|target)>>1;must(maximum(z2,k)===w,"Set transition stable");transitions++}}}for(let i=0;i<ms.length;i++)for(let j=i+1;j<ms.length;j++){const a=ms[i],b=ms[j];must(qb(a,k)!==qb(b,k)||qb(a|b,k)>qb(a,k),"maxima incompatible");maximalPairs++}must(N===2*ms.length-A,"formula");let staticM=0;for(let u=0;u<(1<<k);u++){let ok=true;for(let j=0;j<k;j++)if(((u>>j)&1)+((u>>((j+1)%k))&1)+((u>>((j+2)%k))&1)===0){ok=false;break}if(ok)staticM++}const independent=k<=5?brute(k):null;if(independent)must(independent.minimum===N,"independent partition minimum");rows.push({k,static_minimum_outputs:staticM,external_maximal_words:ms.length,zero_endpoint_maxima:A,adaptive_minimum_states:N,scalar_observation_states:k===3?5:5*k-11,full_source_spectrum_states:1<<k,independent_partition:independent})}return {status:"PASS_R5_SINGLE_SET_EXACT_ADAPTIVE_SOURCE_TRANSDUCER",frozen_input:"435e77af0d180eac32bd1f9c4c464bc4010b7551",domain:"cycle-of-triangles old-source-labelled radius-two indexed-center auxiliary model",k_range:"3..11",independent_partition_coverage:"k=3,4,5 all possible groups of external configurations",arithmetic:"exact integer/Boolean",raw_masks_verified:masks,feasible_optimal_libraries_checked:libraries,deterministic_Set_checks:transitions,distinct_maximal_pair_checks:maximalPairs,rows}}

const evidence = verify(11);

console.log(JSON.stringify(evidence,null,2));

