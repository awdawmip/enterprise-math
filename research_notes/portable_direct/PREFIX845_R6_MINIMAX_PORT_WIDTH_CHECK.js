function gcd(a,b){while(b){let t=a%b;a=b;b=t;}return a}

function gcdBig(a,b){while(b!==0n){let t=a%b;a=b;b=t}return a}

function radBig(n){if(n<=0n)throw Error("rad requires positive");let r=1n;for(let d=2n;d*d<=n;d++){if(n%d===0n){r*=d;while(n%d===0n)n/=d}}if(n>1n)r*=n;return r}

function factBig(k){let r=1n;for(let i=2;i<=k;i++)r*=BigInt(i);return r}

function kthRootCeil(n,k){if(n<1n||k<1)throw Error("bad root");let hi=1n;while(hi**BigInt(k)<n)hi*=2n;let lo=0n;while(lo+1n<hi){let mid=(lo+hi)/2n;if(mid**BigInt(k)>=n)hi=mid;else lo=mid}return hi}

function construct(N,C,k){let D=radBig(C*factBig(k-1));let X=kthRootCeil(N,k);let q=(X-1n+D-1n)/D;let ms=Array.from({length:k},(_,i)=>1n+(q+BigInt(i))*D);let product=ms.reduce((v,w)=>v*w,1n);for(let i=0;i<k;i++){if(gcdBig(ms[i],C)!==1n)throw Error("C gcd");for(let j=i+1;j<k;j++)if(gcdBig(ms[i],ms[j])!==1n)throw Error("not coprime")};if(product<N||ms[k-1]>X+BigInt(k)*D)throw Error("bound");return {N:String(N),C:String(C),k,D:String(D),X:String(X),moduli:ms.map(String),product:String(product),max:String(ms[k-1])}}

function lcm(a,b){return a/gcd(a,b)*b}

function finiteAt(N,C,k,B){const R=2**B,allowed=[];for(let m=1;m<=R;m++)if(gcd(m,C)===1)allowed.push(m);let nodes=0;function recurse(start,vals,L){nodes++;if(L>=N)return {moduli:vals,lcm:L};if(vals.length===k)return null;for(let i=start;i<allowed.length;i++){let r=recurse(i+1,[...vals,allowed[i]],lcm(L,allowed[i]));if(r)return r}return null}return {witness:recurse(0,[],1),nodes,allowedCount:allowed.length}}

function exactMin(N,C,k){let checked=0;for(let B=0;B<=20;B++){let r=finiteAt(N,C,k,B);checked+=r.nodes;if(r.witness)return {N,C,k,B,witness:r.witness.moduli,lcm:r.witness.lcm,enumeratedSearchNodes:checked}}throw Error("bound exceeded")}

function runChecks(){let rows=[],nodes=0;for(const C of [2,6,30])for(const N of [4,16,64,256,1024])for(const k of [1,2,3]){let e=exactMin(N,C,k);let x=construct(BigInt(N),BigInt(C),k);if(Number(x.product)<N)throw Error("construction failure");let low=0;while((2n**BigInt(low*k))<BigInt(N))low++;if(e.B<low)throw Error("info bound");if(e.witness.reduce((v,w)=>lcm(v,w),1)!==e.lcm)throw Error("witness incorrect");if(e.B>0&&finiteAt(N,C,k,e.B-1).witness)throw Error("not minimum");nodes+=e.enumeratedSearchNodes;rows.push(e)}let large=[construct(10n**30n,30n,3),construct(10n**50n,30n,4),construct(10n**60n,2n,5)];let cases={"2:1024:3":4,"30:1024:3":5,"2:256:2":5,"6:64:3":4,"30:16:2":4};for(const e of rows){let key=[e.C,e.N,e.k].join(":");if(cases[key]!==undefined&&e.B!==cases[key])throw Error("known exact mismatch "+key)}return {schema:"PREFIX845_R6_MINIMAX_PORT_WIDTH_EXACT_V1",status:"ALL_EXACT_ASSERTIONS_PASSED",frozen_scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",model:"fixed stateless raw modular ports, full infinite horizon, C=ab",enumeration_domain:{N:[4,16,64,256,1024],C:[2,6,30],ports:[1,2,3]},exact_cases:rows.length,exhaustive_search_nodes:nodes,finite_optima:rows,large_integer_constructions:large,proof_status:"paper argument; finite tests only verify listed cases and construction examples",native_cell_link_port_verified:false}}

const output=runChecks();
console.log(JSON.stringify(output,null,2));
