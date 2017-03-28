import pandas as pd

df = pd.read_csv('train.csv')
cols = df.columns.tolist()
fr = open('summary.csv','w')
fr.write('feature,type,expectations,comments')
fr.write('\n')

for col in cols:
	feat = col
	tpe = str(df[col].dtype)
	expect = raw_input("column is: {}\n".format(col))
	comnt = raw_input("comments about it\n")
	fr.write(feat+","+tpe+","+expect+","+comnt)
	fr.write("\n")
fr.close()