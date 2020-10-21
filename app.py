from os import listdir
from functools import reduce

def main():
    myPath = './home/data'
    fileNames = [f for f in listdir(myPath)]
    myFiles = ['{}/{}'.format(myPath, f) for f in fileNames]

    def getWordCount(text):
        return len(text.replace('\n', ' ').split())

    wordMax = -1
    maxFile = ''
    for i in myFiles:
        f = open(i, 'r')
        wordCount = getWordCount(f.read())
        if wordMax < wordCount:
            maxFile = i
            wordMax = wordCount
        f.close()

    print('Longest file:', maxFile)

    outputFile = './home/output/' + listdir('./home/output')[0]
    fileNamesString = reduce(lambda acc, curr: acc + f'{curr}, ', fileNames, '')[: -2]
    print(fileNamesString)
    with open(outputFile, 'w') as f:
        f.write(f'Files: {fileNamesString}\nLongest file: {maxFile} with {wordMax} words.')
        f.close()

if __name__ == '__main__':
    main()
