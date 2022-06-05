import os

log_dir = "D:\\2021-2022下学期资料\毕设\src\VET-logs"
commands_dir = "D:/2021-2022下学期资料/毕设/src/commands"
output_dir = "D:\\2021-2022下学期资料\毕设\src\STMs"

if __name__ == "__main__":
    files = os.listdir("D:/2021-2022下学期资料/毕设/src/VET-logs")

    '''
    Ktail
    '''
    with open(commands_dir+"/Ktail.txt","w",encoding="utf-8") as f:
        for dir_ in files:
            log_name = str(dir_).split('.')[0]
            command_1 = "-r \"^\[(?<DTIME>[0-9]+)\]\,\\\"(?<TYPE>.+)\\\"$\" -d D:\Graphviz\\bin\dot -o "+output_dir+"\\"+log_name+"_Ktail1 --kTailsK=1 --outputProbLabels=true --outputCountLabels=true  "+ log_dir+"\\"+log_name+".txt"
            command_2 = "-r \"^\[(?<DTIME>[0-9]+)\]\,\\\"(?<TYPE>.+)\\\"$\" -d D:\Graphviz\\bin\dot -o "+output_dir+"\\"+log_name+"_Ktail2 --kTailsK=2 --outputProbLabels=true --outputCountLabels=true  "+ log_dir+"\\"+log_name+".txt"
            f.write(command_1+'\n')
            f.write(command_2+'\n')
    
    with open(commands_dir+"/Synoptic.txt","w",encoding="utf-8") as f:
        for dir_ in files:
            log_name = str(dir_).split('.')[0]
            command_3 = "-r \"^\[(?<DTIME>[0-9]+)\]\,\\\"(?<TYPE>.+)\\\"$\" -d D:\Graphviz\\bin\dot -o "+output_dir+"\\"+log_name+"_Synoptic --outputProbLabels=true --outputCountLabels=true  "+ log_dir+"\\"+log_name+".txt"
            f.write(command_3+'\n')