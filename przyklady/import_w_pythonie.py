from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))
print(sys.path)



import cos1
import cos1 as c1

from cos1 import funkcja