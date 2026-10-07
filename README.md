# Astrologia MCP

Bilingual (English / Spanish) MCP server that gives AI assistants astrology tools powered by the
public [CosmyDay](https://cosmyday.com) API: natal charts, today's transits,
moon phase, upcoming sky events and daily/weekly/monthly horoscopes.

- **No API key, no account.** Only an internet connection is required.
- **14 read-only tools** with typed, validated parameters; descriptions in
  English and Spanish.
- **stdio and Streamable HTTP** transports, Docker image and MCPB bundle.
- Every response includes the attribution field
  `"fuente": "CosmyDay (https://cosmyday.com)"`.

> Español más abajo: [Astrologia MCP (español)](#astrologia-mcp-español).

## Tools

| Tool | What it does | Parameters |
|---|---|---|
| `natal` | Planet positions, Placidus house cusps, aspects and Part of Fortune | `year`, `month`, `day`, `hour`, `minute` (local time), `lat`, `lon` |
| `search_location` | Place name → coordinates (OpenStreetMap Nominatim) | `q` |
| `transit_today` | Today's sky summary, top aspects and interpretation | — |
| `moon_phase` | Article about the current moon phase | — |
| `week_ahead` | Astrological forecast for the next seven days | — |
| `monthly_overview` | Astrological overview of the month | — |
| `events_upcoming` | Lunations, eclipses, retrogrades, ingresses, seasons | `days`, `min_importance`, `kind`, `limit`, `from_date` (all optional) |
| `event_kinds` | Available event types and counts | — |
| `daily_horoscope` | Daily horoscope (all signs or one) | `sign` (optional) |
| `weekly_horoscope` | Weekly horoscope | `sign` (optional) |
| `monthly_horoscope` | Monthly horoscope | `sign` (optional) |
| `monthly_archive_list` | Archived sign/month horoscopes | — |
| `monthly_archive` | One archived monthly horoscope | `sign`, `yyyy_mm` |
| `health_check` | API status | — |

Signs are written in English and lowercase: `aries`, `taurus`, `gemini`,
`cancer`, `leo`, `virgo`, `libra`, `scorpio`, `sagittarius`, `capricorn`,
`aquarius`, `pisces`.

### Example prompts

- "Natal chart for 16/12/1968 at 00:09 in Maracaibo" (the assistant calls
  `search_location`, then `natal`).
- "Show me today's transits."
- "Which eclipses and retrogrades are coming in the next 90 days?"
- "Leo's horoscope for this week."

## Installation

Requires Python 3.10+ (or Docker). The easiest way is with
[uv](https://docs.astral.sh/uv/).

### Claude Code

```bash
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git astrologia-mcp
```

### Claude Desktop, Cursor, Windsurf and other clients

Add this to your client's MCP configuration (for Claude Desktop:
**Settings > Developer > Edit Config**, `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "astrologia": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/luciano234/astrologia-mcp.git",
        "astrologia-mcp"
      ]
    }
  }
}
```

### Install a specific version from GitHub

Every release is a Git tag (see [CHANGELOG.md](CHANGELOG.md)). Add `@<tag>` to
the GitHub URL to pin a version instead of using the latest commit:

```bash
uvx --from git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0 astrologia-mcp
```

```bash
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0 astrologia-mcp
```

With pip:

```bash
pip install git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0
```

In a JSON client configuration, use
`"git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0"` as the
`--from` argument.

### MCPB bundle (one-click install)

Download `astrologia-mcp-<version>.mcpb` from the
[Releases](https://github.com/luciano234/astrologia-mcp/releases) page and open
it with Claude Desktop. To build it yourself:

```bash
npx @anthropic-ai/mcpb pack
```

### Docker

```bash
docker build -t astrologia-mcp .
docker run -i --rm astrologia-mcp
```

Client configuration:

```json
{
  "mcpServers": {
    "astrologia": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "astrologia-mcp"]
    }
  }
}
```

### Streamable HTTP (remote deployments)

```bash
MCP_TRANSPORT=http PORT=8000 astrologia-mcp
```

The endpoint is `http://<host>:8000/mcp`. With Docker:
`docker run --rm -e MCP_TRANSPORT=http -p 8000:8000 astrologia-mcp`.
`app.py` also exposes an ASGI app (`app:app`) for platforms that run Uvicorn.

| Variable | Default | Description |
|---|---|---|
| `MCP_TRANSPORT` | `stdio` | `stdio` or `http` |
| `HOST` | `0.0.0.0` | Bind address in HTTP mode |
| `PORT` | `8000` | Port in HTTP mode |

## Local development

```bash
git clone https://github.com/luciano234/astrologia-mcp.git
cd astrologia-mcp
python -m pip install -e .
npx @modelcontextprotocol/inspector python server.py
```

## Data and attribution

This project does **not** provide its own data. It queries the public CosmyDay
API at `https://api.cosmyday.com` (computed with Swiss Ephemeris). CosmyDay
requires visible attribution to CosmyDay.com when its data is used
commercially; review its terms before publishing an application that displays
the data. Tool descriptions and responses include the credit
"Source / Fuente: CosmyDay (https://cosmyday.com)".

## License

[MIT](LICENSE). The license covers this project's code, not CosmyDay's data or
services.

---

# Astrologia MCP (español)

Servidor MCP bilingüe (inglés / español) que da a los asistentes de IA herramientas de
astrología con datos de la API pública de [CosmyDay](https://cosmyday.com):
cartas natales, tránsitos del día, fase lunar, próximos eventos celestes y
horóscopos diarios, semanales y mensuales.

- **Sin clave de API ni cuenta.** Solo hace falta conexión a Internet.
- **14 herramientas de solo lectura** con parámetros tipados y validados;
  descripciones en inglés y español.
- Transportes **stdio y Streamable HTTP**, imagen Docker y paquete MCPB.
- Todas las respuestas incluyen el campo de atribución
  `"fuente": "CosmyDay (https://cosmyday.com)"`.

## Herramientas

| Herramienta | Qué hace | Parámetros |
|---|---|---|
| `natal` | Posiciones planetarias, cúspides Placidus, aspectos y Parte de la Fortuna | `year`, `month`, `day`, `hour`, `minute` (hora local), `lat`, `lon` |
| `search_location` | Nombre de lugar → coordenadas (OpenStreetMap Nominatim) | `q` |
| `transit_today` | Resumen del cielo de hoy, aspectos principales e interpretación | — |
| `moon_phase` | Artículo sobre la fase lunar actual | — |
| `week_ahead` | Pronóstico de los próximos siete días | — |
| `monthly_overview` | Panorama astrológico del mes | — |
| `events_upcoming` | Lunaciones, eclipses, retrogradaciones, ingresos, estaciones | `days`, `min_importance`, `kind`, `limit`, `from_date` (opcionales) |
| `event_kinds` | Tipos de evento disponibles y su conteo | — |
| `daily_horoscope` | Horóscopo diario (todos los signos o uno) | `sign` (opcional) |
| `weekly_horoscope` | Horóscopo semanal | `sign` (opcional) |
| `monthly_horoscope` | Horóscopo mensual | `sign` (opcional) |
| `monthly_archive_list` | Horóscopos mensuales archivados | — |
| `monthly_archive` | Un horóscopo mensual archivado | `sign`, `yyyy_mm` |
| `health_check` | Estado de la API | — |

Los signos se escriben en inglés y minúsculas: `aries`, `taurus`, `gemini`,
`cancer`, `leo`, `virgo`, `libra`, `scorpio`, `sagittarius`, `capricorn`,
`aquarius`, `pisces`.

### Ejemplos de uso

- "Carta natal del 16/12/1968 a las 00:09 en Maracaibo" (el asistente llama a
  `search_location` y luego a `natal`).
- "Muéstrame los tránsitos de hoy."
- "¿Qué eclipses y retrogradaciones vienen en los próximos 90 días?"
- "Horóscopo semanal de leo."

## Instalación

Requiere Python 3.10+ (o Docker). Lo más sencillo es usar
[uv](https://docs.astral.sh/uv/).

### Claude Code

```bash
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git astrologia-mcp
```

### Claude Desktop, Cursor, Windsurf y otros clientes

Agrega esto a la configuración MCP de tu cliente (en Claude Desktop:
**Settings > Developer > Edit Config**, `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "astrologia": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/luciano234/astrologia-mcp.git",
        "astrologia-mcp"
      ]
    }
  }
}
```

### Instalar una versión concreta desde GitHub

Cada versión es una etiqueta (tag) de Git (ver [CHANGELOG.md](CHANGELOG.md)).
Añade `@<tag>` a la URL de GitHub para fijar una versión en lugar de usar el
último commit:

```bash
uvx --from git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0 astrologia-mcp
```

```bash
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0 astrologia-mcp
```

Con pip:

```bash
pip install git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0
```

En la configuración JSON de un cliente, usa
`"git+https://github.com/luciano234/astrologia-mcp.git@v1.1.0"` como argumento
de `--from`.

### Paquete MCPB (instalación con un clic)

Descarga `astrologia-mcp-<versión>.mcpb` desde
[Releases](https://github.com/luciano234/astrologia-mcp/releases) y ábrelo con
Claude Desktop. Para generarlo tú mismo:

```bash
npx @anthropic-ai/mcpb pack
```

### Docker

```bash
docker build -t astrologia-mcp .
docker run -i --rm astrologia-mcp
```

Configuración del cliente:

```json
{
  "mcpServers": {
    "astrologia": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "astrologia-mcp"]
    }
  }
}
```

### Streamable HTTP (despliegue remoto)

```bash
MCP_TRANSPORT=http PORT=8000 astrologia-mcp
```

El endpoint es `http://<host>:8000/mcp`. Con Docker:
`docker run --rm -e MCP_TRANSPORT=http -p 8000:8000 astrologia-mcp`.
`app.py` expone además una aplicación ASGI (`app:app`) para plataformas que
ejecutan Uvicorn.

| Variable | Por defecto | Descripción |
|---|---|---|
| `MCP_TRANSPORT` | `stdio` | `stdio` o `http` |
| `HOST` | `0.0.0.0` | Dirección de escucha en modo HTTP |
| `PORT` | `8000` | Puerto en modo HTTP |

## Desarrollo local

```bash
git clone https://github.com/luciano234/astrologia-mcp.git
cd astrologia-mcp
python -m pip install -e .
npx @modelcontextprotocol/inspector python server.py
```

## Datos y atribución

Este proyecto **no** ofrece datos propios: consulta la API pública de CosmyDay
en `https://api.cosmyday.com` (calculada con Swiss Ephemeris). CosmyDay requiere
atribución visible a CosmyDay.com cuando sus datos se usan comercialmente;
revisa sus condiciones antes de publicar una aplicación que muestre esos datos.
Las descripciones y las respuestas de las herramientas incluyen el crédito
"Source / Fuente: CosmyDay (https://cosmyday.com)".

## Licencia

[MIT](LICENSE). La licencia cubre el código de este proyecto, no los datos ni
los servicios de CosmyDay.
