# Brand alignment package — 2026-09-14

Deterministic SEO / AEO / GEO calibration for Igor Holt, Genesis Conductor, and Optimization Inversion.

Start at `00_EXECUTIVE_ALIGNMENT.md`.

## Hard constraints from this cycle

- Do **not** treat `github/bench_shm.py` output as a production IPC claim.
- Production DNS was audited and is **not** mutated here.
- `genesisconductor.io` was password-gated at audit; `optimizationinversion.com` returned 503.
- NSF CAIG #2530747 is HOLD (ORCID/Dimensions pointer only).
- Landauer \(k_B T \ln 2\) is physics, not a product SLA.

## Layout

| Path | Role |
|---|---|
| `00_EXECUTIVE_ALIGNMENT.md` | Operator brief |
| `01_RUBRIC_SCORECARD.md` | Admit / hold / reject |
| `immediate_actions.md` | P0–P3 checklist |
| `seo/` | Keywords, GA4, DNS notes |
| `aeo/` | Answer capsules + 30-prompt battery |
| `geo/` | Citation moats |
| `schema/jsonld.json` | Person / SoftwareApplication / WebSite |
| `llms/` | `llms.txt` drafts for apex hosts |
| `github/` | CODEOWNERS, Containerfile, bench harness |
| `trace/` | Execution ledger |

## Reproduce locally

```bash
podman build -t brand-align:2026-09-14 -f github/Containerfile .
podman run --rm brand-align:2026-09-14
```

## Owner

CODEOWNERS: `igor@kovachenterprises.com`  
ORCID: `0009-0008-8389-1297`
