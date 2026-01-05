"""
Main entry point for ClearML + Hydra template.

This module demonstrates the integration of ClearML experiment tracking
with Hydra configuration management for ML experiments.
"""

import os
import hydra
from omegaconf import DictConfig
from hydra.core.config_store import ConfigStore
from configs import Config

# Register the configuration schema with Hydra's ConfigStore
cs = ConfigStore.instance()
cs.store(name="config", node=Config)


def init_clearml(cfg: DictConfig):
    """
    Initialize ClearML task if enabled.

    Set CLEARML_OFFLINE_MODE=1 or DISABLE_CLEARML=1 to skip ClearML initialization.

    Args:
        cfg: Hydra configuration object.

    Returns:
        ClearML Task object or None if disabled.
    """
    if os.environ.get("DISABLE_CLEARML", "0") == "1":
        print("ClearML disabled via DISABLE_CLEARML environment variable")
        return None

    try:
        from clearml import Task
        task = Task.init(
            project_name=cfg.clearml.project_name,
            task_name=cfg.clearml.task_name,
            task_type=cfg.clearml.task_type
        )
        return task
    except Exception as e:
        print(f"Warning: ClearML initialization failed: {e}")
        print("Continuing without ClearML tracking...")
        return None


@hydra.main(config_path="../configs", config_name="config", version_base="1.1")
def main(cfg: DictConfig) -> None:
    """
    Main function to run the experiment.

    This function initializes a ClearML task for experiment tracking
    and demonstrates how to access Hydra configuration values.

    Args:
        cfg: Hydra configuration object containing all experiment settings.
    """
    # Initialize ClearML task for experiment tracking (optional)
    task = init_clearml(cfg)

    # Log experiment configuration
    print(f"Experiment: {cfg.experiment.name} (version {cfg.experiment.version})")
    print(f"Training for {cfg.train.epochs} epochs with batch size {cfg.train.batch_size}")
    print(f"Learning rate: {cfg.train.learning_rate}")

    # Log model and optimizer configuration
    print(f"Using model: {cfg.model.type} with {cfg.model.num_classes} classes")
    print(f"Optimizer: {cfg.optimizer.type}")

    # TODO: Add your training logic here
    # Example:
    # model = build_model(cfg.model)
    # trainer = Trainer(cfg.train)
    # trainer.fit(model, train_loader, val_loader)


if __name__ == "__main__":
    main()
