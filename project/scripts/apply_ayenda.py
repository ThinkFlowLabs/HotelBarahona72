# -*- coding: utf-8 -*-
# Integra la informacion REAL de Ayenda (ayenda.com/.../ayenda-1313-barahona-72) en index.html
import io, sys, os
P = r"C:/Users/JimAn/Desktop/ThinkFlowLabs/Websites Builder/Projects/Hotel Barahona 72/site/index.html"
s = io.open(P, encoding="utf-8").read()
orig = s
def rep(old, new, n=1, label=""):
    global s
    c = s.count(old)
    if c < 1:
        raise SystemExit("NOT FOUND ["+label+"]: " + old[:90])
    s = s.replace(old, new, n)
    print("ok  ", label, "(x%d)"%c)

# reusable svg icons
P_PERSON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0"/></svg>'
P_SIZE='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M8 3H5a2 2 0 0 0-2 2v3M16 3h3a2 2 0 0 1 2 2v3M8 21H5a2 2 0 0 1-2-2v-3M16 21h3a2 2 0 0 0 2-2v-3"/></svg>'
P_AC='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9.5 19A2.5 2.5 0 1 1 7 16.5H22M14 5A2.5 2.5 0 1 1 16.5 7.5H2M19 13a2.5 2.5 0 1 1 2.5 2.5H2"/></svg>'
P_BED1='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 9V7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v2M2 17v-4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4M2 17h20"/></svg>'
P_BED2='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 9V7a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v2M2 17v-4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4M2 17h20M9 11V6M15 11V6"/></svg>'
EXPAND='<span class="cnt"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>Ver fotos</span>'
WA_SVG='<svg viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.945C.16 5.335 5.495 0 12.05 0a11.817 11.817 0 0 1 8.413 3.488 11.824 11.824 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.523 5.273l-.999 3.648 3.965-1.04zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>'

def wa(msg):
    return "https://wa.me/573503189890?text="+msg

# ---- 1. meta description ----
rep('<meta name="description" content="Hotel Barahona 72: hotel de la Calle 72, barrio Prado, Barranquilla. A pasos del Estadio Romelio Martinez y la zona de negocios. Reserva directa por WhatsApp, sin comisiones.">',
    '<meta name="description" content="Hotel Barahona 72, sobre la Calle 72 en el barrio Prado, Barranquilla. Habitaciones con aire acondicionado, WiFi y desayuno incluido, recepcion 24h y restaurante. Desde $118.000 COP la noche. A pasos del Estadio Romelio Martinez. Reserva directa por WhatsApp, sin comisiones.">',
    label="meta-desc")

# ---- 2. og description ----
rep('<meta property="og:description" content="Hotel sobre la Calle 72, barrio Prado. A pasos del Estadio Romelio Martinez. Reserva directa por WhatsApp.">',
    '<meta property="og:description" content="Hotel sobre la Calle 72, barrio Prado, Barranquilla. Aire acondicionado, WiFi y desayuno incluido. Desde $118.000 COP. Reserva directa por WhatsApp.">',
    label="og-desc")

# ---- 3. rich schema (Hotel + Breadcrumb + FAQPage) ----
OLD_SCHEMA='{"@context":"https://schema.org","@type":"Hotel","name":"Hotel Barahona 72","description":"Hotel economico sobre la Calle 72, barrio Prado, Barranquilla, cerca del Estadio Romelio Martinez y la zona de negocios.","starRating":{"@type":"Rating","ratingValue":"3"},"priceRange":"$$","image":"https://hotelbarahona72.com/img/barahona-18.webp","telephone":"+573503189890","hasMap":"https://maps.app.goo.gl/HnyXTPqc7Nxtx7meA","address":{"@type":"PostalAddress","streetAddress":"Carrera 49 #72-19","addressLocality":"Barranquilla","addressRegion":"Atlantico","addressCountry":"CO"},"geo":{"@type":"GeoCoordinates","latitude":"10.9966981","longitude":"-74.8047106"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.1","reviewCount":"430"}}'

HOTEL_JSON=('{"@context":"https://schema.org","@type":"Hotel","@id":"https://hotelbarahona72.com/#hotel",'
'"name":"Hotel Barahona 72","alternateName":"Ayenda 1313 Barahona 72",'
'"description":"Hotel economico sobre la Calle 72, barrio Prado, Barranquilla. Habitaciones con aire acondicionado, WiFi y desayuno incluido, recepcion 24 horas, restaurante y room service. A pasos del Estadio Romelio Martinez, el Parque Tomas Suri Salcedo y el Centro Comercial Gran Centro.",'
'"url":"https://hotelbarahona72.com/","starRating":{"@type":"Rating","ratingValue":"3"},'
'"priceRange":"COP 118.000 - 165.470","currenciesAccepted":"COP","paymentAccepted":"Efectivo, Tarjeta de credito, Transferencia",'
'"image":["https://hotelbarahona72.com/img/barahona-18.webp","https://hotelbarahona72.com/img/room-doble.webp","https://hotelbarahona72.com/img/room-cuadruple.webp"],'
'"telephone":"+573503189890","checkinTime":"15:00","checkoutTime":"12:00","petsAllowed":true,"availableLanguage":["es","en"],'
'"hasMap":"https://maps.app.goo.gl/HnyXTPqc7Nxtx7meA",'
'"address":{"@type":"PostalAddress","streetAddress":"Carrera 49 #72-19","addressLocality":"Barranquilla","addressRegion":"Atlantico","addressCountry":"CO"},'
'"geo":{"@type":"GeoCoordinates","latitude":"10.9966981","longitude":"-74.8047106"},'
'"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.1","reviewCount":"430","bestRating":"5"},'
'"amenityFeature":['
'{"@type":"LocationFeatureSpecification","name":"WiFi gratis","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Aire acondicionado","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Desayuno incluido","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Recepcion 24 horas","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Restaurante","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Room service","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Lavanderia","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Salon de eventos","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Bano privado","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Television","value":true},'
'{"@type":"LocationFeatureSpecification","name":"Se aceptan mascotas","value":true}],'
'"containsPlace":['
'{"@type":"HotelRoom","name":"Habitacion Doble","occupancy":{"@type":"QuantitativeValue","maxValue":2},"floorSize":{"@type":"QuantitativeValue","value":20,"unitCode":"MTK"}},'
'{"@type":"HotelRoom","name":"Habitacion Twin","occupancy":{"@type":"QuantitativeValue","maxValue":2},"floorSize":{"@type":"QuantitativeValue","value":20,"unitCode":"MTK"}},'
'{"@type":"HotelRoom","name":"Habitacion Junior Suite","occupancy":{"@type":"QuantitativeValue","maxValue":2}},'
'{"@type":"HotelRoom","name":"Habitacion Triple","occupancy":{"@type":"QuantitativeValue","maxValue":3},"floorSize":{"@type":"QuantitativeValue","value":22,"unitCode":"MTK"}},'
'{"@type":"HotelRoom","name":"Habitacion Cuadruple","occupancy":{"@type":"QuantitativeValue","maxValue":4},"floorSize":{"@type":"QuantitativeValue","value":24,"unitCode":"MTK"}}],'
'"makesOffer":{"@type":"Offer","priceCurrency":"COP","price":"118000","availability":"https://schema.org/InStock","priceSpecification":{"@type":"PriceSpecification","minPrice":"118000","maxPrice":"165470","priceCurrency":"COP"}}}')

BREADCRUMB_JSON=('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
'{"@type":"ListItem","position":1,"name":"Inicio","item":"https://hotelbarahona72.com/"},'
'{"@type":"ListItem","position":2,"name":"Hoteles en Barranquilla"},'
'{"@type":"ListItem","position":3,"name":"Hotel Barahona 72"}]}')

FAQ_JSON=('{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
'{"@type":"Question","name":"Cuanto cuesta una noche en el Hotel Barahona 72?","acceptedAnswer":{"@type":"Answer","text":"Las tarifas van desde $118.000 COP por noche en la habitacion Doble e incluyen desayuno. El precio varia segun el tipo de habitacion (Doble, Twin, Junior Suite, Triple o Cuadruple) y la temporada. Escribenos por WhatsApp al +57 350 318 9890 para confirmar la tarifa del dia."}},'
'{"@type":"Question","name":"Cual es el horario de check-in y check-out?","acceptedAnswer":{"@type":"Answer","text":"El check-in es a partir de las 3:00 p.m. y el check-out hasta las 12:00 del mediodia."}},'
'{"@type":"Question","name":"El desayuno esta incluido?","acceptedAnswer":{"@type":"Answer","text":"Si, todas las tarifas incluyen desayuno. Los ninos son gratis hasta los 4 anos y solo pagan el desayuno, con un valor de $12.000."}},'
'{"@type":"Question","name":"Que servicios ofrece el hotel?","acceptedAnswer":{"@type":"Answer","text":"WiFi gratis, aire acondicionado, desayuno incluido, recepcion 24 horas, restaurante, room service, lavanderia, salon de eventos, television, telefono, escritorio y bano privado con ducha y agua caliente."}},'
'{"@type":"Question","name":"Se aceptan mascotas?","acceptedAnswer":{"@type":"Answer","text":"Si, el hotel acepta mascotas con un cargo adicional. Avisanos al momento de reservar para preparar tu llegada."}},'
'{"@type":"Question","name":"Donde queda el Hotel Barahona 72 y que hay cerca?","acceptedAnswer":{"@type":"Answer","text":"Esta en la Carrera 49 #72-19, barrio Prado, Barranquilla. A 0,5 km del Parque Tomas Suri Salcedo, 0,6 km del Centro Comercial Gran Centro y a pocas cuadras del Estadio Romelio Martinez. El Aeropuerto Ernesto Cortissoz esta a unos 40 minutos."}},'
'{"@type":"Question","name":"Como reservo directamente?","acceptedAnswer":{"@type":"Answer","text":"Escribenos por WhatsApp al +57 350 318 9890. Reservando directo obtienes la mejor tarifa, sin comisiones de intermediarios."}}]}')

NEW_SCHEMA = (HOTEL_JSON + '\n</script>\n<script type="application/ld+json">\n'
              + BREADCRUMB_JSON + '\n</script>\n<script type="application/ld+json">\n'
              + FAQ_JSON)
rep(OLD_SCHEMA, NEW_SCHEMA, label="schema")

# ---- 4. nav links: add Preguntas ----
rep('<a href="#resenas">Reseñas</a><a href="#negocios">Negocios</a></nav>',
    '<a href="#resenas">Reseñas</a><a href="#faq">Preguntas</a><a href="#negocios">Negocios</a></nav>',
    label="nav-faq")

# ---- 5. hero stamp price ----
rep('<div class="p">$160.000<small>COP · desde / noche</small></div>',
    '<div class="p">$118.000<small>COP · desde / noche</small></div>',
    label="hero-price")

# ---- 6. ubicacion POIs (real landmarks) ----
rep('<h3>Zona de negocios de la 72</h3><span>Bancos, oficinas y centros comerciales</span>',
    '<h3>C.C. Gran Centro <span class="d">a 0,6 km</span></h3><span>Centro comercial, bancos y tiendas</span>',
    label="poi-grancentro")
rep('<h3>Cerca de clinicas del norte</h3><span>Comodo para turismo de salud y acompanantes</span>',
    '<h3>Parque Tomas Suri Salcedo <span class="d">a 0,5 km</span></h3><span>Zona verde en el corazon del Prado</span>',
    label="poi-parque")

# ---- 7. servicios: real services (remove parqueadero, add room service + salon eventos) ----
rep('<b>Desayuno</b><span>Para arrancar el dia</span>',
    '<b>Desayuno incluido</b><span>Incluido en tu tarifa</span>', label="serv-desayuno")
rep('<div class="it"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M5 17H3v-6l2-5h11l4 5v6h-2"/><circle cx="7.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg><b>Parqueadero</b><span>Para tu vehiculo</span></div>',
    '<div class="it"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 18h18M4 18a8 8 0 0 1 16 0M12 6v4M10 6h4"/></svg><b>Room service</b><span>Servicio a la habitacion</span></div>',
    label="serv-roomservice")
rep('<div class="it"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M9 2h6v4H9zM9 12l2 2 4-4"/></svg><b>Factura</b><span>Para tu empresa</span></div>',
    '<div class="it"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg><b>Salon de eventos</b><span>Reuniones y celebraciones</span></div>',
    label="serv-eventos")

io.open(P,"w",encoding="utf-8").write(s)
print("PASS 1 written, len", len(s), "delta", len(s)-len(orig))
