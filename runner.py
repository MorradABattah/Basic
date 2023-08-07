from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import SubmitField
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/mydatabase'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random value

db = SQLAlchemy(app)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Document %r>' % self.filename

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired(), FileAllowed(app.config['ALLOWED_EXTENSIONS'], 'File type not allowed!')])
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_file = Document(filename=filename)
        db.session.add(new_file)
        db.session.commit()
        flash('File uploaded successfully!', 'success')
        return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/files')
def files():
    files = Document.query.all()
    file_links = [url_for('uploaded_file', filename=file.filename) for file in files]
    return '<br>'.join(file_links)

def run():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        app.run(debug=True)

if __name__ == '__main__':
    run()
