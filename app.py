from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de MySQL (WAMP - localhost)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/gamerstore_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos (coinciden con las tablas que creaste)
class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True)
    juego = db.Column(db.String(50))
    nombre = db.Column(db.String(100))
    texto = db.Column(db.Text)
    fecha = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Contacto(db.Model):
    __tablename__ = 'contactos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(120))
    mensaje = db.Column(db.Text)
    fecha = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Calificacion(db.Model):
    __tablename__ = 'calificaciones'
    id = db.Column(db.Integer, primary_key=True)
    juego = db.Column(db.String(50))
    valor = db.Column(db.Integer)  # 1 a 5

# RUTAS PRINCIPALES

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/masjugados')
def masjugados():
    return render_template('masjugados.html')

@app.route('/apisuerte')
def apisuerte():
    return render_template('apisuerte.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        mensaje = request.form.get('mensaje')
        
        if nombre and correo and mensaje:
            nuevo = Contacto(nombre=nombre, correo=correo, mensaje=mensaje)
            db.session.add(nuevo)
            db.session.commit()
    
    return render_template('contacto.html')

# =============================================
# RUTAS DE TODOS LOS JUEGOS (con comentarios y calificaciones)
# =============================================

@app.route('/dota', methods=['GET', 'POST'])
def dota():
    if request.method == 'POST':
        if 'nombre' in request.form and 'comentario' in request.form:
            nombre = request.form['nombre']
            texto = request.form['comentario']
            if nombre and texto:
                nuevo = Comentario(juego='dota', nombre=nombre, texto=texto)
                db.session.add(nuevo)
                db.session.commit()
        
        if 'calificacion' in request.form:
            valor = request.form.get('calificacion')
            print("Calificación RECIBIDA en dota:", valor)  # Debug
            if valor and valor.isdigit() and 1 <= int(valor) <= 5:
                nueva = Calificacion(juego='dota', valor=int(valor))
                db.session.add(nueva)
                db.session.commit()
                print("Calificación GUARDADA en dota con valor=", valor)
            else:
                print("Valor inválido en dota:", valor)
        
        return redirect(url_for('dota'))
    
    comentarios = Comentario.query.filter_by(juego='dota').order_by(Comentario.fecha.desc()).all()
    califs = Calificacion.query.filter_by(juego='dota').all()
    promedio = sum(c.valor for c in califs) / len(califs) if califs else 0
    total_votos = len(califs)
    
    return render_template('dota.html', comentarios=comentarios, promedio=round(promedio, 1), total_votos=total_votos)

@app.route('/minecraft', methods=['GET', 'POST'])
def minecraft():
    if request.method == 'POST':
        if 'nombre' in request.form and 'comentario' in request.form:
            nombre = request.form['nombre']
            texto = request.form['comentario']
            if nombre and texto:
                nuevo = Comentario(juego='minecraft', nombre=nombre, texto=texto)
                db.session.add(nuevo)
                db.session.commit()
        
        if 'calificacion' in request.form:
            valor = request.form.get('calificacion')
            print("Calificación RECIBIDA en minecraft:", valor)
            if valor and valor.isdigit() and 1 <= int(valor) <= 5:
                nueva = Calificacion(juego='minecraft', valor=int(valor))
                db.session.add(nueva)
                db.session.commit()
                print("Calificación GUARDADA en minecraft con valor=", valor)
            else:
                print("Valor inválido en minecraft:", valor)
        
        return redirect(url_for('minecraft'))
    
    comentarios = Comentario.query.filter_by(juego='minecraft').order_by(Comentario.fecha.desc()).all()
    califs = Calificacion.query.filter_by(juego='minecraft').all()
    promedio = sum(c.valor for c in califs) / len(califs) if califs else 0
    total_votos = len(califs)
    
    return render_template('minecraft.html', comentarios=comentarios, promedio=round(promedio, 1), total_votos=total_votos)

@app.route('/pou', methods=['GET', 'POST'])
def pou():
    if request.method == 'POST':
        if 'nombre' in request.form and 'comentario' in request.form:
            nombre = request.form['nombre']
            texto = request.form['comentario']
            if nombre and texto:
                nuevo = Comentario(juego='pou', nombre=nombre, texto=texto)
                db.session.add(nuevo)
                db.session.commit()
        
        if 'calificacion' in request.form:
            valor = request.form.get('calificacion')
            print("Calificación RECIBIDA en pou:", valor)
            if valor and valor.isdigit() and 1 <= int(valor) <= 5:
                nueva = Calificacion(juego='pou', valor=int(valor))
                db.session.add(nueva)
                db.session.commit()
                print("Calificación GUARDADA en pou con valor=", valor)
            else:
                print("Valor inválido en pou:", valor)
        
        return redirect(url_for('pou'))
    
    comentarios = Comentario.query.filter_by(juego='pou').order_by(Comentario.fecha.desc()).all()
    califs = Calificacion.query.filter_by(juego='pou').all()
    promedio = sum(c.valor for c in califs) / len(califs) if califs else 0
    total_votos = len(califs)
    
    return render_template('pou.html', comentarios=comentarios, promedio=round(promedio, 1), total_votos=total_votos)

@app.route('/left', methods=['GET', 'POST'])
def left():
    if request.method == 'POST':
        if 'nombre' in request.form and 'comentario' in request.form:
            nombre = request.form['nombre']
            texto = request.form['comentario']
            if nombre and texto:
                nuevo = Comentario(juego='left', nombre=nombre, texto=texto)
                db.session.add(nuevo)
                db.session.commit()
        
        if 'calificacion' in request.form:
            valor = request.form.get('calificacion')
            print("Calificación RECIBIDA en left:", valor)
            if valor and valor.isdigit() and 1 <= int(valor) <= 5:
                nueva = Calificacion(juego='left', valor=int(valor))
                db.session.add(nueva)
                db.session.commit()
                print("Calificación GUARDADA en left con valor=", valor)
            else:
                print("Valor inválido en left:", valor)
        
        return redirect(url_for('left'))
    
    comentarios = Comentario.query.filter_by(juego='left').order_by(Comentario.fecha.desc()).all()
    califs = Calificacion.query.filter_by(juego='left').all()
    promedio = sum(c.valor for c in califs) / len(califs) if califs else 0
    total_votos = len(califs)
    
    return render_template('left.html', comentarios=comentarios, promedio=round(promedio, 1), total_votos=total_votos)

@app.route('/fortnite', methods=['GET', 'POST'])
def fortnite():
    if request.method == 'POST':
        if 'nombre' in request.form and 'comentario' in request.form:
            nombre = request.form['nombre']
            texto = request.form['comentario']
            if nombre and texto:
                nuevo = Comentario(juego='fortnite', nombre=nombre, texto=texto)
                db.session.add(nuevo)
                db.session.commit()
        
        if 'calificacion' in request.form:
            valor = request.form.get('calificacion')
            print("Calificación RECIBIDA en fortnite:", valor)
            if valor and valor.isdigit() and 1 <= int(valor) <= 5:
                nueva = Calificacion(juego='fortnite', valor=int(valor))
                db.session.add(nueva)
                db.session.commit()
                print("Calificación GUARDADA en fortnite con valor=", valor)
            else:
                print("Valor inválido en fortnite:", valor)
        
        return redirect(url_for('fortnite'))
    
    comentarios = Comentario.query.filter_by(juego='fortnite').order_by(Comentario.fecha.desc()).all()
    califs = Calificacion.query.filter_by(juego='fortnite').all()
    promedio = sum(c.valor for c in califs) / len(califs) if califs else 0
    total_votos = len(califs)
    
    return render_template('fortnite.html', comentarios=comentarios, promedio=round(promedio, 1), total_votos=total_votos)

@app.route('/gta5', methods=['GET', 'POST'])
def gta5():
    if request.method == 'POST':
        if 'nombre' in request.form and 'comentario' in request.form:
            nombre = request.form['nombre']
            texto = request.form['comentario']
            if nombre and texto:
                nuevo = Comentario(juego='gta5', nombre=nombre, texto=texto)
                db.session.add(nuevo)
                db.session.commit()
        
        if 'calificacion' in request.form:
            valor = request.form.get('calificacion')
            print("Calificación RECIBIDA en gta5:", valor)
            if valor and valor.isdigit() and 1 <= int(valor) <= 5:
                nueva = Calificacion(juego='gta5', valor=int(valor))
                db.session.add(nueva)
                db.session.commit()
                print("Calificación GUARDADA en gta5 con valor=", valor)
            else:
                print("Valor inválido en gta5:", valor)
        
        return redirect(url_for('gta5'))
    
    comentarios = Comentario.query.filter_by(juego='gta5').order_by(Comentario.fecha.desc()).all()
    califs = Calificacion.query.filter_by(juego='gta5').all()
    promedio = sum(c.valor for c in califs) / len(califs) if califs else 0
    total_votos = len(califs)
    
    return render_template('gta5.html', comentarios=comentarios, promedio=round(promedio, 1), total_votos=total_votos)

if __name__ == '__main__':
    app.run(debug=True)