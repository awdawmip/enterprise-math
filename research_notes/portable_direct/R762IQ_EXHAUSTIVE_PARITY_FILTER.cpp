#include <bits/stdc++.h>
using namespace std;
struct Tri {array<int,3> p;};
array<array<int,2>,15> ports;
array<array<int,3>,20> supports;
array<Tri,20> tri;
int tri_mask[20], forced[1<<15];
vector<int> masks_by_z[211];
int z_index[1<<20];
long long total[4][4]={}, yes[4][4]={}, no[4][4]={};
long long byD[7][4][2]={};
long long hist[4]={};
long long fail_by_pair[4][7] = {};
int current_def[20];
int root(int a, array<int,15>& par) {while(par[a]!=a){par[a]=par[par[a]];a=par[a];}return a;}
void join(int a,int b,array<int,15>& par){a=root(a,par);b=root(b,par);if(a!=b)par[a]=b;}
static bool feasible(int activeMask){
    array<int,15> par; iota(par.begin(),par.end(),0);
    for(int i=0;i<20;++i){if(current_def[i]>1)continue; int x=tri_mask[i]&activeMask;
        if(__builtin_popcount((unsigned)x)==3){auto [a,b,c]=tri[i].p;join(a,b,par);join(a,c,par);}}
    int fixed=0;int choices[3][3], countChoice=0;
    for(int i=0;i<20;++i){int n=3-current_def[i]; if(n==0)continue; int x=tri_mask[i]&activeMask;
        int sz=__builtin_popcount((unsigned)x);if(sz<2) return false;
        if(sz==2){if(n&1){int a=__builtin_ctz((unsigned)x);int b=__builtin_ctz((unsigned)(x&(x-1)));fixed ^= (1<<root(a,par)) ^(1<<root(b,par));}}
        else if(n==1){if(countChoice>=3){cerr<<"Unexpected >3 singletons\n";abort();}auto [a,b,c]=tri[i].p;
            a=root(a,par);b=root(b,par);c=root(c,par);
            choices[countChoice][0]=(1<<a)^(1<<b);
            choices[countChoice][1]=(1<<a)^(1<<c);
            choices[countChoice][2]=(1<<b)^(1<<c);
            ++countChoice;}}
    int options[27],num=1; options[0]=fixed;
    for(int t=0;t<countChoice;++t){int older=num;num*=3;
      for(int j=older-1;j>=0;--j){int v=options[j];
         options[3*j+0]=v^choices[t][0];options[3*j+1]=v^choices[t][1];options[3*j+2]=v^choices[t][2];}}
    for(int j=0;j<num;++j) if(options[j]==0)return true;
    return false;
}
void visit(int D){
    int z=0,m=0;
    for(int i=0;i<20;++i)if(current_def[i]==3){z|=1<<i;++m;}
    if(m>2) abort();
    int zi=z_index[z];if(zi<0)abort();hist[m]++;
    for(int inactive:masks_by_z[zi]){
        int j=__builtin_popcount((unsigned)inactive);if(j>6)abort();
        bool ok=feasible(0x7fff^inactive);
        total[m][j>=3?3:j]++;
        byD[D][m][ok?1:0]++;
        if(ok)yes[m][j>=3?3:j]++;else{no[m][j>=3?3:j]++;
            if(m==2){int za=-1,zb=-1;for(int t=0;t<20;++t)if(z>>t&1){if(za<0)za=t;else zb=t;}int common=0;for(int a:supports[za])for(int b:supports[zb])if(a==b)++common;fail_by_pair[common][j]++;}
        }
    }
}
void explore(int pos,int remain,int D){
   if(remain<0)return;
   if(pos==20){if(remain==0)visit(D);return;}
   for(int d=0;d<=3&&d<=remain;++d){current_def[pos]=d;explore(pos+1,remain-d,D);}
}
int main(){
  int id[6][6]={};int pp=0,tt=0;
  for(int a=0;a<6;++a)for(int b=a+1;b<6;++b){ports[pp]={a,b};id[a][b]=id[b][a]=pp++;}
  for(int a=0;a<6;++a)for(int b=a+1;b<6;++b)for(int c=b+1;c<6;++c){supports[tt]={a,b,c};tri[tt].p={id[a][b],id[a][c],id[b][c]};tri_mask[tt]=(1<<id[a][b])|(1<<id[a][c])|(1<<id[b][c]);tt++;}
  fill(begin(z_index),end(z_index),-1);
  vector<int> zsets;zsets.push_back(0);
  for(int i=0;i<20;++i)zsets.push_back(1<<i);
  for(int i=0;i<20;++i)for(int j=i+1;j<20;++j)zsets.push_back((1<<i)|(1<<j));
  for(int i=0;i<(int)zsets.size();++i)z_index[zsets[i]]=i;
  for(int M=0;M<(1<<15);++M){int f=0;
     for(int i=0;i<20;++i)if(__builtin_popcount((unsigned)(M&tri_mask[i]))>=2)f|=1<<i;
     forced[M]=f;}
  for(int k=0;k<211;++k)for(int M=0;M<(1<<15);++M)
      if((forced[M]&~zsets[k])==0)masks_by_z[k].push_back(M);
  for(int d:{0,2,4,6})explore(0,d,d);
  long long tally=0,valid=0,invalid=0;
  for(int m=0;m<=2;++m){long long t=0,y=0,n=0;
    for(int j=0;j<4;++j){t+=total[m][j];y+=yes[m][j];n+=no[m][j];}
    tally+=t;valid+=y;invalid+=n;
    cout<<"missing="<<m<<" hist="<<hist[m]<<" candidates="<<t<<" parity_yes="<<y<<" parity_no="<<n<<"\n";}
  cout<<"ALL total="<<tally<<" yes="<<valid<<" no="<<invalid<<"\n";
  for(int d:{0,2,4,6}){long long a=0,b=0;for(int m=0;m<3;++m){a+=byD[d][m][0];b+=byD[d][m][1];}cout<<"D="<<d<<" original_n="<<(60-d)<<" yes="<<b<<" no="<<a<<"\n";}
  for(int c=0;c<=2;++c)for(int j=0;j<=6;++j)if(fail_by_pair[c][j]) cout<<"FAIL_PAIR overlap="<<c<<" inactive="<<j<<" count="<<fail_by_pair[c][j]<<"\n";
  assert(hist[0]==155156 && hist[1]==26600 && hist[2]==190);
  assert(tally==14260096 && valid==14259376 && invalid==720);
  assert(fail_by_pair[1][3]==360 && fail_by_pair[1][4]==360);
  cout<<"PASS R762IQ_EXHAUSTIVE_PARITY_FILTER\n";
  return 0;
}
