function assert(c,msg){if(!c)throw Error(msg);}

function width(a){return Math.ceil(Math.log2(a+1));}

function model(a,k,L,lam){assert(a>=1&&Number.isInteger(a)&&k>=0&&L>=0,"parameters");assert(lam.length===a&&Array.from({length:k},(_,i)=>lam.includes(i)).every(Boolean),"labels");return {a,k,L,lam,b:width(a),d:k+k*(k-1)/2,D:k+k*(k-1)/2+width(a)*L};}

function ident(D){return {sel:Array.from({length:D},(_,i)=>i),val:Array(D).fill(0)};}

function generator(M,x){const {a,k,L,lam,b,d,D}=M;assert(x>=0&&x<a,"symbol");const T=ident(D),label=lam[x];const constant=(r,v)=>{T.sel[r]=-1;T.val[r]=v;};if(label>=0){constant(label,1);let r=k;for(let i=0;i<k;i++)for(let j=i+1;j<k;j++){if(i===label)constant(r,1);else if(j===label)constant(r,0);r++;}}for(let slot=0;slot<L;slot++)for(let bit=0;bit<b;bit++){let row=d+slot*b+bit;if(slot+1===L)constant(row,((x+1)>>bit)&1);else{T.sel[row]=d+(slot+1)*b+bit;T.val[row]=0;}}return T;}

function compose(A,B){assert(A.sel.length===B.sel.length,"dimensions");const D=A.sel.length,sel=[],val=[];for(let i=0;i<D;i++){let j=B.sel[i];if(j<0){sel[i]=-1;val[i]=B.val[i];}else{sel[i]=A.sel[j];val[i]=sel[i]<0?A.val[j]:0;}}return {sel,val};}

function wordAction(M,w){let T=ident(M.D);for(const x of w)T=compose(T,generator(M,x));return T;}

function actionKey(T){return T.sel.join(",")+"|"+T.val.join(",");}

function applyZero(T){return T.sel.map((j,i)=>j<0?T.val[i]:0);}

function observation(M,w){let s=[];for(const x of w){const l=M.lam[x];if(l>=0){s=s.filter(y=>y!==l);s.push(l);}}const t=M.L?w.slice(-M.L):[];return {s,t};}

function observationKey(o){return o.s.join(",")+"|"+o.t.join(",");}

function expectedOrbit(M,w){const bits=Array(M.D).fill(0),last=Array(M.k).fill(-1);w.forEach((x,i)=>{if(M.lam[x]>=0)last[M.lam[x]]=i;});for(let i=0;i<M.k;i++)bits[i]=last[i]>=0?1:0;let p=M.k;for(let i=0;i<M.k;i++)for(let j=i+1;j<M.k;j++)bits[p++]=last[i]>last[j]?1:0;const tail=M.L?w.slice(-M.L):[];const pad=M.L-tail.length;tail.forEach((x,j)=>{for(let bit=0;bit<M.b;bit++)bits[M.d+(pad+j)*M.b+bit]=((x+1)>>bit)&1;});return bits;}

function words(a,max){let out=[[]],front=[[]];for(let len=1;len<=max;len++){let next=[];for(const w of front)for(let x=0;x<a;x++)next.push([...w,x]);out.push(...next);front=next;}return out;}

function factorial(n){let p=1n;for(let j=2;j<=n;j++)p*=BigInt(j);return p;}

function countStates(M){const {a,k,L,lam}=M;let n=0n;for(let h=0;h<L;h++)n+=BigInt(a)**BigInt(h);const d=Array.from({length:k},(_,i)=>lam.filter(x=>x===i).length);for(let mask=0;mask<(1<<k);mask++){let size=0,sum=0;for(let i=0;i<k;i++)if(mask&(1<<i)){size++;sum+=d[i];}n+=factorial(size)*BigInt(a-sum)**BigInt(L);}return n;}

function main(){let specs=[[2,1,2,[-1,0],7],[3,2,2,[-1,0,1],5],[3,2,1,[0,0,1],5],[2,0,3,[-1,-1],6],[2,1,0,[0,-1],7],[1,1,2,[0],8]];let totals={models:0,words:0,state_classes:0,action_orbits:0,composition_checks:0,errors:0},models=[];let seed=0x5A17C201;function rand(){seed ^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return seed>>>0;}for(const [a,k,L,lam,max] of specs){const M=model(a,k,L,lam);const ws=words(a,max),o2a=new Map(),a2o=new Map();for(const w of ws){const T=wordAction(M,w),ak=actionKey(T),ok=observationKey(observation(M,w)),state=applyZero(T),expect=expectedOrbit(M,w);assert(state.join(",")===expect.join(","),"orbit mismatch "+JSON.stringify({M,w,state,expect}));assert(!o2a.has(ok)||o2a.get(ok)===ak,"same observation different affine");assert(!a2o.has(ak)||a2o.get(ak)===ok,"distinct observations same affine");o2a.set(ok,ak);a2o.set(ak,ok);}assert(BigInt(o2a.size)===countStates(M),"not fully enumerated states");for(let i=0;i<300;i++){const w=ws[rand()%ws.length],z=ws[rand()%ws.length];const T=compose(wordAction(M,w),wordAction(M,z));const T2=wordAction(M,w.concat(z));assert(actionKey(T)===actionKey(T2),"composition mismatch");assert(applyZero(T).join(",")===expectedOrbit(M,w.concat(z)).join(","),"concat mismatch");totals.composition_checks++;}totals.models++;totals.words+=ws.length;totals.state_classes+=o2a.size;totals.action_orbits+=a2o.size;models.push({a,k,L,labels:lam,word_test_depth:max,words_checked:ws.length,reachable_states:Number(countStates(M)),affine_dimension:M.D});}const natural=model(84,6,2,Array.from({length:84},(_,x)=>Math.floor(x/12)-1));const N=countStates(natural);assert(N===1407685n,"X6 R200 count mismatch");return {schema:"EM_R201_BINARY_AFFINE_OBSERVER_VERIFICATION_V1",status:"PASS",arithmetic:"exact Boolean/int plus BigInt counts",backend:"JS_DESCRIPTOR_REFERENCE_NOT_INSTALLED_NATIVE_BRC",frozen_science_pin:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",totals,models,native_x6:{direction_count:12,source_count:6,alphabet_count:84,tail_depth:2,observer_state_count:N.toString(),minimal_binary_state_bits:Math.ceil(Math.log2(Number(N))),affine_observer_dimension:natural.D,physical_dim_example:2,dense_rational_slot_increment:2*2*natural.D+natural.D**2+natural.D},native_brc_installed_package_integration:"NOT_EXECUTED"};}

console.log(JSON.stringify(main(),null,2));
