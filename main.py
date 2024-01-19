from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'
tasks_list = []


class ToDo(FlaskForm):
    tasks = StringField('what to do', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/", methods=["POST", "GET"])
def home():
    form = ToDo()
    if form.validate_on_submit():
        task = form.tasks.data
        tasks_list.append(task)
        return redirect(url_for('home'))
    return render_template('index.html', form=form, tasks=tasks_list)


if __name__ == "__main__":
    app.run(debug=True)
