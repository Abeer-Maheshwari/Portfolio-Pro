import gradio as gr
import ollama
from PIL import Image
import io

def analyze_chart(image):
    if image is None:
        return "Please upload a chart image to begin analysis."

    try:
        # Convert PIL image to bytes for Ollama
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_bytes = img_byte_arr.getvalue()

        # Professional technical analysis with LLaVA
        response = ollama.chat(
            model='llava:13b',  # Use 'llava:7b' for faster analysis if needed  
            messages=[{
                'role': 'user',
                'content': (
                    "You are an expert financial technical analyst specializing in stocks and cryptocurrencies.\n\n"
                    "Analyze this chart screenshot in extreme professional detail:\n"
                    "- Identify the asset/ticker symbol and time frame\n"
                    "- Determine the overall trend (bullish, bearish, or sideways/consolidation)\n"
                    "- Detect and describe key technical patterns (e.g., head and shoulders, triangles, flags, double top/bottom, channels)\n"
                    "- Identify major support and resistance levels with approximate prices\n"
                    "- Note all visible indicators (e.g., RSI, MACD, moving averages, volume, Bollinger Bands) and their current signals\n"
                    "- Assess momentum, volume trends, and potential reversal or continuation signals\n"
                    "- Provide an objective summary with risks, opportunities, and potential price targets\n\n"
                    "Structure your response clearly with bullet points for readability."
                ),
                'images': [img_bytes]
            }]
        )

        analysis = response['message']['content']
        return analysis

    except Exception as e:
        return f"Error during analysis: {str(e)}\n\n" \
               "Common fixes:\n" \
               "- Ensure Ollama is running (`ollama serve` in a terminal)\n" \
               "- Confirm the llava model is pulled (`ollama pull llava:13b` or `llava:7b`)\n" \
               "- For faster performance, try the 7B model"

# Gradio UI
with gr.Blocks(title="Stock & Crypto Chart Analyzer") as demo:
    gr.Markdown("**100% Local • Private • Powered by LLaVA (via Ollama)**\n"
                "Upload any chart screenshot → Get technical analysis instantly.")

    with gr.Row():
        with gr.Column(scale=1):
            input_img = gr.Image(label="Upload Chart Screenshot (TradingView, Yahoo Finance, Binance, etc.)", type="pil")
            btn = gr.Button("Analyze Chart", variant="primary")

        with gr.Column(scale=2):
            output_text = gr.Textbox(
                label="Expert Technical Analysis",
                lines=25,
                placeholder="Analysis will appear here...",
                interactive=False
            )
            copy_btn = gr.Button("Copy Analysis to Clipboard")
            copy_btn.click(
                None,
                inputs=output_text,
                js=" (text) => { navigator.clipboard.writeText(text); alert('Copied to clipboard!'); }"
            )

    btn.click(analyze_chart, inputs=input_img, outputs=output_text)

    gr.Markdown("""
    ### Tips for Best Results:
    - Use clear, high-resolution chart screenshots
    - Include visible indicators and price levels
    - Switch to `llava:7b` model for faster analysis
    
    This tool runs entirely on your machine.
    """)

demo.launch(share=True)  # Optional public link for demo/testing