import json
from data.models import Stats,Discretization,Unit,Variable,ConsistencyLevel
from stations.models import Source, StationType, Localization,Coordinate
from stats.models import Reduction
from django.db import models




classes = [['Stats',Stats],['Discretization',Discretization],
           ['Unit',Unit],['Variable',Variable],['ConsistencyLevel',ConsistencyLevel],['Source',Source], ['StationType',StationType],['Reduction',Reduction]]# ['Coordinate',Coordinate], ['Localization',Localization],['Reduction',Reduction]]


'''

#Código utilizado caso queira exportar os dados do seu banco de dados:
dics={}

for classe_ in classes:
    dic={}
    Classe = classe_[1]
    classe = classe_[0]
    dics[classe]={}
    fields = [f for f in Classe._meta.fields]
    dics[classe]['fields']=[]
    for obj in Classe.objects.all():
        fs={}
        for f in fields:
            if f.name!='id':
                if isinstance(f,models.ForeignKey):
                    print( 'obteve')
                    fs["%s__type"%f.name] = eval('obj.%s.type'%f.name)
                else:
                    fs[f.name]=eval('obj.%s'%f.name)
        dics[classe]['fields'].append(fs)

with open('data.json', 'w') as outfile:
    json.dump(dics, outfile)
    
'''

with open('data.json') as infile:
    file = infile.read()
    dics = json.loads(file)

for classe in dics:
    Classe = [c[1] for c in classes if c[0]==classe]
    if Classe:
        Classe=Classe[0]
        aux = Classe.objects.all()
        aux.delete()
        objs=[]
        for obj in dics[classe]['fields']:
            d={}
            for key in obj:
                if key!="stats_type__type":
                    d[key]=obj[key]  
                else:
                    d['stats_type']=Stats.objects.get(type=obj[key])
            objs.append(d)
        Classe.objects.bulk_create([
            Classe(**obj) for obj in objs
        ])
    