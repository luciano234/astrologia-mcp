# Changelog / Registro de cambios

## [1.1.0] - 2026-10-07

**EN**
- Tool descriptions, titles and parameters in English and Spanish.
- Every tool description and response credits CosmyDay
  (`"fuente": "CosmyDay (https://cosmyday.com)"`).
- Typed, validated parameters (signs, dates, coordinates) and read-only tool
  annotations.
- `search_location` and `monthly_archive_list` now return
  `{"resultados": [...]}` (fixes the "structured_content must be a dict" error).
- Streamable HTTP transport (`MCP_TRANSPORT=http`), Dockerfile, MCPB bundle and
  `glama.json` for publishing on mcp.so, Glama and Smithery.

**ES**
- Descripciones, títulos y parámetros de las herramientas en inglés y español.
- Cada descripción y cada respuesta acredita a CosmyDay
  (`"fuente": "CosmyDay (https://cosmyday.com)"`).
- Parámetros tipados y validados (signos, fechas, coordenadas) y anotaciones de
  solo lectura.
- `search_location` y `monthly_archive_list` devuelven ahora
  `{"resultados": [...]}` (corrige el error "structured_content must be a dict").
- Transporte Streamable HTTP (`MCP_TRANSPORT=http`), Dockerfile, paquete MCPB y
  `glama.json` para publicar en mcp.so, Glama y Smithery.

## [1.0.0] - 2026-10-05

- First version / Primera versión.

[1.1.0]: https://github.com/luciano234/astrologia-mcp/releases/tag/v1.1.0
[1.0.0]: https://github.com/luciano234/astrologia-mcp/commit/ffda384
