#!/bin/bash
# =============================================================================
# ClearML + Hydra Template - Run Script
# =============================================================================
# This script demonstrates how to run experiments with Hydra configuration
# overrides from the command line.
# =============================================================================

# Ensure the project root is in the Python path
export PYTHONPATH=$(pwd)

# -----------------------------------------------------------------------------
# Experiment Configuration
# -----------------------------------------------------------------------------
# Customize these variables for your experiment

EXPERIMENT_NAME="my-experiment"
CLEARML_PROJECT_NAME="my-clearml-project"
CLEARML_TASK_NAME="experiment-run"
BATCH_SIZE=64
EPOCHS=10

# Set to 1 to disable ClearML tracking (useful for local development)
export DISABLE_CLEARML=1

# -----------------------------------------------------------------------------
# Run the experiment
# -----------------------------------------------------------------------------
# Hydra allows overriding any configuration value from the command line
# using dot notation (e.g., train.batch_size=64)

uv run python src/main.py \
    experiment.name=${EXPERIMENT_NAME} \
    clearml.project_name=${CLEARML_PROJECT_NAME} \
    clearml.task_name=${CLEARML_TASK_NAME} \
    train.batch_size=${BATCH_SIZE} \
    train.epochs=${EPOCHS}
