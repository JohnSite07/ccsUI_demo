# ccsUI — CCS database interface (demo)

Interface de démonstration pour la base de données de CCS (Kinshasa, RD Congo) — une application
Django qui donne aux différents départements un accès contrôlé aux données d'inventaire et de ventes,
sans passer par des feuilles de calcul partagées.

> **Demo build.** This is the public demonstration version of the interface. It exists to show the
> structure and the flow, not to serve production data.

## Applications

| App | Rôle |
|---|---|
| `homeapp` | Landing page, base template, shared styles |
| `database` | The data request flow — request form, submitted-request view, resume view |
| `users` | Accounts and access control |

## What it does

A user signs in, submits a request against the CCS dataset through a form, and gets the result back
in the browser. `database/` holds the request and response templates (`request_data.html`,
`data_requested.html`, `resume.html`) and the form and view logic behind them.

The production system this demonstrates centralised inventory and sales data for 50+ concurrent
users, with role-based access control and real-time synchronisation across departments.

## Stack

Django · Python · SQLite (demo) · deployed on **AWS Elastic Beanstalk** (see `.ebextensions/`)

## Running it

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Layout

```
ccsUI_demo/        project settings and root URLs
homeapp/           landing page and base template
database/          data request forms, views and templates
users/             authentication
.ebextensions/     Elastic Beanstalk deployment configuration
db_lab.ipynb       notebook used while shaping the data model
```
