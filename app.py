import gradio as gr

from test_apps2_submodule.config import Config

print(Config.TEST_CONFIG)

def greet(name):
    return "Hello" + name + "!!"
    
iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
