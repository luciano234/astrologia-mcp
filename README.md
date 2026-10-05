# Astrologia MCP

Local MCP server that lets compatible assistants access astrology tools from the
public [CosmyDay](https://cosmyday.com) API.

This project is distributed under the [MIT License](LICENSE). The license
covers this project's code, not CosmyDay's data or services.

## Which API does it use?

This project does **not** provide its own REST API. It is an MCP server that
exposes tools to an assistant and queries the CosmyDay API at
`https://api.cosmyday.com`. The API does not require a key or account, but an
internet connection is required.

CosmyDay requires visible attribution to CosmyDay.com when its data is used
commercially. Review its terms before publishing or distributing an application
that displays the data.

## Available tools

- `natal`: planetary positions, houses, and aspects for a birth chart.
- `search_location`: looks up a place's coordinates.
- `events_upcoming` and `event_kinds`: upcoming sky events and their categories.
- `daily_horoscope`, `weekly_horoscope`, `monthly_horoscope`: horoscopes.
- `monthly_archive_list` and `monthly_archive`: archived monthly horoscopes.
- `moon_phase`, `transit_today`, `week_ahead`, `monthly_overview`.
- `health_check`: checks the API status.

## Requirements

- Python 3.10 or later.
- Internet access.
- An MCP-compatible client, such as Claude Code or Claude Desktop.

## Install from GitHub

Repository: `https://github.com/luciano234/astrologia-mcp`.

```powershell
git clone https://github.com/luciano234/astrologia-mcp.git
cd astrologia-mcp
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install .
```

To start the server:

```powershell
astrologia-mcp
```

The process waits for MCP messages over standard input/output; this is
expected. Press `Ctrl+C` to stop it.

## Connect Claude Code

With [uv](https://docs.astral.sh/uv/) installed, Claude Code can install and run
the server directly from GitHub:

```powershell
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git astrologia-mcp
```

Restart Claude Code or start a new conversation. Run `/mcp` to verify that
`astrologia` is connected.

If you installed it in a virtual environment using the steps above, add the
`astrologia-mcp` executable as an `stdio` server in your MCP client. On Windows,
if Claude cannot find the command, configure the full path to the executable
inside `.venv\Scripts`.

## Connect Claude Desktop

In Claude Desktop, open **Settings > Developer > Edit Config** and add the
server to `claude_desktop_config.json`. With `uv` installed, use:

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

Restart Claude Desktop to connect. Do not share configuration files containing
credentials for other servers.

## Local development

```powershell
py -m pip install -r requirements.txt
py server.py
```

The `app.py` file creates a FastMCP HTTP application for remote deployments;
the installation command in this guide runs the local `stdio` transport.

---

# Astrologia MCP (español)

Servidor MCP local que permite a asistentes compatibles consultar herramientas
astrológicas de la API pública de [CosmyDay](https://cosmyday.com).

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE). La licencia cubre
el código del proyecto, no los datos ni los servicios de CosmyDay.

## ¿Qué API utiliza?

Este proyecto **no ofrece una API REST propia**. Es un servidor MCP: expone
herramientas al asistente y consulta la API de CosmyDay en
`https://api.cosmyday.com`. La API no requiere clave ni cuenta, pero se necesita
conexión a Internet para usar las herramientas.

CosmyDay requiere atribución visible a CosmyDay.com cuando sus datos se utilicen
comercialmente. Revisa sus condiciones antes de publicar o distribuir una
aplicación que muestre esos datos.

## Herramientas disponibles

- `natal`: posiciones planetarias, casas y aspectos de nacimiento.
- `search_location`: busca las coordenadas de una localidad.
- `events_upcoming` y `event_kinds`: próximos eventos celestes y sus categorías.
- `daily_horoscope`, `weekly_horoscope`, `monthly_horoscope`: horóscopos.
- `monthly_archive_list` y `monthly_archive`: archivo de horóscopos mensuales.
- `moon_phase`, `transit_today`, `week_ahead`, `monthly_overview`.
- `health_check`: comprueba el estado de la API.

## Requisitos

- Python 3.10 o posterior.
- Conexión a Internet.
- Un cliente compatible con MCP, por ejemplo Claude Code o Claude Desktop.

## Instalar desde GitHub

Repositorio: `https://github.com/luciano234/astrologia-mcp`.

```powershell
git clone https://github.com/luciano234/astrologia-mcp.git
cd astrologia-mcp
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install .
```

Para iniciar el servidor:

```powershell
astrologia-mcp
```

El proceso queda esperando mensajes MCP por la entrada/salida estándar; eso es
normal. Pulsa `Ctrl+C` para detenerlo.

## Conectar Claude Code

Con [uv](https://docs.astral.sh/uv/) instalado, Claude Code puede instalar y
ejecutar el servidor directamente desde GitHub:

```powershell
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git astrologia-mcp
```

Reinicia Claude Code o inicia una conversación nueva. Ejecuta `/mcp` para
verificar que `astrologia` está conectado.

Si prefieres instalarlo en un entorno virtual siguiendo los pasos anteriores,
agrega el ejecutable `astrologia-mcp` como servidor `stdio` en tu cliente MCP.
En Windows, si Claude no encuentra el comando, configura la ruta completa al
ejecutable dentro de `.venv\Scripts`.

## Conectar Claude Desktop

En Claude Desktop, abre **Settings > Developer > Edit Config** y agrega el
servidor a `claude_desktop_config.json`. Con `uv` instalado, usa:

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

Reinicia Claude Desktop para conectarlo. No compartas archivos de configuración
que contengan credenciales de otros servidores.

## Desarrollo local

```powershell
py -m pip install -r requirements.txt
py server.py
```

El archivo `app.py` crea una aplicación HTTP de FastMCP para despliegues
remotos; el comando de instalación de esta guía ejecuta el transporte local
`stdio`.
