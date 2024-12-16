from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import markdown

model = genai.GenerativeModel('gemini-pro')

# import os
# my_api_key_gemini = os.getenv('')

genai.configure(api_key='AIzaSyDBNOOLsgCP7QbUb_HQkhl9eMY2qG2A6XI')

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = f"As a therapist, please respond to the following concern: {prompt}. Be short, and listen more than talk."

            response = model.generate_content(question)

            if response.text:

                return markdown.markdown(response.text)
            else:
                return "Sorry, but I can't answer that!"
        except Exception as e:
            return "Sorry, but I can't answer that!"

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
