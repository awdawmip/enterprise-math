// Executed C++17 search and independent raw transcript replay.
// g++ -O3 -std=c++17 EC49FYQ_FINITE_EXCESS_GAME_VERIFY.cpp -o fyq && ./fyq 5
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;const U ALL=(1ULL<<50)-1;int C=5;U R[10],sup[50],hit[50][1024];int F[]={23,86,91,101,123,157,175,203,211,243,245,281,287,299,301,327,346,367,371,389,394,410,412,447,457,460,486,491,567,599,602,613,615,646,673,697,701,718,721,753,788,789,828,833,857,867,949,965,980,1005};
struct S{U a;vector<U> l;int e,h;bool live;bool operator==(S const&b)const{return a==b.a&&l==b.l&&e==b.e&&h==b.h&&live==b.live;}};struct H{size_t operator()(S const&s)const{U x=s.a*31+s.e*8+s.h*2+s.live;for(U z:s.l)x^=z+0x9e3779b97f4a7c15ULL+(x<<6)+(x>>2);return x;}};
unordered_map<S,int,H> memo;long long calls=0;auto st=chrono::steady_clock::now();
int norm(S&s){bool change=true;while(change&&s.a&&s.h>0){change=false;U a=s.a;while(a){int i=__builtin_ctzll(a);a&=a-1;int b=0;for(U l:s.l)b+=!(l>>i&1);if(b>s.h){s.a&=~(1ULL<<i);change=true;}}vector<U> l;for(U z:s.l){z&=s.a;if(!z){s.h--;s.e--;change=true;}else if(z!=s.a)l.push_back(z);}s.l.swap(l);}sort(s.l.begin(),s.l.end());int low=0;U a=s.a;while(a){int i=__builtin_ctzll(a);a&=a-1;int b=0;for(U l:s.l)b+=!(l>>i&1);low+=(b<s.h);}return low;}
bool bound(S const&s){if(s.h<=0)return true;U a=s.a;while(a){int i=__builtin_ctzll(a);a&=a-1;int b=0;vector<U> opt;for(U l:s.l)if(!(l>>i&1))b++;else opt.push_back(l);if(b>=s.h)continue;int ex=C-s.e+b;if(ex<0)return false;if(ex>=3)continue;int k=max(0,(int)opt.size()-(s.h-1-b));U vs0=sup[i]&s.a;if(!vs0)continue;for(int a=0;a<(1<<(int)opt.size());a++){if(__builtin_popcount((unsigned)a)!=k)continue;U vs=vs0;for(int j=0;j<(int)opt.size();j++)if(a>>j&1)vs&=opt[j];if(!vs)continue;bool ok=false;if(ex==1){for(int t=0;t<10;t++)if(!(vs&~hit[i][1<<t])){ok=true;break;}}else if(ex==2){for(int t=0;t<10&&!ok;t++)for(int r=t+1;r<10;r++)if(!(vs&~hit[i][(1<<t)|(1<<r)])){ok=true;break;}}if(!ok)return false;}}
return true;}
struct Opt{S x,y;int nx,ny,j,t,score;};
bool solve(S s){calls++;int low=norm(s);if(!low)return true;if(!bound(s))return false;if(__builtin_popcountll(s.a)==1)return true;auto it=memo.find(s);if(it!=memo.end())return it->second>=0;if(calls%1000000==0)cerr<<calls<<" memo "<<memo.size()<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<endl;
vector<Opt> opts;for(int j=-1;j<=(int)s.l.size();j++){if(j==-1&&!s.live)continue;if(j>0&&j<(int)s.l.size()&&s.l[j]==s.l[j-1])continue;for(int t=0;t<10;t++){U p=s.a&R[t];if(j>=0&&j<(int)s.l.size())p&=s.l[j];if(!p)continue;if((j==-1||(j==(int)s.l.size()&&s.live))&&p==s.a)continue;S x=s,y=s;x.e++;if(j==-1){x.a&=~R[t];y.a=p;y.e++;}else{if(j==(int)s.l.size())x.l.push_back(s.a&~R[t]);else{x.l[j]&=~R[t];y.l.erase(y.l.begin()+j);}y.a=p;y.live=true;}int nx=norm(x),ny=norm(y);if(!x.a||!y.a||!bound(x)||!bound(y))continue;int score=max(nx,ny)*100+nx+ny;opts.push_back({x,y,nx,ny,j,t,score});}}
sort(opts.begin(),opts.end(),[](auto&a,auto&b){return tie(a.score,a.j,a.t)<tie(b.score,b.j,b.t);});for(auto&o:opts){bool ok=o.nx>=o.ny?(solve(o.x)&&solve(o.y)):(solve(o.y)&&solve(o.x));if(ok){memo[s]=(o.j+1)*10+o.t;return true;}}memo[s]=-1;return false;}
void replay(int m);
int main(int argc,char**argv){if(argc>1)C=atoi(argv[1]);for(int t=0;t<10;t++)for(int i=0;i<50;i++)if(F[i]>>t&1)R[t]|=1ULL<<i;for(int i=0;i<50;i++)for(int v=0;v<50;v++)if(i!=v&&(F[v]&F[i])==F[i]){sup[i]|=1ULL<<v;for(int t=0;t<1024;t++)if(t&(F[v]^F[i]))hit[i][t]|=1ULL<<v;}
S s{ALL,{},0,3,false};bool ok=solve(s);cout<<3<<","<<C<<","<<ok<<","<<calls<<","<<memo.size()<<endl;if(ok)for(int m=8;m<=16;m++)replay(m);}
void replay(int m){
int mx=0,mfresh=0,msat=0;long long total=0,cnt=0;int fail=0;
for(int u:F)for(int H=0;H<(1<<m);H++)if(__builtin_popcount((unsigned)H)<=3){
 vector<int> neg(m),pos(m);int d=0, used=0;
 auto probe=[&](int t,int j){assert(j>=0&&j<m);int bit=1<<t;assert(!((neg[j]|pos[j])&bit));d++;if((u&bit)&&!(H>>j&1)){pos[j]|=bit;return true;}neg[j]|=bit;return false;};
 bool good=true;int recovered=-1,rh=0;
 while(true){
  U a=0;array<int,50> forced{};
  for(int i=0;i<50;i++){bool ok=true;int b=0;for(int j=0;j<m;j++){if(pos[j]){if((pos[j]&F[i])!=pos[j]||(neg[j]&F[i])){ok=false;break;}}else b+=!!(neg[j]&F[i]);}if(ok&&b<=3){a|=1ULL<<i;forced[i]=b;}}
  assert(a&(1ULL<<(find(F,F+50,u)-F)));
  int known=0,confirmed=0,live=-1,fresh=-1,low=0;for(int i=0;i<50;i++)if(a>>i&1)low+=forced[i]<3;
  vector<pair<U,int>> cols;vector<int> unknown;
  for(int j=0;j<m;j++){if(pos[j]){confirmed++;live=j;continue;}U l=a;for(int i=0;i<50;i++)if((l>>i&1)&&(neg[j]&F[i]))l&=~(1ULL<<i);if(!l)known|=1<<j;else {unknown.push_back(j);if(l!=a)cols.push_back({l,j});}if(!neg[j])fresh=j;}
  sort(cols.begin(),cols.end());int b=__builtin_popcount((unsigned)known);
  S s{a,{},d-confirmed-b,3-b,live>=0};for(auto x:cols)s.l.push_back(x.first);
  if(__builtin_popcountll(a)==1){
    recovered=F[__builtin_ctzll(a)];rh=known;
    if(!low){for(int j:unknown)assert(!(neg[j]&recovered));}
    else for(int j:unknown){int t=__builtin_ctz((unsigned)recovered);assert(!(neg[j]>>t&1));if(!probe(t,j))rh|=1<<j;}
    break;
  }
  if(!low){
    int j=live>=0?live:fresh;if(j<0){good=false;break;}
    U rem=a;
    while(__builtin_popcountll(rem)>1){int t=-1,best=99;for(int r=0;r<10;r++){int n=__builtin_popcountll(rem&R[r]),k=__builtin_popcountll(rem&~R[r]);if(n&&k&&max(n,k)<best){best=max(n,k);t=r;}}assert(t>=0);bool x=probe(t,j);rem&=x?R[t]:~R[t];}
    recovered=F[__builtin_ctzll(rem)];rh=0;for(int j=0;j<m;j++)if(!pos[j]&&(neg[j]&recovered))rh|=1<<j;
    msat=max(msat,d);break;
  }
  auto it=memo.find(s);assert(it!=memo.end()&&it->second>=0);
  int j=it->second/10-1,t=it->second%10;
  if(j==-1)j=live;else if(j==(int)cols.size()){j=fresh;if(j<0){good=false;break;}}else j=cols[j].second;
  assert(j>=0);probe(t,j);if(d>m+5){good=false;break;}
 }
 if(!good){fail++;continue;}
 assert(recovered==u&&rh==H);if(d>m+5){fail++;continue;}
 cnt++;total+=d;mx=max(mx,d);
}
cout<<"replay "<<m<<" pass "<<cnt<<" fail "<<fail<<" max "<<mx<<" total "<<total<<" saturatedMax "<<msat<<endl;
}
