#!/usr/bin/env bash
set -e

echo "[1/2] Subindo backend + PostgreSQL..."
docker compose up --build -d

echo "[2/2] Iniciando Flutter Web..."
cd mobile
flutter pub get
flutter run -d chrome
