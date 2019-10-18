import subprocess
import os
import zipfile


def subprocess_execute(cmd,print_info=True):
    ''' Function to use subprocess to execute a shell command and return outputs.
    '''
    if print_info:
        print('... cmd to execute:')
        print(cmd)
        print('... result:')
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (result, error) = process.communicate()
    rc = process.wait()
    if rc != 0:
        print("Error: failed to execute command:", cmd)
        print(error)
    return result.decode('utf-8')


def zipdir(path, zip_name='python.zip'):
    ''' Function to zip a folder.
    '''
    zipf = zipfile.ZipFile('python.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()