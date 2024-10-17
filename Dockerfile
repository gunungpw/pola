FROM ghcr.io/astral-sh/uv:alpine3.20

WORKDIR /app

# Copy the application into the container.
COPY ./pyproject.toml /app
COPY ./uv.lock /app

RUN apk add --no-cache python3~=3.12

RUN uv sync --frozen --no-cache --compile-bytecode

COPY . /app

# Run the application.
CMD ["uv", "run", "rio", "run", "--port", "80", "--release", "--public"]
