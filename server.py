import os
from typing import Annotated, Literal, Optional

import httpx
from fastmcp import FastMCP
from pydantic import Field

BASE_URL = "https://api.cosmyday.com"
USER_AGENT = "astrologia-mcp/1.1"
FUENTE = "CosmyDay (https://cosmyday.com)"

Sign = Literal[
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces",
]

SIGN_HELP = "Zodiac sign in English, lowercase; omit for all twelve / Signo en inglés y minúsculas; omítelo para los doce"

# All tools only read data from an external API.
# Todas las herramientas solo leen datos de una API externa.
READ_ONLY = {"readOnlyHint": True, "idempotentHint": True, "openWorldHint": True}

mcp = FastMCP(
    "Astrologia Cosmyday",
    version="1.1.0",
    instructions=(
        "Astrology tools powered by the public CosmyDay API: natal charts, transits, sky events "
        "and horoscopes. For a natal chart, call search_location first to get lat/lon, then natal. "
        "Signs are written in English and lowercase (e.g. 'leo'). When showing the data, always "
        f"include the attribution: Source: {FUENTE}.\n\n"
        "Herramientas de astrología basadas en la API pública de CosmyDay: cartas natales, "
        "tránsitos, eventos celestes y horóscopos. Para una carta natal, usa primero "
        "search_location para obtener lat/lon y luego natal. Los signos se escriben en inglés "
        "y minúsculas (ej. 'leo'). Al mostrar los datos, incluye siempre la atribución: "
        f"Fuente: {FUENTE}."
    ),
)


async def _request(method: str, path: str, **kwargs) -> dict:
    async with httpx.AsyncClient(base_url=BASE_URL, headers={"User-Agent": USER_AGENT}, timeout=30.0) as client:
        response = await client.request(method, path, **kwargs)
        response.raise_for_status()
        data = response.json()
    if not isinstance(data, dict):
        data = {"resultados": data}
    data["fuente"] = FUENTE
    return data


# --- Charts / Cartas ---

@mcp.tool(annotations={"title": "Natal chart / Carta natal", **READ_ONLY})
async def natal(
    year: Annotated[int, Field(description="Birth year, e.g. 1968 / Año de nacimiento, ej. 1968", ge=1800, le=2400)],
    month: Annotated[int, Field(description="Month (1-12) / Mes (1-12)", ge=1, le=12)],
    day: Annotated[int, Field(description="Day of month (1-31) / Día del mes (1-31)", ge=1, le=31)],
    hour: Annotated[int, Field(description="Local birth hour (0-23) / Hora local de nacimiento (0-23)", ge=0, le=23)],
    minute: Annotated[int, Field(description="Minute (0-59) / Minuto (0-59)", ge=0, le=59)],
    lat: Annotated[float, Field(description="Birthplace latitude (use search_location) / Latitud del lugar de nacimiento (usa search_location)", ge=-90, le=90)],
    lon: Annotated[float, Field(description="Birthplace longitude (use search_location) / Longitud del lugar de nacimiento (usa search_location)", ge=-180, le=180)],
) -> dict:
    """Planetary positions, house cusps and aspects for a birth moment. Time is local to the given coordinates; the time zone is resolved automatically.
    Posiciones planetarias, cúspides de casas y aspectos para un momento de nacimiento. La hora es local a las coordenadas dadas; la zona horaria se resuelve automáticamente.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    payload = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "lat": lat,
        "lon": lon,
    }
    return await _request("POST", "/natal", json=payload)


@mcp.tool(annotations={"title": "Search location / Buscar ubicación", **READ_ONLY})
async def search_location(
    q: Annotated[str, Field(description="Place name, e.g. 'Maracaibo' or 'Madrid, Spain' / Nombre del lugar, ej. 'Maracaibo' o 'Madrid, España'", min_length=1)],
) -> dict:
    """Converts a place name into the coordinates needed by natal (via OpenStreetMap Nominatim).
    Convierte un nombre de lugar en las coordenadas que necesita natal (vía OpenStreetMap Nominatim).
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/search-location", params={"q": q})


# --- Sky events / Eventos celestes ---

@mcp.tool(annotations={"title": "Upcoming sky events / Próximos eventos celestes", **READ_ONLY})
async def events_upcoming(
    days: Annotated[int, Field(description="How many days ahead to search / Cuántos días hacia adelante buscar", ge=1, le=1825)] = 30,
    min_importance: Annotated[Optional[int], Field(description="Minimum importance (0-100) / Importancia mínima (0-100)", ge=0, le=100)] = None,
    kind: Annotated[Optional[str], Field(description="Event type (see event_kinds), e.g. 'new_moon', 'retrograde_start' / Tipo de evento (ver event_kinds)")] = None,
    limit: Annotated[Optional[int], Field(description="Maximum number of events / Número máximo de eventos", ge=1)] = None,
    from_date: Annotated[Optional[str], Field(description="Start date yyyy-mm-dd (default: today) / Fecha inicial yyyy-mm-dd (por defecto, hoy)")] = None,
) -> dict:
    """Astrological events (retrogrades, lunations, eclipses, sign ingresses) in the next N days.
    Eventos astrológicos (retrogradaciones, lunaciones, eclipses, cambios de signo) en los próximos N días.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    params = {"days": days}
    if min_importance is not None:
        params["min_importance"] = min_importance
    if kind is not None:
        params["kind"] = kind
    if limit is not None:
        params["limit"] = limit
    if from_date is not None:
        params["from_date"] = from_date
    return await _request("GET", "/events/upcoming", params=params)


@mcp.tool(annotations={"title": "Event kinds / Tipos de evento", **READ_ONLY})
async def event_kinds() -> dict:
    """Lists all available event kinds with their counts.
    Lista todos los tipos de evento disponibles junto con su conteo.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/events/kinds")


# --- Horoscope content / Horóscopos ---

@mcp.tool(annotations={"title": "Daily horoscope / Horóscopo diario", **READ_ONLY})
async def daily_horoscope(
    sign: Annotated[Optional[Sign], Field(description=SIGN_HELP)] = None,
) -> dict:
    """Daily horoscope. Without 'sign' returns all twelve signs; with 'sign' returns only that sign (English, lowercase, e.g. 'leo').
    Horóscopo diario. Sin 'sign' devuelve los doce signos; con 'sign' devuelve solo ese signo (en inglés y minúsculas, ej. 'leo').
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    path = f"/content/daily/{sign}" if sign else "/content/daily"
    return await _request("GET", path)


@mcp.tool(annotations={"title": "Weekly horoscope / Horóscopo semanal", **READ_ONLY})
async def weekly_horoscope(
    sign: Annotated[Optional[Sign], Field(description=SIGN_HELP)] = None,
) -> dict:
    """Weekly horoscope. Without 'sign' returns all twelve signs; with 'sign' returns only that sign.
    Horóscopo semanal. Sin 'sign' devuelve los doce signos; con 'sign' devuelve solo ese signo.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    path = f"/content/weekly/{sign}" if sign else "/content/weekly"
    return await _request("GET", path)


@mcp.tool(annotations={"title": "Monthly horoscope / Horóscopo mensual", **READ_ONLY})
async def monthly_horoscope(
    sign: Annotated[Optional[Sign], Field(description=SIGN_HELP)] = None,
) -> dict:
    """Monthly horoscope. Without 'sign' returns all twelve signs; with 'sign' returns only that sign.
    Horóscopo mensual. Sin 'sign' devuelve los doce signos; con 'sign' devuelve solo ese signo.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    path = f"/content/monthly/{sign}" if sign else "/content/monthly"
    return await _request("GET", path)


@mcp.tool(annotations={"title": "Monthly archive list / Lista del archivo mensual", **READ_ONLY})
async def monthly_archive_list() -> dict:
    """Lists all available archived sign-months.
    Lista todos los meses-signo archivados disponibles.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/content/monthly-archive/list")


@mcp.tool(annotations={"title": "Archived monthly horoscope / Horóscopo mensual archivado", **READ_ONLY})
async def monthly_archive(
    sign: Annotated[Sign, Field(description="Zodiac sign in English, lowercase, e.g. 'leo' / Signo en inglés y minúsculas, ej. 'leo'")],
    yyyy_mm: Annotated[str, Field(description="Month as yyyy-mm, e.g. '2026-03' / Mes en formato yyyy-mm, ej. '2026-03'", pattern=r"^\d{4}-\d{2}$")],
) -> dict:
    """Archived monthly horoscope for a specific sign and month (yyyy-mm format, e.g. '2026-03').
    Horóscopo mensual archivado para un signo y mes específicos (formato yyyy-mm, ej. '2026-03').
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", f"/content/monthly-archive/{sign}/{yyyy_mm}")


@mcp.tool(annotations={"title": "Moon phase / Fase lunar", **READ_ONLY})
async def moon_phase() -> dict:
    """Article about the current moon phase.
    Artículo sobre la fase lunar actual.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/content/moon")


@mcp.tool(annotations={"title": "Today's transits / Tránsitos de hoy", **READ_ONLY})
async def transit_today() -> dict:
    """Article about today's astrological transits.
    Artículo sobre los tránsitos astrológicos de hoy.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/content/transit")


@mcp.tool(annotations={"title": "Week ahead / Semana próxima", **READ_ONLY})
async def week_ahead() -> dict:
    """Astrological forecast for the next seven days.
    Pronóstico astrológico de los próximos siete días.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/content/week-ahead")


@mcp.tool(annotations={"title": "Monthly overview / Panorama del mes", **READ_ONLY})
async def monthly_overview() -> dict:
    """Article with the astrological overview of the month.
    Artículo con la visión general astrológica del mes.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/content/monthly-overview")


# --- Utility / Utilidades ---

@mcp.tool(annotations={"title": "API status / Estado de la API", **READ_ONLY})
async def health_check() -> dict:
    """API service status.
    Estado del servicio de la API.
    Source / Fuente: CosmyDay (https://cosmyday.com)"""
    return await _request("GET", "/health")


def main() -> None:
    # stdio by default; MCP_TRANSPORT=http serves Streamable HTTP at /mcp.
    # stdio por defecto; MCP_TRANSPORT=http lo sirve por Streamable HTTP en /mcp.
    if os.environ.get("MCP_TRANSPORT", "stdio").lower() == "http":
        mcp.run(
            transport="http",
            host=os.environ.get("HOST", "0.0.0.0"),
            port=int(os.environ.get("PORT", "8000")),
        )
    else:
        mcp.run()


if __name__ == "__main__":
    main()
