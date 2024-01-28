# Mysterious Mansion Game

This project is a text-based game called Mysterious Mansion, built in Python. It's a part of the [`gptlife`](command:_github.copilot.openRelativePath?%5B%22gptlife%22%5D "gptlife") package, which is a collection of games and utilities.

## Project Structure

The project is structured as follows:

- [`gptlife/`](command:_github.copilot.openRelativePath?%5B%22gptlife%2F%22%5D "gptlife/"): The main package directory.
  - [`agents/`](command:_github.copilot.openSymbolInFile?%5B%22gptlife%2Fgames%2Fgame.py%22%2C%22agents%2F%22%5D "gptlife/games/game.py"): Contains classes related to game agents, including their personalities.
  - `games/`: Contains the main game logic and specific game implementations.
    - `mystery_mansion/`: Contains the specific implementation for the Mysterious Mansion game.
- [`setup.py`](command:_github.copilot.openRelativePath?%5B%22setup.py%22%5D "setup.py"): The setup script for the package.
- [`.gitignore`](command:_github.copilot.openRelativePath?%5B%22.gitignore%22%5D ".gitignore"): Specifies which files and directories to ignore in git.
- [`.pre-commit-config.yaml`](command:_github.copilot.openRelativePath?%5B%22.pre-commit-config.yaml%22%5D ".pre-commit-config.yaml"): Configuration for pre-commit hooks.

## Key Files

- [`gptlife/agents/agent.py`](command:_github.copilot.openSymbolInFile?%5B%22gptlife%2Fagents%2Fagent.py%22%2C%22gptlife%2Fagents%2Fagent.py%22%5D "gptlife/agents/agent.py"): Defines the base agent class.
- [`gptlife/agents/personality.py`](command:_github.copilot.openSymbolInFile?%5B%22gptlife%2Fagents%2Fpersonality.py%22%2C%22gptlife%2Fagents%2Fpersonality.py%22%5D "gptlife/agents/personality.py"): Defines the personality of agents.
- [`gptlife/games/game.py`](command:_github.copilot.openSymbolInFile?%5B%22gptlife%2Fgames%2Fgame.py%22%2C%22gptlife%2Fgames%2Fgame.py%22%5D "gptlife/games/game.py"): Defines the abstract game class.
- [`gptlife/games/mystery_mansion/mystery_mansion.py`](command:_github.copilot.openSymbolInFile?%5B%22gptlife%2Fgames%2Fmystery_mansion%2Fmystery_mansion.py%22%2C%22gptlife%2Fgames%2Fmystery_mansion%2Fmystery_mansion.py%22%5D "gptlife/games/mystery_mansion/mystery_mansion.py"): The main game file for Mysterious Mansion.

## How to Run

To run the game, execute the [`main.py`](command:_github.copilot.openRelativePath?%5B%22gptlife%2Fmain.py%22%5D "gptlife/main.py") file in the [`gptlife`](command:_github.copilot.openRelativePath?%5B%22gptlife%22%5D "gptlife") directory.

```sh
python gptlife/main.py
```

## Contributing

Contributions are welcome! Please read the contributing guidelines before making any changes.

## License

This project is licensed under the terms of the MIT license.