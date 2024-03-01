from flask import Flask, render_template
import pandas as pd
import markdown

app = Flask(__name__)

def read_excel():
    df = pd.read_excel("./fakedb/Publications example v7.0 29Nov23.xlsx")
    # Assuming 'abstract' column contains Markdown content
    df['abstract'] = df['abstract'].astype(str).apply(lambda x: markdown.markdown(x)).apply(lambda x: x.replace('\n', '<br>'))
    return df


@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/table')
def show_table():
    dataframe = read_excel()
    return render_template('table_view.html', dataframe=dataframe)

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0", port=5001)

