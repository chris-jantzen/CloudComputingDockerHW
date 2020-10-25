from os import listdir
import socket
from functools import reduce

def main():
    # Get input files
    myPath = './home/data'
    fileNames = [f for f in listdir(myPath)]
    myFiles = ['{}/{}'.format(myPath, f) for f in fileNames]

    def getWordCount(text):
        return len(text.replace('\n', ' ').split())

    # Find Longest File
    wordMax = -1
    maxFile = ''
    totalWords = 0
    wordMapToFile = {}
    for i, n in zip(myFiles, fileNames):
        f = open(i, 'r')
        wordCount = getWordCount(f.read())
        totalWords += wordCount
        wordMapToFile[n] = wordCount
        if wordMax < wordCount:
            maxFile = i
            wordMax = wordCount
        f.close()

    # Find output file and prepare file names text
    outputFilePath = './home/output/' + listdir('./home/output')[0]
    fileNamesString = reduce(lambda acc, curr: acc + f'{curr} ({wordMapToFile[curr]} words), ', fileNames, '')[: -2]

    # Get IP Address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    local_ip_address = s.getsockname()[0]

    writeString = f'Files: {fileNamesString}\nTotal Words: {totalWords} in the {len(myFiles)} files.\nLongest File: {maxFile} with {wordMax} words.\nIP Address: {local_ip_address}'
    print(writeString)

    with open(outputFilePath, 'w') as f:
        f.write(writeString)
        f.close()

if __name__ == '__main__':
    main()
