s='''# MarkovedRyan100C
To gennerate rubbish sentences.
## Rubbish Of The Hour
- '''
import sys
sys.path.append('.')
print(sys.path)
import markov
Ryan100C=markov.model()
with open("Ryan100C_datas.txt",encoding='utf-8') as f:
    Ryan100C.train(f.readlines())
s+='- '.join([Ryan100C.run() for i in range(30)])
print(s)
with open("./README.md","w",encoding="utf-8") as f:
    f.write(s)
