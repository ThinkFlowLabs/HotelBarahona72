# Hotel Barahona 72 — Estado del Proyecto (MASTER)

> Documento maestro del proyecto. Consolida todo lo hecho (auditoría SEO + sitio web + datos
> reales + despliegue). Última actualización: **10 de julio de 2026**.

---

## 1. Resumen

**Cliente:** Hotel Barahona 72 — hotel económico 3 estrellas sobre la Calle 72, barrio Prado,
Barranquilla, Colombia. Opera bajo la red **Ayenda** como *"Ayenda 1313 Barahona 72"*.
**Marca real** (de la foto de recepción): wordmark "BARAHONA 72" (BARAHONA azul, 72 verde).
Submarca en el sitio: **"By: MFM Hoteles"** (pedido del cliente, 10 jul 2026; reemplazó "MFM · HOTEL"
en header, footer y línea legal).

**Dos entregables construidos:**
1. **Auditoría / estrategia SEO de entrada al mercado** (el hotel no tenía web) → reporte HTML.
2. **Sitio web one-page** (landing de reserva directa por WhatsApp + landing de Google Ads).

**Objetivo del sitio:** embudo de reserva directa por WhatsApp (sin comisiones de OTA), servir como
landing de Google Ads y destino del perfil de Google Business.

---

## 2. Estado actual — EN VIVO

- **Sitio en vivo (GitHub Pages):** https://thinkflowlabs.github.io/HotelBarahona72/
- **Sitio en vivo (Railway):** https://hotel-barahona-72-production.up.railway.app/ (mismo contenido)
- **Repo:** https://github.com/ThinkFlowLabs/HotelBarahona72 (público, rama `main`, sirve desde raíz)
- **Reporte SEO en vivo:** https://thinkflowlabs.github.io/SEO/hotel-barahona-72-audit/
- **Dominio final (aún NO registrado):** hotelbarahona72.com (el `canonical` ya apunta ahí)
- **Precios OFICIALES desde el 10 jul 2026** (tabla de tarifas entregada por el cliente, IVA 19%
  incluido) — ya no son los referenciales de Ayenda.

---

## 3. Datos REALES del hotel (fuente: listado oficial en Ayenda)

Fuente: https://ayenda.com/co/hoteles/barranquilla/ayenda-1313-barahona-72 (scrapeado con Playwright
el 1 jul 2026; datos crudos en `research/ayenda/`).

**Contacto y dirección**
- Dirección: **Carrera 49 #72-19, barrio Prado, Barranquilla, Atlántico** (aprox. 10.9966981, -74.8047106)
- **Celular de recepción y reservas (oficial, cliente 10 jul 2026): +57 317 429 6529**
  (wa.me/573174296529) — reemplazó al +57 350 318 9890 en todo el sitio.
- **Correo oficial del hotel: recepcion@hoteles-mfm.com** (footer + schema).
- Google: **4.1 / 5** con **430 reseñas**. Ayenda: **8.2 "Excelente"**.

**Habitaciones — TARIFAS OFICIALES (tabla del cliente, 10 jul 2026; IVA 19% incluido)**
| Tipo | Capacidad | m² | COP/noche (IVA inc.) | Foto en el sitio |
|------|-----------|----|----------------------|------------------|
| Sencilla | 1 persona | — | $120.000 | `barahona-22.webp` |
| Doble | 1-2 personas | 20 m² | $160.000 | `room-doble.webp` (real, mejorada) |
| Triple | 1-3 personas | 22 m² | $210.000 | `room-triple.webp` (real, mejorada) |
| Cuádruple | 1-4 personas | 24 m² | $260.000 | `room-cuadruple.webp` (real, mejorada) |

*Tarifa neta + IVA 19% = total (p. ej. Sencilla $100.840 + $19.160 = $120.000). Los tipos "Twin" y
"Junior Suite" (referenciales de Ayenda) se retiraron del sitio; `room-doble-2.webp` quedó sin uso.*

**Políticas (reales)**
- Check-in **3:00 p.m.** / Check-out **12:00 m.**
- Niños **gratis hasta los 4 años** (solo pagan desayuno, $12.000).
- **Se aceptan mascotas** (cargo extra) → por eso el badge "Pet friendly" en el hero.

**Servicios (reales, según Ayenda)**
WiFi gratis, aire acondicionado, **desayuno incluido**, recepción 24h, restaurante, **room service**,
lavandería (cargo extra), **salón de eventos**, TV, teléfono, escritorio, baño privado con ducha y
agua caliente, botones, estación de café, plancha para ropa. *NOTA: Ayenda NO lista parqueadero — se
quitó del sitio para no prometer algo que no está confirmado.*

**Cerca (POIs reales)**
- C.C. Gran Centro — a 0,6 km · Parque Tomás Suri Salcedo — a 0,5 km
- Estadio Romelio Martínez — a pocas cuadras · Aeropuerto Ernesto Cortissoz — ~40 min

**Reseñas verificadas reales usadas en el sitio**
- *Marcela Rengifo:* "La señora es muy hospitalaria, súper amable y te ayuda. Excelente servicio de aseo."
- *Freddy Alfonso:* "La atención y la amplitud de la habitación."

---

## 4. El sitio web (`site/index.html`)

**Un solo archivo** HTML/CSS/JS estático, sin framework ni build. Fuentes: **Fraunces** (display serif)
+ **Karla** (UI/cuerpo). Dirección editorial "Caribeña": motivo "72" gigante, drop caps, números de
sección, textura de grano, secciones oscuras alternadas, reveals con IntersectionObserver, parallax
del hero. (El primer intento se rechazó por "simplón/hecho por IA"; la v2 editorial es la que quedó.)

**Paleta:** azul #134E8C, verde #3E7C24, dorado #B4893A/#CBA25A, navy #0B2A4A, WhatsApp #25D366,
estrella #F5B301. Botones CTA en dorado; verde WhatsApp solo en botones de WhatsApp.

**Orden de secciones:** header (transparente→sólido al hacer scroll) → hero (con **badge Pet friendly +
icono de hueso SVG**, byline **"BY: MFM HOTELES"** bajo el badge con el estilo del kicker — Karla
bold 11.5px, mayúsculas, letter-spacing .28em, dorado var(--gold-2) —, precio
desde $120.000, 4.1/430) → manifiesto (modelo en la **sala real** del hotel)
→ 01 Ubicación (mapa + POIs reales) → 02 Negocios/salud → 03 Habitaciones (4 tipos oficiales, estilo OTA,
chips por capacidad, modo oscuro) → CTA band → 04 Servicios → 05 Galería (carrusel + lightbox) → 06
Familia → 07 Reseñas (4.1 Google + 8.2 Ayenda + 2 quotes reales) → 08 Carnaval 2027 → **09 Preguntas
Frecuentes (accordion)** → CTA final → footer.

**Funcionalidad JS:** header scroll, reveals, parallax hero, filtros de habitaciones (chips), **lightbox**
con navegación prev/next + teclado + dots, **carrusel de galería** auto-avance. Accesible: focus-visible,
aria-labels, prefers-reduced-motion.

**SEO / LLM SEO:** 3 bloques JSON-LD → `Hotel` (amenityFeature, checkin/out, petsAllowed,
aggregateRating, geo, 4× `HotelRoom` con m²/ocupación, makesOffer, brand "MFM Hoteles", email),
`BreadcrumbList`, `FAQPage` (7 Q&A).
Open Graph + Twitter, meta description con perks reales, `lang=es`, canonical a hotelbarahona72.com.

---

## 5. Imágenes (`site/img/` — 38 WebP; originales en `assets/`)

- **Fotos reales del hotel:** `barahona-01..22.webp` (sin la 19) — del Drive del cliente (carpeta
  1oRmZR..., compartida por aandyccure@gmail.com), mejoradas con GPT Image 2 excepto la 03 (recepción,
  se dejó original para no alterar el rostro de la persona real).
- **Fotos reales de habitaciones (nuevas):** `room-doble`, `room-doble-2`, `room-triple`,
  `room-cuadruple` — extraídas del CDN de Ayenda (imgix) y **mejoradas con GPT Image 2**
  (`openai/gpt-image-2/edit`, input_fidelity high), **neutralizando el logo "Ayenda"** de las almohadas
  (marca directa). Originales en `assets/ayenda/`.
- **Composite:** `life-guest.webp` = la modelo del vestido floral recolocada en la **sala real**
  (barahona-02) con GPT Image 2 pasando 2 imágenes (personaje + locación). Sección "Bienvenido a Barahona 72".
- **Estilo de vida (IA, aspiracionales):** `life-lounge/business/family/carnaval/terrace`.
- **Fondos (IA):** `tex-soft`, `bq-city`, `bq-skyline`, `bq-night`, `bq-night2`, `modern-hotel`, `hotel-hq`.

**Divulgación honesta:** fotos de habitaciones y espacios = reales (mejoradas). Fondos y estilo de vida
con modelos = generados con IA. Documentado en el README del repo.

---

## 6. Despliegue — cómo actualizar

El sitio se sirve desde **GitHub Pages** del repo `ThinkFlowLabs/HotelBarahona72` (rama main, raíz).
La copia de despliegue (clon git) vive en:

```
C:/Users/JimAn/Desktop/ThinkFlowLabs/_deploy/HotelBarahona72   <-- OJO: está en ThinkFlowLabs/_deploy,
                                                                    NO en Websites Builder/_deploy
```
Estructura del repo: `index.html` + `img/` + `.nojekyll` + `README.md` en la raíz; archivos de trabajo
bajo `project/`. (Se excluyen los assets crudos pesados ~158MB.)

**Para publicar un cambio del sitio:**
```bash
# 1. editar site/index.html (o imágenes) en el proyecto
# 2. copiar al deploy
cp "Projects/Hotel Barahona 72/site/index.html" "C:/Users/JimAn/Desktop/ThinkFlowLabs/_deploy/HotelBarahona72/index.html"
#    (y las imágenes nuevas a .../HotelBarahona72/img/)
# 3. commit + push con la cuenta ThinkFlowLabs
cd "C:/Users/JimAn/Desktop/ThinkFlowLabs/_deploy/HotelBarahona72"
gh auth switch --user ThinkFlowLabs
git add -A && git commit -m "..." && git push origin main
# 4. verificar build: gh api repos/ThinkFlowLabs/HotelBarahona72/pages/builds/latest --jq .status
# 5. VOLVER la cuenta gh a la predeterminada
gh auth switch --user LPGMarketing
```
> Cuentas gh en el keyring: **ThinkFlowLabs** (para este repo) y **LPGMarketing** (predeterminada).
> Siempre devolver a LPGMarketing al terminar.

**Railway (segundo hosting, agregado Jul 8 2026):**

El mismo clon de deploy también está linkeado a Railway (cuenta LPGMarketing / ludlowpg@gmail.com,
proyecto `hotel-barahona-72`, servicio `hotel-barahona-72`). Es un static site servido con Caddy
vía el `Dockerfile` en la raíz del repo (`.railwayignore` excluye `project/`).

```bash
# publicar en Railway (después del push a GitHub Pages):
cd "C:/Users/JimAn/Desktop/ThinkFlowLabs/_deploy/HotelBarahona72"
railway up --service hotel-barahona-72 --detach
```
URL pública: https://hotel-barahona-72-production.up.railway.app/

---

## 7. Previsualizar localmente

Servidor de dev corriendo en `http://localhost:8088/` (python http.server desde `site/`). Para levantarlo:
```bash
cd "Projects/Hotel Barahona 72/site" && python -m http.server 8088
```
QA con Playwright: revisar overflow horizontal (=0), imágenes rotas, breakpoints 390/768/1440, lightbox,
carrusel, filtros. **Gotcha:** `scroll-behavior:smooth` desincroniza las mediciones de rects en Playwright
→ setear `document.documentElement.style.scrollBehavior='auto'` antes de hacer scroll en evaluate.

---

## 8. Scripts (`scripts/`)

| Script | Qué hace |
|--------|----------|
| `gen_lifestyle.py` / `gen_lifestyle2.py` | Generan imágenes de estilo de vida con GPT Image 2 (text-to-image). |
| `enhance_photos.py` | Mejora las fotos reales del hotel con GPT Image 2 (edit). |
| `apply_ayenda.py` | Pass 1: integra datos reales de Ayenda (meta, schema enriquecido, POIs, servicios, precio hero). |
| `apply_ayenda2.py` | Pass 2: reconstruye habitaciones reales, galería, reseñas reales, sección FAQ + CSS. |
| `add_accents.py` | Agrega tildes al texto visible protegiendo CSS/JS/JSON-LD/href/id (español impecable). |

**GPT Image 2 (vía fal, `fal_client`) — recordatorios:**
- API key: `FAL_KEY` en `Projects/mb-clean-solutions/site/.env`.
- Generar: `openai/gpt-image-2`; `image_size` DEBE ser dict `{"width":W,"height":H}`.
- Editar: `openai/gpt-image-2/edit`; acepta `image_urls` (varias imágenes → composición), usar
  `input_fidelity:"high"` para fidelidad; `image_size` como dict o `"auto"` (string de tamaño NO sirve).
- Bloquea prompts sexualizados (content_policy_violation).

---

## 9. Historial de cambios (commits del repo)

```
7f37302  Hero: byline By: MFM Hoteles con estilo kicker (Karla bold uppercase, dorado gold-2)
fcdef3d  Hero: byline By: MFM Hoteles bajo el badge Pet friendly (dorado #EBD9AE como El Prado)
e0efe3f  Datos oficiales del hotel: tarifas 2026 (IVA inc.), celular 317 429 6529, correo y By: MFM Hoteles
2072a7a  Reseñas: foto real del comedor (barahona-05 mejorada GPT Image 2 1024x1536) como fondo de sección
9538c78  Fix: reseñas con ñ en el stamp del hero
7487752  Copy: barrio El Prado (nombre completo) + hero en 2 líneas + Dockerfile para Railway
40eb9a5  Copy: ubicación correcta barrio Prado (no centro) en hero, dirección y sección Carnaval
dbb69d8  Ortografía: tildes en todo el texto visible (sin tocar URLs/schema)
846fd57  Hero: badge Pet friendly (hueso SVG) + fix flechas del lightbox (prev izq / next der)
9d78c61  Info real de Ayenda: habitaciones+precios reales, fotos Doble/Cuádruple mejoradas, FAQ + schema
d411dd6  Sección bienvenida: modelo compuesta en la sala real (GPT Image 2)
20a6025  Sitio Hotel Barahona 72 + archivos de proyecto (deploy inicial)
```

---

## 10. Pendientes / por confirmar con el hotel

- [x] **Precios de reserva directa** — CONFIRMADOS 10 jul 2026 (tabla oficial del cliente, IVA 19% inc.).
- [x] **WhatsApp/teléfono** — CONFIRMADO 10 jul 2026: +57 317 429 6529 (recepción y reservas).
- [ ] **Número de RNT** (Registro Nacional de Turismo) — placeholder en el footer.
- [ ] **Registrar dominio** hotelbarahona72.com y apuntarlo (el canonical ya lo referencia).
- [ ] Agregar **GA4 / Meta Pixel** para la campaña de Google Ads.
- [ ] Opcional: reemplazar imágenes de estilo de vida IA por fotos reales si el hotel las tiene.
- [ ] Verificar el sitio en Google Search Console cuando esté en el dominio final.

---

## 11. Carpetas del proyecto

```
Projects/Hotel Barahona 72/
  PROJECT-STATUS.md      <- este documento (master)
  site/                  <- el sitio (index.html + img/)
  scripts/               <- scripts de generación/integración de imágenes y contenido
  assets/                <- originales: drive/ (fotos hotel), ayenda/ (fotos habitaciones), lifestyle/
  research/              <- investigación SEO + ayenda/ (datos crudos scrapeados)
  audit/                 <- material de auditoría
  report/                <- reporte SEO HTML (deployado a thinkflowlabs.github.io/SEO/...)
  screenshots/           <- capturas de QA (desktop + móvil)
```

También hay memoria persistente en:
`~/.claude/projects/.../memory/hotel-barahona-72.md` y `feedback-design-punch.md`.
