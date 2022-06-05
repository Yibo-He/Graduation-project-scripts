import re

if __name__ == "__main__":
    inputPath = "Duolingo2_droidbot_toller.txt"
    outputPath = "test2.txt"
    ui_hierarchy = []
    with open(inputPath, encoding="utf-8") as f:
        lists = f.readlines()
        r1 = "\[[0-9]+\]\[.*\"act_id\"\:.*\]"
        index = 0
        for line in lists:
            matchObj = re.match(r1, line, flags = 0)
            if(matchObj == None):
                index+=1
                continue
            
            matchObj = re.search("\"act_id\"\:\".+\"\,", line, flags=0)
            start, end = matchObj.span()
            act_id = line[start+9: end-1]
            ui_hierarchy.append((index, act_id))
            index += 1

    index_ui = 0
    i = 0
    ans = []
    with open(inputPath, encoding="utf-8") as f:
        lists = f.readlines()
        a,b = ui_hierarchy[index_ui]
        length = len(ui_hierarchy)
        for line in lists:
            r = "\[[0-9]+\]"
            matchObj = re.match(r, line , flags = 0)
            if(matchObj == None):
                i+=1
                continue
            start, end = matchObj.span()
            timeStamp = line[start:end]
            if(i<a):
                ans.append((timeStamp,b))
            if(i>=a):
                index_ui+=1
                if(index_ui<length): a,b = ui_hierarchy[index_ui]
                else: a,b = 0xfffffff, "\"Unknown\""
            i+=1
    
    with open(outputPath, mode='w',encoding='utf-8') as f:
        for timeStamp, act_id in ans:
            f.write(timeStamp+","+act_id+"\n")
    
        