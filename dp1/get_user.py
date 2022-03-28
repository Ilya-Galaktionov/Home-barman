from webapp.models import User

my_user = User.query.first()
print(f"""Имя: {my_user.name}
Email: {my_user.email}""")
