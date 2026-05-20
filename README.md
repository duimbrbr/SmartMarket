# SmartMarket MVP

MVP full stack com Flutter + FastAPI + PostgreSQL + Firebase Auth + OCR (ML Kit).

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

## Funcionalidades MVP
- Google SSO (estrutura no app pronta para integração Firebase).
- Lista de compras manual (arquitetura preparada em camadas).
- Upload de nota e OCR (ML Kit no mobile, parser simplificado no backend).
- Histórico de compras.
- Catálogo inicial de produtos.

## Rodar backend
```bash
cp .env.example .env
docker compose up --build
```

## Rodar mobile
```bash
cd mobile
flutter pub get
flutter run
```

## API endpoints
- `GET /api/health`
- `GET /api/products`
- `POST /api/purchases`
- `POST /api/ocr/parse`

## Arquitetura
- **presentation/domain/data** no mobile.
- **api/services/repositories/models/schemas** no backend.
- Repository + DTO + DI via providers e dependências FastAPI.
