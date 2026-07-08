FROM caddy:2-alpine
COPY index.html /srv/index.html
COPY img /srv/img
CMD ["sh", "-c", "caddy file-server --root /srv --listen :${PORT:-80}"]
