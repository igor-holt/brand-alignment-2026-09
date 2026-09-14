# DNS / surface cutover notes

Audit time: 2026-09-14T18:12:19Z
This cycle does not change DNS records.

| Host | Observed state | Action |
|---|---|---|
| genesisconductor.io | Password store at `/password` | Ungate in app/hosting config |
| www.genesisconductor.io | Same gate | Same |
| optimizationinversion.com | HTTP 503 | Restore origin / Worker |
| optimization-inversion.genesisconductor.io | Live marketing + REST `/v1/tasks` + pricing | Demote; not the identity URL |
| sear.genesisconductor.io | Live docs | Keep |
| news.genesisconductor.io | Live ops | Keep |
