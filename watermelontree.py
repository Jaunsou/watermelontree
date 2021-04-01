import tree
import treeplotter
import json

fr = open('watermalon.txt','rb')

listWm = [inst.decode().strip().split('\t') for inst in fr.readlines()]
labels = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
Trees = tree.createTree(listWm, labels)

print(json.dumps(Trees,ensure_ascii=False))

# 测试算法

labels = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感']
testData = ['浅白', '蜷缩', '浊响', '稍糊', '凹陷', '硬滑']
testClass = tree.classify(Trees, labels, testData)
print(json.dumps(testClass, ensure_ascii=False))
treeplotter.createPlot(Trees)
