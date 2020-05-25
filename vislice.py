import bottle
import model

ID_IGRE_COOKIE_NAME = "id_igre"
COOKIE_SECRET = "my_very_special - secret key and passphrase"

vislice = model.Vislice()
vislice.preberi_iz_datoteke()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('datoteke/views/index.tpl')

@bottle.post('/nova_igra/') #naredimo novo igro
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.response.set_cookie(
        "id_igre", str(id_nove_igre), path="/",
        secret=COOKIE_SECRET
    )
    bottle.redirect(f"/igra/")
    # ali bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/igra/') #cloveku pokazemo igro za igrat
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('datoteke/views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    # dobim crko
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/')
    # ali bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='datoteke/img')

bottle.run(reloader=True, debug=True) 
# reloader=True da zato ko kaj spremenimo v datotekah da ne rabmo na novo pognat programa
# debug=True da vidmo ko pride do napak

