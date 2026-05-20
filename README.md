# SmartMarket MVP (Web-Only)

MVP full stack com Flutter **Web** + FastAPI + PostgreSQL + Firebase Auth + OCR (ML Kit em evolução para Web).

## Estrutura

```bash
smartmarket/
├── mobile/
├── backend/
├── database/
├── docs/
├── .github/workflows/
├── scripts/
├── docker/
├── README.md
├── LICENSE
├── .gitignore
└── .env.example
```

## Decisão atual de escopo
Para simplificar a entrega do MVP e acelerar aprendizado/desenvolvimento:
- **Somente Web no momento**.
- Android e iOS ficam para a próxima versão.

## Funcionalidades MVP
- Google SSO (estrutura no app pronta para integração Firebase Web).
- Lista de compras manual (arquitetura preparada em camadas).
- Upload de nota e OCR (parser simplificado no backend).
- Histórico de compras.
- Catálogo inicial de produtos.

## Rodar backend
```bash
cp .env.example .env
docker compose up --build
```

## Rodar frontend (Web)
```bash
cd mobile
flutter pub get
flutter run -d chrome
```

## API endpoints
- `GET /api/health`
- `GET /api/products`
- `POST /api/purchases`
- `POST /api/ocr/parse`

## Arquitetura
- **presentation/domain/data** no frontend Flutter.
- **api/services/repositories/models/schemas** no backend.
- Repository + DTO + DI via providers e dependências FastAPI.
