import graphviz
from parse import parse
import re
import operator
import os

input_dir = "D:/2021-2022下学期资料/毕设/src/STMs"
output_dir = "D:/2021-2022下学期资料/毕设/src/STMs_color"
r_edge = "[\s|\t]*[0-9]+->[0-9]+ \[label=\".+\".*\]\;"
r_node = "[\s|\t]*[0-9]+ \[label=\".+\".*\]\;"

def highlight(filename, hNum):
    nodes = []
    edges = []
    with open(input_dir+'/'+filename+'.dot', "r", encoding="utf-8") as f_in:
        lines = f_in.readlines()
        for item in lines:
            tmp = parse("  {id} [label={label}];\n",item)
            if(tmp!=None): 
                result = {}
                result['id'] = tmp['id']
                result['label'] = tmp['label']
                nodes.append(result)
                continue
            tmp2 = parse("{start}->{end} [label=\"P: {P}, Cnt: {Cnt}\"];\n",item)
            if(tmp2!=None): 
                result = {}
                result['start'] = tmp2['start']
                result['end'] = tmp2['end']
                result['P'] = tmp2['P']
                result['Cnt'] = tmp2['Cnt']
                edges.append(result)
                continue
        edges.sort( key=(lambda result:int(result['Cnt'])), reverse=True)
    
    #统计各个点的入度
    inDegree = {}
    for item in nodes:
        inDegree[item['id']] = 0
    for item in edges:
        inDegree[item['end']] += int(item['Cnt'])
    inDegree = dict( sorted(inDegree.items(), key = lambda item:item[1], reverse=True) )
    
    x = 0
    top3 = 0
    for value in inDegree.values():
        if(x==0): print("Top1: {}".format(value))
        top3 += value
        x+=1
        if(x>=3 or x>=len(inDegree)-2):break
        
    print("Top3: {}".format(top3))
    print("")
    
    '''
    with open(output_dir+'/'+filename+'.dot', "w", encoding="utf-8") as f_out:
        f_out.write("digraph G {\n")
        #写入节点
        i = 0
        hNode = min(len(inDegree), hNum)
        for item in inDegree:
            #get label
            label = ''
            for node in nodes:
                if(node['id'] == item):
                    label = node['label']
                    break
            if("TERMINAL" in label):
                f_out.write("  {} [label={}];\n".format(item,label))
                i+=1
                continue
            if("INITIAL" in label):
                f_out.write("  {} [label={}];\n".format(item,label))
                i+=1
                continue
            if(i<hNode):
                f_out.write("  {} [label=\"{}\"".format(item,label[1:-1]+",Cnt:{}".format(inDegree[item]))+", fillcolor=\"cyan:yellow\", style=\"filled\"];\n")
            else:
                f_out.write("  {} [label=\"{}\"];\n".format(item,label[1:-1]+",Cnt:{}".format(inDegree[item])))
            i+=1
        
        #写入边
        i = 0
        hEdge = min(len(edges), hNum)
        for item in edges:
            if(i<hEdge):
                f_out.write("{}->{} [label=\"P: {}, Cnt: {}\"".format(item['start'], item['end'], item['P'], item['Cnt'])+", color=\"crimson\", penwidth=4];\n" )
            else:
                f_out.write("{}->{} [label=\"P: {}, Cnt: {}\"];\n".format(item['start'], item['end'], item['P'], item['Cnt']))
            i+=1
        
        f_out.write("}\n")
        '''

if __name__ == "__main__":
    files = os.listdir(input_dir)
    
    #highlight("ape-accuweather-1_Ktail2", 3)

    for fileName in files:
        lists = fileName.split('.')
        if(len(lists)>=3): continue
        trace_name = lists[0]
        print(trace_name+":")

        highlight(trace_name, 3)
        
        '''
        with open(output_dir + "/"+trace_name+".dot", "r", encoding="utf-8") as f:
            dot_graph = f.read()
            dot = graphviz.Source(dot_graph)
            dot.render(output_dir + "/"+trace_name)
        '''
