import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_percentage(x: pd.Series) -> pd.Series:
    x = x.str.replace("%", "")
    x = x.astype(float) / 100
    return x


def _parse_money(x: pd.Series) -> pd.Series:
    x = x.str.replace("$", "").str.replace(",", "")
    x = x.astype(float)
    return x


def preprocess_aug_train(data: pd.DataFrame) -> pd.DataFrame:
    return data


# def create_model_input_table(
#     shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
# ) -> pd.DataFrame:
#     """Combines all data to create a model input table.

#     Args:
#         shuttles: Preprocessed data for shuttles.
#         companies: Preprocessed data for companies.
#         reviews: Raw data for reviews.
#     Returns:
#         Model input table.

#     """
#     rated_shuttles = shuttles.merge(reviews, left_on="id", right_on="shuttle_id")
#     rated_shuttles = rated_shuttles.drop("id", axis=1)
#     model_input_table = rated_shuttles.merge(
#         companies, left_on="company_id", right_on="id"
#     )
#     model_input_table = model_input_table.dropna()
#     return model_input_table
