import hashlib
import os
 
def get_md5_small(file_path):
  md5 = None
  if os.path.isfile(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
  return md5
 
def get_md5_large(file_path):
  f = open(file_path,'rb')  
  md5_obj = hashlib.md5()
  while True:
    d = f.read(8096)
    if not d:
      break
    md5_obj.update(d)
  hash_code = md5_obj.hexdigest()
  f.close()
  md5 = str(hash_code).lower()
  return md5