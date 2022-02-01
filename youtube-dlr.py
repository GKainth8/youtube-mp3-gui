# import required modules
from __future__ import unicode_literals
import youtube_dl
import os
import kivy

from kivy.app import App

from kivy.uix.button import  Button

from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

class ClearApp(App):

    def build(self):

        self.box = BoxLayout(orientation='horizontal', spacing=20)

        self.txt = TextInput(hint_text='Write here', size_hint=(.5,.1))

        self.btn = Button(text='Clear All', on_press=self.clearText, size_hint=(.1,.1))

        self.box.add_widget(self.txt)

        self.box.add_widget(self.btn)

        return self.box

    def clearText(self, instance):

        self.txt.text = ''

ClearApp().run()


# class MyLogger(object):
#     def debug(self, msg):
#         pass
#
#     def warning(self, msg):
#         pass
#
#     def error(self, msg):
#         print(msg)
#
# # define progress hooks
# def my_hook(d):
# 	global flag
# 	if d['status'] == 'downloading':
# 		if(flag == 0):
# 			print('Source size: {0:.2f} MB' .format(d['total_bytes']/(1024*1024)))
# 			print('Downloading: ' + d['filename'])
# 			flag = 1
# 		print('File Progress: {0:.2f}%' .format(d['downloaded_bytes'] / d['total_bytes']*100), end='\r')
# 	if d['status'] == 'finished':
# 		flag = 0
# 		print('Done downloading, now converting ...')
# 		print()
#
# # read links.txt file
# fname = "links.txt"
# with open(fname) as f:
#     content = f.readlines()
#
# content = [x.strip() for x in content]
#
# # create download directory
# directory = '\download\\'
#
# if not os.path.exists(directory):
#     os.makedirs(directory)
#
# print("{0} file(s) queued for download" .format(len(content)))
#
# flag = 0
#
# # setup download configurations
# '''ydl_opts = {
# 	'outtmpl': '\download-vid\%(title)s-%(id)s.%(ext)s',
#     'format': 'bestvideo/best',
#
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
# }'''
#
# ydl_opts = {
# 	'outtmpl': '\download\%(title)s.%(ext)s',
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '320',
#     }],
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
# }
#
# # begin the download now
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(content)
#
# print("All Done!")
