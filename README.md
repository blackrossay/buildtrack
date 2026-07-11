# 🏗️ Murehwa Villa — Build Tracker

An offline-capable construction tracking & management app for a double-storey villa build in **Murehwa, Mashonaland East, Zimbabwe** (8,000 m² communal plot · 2,000 m² house zone).

The production app is a single, self-contained **`index.html`** — no server or internet required. All data is stored privately on your device (localStorage + IndexedDB for photos).

## Features

- **Dashboard** — animated progress ring, KPI tiles, projected completion forecast, and a **Gantt schedule**.
- **6 build stages** — Foundation → Slab → Mid-slab deck → Parapet → Hidden IBR roof → Windows/Glazing & Fittings. Checkable action steps & material lists, per-stage notes, target dates and **photos**.
- **Materials** — master procurement checklist + brick logistics (80,000 bricks).
- **Budget** — expense logging, spend-by-stage bars, and **labour cost tracking** (materials + labour = total outlay).
- **Activity log** — Bought / Added / Removed / Completed / Note, with optional cost and photos.
- **Printable PDF report** and full JSON backup/restore (including photos).
- **Apple-style UI** — light/dark, animations, haptics, confetti on stage completion. Green ColorHunt branding.

## Run locally

Just open `index.html` in any modern browser — that's it.

## Deployment

Deployed as a static site on **Vercel** (`vercel.json` serves `index.html` at the root).

## Roadmap

- `villa-dashboard/` — an in-progress **React + Vite + Tailwind** enterprise dashboard redesign.
