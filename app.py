import gradio as gr
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


model_path = "./qa_weights"


model = AutoModelForQuestionAnswering.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)


qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)


def get_answer(question, context):
    if not question or not context:
        return "Please provide both a question and context."
    
    result = qa_pipeline(question=question, context=context)
    return result["answer"]



demo = gr.Interface(
    fn=get_answer,
    inputs=[
        gr.Textbox(label="Question", placeholder="Ask something..."),
        gr.Textbox(label="Context", lines=5, placeholder="Paste the text to search here...")
    ],
    outputs=gr.Textbox(label="Predicted Answer"),
    title="My LLM Question Answering Bot",
    description="QnA with context provided",
    flagging_mode="never"
)

if __name__ == "__main__":
    demo.launch()