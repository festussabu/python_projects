'''
From: /home/festus/Documents/Downloads

To: /home/festus/newFolder/

documents, pictures, videos
'''

import os
import shutil
import time

src_folder = '/home/festus/Documents/Downloads'
dst_images  = '/home/festus/newFolder/pictures'
dst_videos  = '/home/festus/newFolder/videos'
dst_documents  = '/home/festus/newFolder/documents'
dst_others  = '/home/festus/newFolder/ubuntufiles'


def separate_files(images, videos, documents, ubuntu_files):
  for files in os.listdir(src_folder):
    time.sleep(1)
    
    path_file = os.path.join(src_folder, files)
    
    if os.path.isfile(path_file):
      
      if path_file.endswith(tuple(images)):
        shutil.move(path_file, dst_images)
      elif path_file.endswith(tuple(videos)):
        shutil.move(path_file, dst_videos)
      elif path_file.endswith(tuple(documents)):
        shutil.move(path_file, dst_documents)  
      elif path_file.endswith(tuple(ubuntu_files)):
       shutil.move(path_file, dst_others)     
  print('finished')

def files_type():
  images = [
    '.jpg', '.jpeg', '.png'
  ]
  videos = [
    '.mp4'
  ]
  documents = [
    '.odt', '.pdf', '.csv', '.docx', '.pptx'
  ]
  ubuntu_files = [
    '.deb'
  ]

  return images, videos, documents, ubuntu_files


images, videos, documents, ubuntu_files = files_type()
separate_files(images, videos, documents, ubuntu_files)
