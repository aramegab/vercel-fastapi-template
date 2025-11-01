<div align="center">

# 🚀 FastAPI on Vercel – Starter Template

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com)
[![Python](https://img.shields.io/badge/python-3.12+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)

### **[English](#-english-version) | [Русский](#-русская-версия)**

</div>

---

<a name="english-version"></a>

## English Version

<div align="center">

*Production-ready FastAPI starter configured to run on Vercel's Python runtime as an ASGI app*

[Features](#-features) • [Quick Start](#-quick-start) • [API Reference](#-api-reference) • [Project Structure](#-project-structure) • [Deployment](#-deployment)

</div>

---

### 📋 Overview

A modern, production-ready FastAPI template optimized for deployment on Vercel. This starter includes:

- ⚡ **Async/Sync patterns** with httpx and asyncer for concurrent operations
- 🔒 **Type-safe responses** using Pydantic v2 generics
- 🌐 **CORS configured** and ready for cross-origin requests
- 📦 **Versioned API routing** under `/api/v1` with example weather endpoints
- 🎯 **Zero-config deployment** on Vercel with automatic ASGI detection

---

### ✨ Features


| Feature                | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| **ASGI Entrypoint**    | `api/index.py` exports `app` for automatic Vercel detection             |
| **Versioned Routing**  | API endpoints organized under`/api/v1` prefix                           |
| **Async Concurrency**  | Built-in helpers via`asyncer` and `httpx.AsyncClient`                   |
| **Typed Responses**    | Generic response models with Pydantic v2 (`schemas/response_schema.py`) |
| **Environment Config** | Settings management via`pydantic-settings`                              |
| **CORS Ready**         | Pre-configured CORS middleware in`core/config.py`                       |
| **Example Endpoints**  | Weather API demonstrating sync/async/concurrent patterns                |

---

### 🚀 Quick Start

#### Prerequisites

- **Python 3.12+** recommended
- `pip` or `uv` for dependency management

#### Installation

**Option 1: Using pip**

```bash
pip install -r requirements.txt
```

**Option 2: Using uv (faster)**

```bash
uv sync
```

#### Local Development

1. **Create environment file**

   ```bash
   cp .env.example .env
   ```
2. **Run the development server**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 9096
   ```

   Or using Vercel CLI:

   ```bash
   vercel dev
   ```
3. **Access the API**

   - 🌐 API: `http://127.0.0.1:9096`
   - 📖 Swagger UI: `http://127.0.0.1:9096/docs`
   - 📄 ReDoc: `http://127.0.0.1:9096/redoc`

---

### 📚 API Reference

#### Health Check


| Method | Endpoint | Description           | Response                     |
| ------ | -------- | --------------------- | ---------------------------- |
| `GET`  | `/`      | Health check endpoint | `{"message": "Hello World"}` |

#### Weather Endpoints (Sync)


| Method | Endpoint                     | Query Parameters          | Description                     |
| ------ | ---------------------------- | ------------------------- | ------------------------------- |
| `GET`  | `/api/v1/weather_sync/sync1` | `city` (default: "Quito") | Weather using sync work pattern |
| `GET`  | `/api/v1/weather_sync/sync2` | `city` (default: "Quito") | Weather using sync httpx client |

#### Weather Endpoints (Async)


| Method | Endpoint                                | Query Parameters                                      | Description                             |
| ------ | --------------------------------------- | ----------------------------------------------------- | --------------------------------------- |
| `GET`  | `/api/v1/weather_async`                 | `city` (default: "Quito")                             | Weather using async httpx client        |
| `GET`  | `/api/v1/weather_async_list/sequencial` | `cities[]` (default: ["Quito", "Miami", "Barcelona"]) | Sequential requests for multiple cities |
| `GET`  | `/api/v1/weather_async_list/concurrent` | `cities[]` (default: ["Quito", "Miami", "Barcelona"]) | ⚡ Concurrent requests (faster)         |

#### Example Requests

```bash
# Single city weather
curl "http://localhost:9096/api/v1/weather_async?city=London"

# Multiple cities (sequential)
curl "http://localhost:9096/api/v1/weather_async_list/sequencial?cities=Tokyo&cities=Paris"

# Multiple cities (concurrent - faster)
curl "http://localhost:9096/api/v1/weather_async_list/concurrent?cities=Tokyo&cities=Paris&cities=Berlin"
```

#### Response Format

All endpoints return a standardized response:

```json
{
  "success": true,
  "message": "Weather in London",
  "data": {
    "city": "London",
    "current_condition": [...],
    "weather": [...]
  },
  "meta": {
    "api_reference": "https://github.com/chubin/wttr.in"
  }
}
```

---

### 📁 Project Structure

```
vercel-fastapi-template/
├── 📂 api/
│   ├── 📂 v1/
│   │   ├── 📂 endpoints/
│   │   │   ├── __init__.py
│   │   │   └── weather.py          # Weather API endpoints
│   │   ├── __init__.py
│   │   └── api.py                  # Router aggregation
│   ├── __init__.py
│   └── index.py                    # 🎯 Vercel ASGI entrypoint
│
├── 📂 core/
│   ├── __init__.py
│   └── config.py                   # ⚙️ App settings & configuration
│
├── 📂 schemas/
│   ├── __init__.py
│   └── response_schema.py          # 📝 Pydantic response models
│
├── 📂 utils/
│   ├── 📂 exceptions/
│   │   ├── __init__.py
│   │   ├── common_exception.py     # Common exception handlers
│   │   ├── user_exceptions.py      # User-specific exceptions
│   │   └── user_follow_exceptions.py
│   ├── __init__.py
│   ├── partial.py                  # Utility functions
│   └── uuid6.py                    # UUID v6 implementation
│
├── 📂 test/
│   └── __init__.py
│
├── 📄 main.py                      # 🚀 FastAPI app initialization
├── 📄 pyproject.toml               # Project metadata & dependencies
├── 📄 requirements.txt             # 📦 Pip dependencies
├── 📄 uv.lock                      # UV lock file
├── 📄 vercel.json                  # ▲ Vercel configuration
├── 📄 .env.example                 # Environment variables template
├── 📄 .gitignore
└── 📄 README.md                    # This file
```

---

### ⚙️ Environment Variables

Create a `.env` file based on `.env.example`:


| Variable               | Type        | Default             | Description                                                 |
| ---------------------- | ----------- | ------------------- | ----------------------------------------------------------- |
| `PROJECT_NAME`         | `str`       | `"app"`             | API project name                                            |
| `MODE`                 | `str`       | `"development"`     | Environment mode:`development` \| `production` \| `testing` |
| `API_VERSION`          | `str`       | `"v1"`              | API version for routing                                     |
| `BACKEND_CORS_ORIGINS` | `list[str]` | `["*"]`             | Allowed CORS origins (comma-separated)                      |
| `WHEATER_URL`          | `str`       | `"https://wttr.in"` | Weather API base URL                                        |

#### Example `.env`

```env
PROJECT_NAME=FastAPI Vercel Starter
MODE=development
API_VERSION=v1
BACKEND_CORS_ORIGINS=["http://localhost:3000","https://yourdomain.com"]
WHEATER_URL=https://wttr.in
```

---

### 🚢 Deployment

#### Deploy to Vercel

This project is optimized for Vercel deployment with zero configuration needed.

**Method 1: Using Vercel CLI**

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

**Method 2: GitHub Integration**

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your repository
4. Click **Deploy** ✨

#### Vercel Configuration

The included `vercel.json` configures:

```json
{
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

- **Dependencies**: Resolved from `requirements.txt`
- **Entry Point**: `api/index.py` exports the FastAPI `app`
- **Routing**: All traffic routed to the ASGI application

---

### 🛠️ Common Tasks

#### Adding New Endpoints

1. Create a new router in `api/v1/endpoints/your_endpoint.py`
2. Define your routes using FastAPI decorators
3. Include the router in `api/v1/api.py`:

```python
from api.v1.endpoints import your_endpoint

api_router.include_router(your_endpoint.router, tags=["Your Feature"])
```

#### Configuring CORS

Edit `core/config.py`:

```python
BACKEND_CORS_ORIGINS: list[str] = [
    "http://localhost:3000",
    "https://yourdomain.com"
]
```

#### Updating Settings

1. Add new settings to `Settings` class in `core/config.py`
2. Add corresponding variables to `.env`
3. Access via `settings.YOUR_VARIABLE`

---

### 📦 Technology Stack

- **[FastAPI](https://fastapi.tiangolo.com)** - Modern, fast web framework
- **[Pydantic v2](https://docs.pydantic.dev)** - Data validation using Python type annotations
- **[httpx](https://www.python-httpx.org)** - Async HTTP client
- **[asyncer](https://asyncer.tiangolo.com)** - Async/sync compatibility layer
- **[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** - Settings management
- **[uvicorn](https://www.uvicorn.org)** - ASGI server

---

### 📝 Notes

- This template uses **Pydantic v2**. Generic response models derive from `BaseModel`
- Keep `requirements.txt` in sync with `pyproject.toml` for Vercel deployment
- For `pyproject.toml`-only workflow, update Vercel build to use `pip install .` or `uv`
- The weather endpoint uses [wttr.in](https://github.com/chubin/wttr.in) - a free weather API

---

<br>
<br>
<br>

---

<a name="русская-версия"></a>

## 🇷🇺 Русская версия

<div align="center">

*Production-ready FastAPI шаблон для развертывания на Python runtime Vercel как ASGI приложение*

[Возможности](#-возможности) • [Быстрый старт](#-быстрый-старт-1) • [API справка](#-api-справка) • [Структура проекта](#-структура-проекта-1) • [Развертывание](#-развертывание-1)

</div>

---

### 📋 Обзор

Современный, готовый к продакшену FastAPI шаблон, оптимизированный для развертывания на Vercel. Включает:

- ⚡ **Async/Sync паттерны** с httpx и asyncer для конкурентных операций
- 🔒 **Типобезопасные ответы** с использованием Pydantic v2 generics
- 🌐 **Настроенный CORS** готовый для кросс-доменных запросов
- 📦 **Версионированная маршрутизация API** под `/api/v1` с примерами погодных эндпоинтов
- 🎯 **Развертывание без настройки** на Vercel с автоматическим определением ASGI

---

### ✨ Возможности


| Функция                                                  | Описание                                                                                                  |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **ASGI точка входа**                                  | `api/index.py` экспортирует `app` для автоматического определения Vercel |
| **Версионированная маршрутизация** | API эндпоинты организованы под префиксом`/api/v1`                                |
| **Async конкурентность**                          | Встроенные помощники через`asyncer` и `httpx.AsyncClient`                                |
| **Типизированные ответы**                   | Генерик модели ответов с Pydantic v2 (`schemas/response_schema.py`)                          |
| **Конфигурация окружения**                 | Управление настройками через`pydantic-settings`                                         |
| **Готовый CORS**                                         | Предварительно настроенный CORS middleware в`core/config.py`                            |
| **Примеры эндпоинтов**                         | Weather API демонстрирующий sync/async/concurrent паттерны                                 |

---

### 🚀 Быстрый старт

#### Требования

- **Python 3.12+** рекомендуется
- `pip` или `uv` для управления зависимостями

#### Установка

**Вариант 1: Используя pip**

```bash
pip install -r requirements.txt
```

**Вариант 2: Используя uv (быстрее)**

```bash
uv sync
```

#### Локальная разработка

1. **Создайте файл окружения**

   ```bash
   cp .env.example .env
   ```
2. **Запустите сервер разработки**

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 9096
   ```

   Или используя Vercel CLI:

   ```bash
   vercel dev
   ```
3. **Доступ к API**

   - 🌐 API: `http://127.0.0.1:9096`
   - 📖 Swagger UI: `http://127.0.0.1:9096/docs`
   - 📄 ReDoc: `http://127.0.0.1:9096/redoc`

---

### 📚 API Справка

#### Проверка здоровья


| Метод | Эндпоинт | Описание                                   | Ответ                   |
| ---------- | ---------------- | -------------------------------------------------- | ---------------------------- |
| `GET`      | `/`              | Эндпоинт проверки здоровья | `{"message": "Hello World"}` |

#### Погодные эндпоинты (Sync)


| Метод | Эндпоинт             | Параметры запроса         | Описание                                                                 |
| ---------- | ---------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------- |
| `GET`      | `/api/v1/weather_sync/sync1` | `city` (по умолчанию: "Quito") | Погода используя синхронный паттерн работы |
| `GET`      | `/api/v1/weather_sync/sync2` | `city` (по умолчанию: "Quito") | Погода используя синхронный httpx клиент          |

#### Погодные эндпоинты (Async)


| Метод | Эндпоинт                        | Параметры запроса                                     | Описание                                                                           |
| ---------- | --------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `GET`      | `/api/v1/weather_async`                 | `city` (по умолчанию: "Quito")                             | Погода используя асинхронный httpx клиент                  |
| `GET`      | `/api/v1/weather_async_list/sequencial` | `cities[]` (по умолчанию: ["Quito", "Miami", "Barcelona"]) | Последовательные запросы для нескольких городов |
| `GET`      | `/api/v1/weather_async_list/concurrent` | `cities[]` (по умолчанию: ["Quito", "Miami", "Barcelona"]) | ⚡ Конкурентные запросы (быстрее)                                |

#### Примеры запросов

```bash
# Погода для одного города
curl "http://localhost:9096/api/v1/weather_async?city=Moscow"

# Несколько городов (последовательно)
curl "http://localhost:9096/api/v1/weather_async_list/sequencial?cities=Tokyo&cities=Paris"

# Несколько городов (конкурентно - быстрее)
curl "http://localhost:9096/api/v1/weather_async_list/concurrent?cities=Tokyo&cities=Paris&cities=Berlin"
```

#### Формат ответа

Все эндпоинты возвращают стандартизированный ответ:

```json
{
  "success": true,
  "message": "Weather in Moscow",
  "data": {
    "city": "Moscow",
    "current_condition": [...],
    "weather": [...]
  },
  "meta": {
    "api_reference": "https://github.com/chubin/wttr.in"
  }
}
```

---

### 📁 Структура проекта

```
vercel-fastapi-template/
├── 📂 api/
│   ├── 📂 v1/
│   │   ├── 📂 endpoints/
│   │   │   ├── __init__.py
│   │   │   └── weather.py          # Погодные API эндпоинты
│   │   ├── __init__.py
│   │   └── api.py                  # Агрегация роутеров
│   ├── __init__.py
│   └── index.py                    # 🎯 Vercel ASGI точка входа
│
├── 📂 core/
│   ├── __init__.py
│   └── config.py                   # ⚙️ Настройки приложения
│
├── 📂 schemas/
│   ├── __init__.py
│   └── response_schema.py          # 📝 Pydantic модели ответов
│
├── 📂 utils/
│   ├── 📂 exceptions/
│   │   ├── __init__.py
│   │   ├── common_exception.py     # Общие обработчики исключений
│   │   ├── user_exceptions.py      # Исключения пользователя
│   │   └── user_follow_exceptions.py
│   ├── __init__.py
│   ├── partial.py                  # Вспомогательные функции
│   └── uuid6.py                    # Реализация UUID v6
│
├── 📂 test/
│   └── __init__.py
│
├── 📄 main.py                      # 🚀 Инициализация FastAPI приложения
├── 📄 pyproject.toml               # Метаданные проекта и зависимости
├── 📄 requirements.txt             # 📦 Pip зависимости
├── 📄 uv.lock                      # UV lock файл
├── 📄 vercel.json                  # ▲ Конфигурация Vercel
├── 📄 .env.example                 # Шаблон переменных окружения
├── 📄 .gitignore
└── 📄 README.md                    # Этот файл
```

---

### ⚙️ Переменные окружения

Создайте файл `.env` на основе `.env.example`:


| Переменная   | Тип      | По умолчанию | Описание                                                           |
| ---------------------- | ----------- | ----------------------- | -------------------------------------------------------------------------- |
| `PROJECT_NAME`         | `str`       | `"app"`                 | Название API проекта                                        |
| `MODE`                 | `str`       | `"development"`         | Режим окружения:`development` \| `production` \| `testing`   |
| `API_VERSION`          | `str`       | `"v1"`                  | Версия API для маршрутизации                         |
| `BACKEND_CORS_ORIGINS` | `list[str]` | `["*"]`                 | Разрешенные CORS источники (через запятую) |
| `WHEATER_URL`          | `str`       | `"https://wttr.in"`     | Базовый URL погодного API                                  |

#### Пример `.env`

```env
PROJECT_NAME=FastAPI Vercel Starter
MODE=development
API_VERSION=v1
BACKEND_CORS_ORIGINS=["http://localhost:3000","https://yourdomain.com"]
WHEATER_URL=https://wttr.in
```

---

### 🚢 Развертывание

#### Развертывание на Vercel

Этот проект оптимизирован для развертывания на Vercel без необходимости настройки.

**Метод 1: Используя Vercel CLI**

```bash
# Установите Vercel CLI
npm i -g vercel

# Разверните
vercel
```

**Метод 2: Интеграция с GitHub**

1. Отправьте ваш код на GitHub
2. Перейдите на [vercel.com](https://vercel.com)
3. Импортируйте ваш репозиторий
4. Нажмите **Deploy** ✨

#### Конфигурация Vercel

Включенный `vercel.json` настраивает:

```json
{
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

- **Зависимости**: Разрешаются из `requirements.txt`
- **Точка входа**: `api/index.py` экспортирует FastAPI `app`
- **Маршрутизация**: Весь трафик направляется в ASGI приложение

---

### 🛠️ Частые задачи

#### Добавление новых эндпоинтов

1. Создайте новый роутер в `api/v1/endpoints/your_endpoint.py`
2. Определите ваши маршруты используя декораторы FastAPI
3. Включите роутер в `api/v1/api.py`:

```python
from api.v1.endpoints import your_endpoint

api_router.include_router(your_endpoint.router, tags=["Ваша функция"])
```

#### Настройка CORS

Отредактируйте `core/config.py`:

```python
BACKEND_CORS_ORIGINS: list[str] = [
    "http://localhost:3000",
    "https://yourdomain.com"
]
```

#### Обновление настроек

1. Добавьте новые настройки в класс `Settings` в `core/config.py`
2. Добавьте соответствующие переменные в `.env`
3. Используйте через `settings.YOUR_VARIABLE`

---

### 📦 Технологический стек

- **[FastAPI](https://fastapi.tiangolo.com)** - Современный, быстрый веб-фреймворк
- **[Pydantic v2](https://docs.pydantic.dev)** - Валидация данных используя аннотации типов Python
- **[httpx](https://www.python-httpx.org)** - Асинхронный HTTP клиент
- **[asyncer](https://asyncer.tiangolo.com)** - Слой совместимости async/sync
- **[pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)** - Управление настройками
- **[uvicorn](https://www.uvicorn.org)** - ASGI сервер

---

### 📝 Заметки

- Этот шаблон использует **Pydantic v2**. Генерик модели ответов наследуются от `BaseModel`
- Держите `requirements.txt` синхронизированным с `pyproject.toml` для развертывания на Vercel
- Для работы только с `pyproject.toml`, обновите сборку Vercel для использования `pip install .` или `uv`
- Погодный эндпоинт использует [wttr.in](https://github.com/chubin/wttr.in) - бесплатный погодный API

---

<div align="center">

**Создано с ❤️**

</div>
