# ClearML + Hydra Template

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ClearML](https://img.shields.io/badge/ClearML-1.16+-orange.svg)](https://clear.ml/)
[![Hydra](https://img.shields.io/badge/Hydra-1.3+-blueviolet.svg)](https://hydra.cc/)

A **production-ready template** for integrating [ClearML](https://clear.ml/) experiment tracking with [Hydra](https://hydra.cc/) configuration management for machine learning projects.

## ✨ Features

- 🔧 **Type-safe Configuration**: Structured configs using Python dataclasses with full IDE support
- 📊 **Experiment Tracking**: Automatic logging to ClearML for reproducibility
- 🔄 **Configuration Overrides**: Easy command-line overrides with Hydra's dot notation
- 📦 **Modern Python Packaging**: Uses `pyproject.toml` with [uv](https://github.com/astral-sh/uv) for fast dependency management
- 🏗️ **Clean Architecture**: Modular structure separating config, source code, and scripts

## 📁 Project Structure

```
clearml-hydra/
├── configs/
│   ├── __init__.py          # Exports Config class
│   └── config.py             # Dataclass-based configuration schema
├── src/
│   └── main.py               # Main entry point with ClearML integration
├── run_main.sh               # Example shell script for running experiments
├── pyproject.toml            # Project metadata and dependencies (uv)
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- A ClearML account (free tier available at [app.clear.ml](https://app.clear.ml))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/clearml-hydra-template.git
   cd clearml-hydra-template
   ```

2. **Set up the environment with uv**:
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create virtual environment and install dependencies
   uv sync
   ```

3. **Configure ClearML** (first time only):
   ```bash
   clearml-init
   ```
   Follow the prompts to connect to your ClearML server.

### Running an Experiment

Using the provided shell script:
```bash
./run_main.sh
```

Or directly with uv:
```bash
export PYTHONPATH=$(pwd)
uv run python src/main.py
```

## ⚙️ Configuration

### Configuration Schema

All configurations are defined as Python dataclasses in `configs/config.py`:

| Config Section | Parameters | Description |
|----------------|------------|-------------|
| `experiment` | `name`, `version` | Experiment metadata |
| `train` | `batch_size`, `epochs`, `learning_rate` | Training hyperparameters |
| `model` | `type`, `num_classes` | Model architecture settings |
| `optimizer` | `type` | Optimizer selection |
| `clearml` | `project_name`, `task_name`, `task_type` | ClearML tracking settings |

### Overriding Configuration

Hydra allows overriding any configuration value from the command line:

```bash
# Override a single value
uv run python src/main.py train.batch_size=128

# Override multiple values
uv run python src/main.py \
    experiment.name="my-experiment" \
    train.epochs=50 \
    train.learning_rate=0.0001 \
    model.type="efficientnet" \
    clearml.project_name="my-project"
```

### Adding New Configuration Options

1. Define a new dataclass in `configs/config.py`:
   ```python
   @dataclass
   class DataConfig:
       """Configuration for dataset settings."""
       dataset_path: str = "./data"
       train_split: float = 0.8
       num_workers: int = 4
   ```

2. Add it to the root `Config` class:
   ```python
   @dataclass
   class Config:
       # ... existing configs ...
       data: DataConfig = field(default_factory=DataConfig)
   ```

3. Access in your code:
   ```python
   print(f"Using dataset from: {cfg.data.dataset_path}")
   ```

## 📊 ClearML Integration

The template automatically:
- Creates a new ClearML task for each experiment run
- Logs all Hydra configuration parameters
- Tracks console output and errors
- Enables easy experiment comparison in the ClearML web UI

### Viewing Experiments

1. Go to [app.clear.ml](https://app.clear.ml) (or your self-hosted ClearML server)
2. Navigate to your project
3. Compare experiments, view logs, and analyze hyperparameters

## 🛠️ Development

### Install Development Dependencies

```bash
uv sync --all-extras
```

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Linting
ruff check .

# Type checking
mypy src/
```

## 📋 Extending the Template

### Adding Training Logic

Replace the placeholder in `src/main.py`:

```python
def main(cfg: DictConfig) -> None:
    # Initialize ClearML task
    task = Task.init(...)

    # Build model
    model = YourModel(
        model_type=cfg.model.type,
        num_classes=cfg.model.num_classes
    )

    # Set up training
    optimizer = get_optimizer(cfg.optimizer.type, model, cfg.train.learning_rate)

    # Training loop
    for epoch in range(cfg.train.epochs):
        train_one_epoch(model, train_loader, optimizer, cfg.train.batch_size)
        validate(model, val_loader)
```

### Using YAML Configs (Alternative)

While this template uses structured Python configs, Hydra also supports YAML files. Create `configs/config.yaml`:

```yaml
experiment:
  name: default_experiment
  version: 1.0

train:
  batch_size: 32
  epochs: 10
  learning_rate: 0.001
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Resources

- [ClearML Documentation](https://clear.ml/docs/latest/)
- [Hydra Documentation](https://hydra.cc/docs/intro/)
- [uv Documentation](https://docs.astral.sh/uv/)
- [OmegaConf Documentation](https://omegaconf.readthedocs.io/)
