import maths
print(maths.topla(10,20))

#alias
import maths as m
print(m.topla(10,20))

#pythondaki hazır modüller (built in)
import random
print(random.randint(0,100))

#modüllerin belli kısımlarını import etmek
from maths import topla as toplamaIslemi
print(toplamaIslemi(10,20))

import classes
human1 =Human("Zeynep")
human1.talk("Selam!")