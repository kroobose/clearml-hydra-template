"""
Hydra Configuration Classes for ClearML Integration

This module defines structured configuration classes using Python dataclasses
for type-safe configuration management with Hydra and ClearML.
"""

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import List


# Experiment configuration
@dataclass
class ExperimentConfig:
    """Configuration for experiment metadata."""
    name: str = "default_experiment"
    version: float = 1.0


# Training configuration
@dataclass
class TrainConfig:
    """Configuration for training hyperparameters."""
    batch_size: int = 32
    epochs: int = 10
    learning_rate: float = 0.001


# Model configuration
@dataclass
class ModelConfig:
    """Configuration for model architecture."""
    type: str = "resnet50"
    num_classes: int = 10


# Optimizer configuration
@dataclass
class OptimizerConfig:
    """Configuration for optimizer settings."""
    type: str = "adam"


# ClearML configuration
@dataclass
class ClearMLConfig:
    """Configuration for ClearML experiment tracking."""
    project_name: str = "my-project"
    task_name: str = "experiment-task"
    task_type: str = "training"


# Root configuration class
@dataclass
class Config:
    """Root configuration class that combines all sub-configurations."""
    experiment: ExperimentConfig = field(default_factory=ExperimentConfig)
    train: TrainConfig = field(default_factory=TrainConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    optimizer: OptimizerConfig = field(default_factory=OptimizerConfig)
    clearml: ClearMLConfig = field(default_factory=ClearMLConfig)
