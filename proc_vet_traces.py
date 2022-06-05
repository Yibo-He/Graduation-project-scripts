import re
import os

input_dir = "D:/2021-2022下学期资料/毕设/src/VET-traces"
output_dir = "D:/2021-2022下学期资料/毕设/src/VET-logs"
'''
input_dir = "D:/2021-2022下学期资料/毕设/src/VET-traces"
output_dir = "D:/2021-2022下学期资料/毕设/src/VET-logs"
trace_name = "ape-accuweather-v1d2"
'''
def generate_log(input_dir, output_dir, trace_name):
    contents = []
    files = os.listdir(input_dir+"/"+trace_name)
    
    i = 1
    total = len(files)
    for f in files:
        filePath = input_dir+"/"+trace_name+"/"+str(f)
        fileName = os.path.basename(filePath).split('.')[0]
        fileType = os.path.splitext(filePath)[-1]
        if(fileType!=".json"):
            continue
        with open(filePath,"r",encoding="utf-8") as trace:
            for line in trace:
                matchObj = re.search("\"act_id\"\:\".+\"\,", line, flags=0)
                start, end = matchObj.span()
                act_id = line[start+9: end-1]
                contents.append((fileName,act_id))
        if(i%50==0):
            print("{}/{}".format(i,total))
        i+=1
    
    logPath = output_dir+"/"+trace_name+".txt"
    with open(logPath,"w",encoding="utf-8") as log:
        for a,b in contents:
            log.write("["+a+"],"+b+"\n")

if __name__ == "__main__":
    files = os.listdir(input_dir)
    for dir_ in files:
        trace_name = str(dir_)
        print(trace_name)
        generate_log(input_dir, output_dir, trace_name)
