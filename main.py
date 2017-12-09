# most of this code was copied from https://www.youtube.com/watch?v=-7YH6rdR-tk
import os
from oauth2client import file, client

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets('client_secrets.json', scope=SCOPES)
  cred = tools.run_flow(flow, store, flags) if flags else tools.run(flow,store)

DRIVE = build('drive','v3',http=creds.authorize(Http()))

for filename in os.listdir('/home/erich/Documents/Drive/'):
  metadata = {'name': filename}
  res = DRIVE.files().create(body=metadata, media_body=filename).execute()
  print(res)