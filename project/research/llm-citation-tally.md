# Hotel Barahona 72 - LLM Citation Test (AEO/GEO)

Test run 2026-06-30 via DataForSEO `ai_optimization_llm_response` (web_search=true).
Brand variants counted as a HIT: "Hotel Barahona 72", "Ayenda 1313 Barahona 72", "Hotel Ayenda Barahona 72".

Models: Claude Sonnet 4.6, Gemini 3.1 Pro, GPT-5.5, Sonar Reasoning Pro.

## Headline: 4 of 20 citations

| # | Prompt (ES) | Claude | Gemini | GPT-5.5 | Perplexity |
|---|---|---|---|---|---|
| 1 | mejores hoteles economicos 3 estrellas en Barranquilla | HIT (#9) | miss | miss | miss |
| 2 | hotel economico cerca Calle 72 / El Prado | HIT (#5) | miss | miss | miss |
| 3 | cerca Estadio Romelio Martinez + negocios Calle 72 | HIT (#1) | miss | HIT (#3) | miss |
| 4 | 3 estrellas calidad-precio para negocios | miss | miss | miss | miss |
| 5 | hotel economico Carnaval de Barranquilla 2027 | miss | miss | miss | miss |

Per model: Claude 3/5, GPT-5.5 1/5, Gemini 0/5, Perplexity 0/5. Total 4/20 (20%).

Note: 3 of the 4 hits are Claude (the model that shares the brand name lineage). The only
non-Claude hit (GPT-5.5, prompt 3) came on the one query that literally contains "72" /
"Romelio Martinez", which the hotel's name encodes. On the two HIGHEST commercial-value
prompts (business value-for-money + Carnaval, the biggest revenue window) the hotel scored 0/8.

## Brands that WIN the AI answer (cited across models/prompts)

- Hotel Prado 72 / Prado 72 INN  - direct Calle 72 rival. Cited by ALL 4 models on prompt 2,
  by Claude+Gemini+GPT on prompt 3, by Perplexity on prompt 5. The single biggest AEO threat.
- ibis Budget Barranquilla / ibis Barranquilla - own "budget 3-star" + "business" answers.
- Hotel Casa Ballesteros - 1,494 Google reviews (Apify) / 1,737 (KAYAK). Cited P1, P2, P5.
- Hotel Casa Colonial - cited P1, P2, P5.
- Hotel Genova Prado - cited P1, P4, P5.
- Holiday Inn Express Buenavista, Howard Johnson Versalles - "business" answers.
- OTHER Ayenda siblings cited MORE than Barahona 72: Ayenda 1315 Candiac, Ayenda Costa Linda
  1321, Ayenda Casa Prado, Ayenda 1317 House Concepcion, Ayenda 1309 Villa Dilia, Ayenda 1311
  Doral. Even inside its own chain, Barahona 72 is not the model's default pick.

## Why it loses
The models pull from TripAdvisor "10 best" lists, Booking/Expedia district pages, KAYAK and
Ayenda's own neighborhood pages. Barahona 72 has no owned web property feeding those answers,
a middling 4.1 rating, and far fewer reviews than the review leaders (Casa Ballesteros 1,494,
Hotel Platinum 776). It is present in the OTA graph but never the "top pick".
