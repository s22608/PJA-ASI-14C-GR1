from kedro.pipeline import Pipeline, node, pipeline

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="aug_train",
                outputs="preprocessed_aug_train",
                name="preprocess_aug_train_node",
            )
            # ,
            # node(
            #     func=preprocess_shuttles,
            #     inputs="shuttles",
            #     outputs="preprocessed_shuttles",
            #     name="preprocess_shuttles_node",
            # ),
            # node(
            #     func=create_model_input_table,
            #     inputs=["preprocessed_shuttles", "preprocessed_aug_train", "reviews"],
            #     outputs="model_input_table",
            #     name="create_model_input_table_node",
            # ),
        ]
    )
