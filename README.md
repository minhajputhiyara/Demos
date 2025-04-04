# Discord Project

This project is designed to manage and enhance Discord functionalities.

## Folder Structure

- `env/` and `venv/` - Virtual environment directories.
- `dist/`, `build/`, and `*.egg-info/` - Distribution and packaging files.
- `.vscode/` and `.idea/` - IDE-specific configuration files.
- `.env` - Environment variables file.

## Key Files

- `discord_bot.py` - A base code for creating a Discord bot.
- `bot.py` - A code implementation that integrates with Opeanai to produce DFM response according to the user query.

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Contributing

Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.
