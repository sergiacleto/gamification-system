from flask import Flask, jsonify
from user import User
from badge import Badge
from leaderboard import Leaderboard

app = Flask(__name__)

# Criando usuários
user1 = User("Alice")
user2 = User("Bob")
user3 = User("Charlie")

# Criando badges
badge1 = Badge("Iniciante", "Completou o primeiro curso")
badge2 = Badge("Avançado", "Completou cinco cursos")

# Adicionando pontos e badges aos usuários
user1.add_points(100)
user1.add_badge(badge1.name)

user2.add_points(150)
user2.add_badge(badge1.name)
user2.add_badge(badge2.name)

user3.add_points(200)

# Criando e populando o leaderboard
leaderboard = Leaderboard()
leaderboard.add_user(user1)
leaderboard.add_user(user2)
leaderboard.add_user(user3)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    top_users = leaderboard.get_top_users()
    return jsonify([{'name': user.name, 'points': user.points, 'badges': user.badges} for user in top_users])

if __name__ == '__main__':
    app.run(debug=True)
