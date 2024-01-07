import subprocess
from subprocess import Popen, PIPE

process = Popen(['zip', '-r', '-', 'TestFolder'], stdout=PIPE, stderr=PIPE)
zipFile, output = process.communicate()

print(output)

with open('photos.zip', 'wb') as f:
    f.write(zipFile)
