from checksum import sha256
import os
from progressbar import progressbar

outputFile = 'output.txt'

if os.path.exists(outputFile):
    os.remove(outputFile)

# fileDirMain = input("Enter the main file directory: ")
# fileDirComp = input("Enter the comparing file directory: ")

fileDirMain = r'E:\Users\Public\Documents\BatchProcessingOutputMat'
fileDirComp = r'F:\BatchProcessingOutputMat'

mainList = os.listdir(fileDirMain)

for idx in progressbar(range(len(mainList)), redirect_stdout=True):
    fileName = mainList[idx]
    filePathMain = os.path.join(fileDirMain, fileName)
    filePathComp = os.path.join(fileDirComp, fileName)

    if os.path.exists(filePathComp):
        hashMain = sha256(filePathMain)
        hashComp = sha256(filePathComp)

        if hashMain != hashComp:
            print('Hash check failed for ', fileName)
            with open(outputFile, 'a') as fd:
                fd.write("Hash check failed for {}\n".format(fileName))
    else:
        # file did not exist error
        print("File did not exist in comp dir: ", fileName)
        with open(outputFile, 'a') as fd:
            fd.write("File did not exist in comp dir: ", fileName)

# hashStr = sha256(filename)
# print(hashStr)