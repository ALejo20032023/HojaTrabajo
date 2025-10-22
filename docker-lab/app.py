from flask import Flask, request
import psycopg2, os

app = Flask(__name__)

# Function to connect to PostgreSQL using environment variables
def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route('/')
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mensajes (id SERIAL PRIMARY KEY, texto VARCHAR(100));")
    conn.commit()
    cur.close()
    conn.close()
    return "App connected to PostgreSQL "

@app.route('/add', methods=['POST'])
def add():
    texto = request.args.get('texto', 'Sin mensaje')
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO mensajes (texto) VALUES (%s);", (texto,))
    conn.commit()
    cur.close()
    conn.close()
    return f"Message added: {texto}"

@app.route('/list')
def list_msg():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mensajes;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return {'mensajes': rows}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
