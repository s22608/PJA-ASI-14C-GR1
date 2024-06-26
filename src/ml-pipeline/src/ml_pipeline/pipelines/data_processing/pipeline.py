from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_aug_train, create_metrics


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_aug_train,
                inputs="aug_train",
                outputs="preprocess_aug_train",
                name="preprocess_aug_train_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocess_aug_train"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )
