# sunnysmith.com

Personal site for Sunny P Smith — themed after *Colossus: The Forbin Project* (1970) and *WarGames* (1983).

## Features

- **CRT terminal aesthetic** — scanlines, sweep line, vignette, and subtle screen flicker
- **Typewriter animation** — terminal lines type out sequentially with keystroke audio
- **Ambient mainframe audio** — 60Hz hum, electronics hiss, random data blips (Web Audio API, no files)
- **Dual thought stacks** — primary and secondary project/link lists load in sequence
- **WarGames easter egg** — 30 seconds after boot, the system types *"GREETINGS PROFESSOR SMITH. SHALL WE PLAY A GAME?"*
- **Contact form** — Colossus-styled form backed by a Python API that delivers via Postfix
- **Fully responsive** — mobile-friendly with data streams hidden on small screens

## Stack

- **Frontend:** Vanilla HTML/CSS/JS, Google Fonts (Orbitron, Share Tech Mono)
- **Web server:** [Caddy](https://caddyserver.com/) with automatic TLS, gzip/zstd, HTTP/2
- **Contact API:** Python + Flask + Gunicorn, reverse proxied through Caddy
- **Mail:** Postfix (send-only, IPv4)
- **Server:** Ubuntu 24.04 LTS on Linode

## Files

```
index.html          — main site
contact.html        — contact form page
contact-api.py      — form submission handler (Flask)
assets/images/      — logo + mainframe background
```

## Deployment

The site is served from `/var/www/sunnysmith.com` by Caddy. The contact form runs as a systemd service (`contact-form.service`) with Gunicorn on `localhost:5000`, reverse proxied at `/api/contact`.

## License

All rights reserved.
