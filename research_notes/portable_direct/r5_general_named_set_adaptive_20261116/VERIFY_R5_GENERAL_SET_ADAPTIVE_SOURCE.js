// Run: node VERIFY_R5_GENERAL_SET_ADAPTIVE_SOURCE.js > reproduced.json

// Exact integer/Boolean exhaustive cross-check (k=3..8, every J).

function must(c,m){if(!c)throw Error("FAIL "+m)}

function q(u,k){let s=0;for(let i=0;i<k;i++)s+=((u>>i)&1)*((u>>((i+1)%k))&1);return s}

function compose(z,x,J,K){let u=0;for(let i=0;i<J.length;i++)if((x>>i)&1)u|=1<<J[i];for(let i=0;i<K.length;i++)if((z>>i)&1)u|=1<<K[i];return u}

function cdata(z,k,J,K){const c=q(compose(z,0,J,K),k),b=J.map((_,i)=>q(compose(z,1<<i,J,K),k)-c),d=J.map(i=>J.filter(j=>j!==i&&(j===(i+1)%k||i===(j+1)%k)).length);const active=b.reduce((s,v,i)=>s|((v+d[i]>0)?(1<<i):0),0);return{c,b,active}}

function full(z,k,J,K){return q(compose(z,(1<<J.length)-1,J,K),k)}

function maximum(z,k,J,K){for(let i=0;i<K.length;i++){const w=z|(1<<i);if(full(w,k,J,K)===full(z,k,J,K))z=w}return z}

function edges(k){const a=[];for(let i=0;i<k;i++){const j=(i+1)%k;a.push([i,j],[i,k+i],[j,k+i])}return a}

function lib(k,u){const e=edges(k),L=new Set();for(let i=0;i<k;i++)if(!((u>>i)&1)){L.add("H0:"+i);L.add("H4:"+i)}for(let t=0;t<e.length;t++){const [a,b]=e[t];L.add("E1:"+t);if(!(a<k&&!((u>>a)&1))&&!(b<k&&!((u>>b)&1)))L.add("E0:"+t)}return L}

function sourceok(L,u,k){for(let i=0;i<k;i++)if((u>>i)&1)if(L.has("H0:"+i)||L.has("H4:"+i))return false;const e=edges(k);for(let t=0;t<e.length;t++){const [a,b]=e[t];if(!L.has("E1:"+t))return false;if(L.has("E0:"+t))continue;if(!(a<k&&L.has("H0:"+a)&&L.has("H4:"+a))&&!(b<k&&L.has("H0:"+b)&&L.has("H4:"+b)))return false}return true}

function brute(k,J){const K=Array.from({length:k},(_,i)=>i).filter(i=>!J.includes(i)),m=1<<K.length,lim=1<<m,byFirst=Array.from({length:m},()=>[]);let groups=0;for(let g=1;g<lim;g++){let orz=0,f=-1,ok=true;for(let z=0;z<m;z++)if((g>>>z)&1){orz|=z;const v=full(z,k,J,K);if(f<0)f=v;else if(f!==v){ok=false;break}}if(!ok||full(orz,k,J,K)!==f)continue;groups++;const a=cdata(orz,k,J,K).active;let cost=1;for(let i=0;i<J.length;i++)if((a>>i)&1)cost*=2;for(let z=0;z<m;z++)if((g>>>z)&1)byFirst[z].push([g,cost])}const memo=new Map([[0,0]]);function go(mask){if(memo.has(mask))return memo.get(mask);const i=31-Math.clz32(mask&-mask);let ans=Infinity;for(const [g,c] of byFirst[i])if((g&mask)===g)ans=Math.min(ans,c+go(mask^g));memo.set(mask,ans);return ans}return{minimum:go(lim-1),compatible_groups:groups,dp_masks:memo.size}}

function verify(maxK=8){let cases=0,rawChecks=0,setChecks=0,pairChecks=0;const selected=[];for(let k=3;k<=maxK;k++)for(let mJ=0;mJ<(1<<k);mJ++){const J=Array.from({length:k},(_,i)=>i).filter(i=>(mJ>>i)&1),K=Array.from({length:k},(_,i)=>i).filter(i=>!((mJ>>i)&1)),m=1<<K.length,maxima=[],groups=new Map();for(let z=0;z<m;z++){let mx=true;for(let i=0;i<K.length;i++)if(!((z>>i)&1)&&full(z|(1<<i),k,J,K)===full(z,k,J,K))mx=false;if(mx){maxima.push(z);groups.set(z,[])}}for(let z=0;z<m;z++){const w=maximum(z,k,J,K);must(groups.has(w)&&(w&z)===z&&full(w,k,J,K)===full(z,k,J,K),"maximal extension");const a=cdata(z,k,J,K),b=cdata(w,k,J,K);must(a.c===b.c&&a.b.join(",")===b.b.join(",")&&a.active===b.active,"positive-part descent");groups.get(w).push(z)}let N=0;for(const w of maxima){const a=cdata(w,k,J,K);let weight=1;for(let i=0;i<J.length;i++)if((a.active>>i)&1)weight*=2;N+=weight;for(const z of groups.get(w))for(let x=0;x<(1<<J.length);x++){const xx=x|(((1<<J.length)-1)^a.active),L=lib(k,compose(w,xx,J,K)),u=compose(z,x,J,K);must(sourceok(L,u,k)&&L.size===5*k+q(u,k),"feasible individual optimum");rawChecks++;for(let i=0;i<J.length;i++)for(let v=0;v<2;v++){const xnext=(x&~(1<<i))|(v<<i),abstractNext=(a.active&(1<<i))?((x&a.active&~(1<<i))|(v<<i)):(x&a.active);must((xnext&a.active)===abstractNext&&maximum(z,k,J,K)===w,"Set congruence");setChecks++}}}for(let i=0;i<maxima.length;i++)for(let j=i+1;j<maxima.length;j++){const a=maxima[i],b=maxima[j];must(full(a,k,J,K)!==full(b,k,J,K)||full(a|b,k,J,K)>full(a,k,J,K),"maximal words not separated");pairChecks++}must(N<=1<<k,"state upper bound");cases++;const adj=J.join(",")==="0,1",opp=k===6&&J.join(",")==="0,3";if((adj&&k<=8)||opp||(k===6&&(J.length===0||J.length===k))){let ind=null;if(k<=6&&J.length===2)ind=brute(k,J);if(ind)must(ind.minimum===N,"independent exact grouping");if(adj){let t=0;for(let z=0;z<(1<<(k-2));z++){let ok=true;for(let i=0;i<k-4;i++)if(((z>>i)&7)===0)ok=false;if(ok)t++}must(N===4*t,"adjacent two controls");}selected.push({k,J,external_maxima:maxima.length,exact_states:N,independent_partition:ind})}}return{status:"PASS_R5_ARBITRARY_NAMED_SET_ADAPTIVE_SOURCE_QUOTIENT",frozen_pin:"435e77af0d180eac32bd1f9c4c464bc4010b7551",domain:"cycle of k triangles; all named Set control subsets; k=3..8",arithmetic:"exact integer and Boolean",control_subsets_checked:cases,raw_state_source_checks:rawChecks,named_Set_transition_checks:setChecks,distinct_fiber_maxima_checks:pairChecks,selected}}

console.log(JSON.stringify(verify(8),null,2));

