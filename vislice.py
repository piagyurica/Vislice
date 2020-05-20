import bottle
import model

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('datoteke/views/index.tpl')

@bottle.post('/igra/') #naredimo novo igro
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.redirect(f"/igra/{id_nove_igre}/")
    # ali bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/igra/<id_igre:int>/') #cloveku pokazemo igro za igrat
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]
    return bottle.template('datoteke/views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    # dobim crko
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f'/igra/{id_igre}/')
    # ali bottle.redirect('/igra/{}/'.format(id_igre))

@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='datoteke/img')

bottle.run(reloader=True, debug=True) 
# reloader=True da zato ko kaj spremenimo v datotekah da ne rabmo na novo pognat programa
# debug=True da vidmo ko pride do napak

