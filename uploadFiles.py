import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        
    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root,fileName)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = 'sl.BLsZXnz9a0q7zHLXL7KV9b0xR2LREm6ch-9zq_r-RQR6DhH3DNdKb9rBxoRf2nZronhfmqrQlR5CUpZJanJ2l52F00FbPTt3zt0quZd9xAirFxcp6DMtUa_uPWqT_ZRxuMZ4T7DJ'
    transferData = TransferData(access_token)

    file_from = 'D:/KANAV/python/p101'
    file_to = '/CloudsBringRain' 
    # API v2
    transferData.uploadFile(file_from, file_to)
    print('file has been moved')
if __name__ == '__main__':
    main()