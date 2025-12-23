# Rock Paper Scissors Backend

Stateless FastAPI service for Rock-Paper-Scissors with clean layering to allow easy future persistence without changing the API.

- Base URL: http://localhost:3001
- Docs: /docs
- OpenAPI: /openapi.json

Endpoints:
- GET /           Health check
- POST /play      Play a round

POST /play request body:
{
  "choice": "rock" | "paper" | "scissors"
}

Response:
{
  "player": "rock" | "paper" | "scissors",
  "computer": "rock" | "paper" | "scissors",
  "result": "win" | "lose" | "draw"
}

Structure:
- src/domain: Pure domain model and rules
- src/services: Application services (stateless orchestration)
- src/api/schemas.py: Pydantic request/response models
- src/api/routers: Route handlers
- src/api/app.py: App factory and wiring
- src/api/main.py: ASGI entrypoint (app)
- src/core: Shared config and OpenAPI metadata

Extending with persistence:
Introduce a repository interface and an implementation under, e.g., src/infrastructure, then inject into GameService without changing routers or schemas.
