from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField

class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)
        return redirect(url_for('index'))
    return render_template('index.html')