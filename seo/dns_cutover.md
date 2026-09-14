# DNS cutover — ungating genesisconductor.io without destroying commerce

Connected Cloudflare account contains zone `genesisconductor.io` (id `9c206e4bb8ce3a254dcb1cc90062de06`).
`optimizationinversion.com` is **not** in this account.

## Current (observed)

| Name | Type | Content | Effect |
|---|---|---|---|
| genesisconductor.io | A | 23.227.38.65 | Shopify apex → `/password` |
| genesisconductor.io | AAAA | 2620:127:f00f:5:: | Shopify IPv6 |
| www.genesisconductor.io | CNAME | cname.vercel-dns.com | Intended engineering origin |
| shop.genesisconductor.io | CNAME | shops.myshopify.com | Correct shop host |

## Required cutover (human-gated; not executed this cycle)

1. Confirm Vercel project for `www` serves the ungated technical page.
2. Point apex A/AAAA away from Shopify.
3. Keep Shopify exclusively on `shop.genesisconductor.io`.
4. Deploy OpenAPI to `sear.genesisconductor.io/openapi.yaml`.
5. Verify HTTP 200 on `/`, `/llms.txt`, `/robots.txt` with no password interstitial.
