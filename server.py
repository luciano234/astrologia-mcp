from typing import Optional

import httpx
from fastmcp import FastMCP

BASE_URL = "https://api.cosmyday.com"
USER_AGENT = "astrologia-mcp/1.0"

mcp = FastMCP("Astrologia Cosmyday")


async def _request(method: str, path: str, **kwargs) -> dict:
    async with httpx.AsyncClient(base_url=BASE_URL, headers={"User-Agent": USER_AGENT}, timeout=30.0) as client:
        response = await client.request(method, path, **kwargs)
        response.raise_for_status()
        return response.json()


# --- Charts ---

@mcp.tool
async def natal(year: int, month: int, day: int, hour: int, minute: int, lat: float, lon: float) -> dict:
    """Posiciones planetarias, cúspides de casas y aspectos para un momento de nacimiento.
    La hora es local a las coordenadas dadas; la zona horaria se resuelve automáticamente."""
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


@mcp.tool
async def search_location(q: str) -> dict:
    """Convierte un nombre de lugar en las coordenadas que necesita /natal (vía OpenStreetMap Nominatim)."""
    return await _request("GET", "/search-location", params={"q": q})


# --- Sky events ---

@mcp.tool
async def events_upcoming(
    days: int = 30,
    min_importance: Optional[int] = None,
    kind: Optional[str] = None,
    limit: Optional[int] = None,
    from_date: Optional[str] = None,
) -> dict:
    """Eventos astrológicos (retrogradaciones, lunaciones, eclipses, cambios de signo) en los próximos N días."""
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


@mcp.tool
async def event_kinds() -> dict:
    """Lista todos los tipos de evento disponibles junto con su conteo."""
    return await _request("GET", "/events/kinds")


# --- Horoscope content ---

@mcp.tool
async def daily_horoscope(sign: Optional[str] = None) -> dict:
    """Horóscopo diario. Sin 'sign' devuelve los doce signos; con 'sign' devuelve solo ese signo (en inglés y minúsculas, ej. 'leo')."""
    path = f"/content/daily/{sign}" if sign else "/content/daily"
    return await _request("GET", path)


@mcp.tool
async def weekly_horoscope(sign: Optional[str] = None) -> dict:
    """Horóscopo semanal. Sin 'sign' devuelve los doce signos; con 'sign' devuelve solo ese signo."""
    path = f"/content/weekly/{sign}" if sign else "/content/weekly"
    return await _request("GET", path)


@mcp.tool
async def monthly_horoscope(sign: Optional[str] = None) -> dict:
    """Horóscopo mensual. Sin 'sign' devuelve los doce signos; con 'sign' devuelve solo ese signo."""
    path = f"/content/monthly/{sign}" if sign else "/content/monthly"
    return await _request("GET", path)


@mcp.tool
async def monthly_archive_list() -> dict:
    """Lista todos los meses-signo archivados disponibles."""
    return await _request("GET", "/content/monthly-archive/list")


@mcp.tool
async def monthly_archive(sign: str, yyyy_mm: str) -> dict:
    """Horóscopo mensual archivado para un signo y mes específicos (formato yyyy-mm, ej. '2026-03')."""
    return await _request("GET", f"/content/monthly-archive/{sign}/{yyyy_mm}")


@mcp.tool
async def moon_phase() -> dict:
    """Artículo sobre la fase lunar actual."""
    return await _request("GET", "/content/moon")


@mcp.tool
async def transit_today() -> dict:
    """Artículo sobre los tránsitos astrológicos de hoy."""
    return await _request("GET", "/content/transit")


@mcp.tool
async def week_ahead() -> dict:
    """Pronóstico astrológico de los próximos siete días."""
    return await _request("GET", "/content/week-ahead")


@mcp.tool
async def monthly_overview() -> dict:
    """Artículo con la visión general astrológica del mes."""
    return await _request("GET", "/content/monthly-overview")


# --- Utility ---

@mcp.tool
async def health_check() -> dict:
    """Estado del servicio de la API."""
    return await _request("GET", "/health")


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
