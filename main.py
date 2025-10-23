import markov
Ryan100C=markov.🥵()
with open("Ryan100C_datas.txt",encoding='utf-8') as f:
    Ryan100C.train(f.readlines())
print("请欣赏马尔可夫梦话十句：")
for i in range(10):

    Ryan100C.run()
