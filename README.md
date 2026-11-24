# envcheck

A small Python CLI tool that compares `.env` files and identifies missing or unexpected environment variables.

## Features

- Detects missing environment variables.
- Identifies unexpected variables.
- Ignores comments and blank lines.
- Never displays secret values.
- No external dependencies.

## Usage

Run the following command:

```bash
python envcheck.py .env.example .env
```

## Example

**.env.example**
```env
DATABASE_URL=
API_KEY=
PORT=3000
```

**.env**
```env
DATABASE_URL=localhost
PORT=3000
```

Output:

```text
Missing:
  API_KEY

Extra:
  None

1 missing, 0 extra
```

## Tests

Run the automated tests:

```bash
python -m unittest -v
```

## Requirements

- Python 3.10 or newer
- No third-party packages

## License

MIT
