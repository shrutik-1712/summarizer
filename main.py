import click
import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2:0.5b"

def summarize_text(text):
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    
    response = requests.post(OLLAMA_API_URL, json=payload)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        return result['response'].strip()
    else:
        return f"Error: Unable to generate summary. Status code: {response.status_code}"

@click.command()
@click.option('--file', '-f', type=click.File('r'), help='Input text file')
@click.option('--text', '-t', help='Input text')
def main(file, text):
    """Summarize text from a file or direct input using Ollama API with Qwen2 0.5B model."""
    """
    
    python main.py -f input.txt




    python main.py --text "Your long text goes here..."
    
    """
    if file:
        content = file.read()
    elif text:
        content = text
    else:
        click.echo("Error: Please provide either a file or text input.")
        return
    
    summary = summarize_text(content)
    
    
    file = open("myfile.txt","w")
    file.write("Summarize:\n \n")
    file.writelines(summary)
    file.close()

    click.echo(summary)

if __name__ == '__main__':
    main()