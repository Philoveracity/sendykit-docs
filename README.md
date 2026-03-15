# SendyKit Public Docs

Public Mintlify repo for `docs.sendykit.dev`.

## Source of truth

This repo is the **public publishing surface**.
The canonical product/docs source lives in the main SendyKit repo:

- product/docs repo: `/home/thedream/mail.thedream.rocks/sendykit`
- canonical docs content: `/home/thedream/mail.thedream.rocks/sendykit/docs-site`
- canonical OpenAPI spec: `/home/thedream/mail.thedream.rocks/sendykit/docs/openapi/sendykit-v2.yaml`

## Efficient workflow

Use this split:

- **OpenAPI** for API truth
- **Mintlify** for public rendering
- **MDX** for guides, concepts, pricing, readiness, and operator explanation

### Sync OpenAPI

```bash
cd /home/thedream/mail.thedream.rocks/sendykit-docs
python3 scripts/sync-openapi.py
```

That updates:

- `api-reference/openapi.json`

from the canonical spec in the main SendyKit repo.

## Preview locally

```bash
npm i -g mint
mint dev
```

## Publish

Push to the default branch:

```bash
git push origin main
```

Mintlify/Vercel should sync from the public repo automatically.
