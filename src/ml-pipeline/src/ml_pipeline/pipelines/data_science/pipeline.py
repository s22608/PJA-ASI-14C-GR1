from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, train_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_model,
                inputs=["model_input_table"],
                outputs="championModel",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["championModel", "model_input_table"],
                outputs="output_metrics",
                name="evaluate_model_node",
            ),
        ]
    )
