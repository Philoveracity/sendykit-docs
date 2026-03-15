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

- **`sendykit/docs-site`** for canonical Mintlify content
- **`sendykit/docs/openapi/sendykit-v2.yaml`** for canonical API truth
- **`sendykit-docs`** as the public publishing repo

### Sync from canonical repo

```bash
cd /home/thedream/mail.thedream.rocks/sendykit
make openapi-sync
```

That now syncs:

- canonical `docs-site/*` content into this public repo
- `docs/openapi/sendykit-v2.yaml` into `api-reference/openapi.json`

GitHub Actions also runs this sync on pushes touching `docs-site/**`, OpenAPI, or sync automation.

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
