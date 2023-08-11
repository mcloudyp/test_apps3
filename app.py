"""
import gradio as gr
import time

def greet(name):
    return "Hello " + name + "!!"
    
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
time.sleep(60)
iface.launch()
"""
import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone https://github.com/mcloudyp/test_apps3 /home/xlab-app-center/test_apps3")
os.chdir(f"/home/xlab-app-center/test_apps3")
os.system(f"python index.py")
