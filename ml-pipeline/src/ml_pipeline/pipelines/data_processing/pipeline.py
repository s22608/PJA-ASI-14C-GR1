from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_aug_train


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_aug_train,
                inputs="aug_train",
                outputs="preprocess_aug_train",
                name="preprocess_aug_train_node",
            ),
            # ,
            # node(
            #     func=preprocess_shuttles,
            #     inputs="shuttles",
            #     outputs="preprocessed_shuttles",
            #     name="preprocess_shuttles_node",
            # ),
            node(
                func=create_model_input_table,
                inputs=["preprocess_aug_train"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )
