# -*- coding: utf-8 -*-
import io, re
P = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/Hotel Barahona 72/site/index.html"
s = io.open(P, encoding="utf-8").read()
orig = s

PERSON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0"/></svg>'
SIZE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 3H5a2 2 0 0 0-2 2v3M16 3h3a2 2 0 0 1 2 2v3M8 21H5a2 2 0 0 1-2-2v-3M16 21h3a2 2 0 0 0 2-2v-3"/></svg>'
AC='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9.5 19A2.5 2.5 0 1 1 7 16.5H22M14 5A2.5 2.5 0 1 1 16.5 7.5H2M19 13a2.5 2.5 0 1 1 2.5 2.5H2"/></svg>'
BED1='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 9V7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v2M2 17v-4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4M2 17h20"/></svg>'
BED2='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 9V7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v2M2 17v-4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4M2 17h20M9 11V6M15 11V6"/></svg>'
FAMICO='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2"/><path d="M3 20a6 6 0 0 1 12 0M14 20a5 5 0 0 1 7-4"/></svg>'
EXP='<span class="cnt"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>Ver fotos</span>'

def m(label): return "Hola,%20quiero%20reservar%20la%20"+label+"%20en%20Hotel%20Barahona%2072"

def room(dataf, img, w, h, name, tag, meta_items, amen, price, ref, waname):
    tagh = ('<span class="rtag">%s</span>'%tag) if tag else ''
    metah = ''.join('<span>%s%s</span>'%(ic,txt) for ic,txt in meta_items)
    amenh = ''.join('<li>%s</li>'%a for a in amen)
    return ('''      <article class="room reveal" data-f="%s">
        <button class="rimg zoomable" data-group="rooms" data-full="./img/%s" data-cap="%s" aria-label="Ampliar foto de %s"><img src="./img/%s" width="%d" height="%d" loading="lazy" alt="%s del Hotel Barahona 72">%s</button>
        <div class="rinfo">
          %s<h3>%s</h3>
          <div class="rmeta">%s</div>
          <ul class="ramen">%s</ul>
          <a class="rdet zoomable" data-group="rooms" data-full="./img/%s" data-cap="%s">Ver fotos de la habitacion</a>
        </div>
        <div class="rbuy"><div class="pr"><span class="from">Desde</span>%s <small>COP/noche</small></div><div class="ref">%s</div><a class="btn btn-gold" href="https://wa.me/573503189890?text=%s">Reservar</a></div>
      </article>
'''%(dataf, img, name, name, img, w, h, name, EXP, (tagh+"\n          " if tagh else ""), name, metah, amenh, img, name, price, ref, m(waname)))

rooms_html = "".join([
 room("d2","room-doble.webp",1400,933,"Habitacion Doble","Mas reservada",
      [(PERSON,"1-2 personas"),(SIZE,"20 m&sup2;"),(AC,"Aire acond.")],
      ["Desayuno incluido","WiFi gratis","Bano privado","Television","Agua caliente","Toallas y amenities"],
      "$118.000","Desayuno incluido","Habitacion%20Doble"),
 room("d2","room-doble-2.webp",1400,933,"Habitacion Twin",None,
      [(PERSON,"1-2 personas"),(SIZE,"20 m&sup2;"),(BED2,"2 camas")],
      ["Desayuno incluido","WiFi gratis","Aire acondicionado","Bano privado","Escritorio","Television"],
      "$130.000","Desayuno incluido","Habitacion%20Twin"),
 room("d2","barahona-22.webp",1600,1067,"Habitacion Junior Suite","Mas espacio",
      [(PERSON,"1-2 personas"),(BED1,"Cama amplia"),(AC,"Aire acond.")],
      ["Desayuno incluido","WiFi gratis","Bano privado","Television","Escritorio","Habitacion amplia"],
      "$153.000","Desayuno incluido","Habitacion%20Junior%20Suite"),
 room("d3","room-triple.webp",1400,933,"Habitacion Triple",None,
      [(PERSON,"1-3 personas"),(SIZE,"22 m&sup2;"),(BED2,"3 camas")],
      ["Desayuno incluido","WiFi gratis","Aire acondicionado","Bano privado","Television","Ideal grupos"],
      "$159.000","Desayuno incluido","Habitacion%20Triple"),
 room("d4","room-cuadruple.webp",1400,933,"Habitacion Cuadruple","Familiar",
      [(PERSON,"1-4 personas"),(SIZE,"24 m&sup2;"),(BED2,"4 camas")],
      ["Desayuno incluido","WiFi gratis","Aire acondicionado","Bano privado","Television","Ideal familias"],
      "$165.000","Desayuno incluido","Habitacion%20Cuadruple"),
])

note_html = ('<p class="note">Tarifas "desde" por noche en pesos colombianos (COP), con desayuno incluido, sujetas a '
 'disponibilidad y temporada. Los ninos son gratis hasta los 4 anos (pagan desayuno $12.000). Check-in 3:00 p.m. '
 '/ Check-out 12:00 m. Confirma tu tarifa final por WhatsApp.</p>')

# ---- chips (regex) ----
chips_new = ('''    <div class="rfilters reveal d1">
      <button class="chip active" data-f="all">%s Todas <span class="c">(5)</span></button>
      <button class="chip" data-f="d2">%s 1-2 personas <span class="c">(3)</span></button>
      <button class="chip" data-f="d3">%s 3 personas <span class="c">(1)</span></button>
      <button class="chip" data-f="d4">%s Familiar <span class="c">(1)</span></button>
    </div>'''%(BED1,PERSON,BED2,FAMICO))
s2, n = re.subn(r'<div class="rfilters reveal d1">.*?</div>', chips_new, s, count=1, flags=re.S)
assert n==1, "chips"; s=s2

# ---- rlist + note (regex from rlist open to note close) ----
rlist_new = '<div class="rlist" id="rlist">\n'+rooms_html+'    </div>\n    '+note_html
s2, n = re.subn(r'<div class="rlist" id="rlist">.*?<p class="note">.*?</p>', rlist_new, s, count=1, flags=re.S)
assert n==1, "rlist"; s=s2

# ---- gallery: add 2 real room photos after Comedor ----
COMEDOR='<figure class="gslide zoomable" data-group="gal" data-full="./img/barahona-05.webp" data-cap="Comedor"><img src="./img/barahona-05.webp" width="1067" height="800" loading="lazy" alt="Comedor del Hotel Barahona 72"><figcaption>Comedor</figcaption></figure>'
GAL_ADD=('\n        <figure class="gslide zoomable" data-group="gal" data-full="./img/room-doble.webp" data-cap="Habitacion Doble"><img src="./img/room-doble.webp" width="1400" height="933" loading="lazy" alt="Habitacion Doble del Hotel Barahona 72"><figcaption>Doble</figcaption></figure>'
 '\n        <figure class="gslide zoomable" data-group="gal" data-full="./img/room-cuadruple.webp" data-cap="Habitacion Cuadruple"><img src="./img/room-cuadruple.webp" width="1400" height="933" loading="lazy" alt="Habitacion Cuadruple del Hotel Barahona 72"><figcaption>Cuadruple</figcaption></figure>')
assert s.count(COMEDOR)==1, "comedor"; s=s.replace(COMEDOR, COMEDOR+GAL_ADD, 1)

# ---- resenas: replace bars with Ayenda badge + dims ----
BARS='''        <div class="bars">
          <div class="br"><span>5 estrellas</span><div class="bg"><div class="fl" style="width:46%"></div></div></div>
          <div class="br"><span>4 estrellas</span><div class="bg"><div class="fl" style="width:30%"></div></div></div>
          <div class="br"><span>3 estrellas</span><div class="bg"><div class="fl" style="width:14%"></div></div></div>
          <div class="br"><span>2 estrellas</span><div class="bg"><div class="fl" style="width:5%"></div></div></div>
          <div class="br"><span>1 estrella</span><div class="bg"><div class="fl" style="width:5%"></div></div></div>
        </div>'''
BADGE='''        <div class="ayb"><span class="n">8.2</span><span class="t">Excelente<br><em>en Ayenda</em></span></div>
        <div class="dims"><span>Aseo</span><span>Wifi</span><span>Amenidades</span><span>Experiencia</span><span>Television</span></div>'''
assert s.count(BARS)==1, "bars"; s=s.replace(BARS,BADGE,1)

# ---- resenas: real verified quotes ----
MIDOLD='''      <div class="reveal d1">
        <p class="quote"><span class="dc">"</span>Buena ubicacion sobre la 72, habitaciones limpias y personal muy atento. Excelente relacion precio para quedarse en el centro de Barranquilla.</p>
        <div class="themes"><span>Ubicacion sobre la 72</span><span>Atencion del personal</span><span>Limpieza</span><span>Buen precio</span><span>Desayuno</span></div>
        <div style="margin-top:26px"><a class="btn btn-line" href="https://maps.app.goo.gl/HnyXTPqc7Nxtx7meA" target="_blank" rel="noopener">Ver reseñas en Google</a></div>
        <p class="note">La calificacion 4.1 y las 430 reseñas son reales de Google; la distribucion por estrellas y la cita son ilustrativas.</p>
      </div>'''
MIDNEW='''      <div class="reveal d1">
        <div class="rq">
          <p class="quote"><span class="dc">"</span>La senora es muy hospitalaria, super amable y te ayuda. Excelente servicio de aseo.</p>
          <div class="who">Marcela Rengifo<span>Huesped verificada &middot; Ayenda</span></div>
        </div>
        <div class="rq2">
          <p>"La atencion y la amplitud de la habitacion."</p>
          <div class="who">Freddy Alfonso<span>Huesped verificado &middot; Ayenda</span></div>
        </div>
        <div class="themes"><span>Hospitalidad</span><span>Amplitud de la habitacion</span><span>Aseo</span><span>Atencion</span><span>Ubicacion en la 72</span></div>
        <div style="margin-top:24px;display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-line" href="https://maps.app.goo.gl/HnyXTPqc7Nxtx7meA" target="_blank" rel="noopener">Ver en Google</a><a class="btn btn-line" href="https://ayenda.com/co/hoteles/barranquilla/ayenda-1313-barahona-72" target="_blank" rel="noopener">Ver en Ayenda</a></div>
        <p class="note">Calificaciones reales: 4.1/5 en Google (430 reseñas) y 8.2 "Excelente" en Ayenda. Testimonios de huespedes verificados en Ayenda.</p>
      </div>'''
assert s.count(MIDOLD)==1, "mid"; s=s.replace(MIDOLD,MIDNEW,1)

# ---- footer: add FAQ link ----
FOOT='<div><h4>El hotel</h4><a href="#habitaciones">Habitaciones</a><a href="#servicios">Servicios</a><a href="#ubicacion">Ubicacion</a><a href="#resenas">Reseñas</a></div>'
FOOTN='<div><h4>El hotel</h4><a href="#habitaciones">Habitaciones</a><a href="#servicios">Servicios</a><a href="#ubicacion">Ubicacion</a><a href="#resenas">Reseñas</a><a href="#faq">Preguntas frecuentes</a></div>'
assert s.count(FOOT)==1,"foot"; s=s.replace(FOOT,FOOTN,1)

# ---- CSS additions ----
CSSANCHOR='.rev::before{background-image:url(./img/hotel-hq.webp);opacity:.34}'
CSSADD='''
.rev .ayb{display:inline-flex;align-items:center;gap:13px;margin-top:22px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:11px 18px;box-shadow:var(--sh1)}
.rev .ayb .n{font-family:var(--serif);font-size:34px;color:var(--green);line-height:1}
.rev .ayb .t{font-size:12.5px;color:var(--ink-2);font-weight:700;line-height:1.2}.rev .ayb .t em{color:var(--muted);font-weight:500;font-style:normal}
.rev .dims{display:flex;flex-wrap:wrap;gap:7px;margin-top:16px;max-width:320px}
.rev .dims span{font-size:11.5px;color:var(--muted);border:1px solid var(--line);border-radius:100px;padding:5px 11px;background:var(--card)}
.rev .rq .who,.rev .rq2 .who{margin-top:12px;font-family:var(--sans);font-weight:700;font-size:14px;color:var(--ink)}
.rev .who span{display:block;font-weight:500;font-size:12px;color:var(--muted);margin-top:1px}
.rev .rq2{margin-top:22px;padding-top:22px;border-top:1px solid var(--line)}
.rev .rq2 p{font-family:var(--serif);font-style:italic;font-size:18px;color:var(--ink-2);line-height:1.4}
.faq .faqlist{margin-top:6px}
.faq details{border-top:1px solid var(--line)}
.faq details:last-of-type{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:20px;padding:24px 2px;font-family:var(--serif);font-size:clamp(19px,2.3vw,26px);font-weight:400;color:var(--ink);letter-spacing:-.01em}
.faq summary::-webkit-details-marker{display:none}
.faq summary:hover{color:var(--blue)}
.faq summary .ic{flex:none;width:34px;height:34px;border-radius:50%;border:1px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--gold);font-size:22px;line-height:1;background:var(--card);transition:transform .3s,background .3s,color .3s}
.faq details[open] summary .ic{transform:rotate(45deg);background:var(--ink);color:#fff;border-color:var(--ink)}
.faq .a{padding:0 2px 26px;max-width:74ch;animation:faqin .35s ease}
@keyframes faqin{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.faq .a p{color:var(--ink-2);font-size:16.5px}
.faq .a b{color:var(--ink);font-weight:700}
.faq .a a{color:var(--blue);font-weight:600;border-bottom:1px solid var(--gold)}
.faq-cta{display:flex;justify-content:center;margin-top:38px}'''
assert s.count(CSSANCHOR)==1,"cssanchor"; s=s.replace(CSSANCHOR, CSSANCHOR+CSSADD, 1)

# ---- FAQ section before final ----
FAQ_SECTION='''<section class="faq tint-b" id="faq">
  <div class="wrap">
    <div class="eyerow reveal"><span class="ln"></span><span class="snum">09</span><span class="kicker">Preguntas frecuentes</span></div>
    <h2 class="disp reveal" style="margin-bottom:8px">Todo lo que necesitas <span class="it">saber</span>.</h2>
    <p class="reveal d1" style="color:var(--muted);font-size:16px;margin-bottom:30px;max-width:54ch">Horarios, tarifas, servicios y ubicacion del Hotel Barahona 72. Si te queda una duda, escribenos por WhatsApp.</p>
    <div class="faqlist reveal d1">
      <details><summary>&iquest;Cuanto cuesta una noche en el Hotel Barahona 72?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>Las tarifas van <b>desde $118.000 COP por noche</b> en la habitacion Doble e incluyen desayuno. El precio varia segun el tipo de habitacion (Doble, Twin, Junior Suite, Triple o Cuadruple) y la temporada. Escribenos por WhatsApp para confirmar la tarifa del dia.</p></div></details>
      <details><summary>&iquest;Cual es el horario de check-in y check-out?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>El <b>check-in es a partir de las 3:00 p.m.</b> y el <b>check-out hasta las 12:00 del mediodia</b>.</p></div></details>
      <details><summary>&iquest;El desayuno esta incluido?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>Si, todas las tarifas <b>incluyen desayuno</b>. Los ninos son gratis hasta los 4 anos y solo pagan el desayuno, con un valor de $12.000.</p></div></details>
      <details><summary>&iquest;Que servicios ofrece el hotel?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>WiFi gratis, aire acondicionado, desayuno incluido, recepcion 24 horas, restaurante, room service, lavanderia, salon de eventos, television, telefono, escritorio y bano privado con ducha y agua caliente.</p></div></details>
      <details><summary>&iquest;Se aceptan mascotas?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>Si, el hotel <b>acepta mascotas con un cargo adicional</b>. Avisanos al momento de reservar para preparar tu llegada.</p></div></details>
      <details><summary>&iquest;Donde queda y que hay cerca?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>Estamos en la <b>Carrera 49 #72-19, barrio Prado, Barranquilla</b>. A 0,5 km del Parque Tomas Suri Salcedo, 0,6 km del Centro Comercial Gran Centro y a pocas cuadras del Estadio Romelio Martinez. El Aeropuerto Ernesto Cortissoz esta a unos 40 minutos.</p></div></details>
      <details><summary>&iquest;Como reservo directamente?<span class="ic" aria-hidden="true">+</span></summary><div class="a"><p>Escribenos por <a href="https://wa.me/573503189890?text=Hola,%20quiero%20reservar%20en%20Hotel%20Barahona%2072">WhatsApp al +57 350 318 9890</a>. Reservando directo obtienes la <b>mejor tarifa, sin comisiones</b> de intermediarios.</p></div></details>
    </div>
    <div class="faq-cta reveal d1"><a class="btn btn-wa" href="https://wa.me/573503189890?text=Hola,%20tengo%20una%20pregunta%20sobre%20Hotel%20Barahona%2072"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.945C.16 5.335 5.495 0 12.05 0a11.817 11.817 0 0 1 8.413 3.488 11.824 11.824 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.523 5.273l-.999 3.648 3.965-1.04zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>Preguntar por WhatsApp</a></div>
  </div>
</section>

'''
assert s.count('<section class="final">')==1,"final"; s=s.replace('<section class="final">', FAQ_SECTION+'<section class="final">',1)

io.open(P,"w",encoding="utf-8").write(s)
print("PASS 2 written, len", len(s), "delta", len(s)-len(orig))
