#define main unused_three_main
#include "three.cpp"
#undef main
struct R5{M m;array<M,5> row;};
int main(int argc,char**argv){ifstream f(argv[1]),data(argv[2]);int n=stoi(argv[3]);int rep,p,gi;W l,h;data>>rep>>l>>h>>p>>gi;base=(M(h)<<64)|l;vector<M> nine;
 while(f>>l>>h){M m=(M(h)<<64)|l;nine.push_back(m);if(!(m&base))nines.push_back(m);}
 for(int d=1;d<125;d++){int dx=d/25,dy=d/5%5,dz=d%5;if((dx?dx:dy?dy:dz)!=1)continue;
  for(int i=0;i<125;i++)g[i]=25*((i/25+dx)%5)+5*((i/5%5+dy)%5)+(i%5+dz)%5;
  vector<R5> A;for(auto m:nines){R5 r{m,{m}};M cur=m;bool good=true;for(int i=1;i<5;i++){cur=mv(cur);if(cur<m|| (cur&r.m)||(cur&base)){good=false;break;}r.row[i]=cur;r.m|=cur;}if(good)A.push_back(r);}
  size_t cases=0;for(int i=0;i<A.size();i++){
   vector<M> q;for(auto m:nines)if(!(m&A[i].m))q.push_back(m);
   auto test=[&](int j){trail={base};for(auto m:A[i].row)trail.push_back(m);M u=base|A[i].m;if(j>=0){for(auto m:A[j].row)trail.push_back(m);u|=A[j].m;}++cases;
    return tail(full^u,q,13-5*n);};
   if(n==1&&test(-1)){for(auto m:trail)cout<<W(m)<<" "<<W(m>>64)<<"\n";return 0;}
   if(n==2)for(int j=0;j<i;j++)if(!(A[i].m&A[j].m)&&test(j)){for(auto m:trail)cout<<W(m)<<" "<<W(m>>64)<<"\n";return 0;}
  }
  cerr<<d<<" "<<A.size()<<" "<<cases<<" "<<nodes<<endl;
 }}
