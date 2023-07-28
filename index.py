import gradio as gr
import os

def greet(name):
    return "Hello " + name + "!!"
    
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

