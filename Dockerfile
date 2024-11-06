FROM ghcr.io/astral-sh/uv:latest

WORKDIR /app

# Copy the application into the container.
COPY ./pyproject.toml /app/

RUN uv sync --frozen --no-cache --compile-bytecode

COPY /pola /rio.toml /app/

# Run the application.
CMD ["uv", "run", "rio", "run", "--release", "--public"]
