# Publish on Smithery / Publicar en Smithery

**Where / Dónde:** https://smithery.ai/new (sign in with GitHub / inicia sesión con GitHub).

**EN:** Smithery no longer uses `smithery.yaml`. For a Python server it accepts
an MCPB bundle or a public HTTP URL.

**ES:** Smithery ya no usa `smithery.yaml`. Para un servidor en Python acepta un
paquete MCPB o una URL HTTP pública.

## Option A (recommended): MCPB bundle, no hosting / Opción A (recomendada): paquete MCPB, sin hosting

| File / Archivo | Purpose / Para qué |
|---|---|
| `astrologia-mcp-1.1.0.mcpb` | Bundle to upload; users run it locally with `uv` / Paquete que se sube; los usuarios lo ejecutan en local con `uv` |
| `manifest.json` | Reference copy of the manifest inside the bundle / Copia del manifiesto que va dentro del paquete |

1. **EN:** At https://smithery.ai/new choose to publish a **local / stdio (MCPB)** server.
   **ES:** En https://smithery.ai/new elige publicar un servidor **local / stdio (MCPB)**.
2. **EN / ES:** Name / Nombre: `@luciano234/astrologia-mcp`.
3. **EN:** Upload `astrologia-mcp-1.1.0.mcpb`.
   **ES:** Sube `astrologia-mcp-1.1.0.mcpb`.

## Option B: remote URL / Opción B: URL remota

**EN:** Deploy the root Docker image to an HTTPS host (Render, Railway, Fly.io,
FastMCP Cloud…) with `MCP_TRANSPORT=http`, then publish the URL.

**ES:** Despliega la imagen Docker de la raíz en un servicio con HTTPS (Render,
Railway, Fly.io, FastMCP Cloud…) con `MCP_TRANSPORT=http`, y publica la URL:

```bash
npx @smithery/cli mcp publish "https://<your-domain>/mcp" -n @luciano234/astrologia-mcp
```

## New version / Versión nueva

**EN:** Bump the version in `pyproject.toml`, `manifest.json` and `server.py`,
then rebuild the bundle from the repository root and copy it here.

**ES:** Sube la versión en `pyproject.toml`, `manifest.json` y `server.py`;
luego regenera el paquete desde la raíz del repositorio y cópialo aquí:

```bash
npx @anthropic-ai/mcpb pack . Smithery/astrologia-mcp-<version>.mcpb
```
