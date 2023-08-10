import gradio as gr
import time

def greet(name):
    return "Hello " + name + "!!"
    
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
time.sleep(60)
iface.launch()

