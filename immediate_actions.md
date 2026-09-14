# Immediate actions (operator checklist)

Production DNS is **not** mutated by this package. Execute these on the live accounts.

## P0 — execution-proof failures

1. **genesisconductor.io** — Remove the password store gate. Serve HTTP 200 on `/` with architecture diagram and links to GitHub org, ORCID, SEAR, news, optimizationinversion.com. Do not put checkout above the fold.
2. **optimizationinversion.com** — Clear the 503. Publish one HTML note with inversion definition, Landauer inequality as physics, Zenodo DOIs, ORCID.
3. **sear.genesisconductor.io** — Keep public. Add `/openapi.json` only if a real contract exists.

## P1 — claim hygiene

4. Relabel SHM numbers as local POSIX demo via `bench_shm.py` until a hardware lab note exists.
5. NSF #2530747: publish Award Search URL listing Holt as PI, or remove federal-PI language.
6. ORCID hygiene: drop imported works Holt did not author.

## P2 — repo governance

7. CODEOWNERS `igor@kovachenterprises.com`, Podman Containerfile, SPDX MIT/Apache-2.0.
8. GA4 custom channel AI Discovery regex: `(chatgpt|perplexity|claude|gemini|copilot|you\.com|phind)`.

## P3 — GEO ingestion

9. Deploy `schema/jsonld.json` and `llms/llms.txt` after ungating.
10. Do not submit gated URLs to Search Console.
