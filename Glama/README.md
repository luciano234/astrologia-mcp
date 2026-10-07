# Publish on Glama / Publicar en Glama

**Where / Dónde:** https://glama.ai/mcp/servers → **Add Server**.

**EN:** Glama reads the files straight from the GitHub repository.
`glama.json` and `Dockerfile` **must be at the repository root**; the files in
this folder are reference copies. If you change one, change the root copy too.

**ES:** Glama lee los archivos directamente del repositorio de GitHub.
`glama.json` y `Dockerfile` **deben estar en la raíz del repositorio**; los de
esta carpeta son copias de referencia. Si cambias alguno, cambia también el de
la raíz.

| File / Archivo | Purpose / Para qué |
|---|---|
| `glama.json` | Claim ownership (maintainer `luciano234`) / Reclamar la propiedad (mantenedor `luciano234`) |
| `Dockerfile` | Lets Glama build the server, list its tools and score it / Que Glama construya el servidor, liste sus herramientas y lo puntúe |
| `.dockerignore` | Keeps unneeded files out of the image / Excluye archivos innecesarios de la imagen |

## Steps / Pasos

1. **EN:** Push the changes to the repository.
   **ES:** Sube los cambios al repositorio (push).
2. **EN:** On Glama click **Add Server** and paste `https://github.com/luciano234/astrologia-mcp`.
   **ES:** En Glama pulsa **Add Server** y pega `https://github.com/luciano234/astrologia-mcp`.
3. **EN:** Sign in with the `luciano234` GitHub account and **Claim** the server; Glama verifies it with `glama.json`.
   **ES:** Inicia sesión con la cuenta de GitHub `luciano234` y reclama el servidor (**Claim**); Glama lo verifica con `glama.json`.
4. **EN:** In the server dashboard, run the Dockerfile build. The start command is `astrologia-mcp` (stdio) and no environment variables are needed.
   **ES:** En el panel del servidor, lanza la build del Dockerfile. El comando de inicio es `astrologia-mcp` (stdio) y no necesita variables de entorno.
5. **EN (optional):** Add the badge Glama gives you to the top of `README.md`.
   **ES (opcional):** Añade al principio del `README.md` el badge que te da Glama.

**EN:** Before publishing, check that the image builds.
**ES:** Antes de publicar, comprueba que la imagen se construye:

```bash
docker build -t astrologia-mcp .
```
