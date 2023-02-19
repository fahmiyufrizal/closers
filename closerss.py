# CLO simple launcher
# by fahmiyufrizal@2023

import os
import subprocess
from os import path
from sys import exit
import asyncio
import webbrowser

#protection
if not path.exists (CLOFN):
	print(" [x] Don't change filename!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()
if not path.exists (CLOLN):
	print(" [x] Launcher.exe not found, Place inside Closers folder!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()
if not path.exists (CLOLN_game):
	print(" [x] Complete the Installation first!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()

#window_init
os.system('title ' + titlewindow)
print(" ")
print("      Closers Global Netcafe Launcher       ")
print("              " + version)
print("        by fahmiyufrizal@2023        ")
print(" ")
print("[+] Initializing....")
print("[+] Importing module & config...")

#launch-in-webbrowser
print('[+] Redirecting you to Closers Website. After sign in, click "GAME START" to launch launcher....')
async def display():
	await asyncio.sleep(5)
asyncio.run(display())
webbrowser.open(url_closers)