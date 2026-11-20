"""Cross-check the C++ signed prices against independent Python menu scoring."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json,subprocess,sys
HERE=Path(__file__).resolve().parent
release=HERE.parent/'previous'
sixth=release/'previous';second=sixth/'previous/previous/previous/previous'
sys.path.insert(0,str(second/'bounds'))
from cyclic11 import class_cost,observations
from prior_bounds import observation_file
_,menus=observations();blocks=[[[v&((1<<125)-1)for v in r]for r in menus],[[v>>125 for v in r]for r in menus]]
eleven=json.loads((release/'previous/previous/previous/eleven_six_counts/groups.json').read_text())
twelve=json.loads((sixth/'previous/c3/groups.json').read_text())
def double(x):return 25*(2*(x//25)%5)+5*(2*(x//5%5)%5)+2*(x%5)%5
tables=eleven+[twelve]
tables=tables+[[[double(x)for x in r]for r in t]for t in tables]
classes=[r for t in tables for r in t]
expected=[]
for row in classes:
 i,d=[class_cost(row,m)for m in blocks];expected.append([i+d,i-d])
with TemporaryDirectory()as t:
 w=Path(t);observation_file(w/'obs')
 (w/'check.cpp').write_text('#define main native_main\n#include "'+str(HERE/'weighted_native.cpp')+'"\n#undef main\nint main(int argc,char**av){std::ifstream f(av[1],std::ios::binary);f.read((char*)obs,sizeof(obs));int n;while(std::cin>>n){M m=0;for(int j=0,x;j<n;j++){std::cin>>x;m|=M(1)<<x;}std::cout<<price(m)<<" "<<difference(m)<<"\\n";}}\n')
 subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',w/'check.cpp','-o',w/'check'],check=True,capture_output=True)
 result=subprocess.check_output([w/'check',w/'obs'],input=''.join(str(len(r))+' '+' '.join(map(str,r))+'\n'for r in classes),text=True)
 actual=[list(map(int,l.split()))for l in result.splitlines()];assert actual==expected
print(json.dumps({'classes_checked':len(classes),'tables_checked':len(tables),'table_action_costs':[[sum(class_cost(r,m)for r in t)for m in blocks]for t in tables]},indent=2))
