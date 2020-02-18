import os, sys
import pandas as pd

filename = sys.argv[0]
cwd = os.path.abspath(filename+"/..")


print(cwd)
veritas3 = pd.read_csv(cwd+"/datasets/datasetVeritas3.csv")

print(len(veritas3))
