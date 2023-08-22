from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


# Forma para el Sign up de usuarios
class SignUpForm(FlaskForm):
    username = StringField("Nombre de Usuario: ", validators=[DataRequired(), Length(min=4, max=12)])
    email = EmailField("Correo Electrónico: ", validators=[DataRequired()])
    password = PasswordField(" Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    password2 = PasswordField("Confirma la Contraseña: ", validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Sign up")

    def validate(self, extra_validators=None):
        if not super().validate():
            return False

        if self.password.data != self.password2.data:
            self.password2.errors.append("Las contraseñas deben coincidir.")
            return False

        return True
    

# Forma para el Log in de usuarios
class LoginForm(FlaskForm):
    username_or_email = StringField('Usuario o Email', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Log in')