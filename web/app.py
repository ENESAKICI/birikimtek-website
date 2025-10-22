from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from forms import ContactForm
from utils import init_db, SessionLocal
from models import ContactMessage

app = Flask(__name__)
app.config.from_object(Config)

# DB initialize
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    # Örnek hizmet listesi (isteğe göre dinamikleştirilebilir)
    services = [
        {
            'title': 'Endüstriyel Görüntü İşleme',
            'desc': 'Üretim hattı kusur tespit sistemleri, otomatik kalite kontrol.'
        },
        {
            'title': 'Malzeme Mikroyapı Analizi',
            'desc': 'Metalürji görüntülerinden faz tespiti, otomatik sınıflandırma.'
        },
        {
            'title': 'Ölçümlere Dayalı Optimizasyon',
            'desc': 'Makine verileri ile süreç optimizasyonu ve kestirimci bakım.'
        }
    ]
    return render_template('services.html', services=services)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        data = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            company=form.company.data,
            message=form.message.data
        )
        db = SessionLocal()
        db.add(data)
        db.commit()
        db.close()
        flash('Mesajınız alındı. Teşekkürler!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)

@app.route('/admin')
def admin():
    # Basit yönetici görünümü — prod ortamda kimlik doğrulama ekleyin
    db = SessionLocal()
    messages = db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()
    db.close()
    return render_template('admin.html', messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
