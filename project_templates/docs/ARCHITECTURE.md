# Architecture

Version: 0.1
Last Updated: {{DATE}}

> Fill this in when starting the project. AI agents read this before making changes to prevent architectural drift.

## Overview

<!-- Describe the system in 2-3 sentences. What does it do? Who uses it? -->

## Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | | |
| Backend / API | | |
| Database | | |
| Hosting | | |
| Auth | | |

## Components

<!-- List the major parts of the system and what each one does. -->

- **UI**:
- **API**:
- **Data layer**:
- **External integrations**:

## Data Flow

<!-- Describe how data moves through the system. A simple text diagram works. -->

```
User -> [Frontend] -> [API] -> [Database]
                   -> [External Service]
```

## Security Boundaries

<!-- Where do secrets live? Where does authentication happen? What is publicly accessible? -->

- Secrets: stored in `.env` locally, platform secret manager in production.
- Auth:
- Public surface:

## Environments

| Environment | URL / Access | Notes |
|-------------|-------------|-------|
| Local | `localhost:XXXX` | |
| Staging | | |
| Production | | |
