import sys
import os
import django

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phi.settings")
django.setup()

import pandas as pd

from odm2.models import Units
from odm2.models import CvUnitsType

path_to_file = "./odm2/load_cvs/cvs/units.csv"

df = pd.read_csv(path_to_file)

for i in range(len(df)):
    name = df["UnitsName"][i]
    if not Units.objects.filter(unitsname=name).exists():
        typeCV = CvUnitsType.objects.get(name=df["UnitsTypeCV"][i])
        abbreviation = df["UnitsAbbreviation"][i]

        link = df["UnitsLink"][i]

        obj = Units(unittypecv=typeCV, unitsabbreviation=abbreviation, unitsname=name, unitslink=link)
        obj.save()
    print('{:.2f}%'.format((i+1)/len(df)*100))
print("Done.")
