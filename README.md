# Astrologia MCP

Servidor MCP local en español que permite a asistentes compatibles consultar
herramientas astrologicas de la API publica de [CosmyDay](https://cosmyday.com).

Este proyecto se distribuye bajo la licencia [MIT](LICENSE). La licencia cubre
el codigo del proyecto, no los datos ni los servicios de CosmyDay.

## Que API utiliza

Este proyecto **no ofrece una API REST propia**. Es un servidor MCP: expone
herramientas al asistente y consulta la API de CosmyDay en
`https://api.cosmyday.com`. La API no requiere clave ni cuenta, pero se necesita
conexion a Internet para usar las herramientas.

La API de CosmyDay tambien requiere atribucion visible a CosmyDay.com cuando sus
datos se usen comercialmente. Revisa sus condiciones antes de publicar o
distribuir una aplicacion que muestre esos datos.

## Herramientas disponibles

- `natal`: posiciones planetarias, casas y aspectos de nacimiento.
- `search_location`: busca las coordenadas de una localidad.
- `events_upcoming` y `event_kinds`: eventos celestes proximos y sus categorias.
- `daily_horoscope`, `weekly_horoscope`, `monthly_horoscope`: horoscopos.
- `monthly_archive_list` y `monthly_archive`: archivo de horoscopos mensuales.
- `moon_phase`, `transit_today`, `week_ahead`, `monthly_overview`.
- `health_check`: comprueba el estado de la API.

## Requisitos

- Python 3.10 o posterior.
- Internet.
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

Comprueba que el comando se instalo:

```powershell
astrologia-mcp
```

El proceso queda esperando mensajes MCP por la entrada/salida estandar; eso es
normal. Detenlo con `Ctrl+C`.

## Conectar Claude Code

Con [uv](https://docs.astral.sh/uv/) instalado, Claude Code puede instalar y
ejecutar el servidor directamente desde GitHub:

```powershell
claude mcp add --scope user --transport stdio astrologia -- uvx --from git+https://github.com/luciano234/astrologia-mcp.git astrologia-mcp
```

Reinicia Claude Code o inicia una conversacion nueva. Usa `/mcp` para verificar
que `astrologia` esta conectado.

Si prefieres instalarlo en un entorno virtual siguiendo los pasos anteriores,
agrega el ejecutable `astrologia-mcp` como servidor `stdio` en tu
cliente MCP. En Windows, si Claude no encuentra el comando instalado, configura
la ruta completa al ejecutable dentro de `.venv\Scripts`.

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

Reinicia Claude Desktop para conectar. No compartas la configuracion de otros
servidores si contiene credenciales.

## Desarrollo local

```powershell
py -m pip install -r requirements.txt
py server.py
```

El archivo `app.py` crea la aplicacion HTTP de FastMCP para despliegues remotos;
el comando de instalacion de esta guia ejecuta el transporte local `stdio`.
