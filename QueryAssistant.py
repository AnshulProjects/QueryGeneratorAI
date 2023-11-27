import gradio as gr
import QueryGenerator
import os

'''
Demo Front end using Gradio
'''
with gr.Blocks() as demo:
    user_query = gr.Textbox(label="What to query")
    schema = gr.Textbox(label="Schema")
    context = gr.Textbox(label="Context", info = "Be as specfifc as possibe for the most accurate results")
    language = gr.Textbox(label="Language")
    greet_btn = gr.Button("Get query")
    
    api_key = open("API_KEY.txt" , "r")

    generator = QueryGenerator.QueryGenerator(api_key.read())
    api_key.close()
    greet_btn.click(fn= generator.query, inputs=[user_query,[schema],context,language], outputs=gr.Label(label="Query"), api_name="greet")
    
demo.launch()