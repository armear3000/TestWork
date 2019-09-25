import os
import json

FileName = "Configuration.json"

InfoServer = "InfoServer"

File1 = {
    'Path': "file1.txt",
    'PathFtp': "..."
}

File2 = {
    'Path': "file2.txt",
    'PathFtp': "...2f"
}

Configuration = []
Configuration.append(InfoServer)
Configuration.append(File1)
Configuration.append(File2)

# сохранение конфигурации в JSON

MyFile = open(FileName,'w')

json.dump(Configuration,MyFile)

MyFile.close()

# загрузка конфигурации из JSON

MyFile = open(FileName,'r')

JsonDate = json.load(MyFile)

MyFile.close()

# копирования файлов на FTP

print("InfoServer: " + str(JsonDate[0]))

os.system('git init')

# os.system('git add ' + JsonDate[1]['Path'])
# os.system('git add ' + JsonDate[2]['Path'])
# os.system('git config --global user.name "marek"')
# os.system('git config --global user.email user@example.com')
# os.system('git commit -m "first commit"')
# os.system('git remote add origin https://github.com/armear3000/TestWork.git')
# os.system('git push -u origin master')