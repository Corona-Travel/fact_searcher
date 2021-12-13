# fact_searcher

## Development

To run this service solo use following commands:
* Donwload script for database initialization in the root of the repository
  ```sh
  curl -O https://raw.githubusercontent.com/Corona-Travel/deploy/main/mongo-init.js
  ```
* Start services
  ```sh
  docker compose up
  ```
  or
  
      docker compose pull && docker compose down && docker compose rm && docker compose build && docker compose up --build --force-recreate -d && docker compose logs -f
